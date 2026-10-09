"""Build the demand corpus and count skill mentions.

Usage: python -I extract_skills.py <raw_dir> <date> <out_csv>
Inputs:  <raw_dir>/postings/_corpus-<date>.json (ATS boards, from normalize.py)
         <raw_dir>/aggregators/himalayas-india-<date>.json (from fetch_himalayas.py)
Outputs: <raw_dir>/postings/_demand-corpus-<date>.json and <out_csv>

Segments:
  A_india_remote  - remote software-engineering IC postings (not staff/lead) that list India
                    or a worldwide/global/APAC location (ATS) or are returned by Himalayas
                    for country=India; IT-services/staffing firms excluded.
  B_fullstack_all - full-stack/product/frontend IC postings on the ATS boards, any location
                    (what full-stack roles at these companies ask for, regardless of India access).
A skill counts once per posting. "required" means the mention appears outside any
section whose heading reads like nice-to-have/bonus/preferred.
"""
import csv
import html
import json
import re
import sys
from collections import defaultdict

SKILLS = {
    # skill: (family, regex)
    "typescript": ("languages", r"\btypescript\b|\bts\b(?=[ /,])"),
    "javascript": ("languages", r"\bjavascript\b|\bes6\b|\bjs\b"),
    "python": ("languages", r"\bpython\b"),
    "go": ("languages", r"\bgolang\b|\bgo\b(?= ?[,/)]| developer| engineer| services| backend)"),
    "java": ("languages", r"\bjava\b(?!script)"),
    "ruby/rails": ("languages", r"\bruby\b|\brails\b"),
    "php": ("languages", r"\bphp\b|\blaravel\b|\bsymfony\b"),
    "rust": ("languages", r"\brust\b"),
    "c#/.net": ("languages", r"c#|\.net\b"),
    "elixir": ("languages", r"\belixir\b|\bphoenix\b"),
    "react": ("frontend", r"\breact(?![ -]?native)(\.js|js)?\b"),
    "next.js": ("frontend", r"\bnext\.?js\b|\bnextjs\b"),
    "vue": ("frontend", r"\bvue(\.js|js)?\b|\bnuxt\b"),
    "angular": ("frontend", r"\bangular\b"),
    "svelte": ("frontend", r"\bsvelte(kit)?\b"),
    "html/css": ("frontend", r"\bhtml5?\b|\bcss3?\b|\btailwind\b"),
    "frontend state/data": ("frontend", r"\bredux\b|\bzustand\b|react query|tanstack|\bmobx\b"),
    "accessibility": ("frontend", r"accessibility|\bwcag\b|\ba11y\b"),
    "web performance": ("frontend", r"core web vitals|web performance|frontend performance|lighthouse"),
    "react native/mobile": ("mobile", r"react[ -]?native|\bflutter\b|\bios\b|\bandroid\b"),
    "node.js": ("backend", r"\bnode(\.js|js)?\b"),
    "nestjs": ("backend", r"\bnest\.?js\b"),
    "express": ("backend", r"\bexpress(\.js|js)?\b"),
    "rest api": ("api", r"\brest(ful)?\b|\bapi design\b|\bapis?\b"),
    "graphql": ("api", r"\bgraphql\b|\bapollo\b"),
    "grpc": ("api", r"\bgrpc\b|protobuf|protocol buffers"),
    "websockets/realtime": ("api", r"websocket|real[- ]time|webrtc"),
    "microservices/distributed": ("distributed systems", r"microservice|distributed system|event[- ]driven|message queue"),
    "queues/streaming": ("distributed systems", r"\bkafka\b|rabbitmq|\bsqs\b|pub/?sub|\bnats\b|bullmq|\bcelery\b"),
    "postgresql": ("data", r"\bpostgres(ql)?\b"),
    "mysql": ("data", r"\bmysql\b|mariadb"),
    "sql (generic)": ("data", r"\bsql\b"),
    "mongodb": ("data", r"\bmongo(db)?\b"),
    "redis": ("data", r"\bredis\b|\bvalkey\b"),
    "elasticsearch/search": ("data", r"elasticsearch|opensearch|\bsolr\b"),
    "orm": ("data", r"\bprisma\b|\btypeorm\b|\bdrizzle\b|\bsequelize\b|\bactiverecord\b|\borm\b"),
    "data modeling/schema": ("data", r"data model(l)?ing|schema design|database design"),
    "aws": ("cloud/infra", r"\baws\b|amazon web services|\blambda\b|\bs3\b|\bec2\b"),
    "gcp": ("cloud/infra", r"\bgcp\b|google cloud"),
    "azure": ("cloud/infra", r"\bazure\b"),
    "docker": ("cloud/infra", r"\bdocker\b|container"),
    "kubernetes": ("cloud/infra", r"\bkubernetes\b|\bk8s\b"),
    "terraform/iac": ("cloud/infra", r"terraform|infrastructure as code|\bpulumi\b|cloudformation"),
    "ci/cd": ("cloud/infra", r"\bci/cd\b|\bci\b|continuous (integration|delivery|deployment)|github actions"),
    "serverless/edge": ("cloud/infra", r"serverless|vercel|cloudflare workers|edge functions"),
    "testing": ("quality", r"\btest(s|ing)?\b|\bjest\b|vitest|cypress|playwright|\btdd\b"),
    "e2e testing": ("quality", r"cypress|playwright|end[- ]to[- ]end|\be2e\b"),
    "code review": ("quality", r"code review"),
    "observability": ("operations", r"observability|monitoring|\blogging\b|datadog|sentry|opentelemetry|grafana|prometheus"),
    "on-call/incidents": ("operations", r"on[- ]call|incident|production issues|debugging production"),
    "debugging": ("operations", r"debug"),
    "performance/scalability": ("performance", r"(?<!high[- ])(?<!high )performance(?! (review|bonus|cycle|culture|management))|scalab|latency|optimi[sz]"),
    "security": ("security", r"\bsecurity\b|\bsecure\b|\bowasp\b|authentication|authori[sz]ation|\boauth\b|\bsso\b"),
    "system design/architecture": ("design", r"system design|architect|design (scalable|robust|systems)|technical design"),
    "llm api integration": ("ai product", r"\bllms?\b|large language model|openai|anthropic|claude\b|\bgpt\b|gemini|generative ai|genai|gen ai"),
    "rag/vector search": ("ai product", r"\brag\b|retrieval[- ]augmented|vector (db|database|search|store)|embeddings|pgvector|pinecone"),
    "ai agents": ("ai product", r"\b(ai|llm|autonomous|coding|voice|conversational) agents?\b|agentic|tool[- ]calling|function calling|\bmcp\b|model context protocol"),
    "evals": ("ai product", r"\bevals?\b|evaluation (framework|pipeline|harness)s?|llm evaluation"),
    "ai-assisted development": ("ai-assisted engineering", r"ai[- ](assisted|augmented|native) (development|engineering|coding)|ai (coding|dev) tools|copilot|cursor\b|claude code|codex|windsurf|ai tools|ai-first|leverage ai|using ai"),
    "product sense/ownership": ("product/ownership", r"product (sense|mindset|minded|thinking)|ownership|own (features|projects)|end[- ]to[- ]end|customer|user empathy"),
    "startup/ambiguity": ("product/ownership", r"ambiguity|fast[- ]paced|startup|scrappy|autonomy|autonomous|self[- ](starter|directed|motivated)"),
    "written communication": ("communication", r"written communication|writing|async(hronous)?|documentation|communicat"),
    "english": ("communication", r"\benglish\b"),
    "mentoring": ("collaboration", r"mentor"),
    "collaboration": ("collaboration", r"collaborat|cross[- ]functional|work closely"),
    "open source": ("other", r"open[- ]source"),
}
PREF_HEAD = re.compile(
    r"(nice[- ]to[- ]haves?|bonus( points)?|preferred( qualifications)?|pluses|a plus|it'?s a plus|"
    r"would be great|extra credit|good to have|not required)", re.I)
