# Drivetrain — Frontend Engineer (India, Remote) (primary) and Backend Engineer (India, Remote)

Researched 2026-10-09 as the replacement for Plane, which was excluded for being on-site in Hyderabad. All access dates are 2026-10-09.

## 1. Summary

- **Company:** Drivetrain (drivetrain.ai) makes AI financial planning and analysis (FP&A) software. It was founded in 2021 by former Google engineers and describes itself as a "remote-first company headquartered in the San Francisco Bay Area". Its about page lists offices in New York, Sunnyvale, Toronto and Bengaluru (Koramangala). The first-party careers page is the Lever board at jobs.lever.co/drivetrain, which the site's "View openings" link points to. The drivetrain.ai/careers URL returns 404.
- **Roles:** Frontend Engineer (India) asks for 1–3 years of React plus data structures. Backend Engineer (India) asks for 3+ years, with a Java/Spring/Hibernate stack.
- **Eligibility: pass.** Lever tags both roles "India" with workplace type "Remote". The posting text says "Drivetrain is a remote-first company..." and "Remote-friendly: Drivetrain brings together the best and the brightest, no matter where they are". One other India posting (SDET) is tagged "hybrid", so the "remote" tag on these two is a deliberate setting. Employment type is "Full Time". The employing entity (Indian subsidiary or employer of record) is not stated. Drivetrain has a Bengaluru office and raised its Series A in rupees (₹123 crore), so an Indian entity is likely, but that is an inference.
- **Live, with a caveat:** Both postings are live today, but they were **created on Lever in November 2024 (frontend) and July 2024 (backend)** and get periodically reposted, so they look like evergreen pipeline postings.
- **Pay versus target: borderline, by inference.** No range is published. Levels.fyi shows a Software Engineer median total compensation of **$28.3K a year (about ₹24–25 lakh)**, with location and level unspecified. That works out to roughly ₹1.5–1.7 lakh a month take-home after tax and provident fund (estimate), which sits at the bottom of the 1.5–2 lakh target.
- **Process (candidate reports only, 2025, anecdotal to corroborated):** Data-structures-and-algorithms (DSA) heavy live coding over Google Meet. Problems include stack variants such as asteroid collision and a min/max stack, recursion, and 0/1 knapsack. Some loops add low-level and high-level design (a movie or concert booking app). Reports describe 2–3 technical rounds plus a hiring-manager round and an HR round. **AI policy: unknown.**
- **Fit:** The **Frontend Engineer role is realistic (preliminary).** The candidate's 3 years of React sits at the top of the 1–3-year band. The gaps are DSA fluency under live conditions, and spreadsheet-style or data-visualization UI performance. The **Backend Engineer role is a stretch**, because it needs Java/Spring rather than Node.

## 2. Hard filters

| Filter | Result | Evidence |
|---|---|---|
| India remote explicitly allowed | **pass** | Lever API: `categories.location: "India"`, `workplaceType: "remote"`, `country: "IN"` for both postings. The hosted page shows "India" and "Remote" (D1, D2). Posting text: "Drivetrain is a remote-first company headquartered in the San Francisco Bay Area." and "Remote-friendly: Drivetrain brings together the best and the brightest, no matter where they are and provides them a great degree of autonomy." (D1) |
| Posting live | **pass (evergreen caveat)** | Both are present in the Lever API and return HTTP 200 on 2026-10-09 (D3). Created 2024-11-06 (frontend) and 2024-07-02 (backend). Built In shows "Reposted One Month Ago" (D8). Himalayas shows "20 days ago" (D14). |
| Employment type | Full Time. The legal employer is unverified. | D1. Bengaluru office (D4). INR-denominated Series A (D10, inference: an Indian entity exists). |
| US/EU company | **pass** | Headquarters in the San Francisco Bay Area (Sunnyvale) per the postings and the about page (D1, D4). Series A of $15M in October 2022 from Elevation Capital, Jungle Ventures and Venture Highway (D9, D10). |

## 3. Current role requirements

