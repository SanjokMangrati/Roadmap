"""Normalize saved ATS boards into one corpus of software-engineering postings.

Usage: python -I normalize.py <postings_dir> <date>
Writes <postings_dir>/_corpus-<date>.json: one record per engineering IC posting
with company, title, url, location text, india_eligibility, seniority, role_family,
compensation text and plain description.
"""
import glob
import html
import json
import os
import re
import sys

ENG_TITLE = re.compile(
    r"\b(engineer|developer|swe|programmer)\b", re.I)
NOT_SWE = re.compile(
    r"\b(manager|director|head of|vp|vice president|recruit|sales|solutions? engineer|"
    r"support engineer|customer|success|forward deployed|deployed engineer|field|"
    r"intern|internship|apprentice|graduate program|data scientist|analyst|"
    r"hardware|mechanical|electrical|firmware|asic|silicon|network engineer|"
    r"it engineer|it support|helpdesk|technical writer|account|partner|"
    r"pre-?sales|post-?sales|implementation|consultant|qa analyst)\b", re.I)
LEVEL_EXCLUDE = re.compile(r"\b(staff|principal|distinguished|architect|lead|tech lead|fellow)\b", re.I)

INDIA = re.compile(
    r"\b(india|bangalore|bengaluru|hyderabad|pune|mumbai|delhi|new delhi|gurgaon|gurugram|"
    r"noida|chennai|kolkata|ahmedabad|jaipur|kochi)\b", re.I)
GLOBAL = re.compile(
    r"\b(anywhere|worldwide|world-wide|global|globally|international|any location|"
    r"apac|apj|asia|asia[- ]pacific|emea ?/ ?apac|all time ?zones|fully remote, any)\b", re.I)
REGION_LOCK = re.compile(
    r"\b(united states|usa|u\.s\.|us only|us-based|canada|united kingdom|uk|"
    r"europe|eu|emea|germany|france|spain|netherlands|poland|portugal|ireland|"
    r"brazil|latam|latin america|americas|north america|mexico|argentina|australia|"
    r"japan|singapore|new york|san francisco|london|berlin|amsterdam|toronto|seattle|"
    r"austin|boston|chicago|denver|paris|dublin|tel aviv|israel|sydney|tokyo|"
    r"ny|nyc|sf|ca|tx|wa)\b", re.I)


def strip_html(s):
    s = html.unescape(s or "")
    s = re.sub(r"<(br|/p|/li|/h\d|/div)[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n", s).strip()


def from_greenhouse(company, d):
    for j in d.get("jobs", []):
        offices = ", ".join(o.get("name", "") for o in j.get("offices", []) or [])
        yield {
            "company": company, "ats": "greenhouse", "title": j.get("title", ""),
            "url": j.get("absolute_url", ""),
            "location": "; ".join(x for x in [(j.get("location") or {}).get("name", ""), offices] if x),
            "updated": j.get("updated_at", ""),
            "comp": "",
            "text": strip_html(j.get("content", "")),
        }


def from_ashby(company, d):
    for j in d.get("jobs", []):
        locs = [j.get("location", "")]
        for s in j.get("secondaryLocations", []) or []:
            locs.append(s.get("location", ""))
        addr = ((j.get("address") or {}).get("postalAddress") or {})
        locs.append(addr.get("addressCountry", "") or "")
        comp = j.get("compensation") or {}
        yield {
            "company": company, "ats": "ashby", "title": j.get("title", ""),
            "url": j.get("jobUrl", ""),
            "location": "; ".join(x for x in locs if x),
            "workplace": j.get("workplaceType", "") or ("Remote" if j.get("isRemote") else ""),
            "updated": j.get("publishedAt", ""),
            "comp": comp.get("compensationTierSummary") or comp.get("scrapeableCompensationSalarySummary") or "",
            "text": j.get("descriptionPlain") or strip_html(j.get("descriptionHtml", "")),
        }