NEXT_HEAD = re.compile(
    r"\n\s*(what we offer|benefits|perks|why (join|us)|about (us|the company)|compensation|"
    r"what you'?ll do|responsibilities|requirements|what we'?re looking for|you have|who you are)", re.I)
SERVICES = re.compile(
    r"^(PradeepIT|Xperteez|Photon|Nagarro|Pontoon|Harris|KDCI|Talent Sam|DXC|TD SYNNEX|Miratech|Girman|"
    r"Marrina|ACMO|Accellor|Acrobyte|Anteelo|People's Growth|R\.S\.Consultants|STIC|Quest Global|Supersourcing|"
    r"Particle41|Smart Working|Proximity Works|Flatgigs|IWConnect|Teravision|S-PRO|Opinov8|gravity9|Curotec|Volga)", re.I)
ENG = re.compile(r"engineer|developer|programmer", re.I)
NOT_ENG = re.compile(
    r"manager|director|head of|sales|recruit|support|intern\b|internship|lead\b|principal|staff|architect|"
    r"data scien|analyst|qa |tester|quality|sdet|designer\b|marketing|mechanical|security|sre\b|"
    r"site reliability|devops|it automation|it service|solution|consulting|customer success|demo|gtm|"
    r"forward[- ]deploy|business system|seo|prompt engineer", re.I)