**Frontend Engineer (India) (D1). The US Frontend posting uses identical text (D5).**
- `required` 1–3 years "as a web, UI, JavaScript or frontend engineer with sound knowledge in Javascript, HTML and CSS, and a strong eye for design, with experience debugging using browser console".
- `required` "ReactJS and Data structure skills are important." The data-structures emphasis is echoed in the backend posting and the intern posting, so DSA is `inferred from repeated job language` (D2, D6).
- `required` "clean and maintainable code with attention to performance, but also be able to ship quickly"; working in a "fast-paced environment" with "rapidly changing design".
- Scope: "complex yet performant... frontend components like a data visualisation system to create beautiful charts/tables and a spreadsheet-inspired business modelling system". This implies large-grid rendering, virtualization and memoization (`inferred`).
- Scope: turning UI/UX designs into prototypes, reusable components, accessibility and responsiveness.
- `nice to have` Java and AWS.
- Not mentioned: TypeScript or Next.js, testing, system design, AI tools. A Built In listing for a Drivetrain frontend role shows "Top Skills" (TypeScript, Next.js, Vite, Vitest, Playwright, AG Grid, TanStack Table, Claude Code, Cursor, GitHub Copilot), but a fetch of the India listing showed those skills belong to a "similar jobs" panel. Treat them as **unverified**.

**Backend Engineer (India) (D2)**
- `required` "at least 3 years of experience in software engineering"; "deep understanding of algorithms, data structures, and distributed systems"; "excellent communication skills".
- Stack: "Java, Spring, Hibernate, Redis, Elasticsearch, PostgreSQL, BigQuery, and AWS". The posting adds: "Experience with the above-mentioned stack would be helpful but is not necessary."
- Duties: code review, ownership of quality, cost, maintainability and security, documentation, and system design.

**Company-wide signals**
- `inferred from repeated job language` "Great problem solver", "self-driven, proactive", "shape our company culture" (early-team framing).
- Infrastructure: AWS and GCP, Kubernetes, Terraform, Prometheus/Grafana (SRE posting, D7).
- AI and LLM product work: the Generative AI intern posting asks for "RAG, Agentic AI, and LLMs" and "AI/ML frameworks" (D6). Drivetrain markets an AI FP&A platform. The full-time frontend and backend postings ask nothing AI-specific (`explicit`). AI-assisted development expectations are **not stated**.
- Location or authorization: India only for these postings.
- Compensation: not published.

## 4. Interview stages

No first-party process description exists (the postings and the about page have none). The stages below come only from candidate reports, which were seen as Glassdoor search-engine excerpts because direct Glassdoor fetches returned HTTP 403.

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Apply | Lever form, or email careers@drivetrain.ai | — | unknown | — | official | D1 |
| 1 | Technical round 1 | Live DSA coding on Google Meet with a senior developer. Examples: an asteroid-collision variant (stack, with edge cases), a min/max-tracking stack, flattening a sorted 2D matrix, recursion problems. | ~60 min (inferred from "25 more mins left" in one report) | unknown | DSA, edge cases, clarifying questions, brute force to optimal | corroborated (several 2025 reports agree on DSA focus) | D12, D13 |
| 2 | Technical round 2 | DSA (0/1 knapsack, dynamic programming) then low-level design plus high-level design of a movie or concert booking app | ~60 min | unknown | DP, object-oriented low-level design, high-level system design, time management | anecdotal (one report) | D12 |
| 3 | Technical round 3 | Not described | — | unknown | — | anecdotal | D12 |
| 4 | Hiring manager round | Not described | — | unknown | — | anecdotal | D12 |
| 5 | HR round | Not described | — | unknown | — | anecdotal | D12 |

Reported loop lengths conflict: one report says three technical rounds, a hiring-manager round and an HR round over about two weeks; another says "two tech rounds... both focused on DSA" completed in one day. Both are kept (`conflicting`). The process may vary by role and level. No report mentions a frontend-specific (React machine-coding) round, but no frontend reports were found at all.

## 5. Stage-by-stage evaluation targets

- **DSA rounds:** Medium-level LeetCode-style problems on stacks (monotonic stack, asteroid collision, min/max stack), recursion and backtracking, 2D matrix traversal, and 0/1 knapsack or other classic dynamic programming. Interviewers watch the sequence of clarifying questions, then brute force, then the optimal solution, and how you handle edge cases. Narrate your reasoning continuously, because one report describes an interviewer ending early with "wasn't meeting the bar" despite an acknowledged approach. **Stakes are high given the candidate's weak area of explaining aloud.**
- **Design segment:** Low-level design (classes, entities, seat locking for a booking app) and high-level design (services, database, concurrency for double booking). Budget about 25 minutes. One report says an interviewer "kept on increasing the scope", so practise scoping and stating assumptions.
- **Frontend-specific (inferred from the posting, unconfirmed as a stage):** Be ready to discuss rendering large tables and spreadsheet grids (virtualization, memoization, avoiding re-renders), chart components, and debugging in browser DevTools. These are the posting's stated scope.
- **Hiring manager:** Fast shipping amid changing designs, ownership, and early-team culture fit.

