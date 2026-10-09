"""Fetch India-eligible remote engineering jobs from the Himalayas public search API.

Source: https://himalayas.app/jobs/api/search (attribution: Himalayas, himalayas.app).
Usage: python -I fetch_himalayas.py <out_file> <date>
Queries are full-stack/TypeScript oriented; country=India returns jobs that list
India or are worldwide-friendly. Records are deduplicated by guid.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

QUERIES = ["full stack engineer", "fullstack developer", "full-stack typescript",
           "react node", "next.js", "nestjs", "product engineer", "software engineer typescript",
           "frontend engineer react", "backend engineer node"]
SENIORITY = ["Mid-level", "Senior"]
PAGES = 5
HEADERS = {"User-Agent": "Mozilla/5.0 (research script)"}


def get(params):
    url = "https://himalayas.app/jobs/api/search?" + urllib.parse.urlencode(params, doseq=True)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(10 * (attempt + 1))
                continue
            raise
    return {}


def main():
    out, date = sys.argv[1], sys.argv[2]
    jobs, log = {}, []
    for q in QUERIES:
        for sen in SENIORITY:
            for page in range(1, PAGES + 1):
                d = get({"q": q, "country": "India", "seniority": sen, "page": page, "sort": "recent"})
                batch = d.get("jobs", []) or []
                log.append({"q": q, "seniority": sen, "page": page, "n": len(batch),
                            "total": d.get("totalCount")})
                for j in batch:
                    j["_query"] = q
                    jobs.setdefault(j.get("guid") or j.get("applicationLink"), j)
                time.sleep(1.2)
                if len(batch) < 20:
                    break
    json.dump({"source": "Himalayas public search API", "fetched": date, "log": log,
               "jobs": list(jobs.values())}, open(out, "w", encoding="utf-8"))
    print("unique jobs:", len(jobs))
    for l in log:
        if l["page"] == 1:
            print(l)


if __name__ == "__main__":
    main()