def plain(s):
    s = html.unescape(s or "")
    s = re.sub(r"<(br|/p|/li|/h\d|/div|/ul)[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"[ \t]+", " ", s)


def split_pref(text):
    """Return (required_text, preferred_text)."""
    req, pref, pos = [], [], 0
    for m in PREF_HEAD.finditer(text):
        req.append(text[pos:m.start()])
        nxt = NEXT_HEAD.search(text, m.end())
        end = nxt.start() if nxt else min(len(text), m.end() + 1500)
        pref.append(text[m.start():end])
        pos = end
    req.append(text[pos:])
    return "\n".join(req), "\n".join(pref)


def load(raw, date):
    recs = []
    for r in json.load(open(f"{raw}/postings/_corpus-{date}.json", encoding="utf-8")):
        if r["seniority"] in ("staff+", "lead") or NOT_ENG.search(r["title"]):
            continue
        wp = (r.get("workplace") or "").lower()
        segs = []
        if r["india_eligibility"] != "region-locked-or-onsite" and wp not in ("onsite", "hybrid") \
                and not re.search(r"office based", r["location"], re.I):
            segs.append("A_india_remote")
        if r["role_family"] in ("full-stack/product", "frontend"):
            segs.append("B_fullstack_all")
        if segs:
            recs.append({"source": f"ats:{r['ats']}", "company": r["company"], "title": r["title"],
                         "url": r["url"], "location": r["location"], "segments": segs,
                         "role_family": r["role_family"], "comp": r["comp"], "text": r["text"]})
    hj = json.load(open(f"{raw}/aggregators/himalayas-india-{date}.json", encoding="utf-8"))["jobs"]
    for j in hj:
        if not ENG.search(j["title"]) or NOT_ENG.search(j["title"]) or SERVICES.search(j["companyName"]):
            continue
        loc = ", ".join(j.get("locationRestrictions") or []) or "Worldwide"
        recs.append({"source": "himalayas", "company": j["companyName"], "title": j["title"],
                     "url": j.get("applicationLink") or j.get("guid"), "location": loc,
                     "segments": ["A_india_remote"], "role_family": "",
                     "comp": f"{j.get('minSalary')}-{j.get('maxSalary')} {j.get('currency')}" if j.get("minSalary") else "",
                     "employment": j.get("employmentType"), "text": plain(j.get("description"))})
    # dedupe by company+title (multi-country clones of the same role)
    seen, out = set(), []
    for r in recs:
        k = (r["company"].lower().strip(), re.sub(r"\s*\(.*?\)\s*$", "", r["title"].lower().strip()))
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out


def main():
    raw, date, out_csv = sys.argv[1], sys.argv[2], sys.argv[3]
    recs = load(raw, date)
    counts = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    nseg = defaultdict(int)
    for r in recs:
        text = r["title"] + "\n" + r["text"]
        req_t, pref_t = split_pref(text)
        r["skills"] = {}
        for skill, (fam, rx) in SKILLS.items():
            in_req = re.search(rx, req_t, re.I) is not None
            in_any = in_req or re.search(rx, pref_t, re.I) is not None
            if in_any:
                r["skills"][skill] = "required" if in_req else "preferred"
        for seg in r["segments"]:
            nseg[seg] += 1
            for skill, kind in r["skills"].items():
                counts[seg][skill][0] += 1
                if kind == "required":
                    counts[seg][skill][1] += 1
    json.dump(recs, open(f"{raw}/postings/_demand-corpus-{date}.json", "w", encoding="utf-8"), indent=1)
    seg_desc = {
        "A_india_remote": "remote SWE IC (non-staff) postings open to India-based candidates; ATS boards + Himalayas country=India; IT-services firms excluded",
        "B_fullstack_all": "full-stack/product/frontend IC (non-staff) postings on 170 ATS boards, any location",
    }
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["skill", "skill_family", "postings_mentioning", "share", "required_mentions",
                    "required_share", "n_postings", "corpus_date", "segment"])
        for seg in ("A_india_remote", "B_fullstack_all"):
            n = nseg[seg]
            rows = sorted(counts[seg].items(), key=lambda kv: -kv[1][0])
            for skill, (m, rq) in rows:
                w.writerow([skill, SKILLS[skill][0], m, f"{m / n:.2f}", rq, f"{rq / n:.2f}", n, date,
                            f"{seg}: {seg_desc[seg]}"])
    for seg in ("A_india_remote", "B_fullstack_all"):
        n = nseg[seg]
        print(f"\n== {seg} N={n}")
        for skill, (m, rq) in sorted(counts[seg].items(), key=lambda kv: -kv[1][0]):
            print(f"{skill:28} {m:4} {m / n:5.0%}  req {rq / n:5.0%}")


if __name__ == "__main__":
    main()