## 6. Competency taxonomy for Drivetrain

- **Algorithms:** stacks, recursion, dynamic programming (knapsack), matrices; complexity analysis; edge cases.
- **Frontend engineering:** React component design, performance on data-dense UIs (grids, charts), CSS and responsiveness, accessibility, browser debugging.
- **Design:** object-oriented low-level design; high-level design of a transactional system (booking, concurrency).
- **Backend (backend role):** Java/Spring/Hibernate, PostgreSQL, Redis, Elasticsearch, BigQuery, AWS, distributed systems.
- **Behavioural:** problem solving narrated aloud, speed, self-direction, communication.

## 7. Process changes and history

- No dated official process or changes were found. The candidate reports cluster in 2025. A January 2025 backend report from Bengaluru describes two rounds with repeated last-minute rescheduling (D13). August to November 2025 reports describe DSA-heavy loops (D12; the exact months differ between search excerpts). No AI-driven changes were found.

## 8. Candidate-report findings

- **DSA-centric technical rounds: `corroborated`.** At least three to four independent 2025 Glassdoor reports agree (D12). Glassdoor shows a Software Engineer interview difficulty of 3.3/5 with 33% positive experiences, based on few reports. The breakdown is "Skills test 33%, Phone interview 33%" from only three interviews (D12).
- **Low-level plus high-level design (booking app): `anecdotal`.** One report.
- **Loop length: `conflicting`.** Two rounds in one day versus three technical, hiring-manager and HR rounds over about two weeks.
- **Scheduling reliability problems: `anecdotal`.** One January 2025 report (D13).
- **Frontend-specific rounds: no reports found.**
- Blocked sources: Glassdoor (all domains, 403), AmbitionBox (403), NodeFlair (403). Report contents come from search-engine excerpts and were not read in full.

## 9. Fit check

**Frontend Engineer (India): realistic (preliminary).**
- Hard requirements: years pass. The candidate's 3 years sits at the top of the 1–3 band, so the candidate may be seen as senior for the band. Location passes.
- Gaps:
  1. Live DSA performance with narration (D12). The candidate's self-reported weakness in explaining thought process aloud makes this the top risk.
  2. Data-dense UI performance, spreadsheet grids and charts (D1). The candidate's depth is unmeasured.
  3. Pay may land at the low end of the target (D11, inference).
  4. Low-level and high-level design segment (D12).

**Backend Engineer (India): stretch (preliminary).** The Java/Spring/Hibernate stack is a mismatch for the candidate's Node/NestJS. The posting says stack experience is "helpful but is not necessary", but the interviews are DSA plus design, so the candidate could still compete.

**Applicant pool (inference):** The postings are syndicated widely (Built In, Himalayas, Remotive, startup.jobs, Glassdoor jobs). "Remote India" plus a junior band suggests a large applicant pool. No applicant counts were found.

## 10. Exclusions and unknowns

- Unknown: the legal employer in India; the pay band; whether a frontend machine-coding round exists; AI tool policy in interviews; whether the evergreen postings are actively filling seats; the time-zone overlap expected.
- Layoffs and hiring freezes: none found for the last 12 months (search only; absence of reports is not proof). No funding after the October 2022 Series A was found, which leaves the runway question open.
- Levels.fyi's $28.3K median has an unknown sample size, location and level.

## 11. Source ledger