def from_lever(company, d):
    for j in d if isinstance(d, list) else []:
        cats = j.get("categories") or {}
        locs = [cats.get("location", "")] + list(cats.get("allLocations") or [])
        lists = "\n".join(
            l.get("text", "") + "\n" + strip_html(l.get("content", "")) for l in j.get("lists", []) or [])
        sal = j.get("salaryRange") or {}
        yield {
            "company": company, "ats": "lever", "title": j.get("text", ""),
            "url": j.get("hostedUrl", ""),
            "location": "; ".join(dict.fromkeys(x for x in locs + [j.get("country", "") or ""] if x)),
            "workplace": j.get("workplaceType", ""),
            "updated": j.get("createdAt", ""),
            "comp": f"{sal.get('min')}-{sal.get('max')} {sal.get('currency')} {sal.get('interval')}" if sal else "",
            "text": "\n".join([j.get("descriptionPlain", "") or "", lists, j.get("additionalPlain", "") or ""]),
        }


def india_eligibility(rec):
    loc = rec["location"]
    if INDIA.search(loc):
        return "india-listed"
    if GLOBAL.search(loc):
        return "global-listed"
    # Remote with no region in the location field: check the description.
    remote_only = re.fullmatch(r"\s*(remote|fully remote|distributed)\s*", loc, re.I) is not None
    body_india = INDIA.search(rec["text"]) is not None
    if body_india and re.search(r"\b(remote|hire|located|based|countries|eligible)\b", rec["text"], re.I):
        return "india-in-description"
    if remote_only:
        return "remote-unspecified"
    return "region-locked-or-onsite"


def seniority(title):
    t = title.lower()
    if re.search(r"\b(staff|principal|distinguished|architect|fellow)\b", t):
        return "staff+"
    if re.search(r"\b(lead|tech lead)\b", t):
        return "lead"
    if re.search(r"\b(senior|sr\.?|iii|level 3|l3)\b", t):
        return "senior"
    if re.search(r"\b(junior|jr\.?|entry|new grad|associate|i)\b", t):
        return "junior"
    return "unlabelled/mid"


def role_family(title):
    t = title.lower()
    if re.search(r"full[- ]?stack|product engineer|web engineer|software engineer, product|product software", t):
        return "full-stack/product"
    if re.search(r"front[- ]?end|ui engineer|web developer|design engineer", t):
        return "frontend"
    if re.search(r"back[- ]?end|api|platform|infrastructure|distributed|systems|database|storage|runtime", t):
        return "backend/platform"
    if re.search(r"\b(ai|ml|machine learning|llm|applied ai|agent)\b", t):
        return "ai/ml"
    if re.search(r"mobile|ios|android|react native|flutter", t):
        return "mobile"
    if re.search(r"sre|site reliability|devops|security|data engineer|analytics engineer", t):
        return "other-eng"
    return "general-swe"


def main():
    pdir, date = sys.argv[1], sys.argv[2]
    out = []
    for path in sorted(glob.glob(os.path.join(pdir, f"*-{date}.json"))):
        name = os.path.basename(path)
        if name.startswith("_"):
            continue
        blob = json.load(open(path, encoding="utf-8"))
        parser = {"greenhouse": from_greenhouse, "ashby": from_ashby, "lever": from_lever}[blob["ats"]]
        for rec in parser(blob["company"], blob["data"]):
            title = rec["title"]
            if not ENG_TITLE.search(title) or NOT_SWE.search(title):
                continue
            rec["seniority"] = seniority(title)
            rec["role_family"] = role_family(title)
            rec["india_eligibility"] = india_eligibility(rec)
            out.append(rec)
    seen, dedup = set(), []
    for r in out:
        key = r["url"] or (r["company"], r["title"].lower())
        key2 = (r["company"], r["title"].lower().strip(), r["location"].lower())
        if key in seen or key2 in seen:
            continue
        seen.update([key, key2])
        dedup.append(r)
    json.dump(dedup, open(os.path.join(pdir, f"_corpus-{date}.json"), "w", encoding="utf-8"), indent=1)
    from collections import Counter
    print("eng IC postings:", len(dedup))
    print(Counter(r["india_eligibility"] for r in dedup))
    print(Counter(r["role_family"] for r in dedup))
    print(Counter(r["seniority"] for r in dedup))


if __name__ == "__main__":
    main()
