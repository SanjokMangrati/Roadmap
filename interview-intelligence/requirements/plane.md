# Plane (Plane Software, Inc.) — EXCLUDED: India roles appear to be on-site in Hyderabad

Researched 2026-10-09. All access dates are 2026-10-09.

## 1. Summary

- **Roles checked:** Software Engineer, Backend (Node.js), location "India", first published 2025-12-26. Software Engineer, Frontend (React), location "India", first published 2026-04-22. Both are live on Ashby today (P1, P2, P3).
- **Eligibility: fail (on-site Hyderabad). This is a high-confidence inference, not an explicit first-party statement.**
  - Plane's own postings leave the workplace type blank (Ashby `workplaceType: null`). This contradicts the careers page's claim that "Every listing states its location and workplace type."
  - Every first-party signal points to the Hyderabad office. The careers page says "we are hiring in Hyderabad and San Francisco". The frontend posting says "You will work with designers, product, and backend engineers in San Francisco and Hyderabad". The work-trial page says a job may mean "sometimes a move to another city".
  - Plane's recruiting partner Uplers lists the same title, "Software Engineer, Backend (Node.js)", as **"Onsite - Hyderabad"** (3 years), together with every other Plane India role. It gives the office address as Hitech City Main Road, Hyderabad 500081.
  - Built In's company profile says "OnSite Workspace — Employees work from physical offices."
  - No source anywhere says the India engineering roles are remote.
- **Is Plane a US/EU company?** Only partly. The legal hiring entity in the postings is **Plane Software, Inc.**, a US-style corporation (the state of incorporation was not verified). The postings say it is "built across San Francisco, London, and Hyderabad", but Built In and aggregators list the headquarters as Hyderabad, and the India engineering team sits there.
- **Funding stage: seed.** Plane raised $4M from OSS Capital, with the date reported inconsistently as November 2023 or April 2024. No Series A was found.
- **Process (for the record):** a person reviews the application, then one or two conversations, then a **paid 2–5-day work trial** "with the team you'd join", then a decision with feedback within three working days. On AI, the careers page says no AI decides admission ("A person reads every application, people conduct every conversation"). During the trial, "You will work alongside the agents we are building, the same way the team does every day."
- **Pay:** No range is published on the postings. The only older data point is a July 2024 Cutshort listing for a Frontend Engineer (2–4 years) in Hyderabad at ₹6–11 lakh a year. That is far below the target, but it is old.
- **Action:** Excluded for the remote requirement. Researched Drivetrain instead (see `requirements/drivetrain.md`). If the candidate still wants Plane, one email to careers@plane.so asking "Is the India Node.js/React role open to fully remote candidates outside Hyderabad?" would settle it.

## 2. Hard filters

| Filter | Result | Evidence |
|---|---|---|
| India remote explicitly allowed | **fail (inferred, high confidence)** | First-party postings show location "India · Full Time" with no workplace type (P1, P2, P11). Careers page: "we are hiring in Hyderabad and San Francisco, across engineering, marketing, sales, and QA" (P4). Recruiting partner: "Software Engineer, Backend (Node.js) — Onsite - Hyderabad" (P6). Built In: "OnSite Workspace... Employees work from physical offices" (P7). **Conflict:** Built In's job cards label the same jobs "Remote, India" (P7). That label looks like an automatic default, because the same page's own policy field says on-site. Wellfound (blocked to fetch) shows a Plane Hyderabad marketing role marked "in office" (P8, search excerpt). |
| Posting live | pass | Both postings are listed in the Ashby API on 2026-10-09 (P3). |
| Employment type | Full-time (Ashby). The legal entity is not stated beyond "Plane Software, Inc." in the posting's structured data. | P1, P11 |

## 3–9. Not mapped

The remaining sections were not mapped because the hard filter failed. Facts captured in passing:

- **Node.js role stack:** Node.js and TypeScript (the posting literally reads "[Express or NestJS, confirm with engineering]"), Python/Django, Postgres, Redis, RabbitMQ, AWS, Kubernetes, Datadog and Sentry. Requirements are queue and worker systems (retries, idempotency), third-party API integrations, OAuth, and Postgres indexing. No years of experience are stated. The posting asks the candidate to "Point us to something you built, and tell us one decision in it you would make differently now" (P1). This would have been a strong skills match for the candidate.
- **Process:** the paid work trial described above. Trials can be "Consecutive days, evenings across two weeks, or weekends" (P4, P5).

## 10. Exclusions and unknowns

- The exclusion rests on inference and the recruiting-partner listing, not on an explicit first-party statement. Confidence is high but not certain.
- Not verified: the incorporation state, the paid-trial rate, and current India pay.
- Wellfound and Glassdoor returned HTTP 403.

## 11. Source ledger