```yaml
company: "Drivetrain"
anchor: false
match:
  hard_filters:
    eligibility: "pass — Lever location 'India', workplaceType 'remote'; 'remote-first company... no matter where they are'; employer entity unverified"
    hiring_now: "pass (evergreen caveat) — https://jobs.lever.co/drivetrain/cd39cc4e-056e-444c-8c17-9f97e34ddbce live 2026-10-09; created 2024-11-06, reposted"
  soft_dimensions:
    - dimension: "US-HQ (Bay Area) Series A FP&A SaaS with Bengaluru office"
      evidence: [D1, D4, D9]
    - dimension: "React frontend 1-3 yrs band matches candidate"
      evidence: [D1]
    - dimension: "Pay median ~₹24-25L TC (borderline vs target)"
      evidence: [D11]
fit:
  verdict: "realistic"
  preliminary: true
  gaps:
    - gap: "Live DSA (stack, recursion, DP) with continuous verbal reasoning"
      evidence: [D12]
    - gap: "Performance on data-dense React UIs (grids/charts/spreadsheet modelling)"
      evidence: [D1]
    - gap: "LLD/HLD segment (booking system)"
      evidence: [D12]
    - gap: "Pay likely at low end of 1.5-2L/month take-home"
      evidence: [D11]
role:
  title: "Frontend Engineer (India, Remote)"
  url: "https://jobs.lever.co/drivetrain/cd39cc4e-056e-444c-8c17-9f97e34ddbce"
  seniority: "1-3 years (junior-mid)"
  compensation: "not published; levels.fyi SWE median $28.3K TC (unspecified)"
  verified_date: "2026-10-09"
process:
  url: "https://www.glassdoor.com/Interview/Drivetrain-Interview-Questions-E8914494.htm"
  verified_date: "2026-10-09"
  stages:
    - id: "1"
      name: "Technical round 1 (DSA)"
      format: "Live coding on Google Meet"
      timebox: "~60 min (inferred)"
      ai_policy: "unknown"
      competencies: ["stacks", "recursion", "edge cases", "brute force to optimal"]
      evidence_quality: "corroborated"
      sources: [D12]
    - id: "2"
      name: "Technical round 2 (DSA + LLD/HLD)"
      format: "Live DP problem then booking-app design"
      timebox: "~60 min"
      ai_policy: "unknown"
      competencies: ["dynamic programming", "low-level design", "high-level design"]
      evidence_quality: "anecdotal"
      sources: [D12]
    - id: "3"
      name: "Technical round 3"
      format: "not described"
      timebox: ""
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "anecdotal"
      sources: [D12]
    - id: "4"
      name: "Hiring manager"
      format: "not described"
      timebox: ""
      ai_policy: "unknown"
      competencies: ["ownership", "fit"]
      evidence_quality: "anecdotal"
      sources: [D12]
    - id: "5"
      name: "HR"
      format: "not described"
      timebox: ""
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "anecdotal"
      sources: [D12]
  changes: []
requirements:
  explicit_required: ["1-3 yrs web/UI/JS/frontend", "JavaScript, HTML, CSS", "ReactJS", "data structures", "browser-console debugging", "performance-aware clean code", "ship fast amid changing designs"]
  explicit_preferred: ["Java", "AWS"]
  inferred_repeated: ["data structures and algorithms emphasis across FE/BE/intern postings", "remote-first", "early-team ownership"]
  ai_expectations: ["none stated for FE/BE; Gen AI intern posting asks RAG/agentic/LLM familiarity"]
uncertainty:
  - claim: "Postings are actively hiring"
    reason: "Created 2024, periodically reposted; may be evergreen pipelines"
    confidence: "medium"
  - claim: "India employment via Indian entity"
    reason: "Bengaluru office and INR Series A suggest it; not stated"
    confidence: "medium"
  - claim: "Interview is DSA-heavy for frontend too"
    reason: "All reports are general SWE/backend; none frontend"
    confidence: "low"
  - claim: "Pay ~₹24-25L TC"
    reason: "Single levels.fyi median with unknown sample, location, level"
    confidence: "low"
sources:
  - id: "D1"
    url: "https://jobs.lever.co/drivetrain/cd39cc4e-056e-444c-8c17-9f97e34ddbce"
    title: "Frontend Engineer — India — Remote (Lever)"
    tier: 1
    published_or_updated: "created 2024-11-06; live 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current (live), text old"
    supports: ["eligibility", "requirements", "remote-first quote"]
  - id: "D2"
    url: "https://jobs.lever.co/drivetrain/e2aafad8-a785-4515-9e3f-2b4981b727b8"
    title: "Backend Engineer — India — Remote (Lever)"
    tier: 1
    published_or_updated: "created 2024-07-02; live 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current (live), text old"
    supports: ["backend stack Java/Spring/Hibernate", "3+ yrs", "DSA/distributed systems"]
  - id: "D3"
    url: "https://api.lever.co/v0/postings/drivetrain?mode=json"
    title: "Drivetrain Lever postings API (33 postings)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["live", "workplaceType remote vs hybrid"]
  - id: "D4"
    url: "https://www.drivetrain.ai/about"
    title: "Drivetrain About (offices NYC, Sunnyvale, Toronto, Bengaluru; founders; 'View openings' -> Lever)"
    tier: 1
    published_or_updated: "undated"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["first-party careers link", "Bengaluru office", "HQ"]
  - id: "D5"
    url: "https://jobs.lever.co/drivetrain/5ebd7e09-3f2b-4c53-a0be-0649bdd84842"
    title: "Frontend Engineer — United States (identical text)"
    tier: 1
    published_or_updated: "created 2025-04-05"
    accessed: "2026-10-09"
    freshness: "current (live)"
    supports: ["repeated language"]
  - id: "D6"
    url: "https://jobs.lever.co/drivetrain/bc1c17bc-86ac-4f00-a1e3-0eb85aae4fdc"
    title: "Engineering Intern – Gen AI for FP&A Platform (India)"
    tier: 1
    published_or_updated: "created 2025-06-08"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["AI/LLM direction", "DSA emphasis"]
  - id: "D7"
    url: "https://jobs.lever.co/drivetrain/d1bc29ad-d0aa-47c8-8785-1094f279ccff"
    title: "Site Reliability Engineer - SRE (India)"
    tier: 1
    published_or_updated: "created 2025-09-01"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["infra: AWS+GCP, Kubernetes, Terraform"]
  - id: "D8"
    url: "https://builtinhyderabad.in/job/frontend-engineer/3558949"
    title: "Frontend Engineer — Drivetrain (Built In; 'Reposted One Month Ago', Junior, Hiring Remotely in India)"
    tier: 4
    published_or_updated: "~2026-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repost cadence", "remote India"]
  - id: "D9"
    url: "https://yourstory.com/2022/10/funding-us-saas-startup-drivetrain-ai-elevation-capital-jungle-ventures/amp"
    title: "SaaS startup Drivetrain AI raises $15M in Series A round (via search excerpt)"
    tier: 4
    published_or_updated: "2022-10"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["funding stage", "investors"]
  - id: "D10"
    url: "https://www.barandbench.com/dealstreet/burgeon-law-acts-on-drivetrain-ai-fundraising"
    title: "Burgeon Law acts on Drivetrain AI's ₹123 crore fundraising"
    tier: 4
    published_or_updated: "2022-10-31"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["INR-denominated round (Indian entity inference)"]
  - id: "D11"
    url: "https://www.levels.fyi/companies/drivetrain/salaries"
    title: "Drivetrain salaries — levels.fyi (SWE median $28.3K TC)"
    tier: 4
    published_or_updated: "2026-10-09 (page updated)"
    accessed: "2026-10-09"
    freshness: "unknown (data-point dates not shown)"
    supports: ["pay estimate"]
  - id: "D12"
    url: "https://www.glassdoor.com/Interview/Drivetrain-Software-Engineer-Interview-Questions-EI_IE8914494.0,10_KO11,28.htm"
    title: "Glassdoor — Drivetrain Software Engineer interviews (HTTP 403; content via search excerpts)"
    tier: 4
    published_or_updated: "2025 (Aug-Nov, excerpt dates inconsistent)"
    accessed: "2026-10-09"
    freshness: "current/old boundary (~11-14 months)"
    supports: ["DSA rounds", "LLD/HLD", "round counts", "difficulty 3.3/5"]
  - id: "D13"
    url: "https://fr.glassdoor.ca/Entretien/Drivetrain-Entretien-E8914494-RVW102333195.htm"
    title: "Glassdoor review — Backend Engineer, Bengaluru, Jan 2025 (HTTP 403; via search excerpt)"
    tier: 4
    published_or_updated: "2025-01"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["two rounds", "rescheduling issues"]
  - id: "D14"
    url: "https://himalayas.app/companies/drivetrain/jobs"
    title: "Drivetrain jobs on Himalayas (Frontend Engineer, Backend Engineer — India only)"
    tier: 4
    published_or_updated: "~2026-09-19 ('20 days ago')"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["syndication/repost", "India-only restriction"]
```