```yaml
company: "Plane"
anchor: false
match:
  hard_filters:
    eligibility: "fail — India roles appear on-site in Hyderabad (recruiting partner Uplers: 'Onsite - Hyderabad'; careers page 'hiring in Hyderabad and San Francisco'); first-party postings leave workplace type blank; remote never stated"
    hiring_now: "pass — https://jobs.ashbyhq.com/plane/188f905e-3f6f-4569-9a32-d8ec48dfe656 and https://jobs.ashbyhq.com/plane/15cf6387-af74-4616-924f-3659fb76de01 live 2026-10-09"
  soft_dimensions:
    - dimension: "Seed stage ($4M OSS Capital); Plane Software, Inc.; HQ ambiguous (SF/Hyderabad)"
      evidence: [P4, P9, P11, P7]
fit:
  verdict: "out of reach"
  preliminary: false
  gaps:
    - gap: "Hard filter: role is on-site Hyderabad, candidate requires remote"
      evidence: [P4, P6, P7]
role:
  title: "Software Engineer, Backend (Node.js) / Software Engineer, Frontend (React)"
  url: "https://jobs.ashbyhq.com/plane/188f905e-3f6f-4569-9a32-d8ec48dfe656"
  seniority: "not stated (Uplers lists 3 yrs for Node.js)"
  compensation: "not published"
  verified_date: "2026-10-09"
process:
  url: "https://plane.so/careers"
  verified_date: "2026-10-09"
  stages:
    - id: "1"
      name: "Application (human-read)"
      format: "Application; 'Tell us what you have built and why this role fits'"
      timebox: ""
      ai_policy: "unknown"
      competencies: ["evidence of building"]
      evidence_quality: "official"
      sources: [P4, P2]
    - id: "2"
      name: "Conversations (1-2)"
      format: "Talks about shipped work and current problems"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["past work depth", "problem discussion"]
      evidence_quality: "official"
      sources: [P4]
    - id: "3"
      name: "Paid work trial"
      format: "2-5 days of real scoped work with the team; alongside Plane's agents"
      timebox: "2-5 days"
      ai_policy: "allowed"
      competencies: ["real delivery", "judgment", "finishing"]
      evidence_quality: "official"
      sources: [P4, P5]
    - id: "4"
      name: "Decision"
      format: "Decision with specific feedback within 3 working days"
      timebox: "3 working days"
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "official"
      sources: [P4]
  changes: []
requirements:
  explicit_required: ["Node.js+TypeScript in production", "Express/NestJS", "queue/worker systems", "third-party API integration", "Postgres"]
  explicit_preferred: ["Plane contribution/self-hosting", "importer/migration tools", "OAuth provider side", "AI agents acting on real data"]
  inferred_repeated: ["work daily with teams in San Francisco and Hyderabad", "public GitHub repo / community PRs"]
  ai_expectations: ["humans and agents working together; trial alongside agents"]
uncertainty:
  - claim: "India roles are on-site Hyderabad"
    reason: "First-party postings omit workplace type; on-site label comes from recruiting partner and Built In policy field; Built In job cards conflict ('Remote')"
    confidence: "high"
  - claim: "Seed round date"
    reason: "Reported as Nov 2023 and Apr 2024 by different outlets"
    confidence: "medium"
sources:
  - id: "P1"
    url: "https://jobs.ashbyhq.com/plane/188f905e-3f6f-4569-9a32-d8ec48dfe656"
    title: "Software Engineer, Backend (Node.js) — Plane (Ashby)"
    tier: 1
    published_or_updated: "2025-12-26"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["location India", "workplaceType null", "stack", "requirements"]
  - id: "P2"
    url: "https://jobs.ashbyhq.com/plane/15cf6387-af74-4616-924f-3659fb76de01"
    title: "Software Engineer, Frontend (React) — Plane (Ashby)"
    tier: 1
    published_or_updated: "2026-04-22"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'engineers in San Francisco and Hyderabad'", "workplaceType null"]
  - id: "P3"
    url: "https://api.ashbyhq.com/posting-api/job-board/plane"
    title: "Plane Ashby job board API (33 postings)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["live postings", "no workplace types set"]
  - id: "P4"
    url: "https://plane.so/careers"
    title: "Careers at Plane"
    tier: 1
    published_or_updated: "undated"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["hiring in Hyderabad and San Francisco", "process", "AI-in-hiring FAQ", "equity in every offer"]
  - id: "P5"
    url: "https://plane.so/work-trials"
    title: "Plane work trials"
    tier: 1
    published_or_updated: "undated"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["paid trial", "'sometimes a move to another city'", "work alongside agents"]
  - id: "P6"
    url: "https://www.uplers.com/company/plane-4755"
    title: "Plane jobs on Uplers (recruiting partner) — all 'Onsite - Hyderabad'"
    tier: 4
    published_or_updated: "2026 (page lists current roles)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["on-site Hyderabad for Software Engineer, Backend (Node.js)", "Hitech City address"]
  - id: "P7"
    url: "https://builtin.com/company/plane"
    title: "Plane on Built In (OnSite Workspace; HQ Hyderabad; 77 employees)"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["on-site policy", "conflicting 'Remote' job-card labels"]
  - id: "P8"
    url: "https://wellfound.com/company/planepowers"
    title: "Plane on Wellfound (HTTP 403; search excerpt: Hyderabad marketing role 'in office', ₹12-25L)"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["lead only: in-office"]
  - id: "P9"
    url: "https://www.outlookbusiness.com/corporate/plane-raises-4-million-in-seed-round-from-oss-capital"
    title: "Plane raises $4 million in seed round from OSS Capital (via search excerpt)"
    tier: 4
    published_or_updated: "2023-11 or 2024-04 (conflicting)"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["funding stage"]
  - id: "P10"
    url: "https://cutshort.io/job/Frontend-Engineer-Next-and-React-Hyderabad-Plane-gYw85CSe"
    title: "Plane Frontend Engineer (Next and React), Hyderabad, ₹6-11L"
    tier: 4
    published_or_updated: "2024-07-17"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["historical pay", "Hyderabad location"]
  - id: "P11"
    url: "https://jobs.ashbyhq.com/plane/188f905e-3f6f-4569-9a32-d8ec48dfe656"
    title: "Ashby JSON-LD structured data (hiringOrganization 'Plane Software, Inc.', empty address)"
    tier: 1
    published_or_updated: "2025-12-26"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["legal entity name", "no location type"]
```
