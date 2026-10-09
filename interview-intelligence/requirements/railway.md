# Railway: Senior Full-Stack Engineer - Product

Researched and verified 2026-10-09 (REACH list, lighter pass).

## 1. Summary

- **Role:** Senior Full-Stack Engineer - Product. You would build features end to end, from the dashboard UI to Temporal workflows that call Railway's microservices, and write TypeScript + GraphQL APIs. The posting is live today. It is an evergreen posting, first published 2024-02-07 (S1).
- **Eligibility: pass.** The posting says "This is a remote position available anywhere in the world!" India is not named, but the wording covers it (S1, S5). Employment type is "FullTime"; whether an India hire would be an employee, employer-of-record or contractor is not stated.
- **Pay vs target:** Railway publishes no pay range. The only pay data is a small Levels.fyi sample, which includes a Software Engineer in Uzbekistan at US$9,765 total compensation. That hints at location-adjusted pay, but the sample is too small to rely on (S9). Whether pay clears 1.5–2 lakh INR per month take-home is **unknown**.
- **Process (official, published in the posting):** intro call → asynchronous take-home (a small app with a UI that starts and stops a container through Railway's GraphQL API, deployed on Railway) → 60-minute code walkthrough → "Meet the Team" (4 people) → 30-minute 1:1 with the CEO → offer call (S1, S2, S3). **No paid work trial appears in any first-party source.**
- **AI policy in interviews:** `unknown`. The take-home is asynchronous and no rule is stated. You must walk through and extend the code live, so any AI-written code has to be code you can defend.
- **Fit: stretch (preliminary).** The take-home matches the candidate's stack (React plus a Node/GraphQL client). The gaps are the senior title, autonomous product leadership, Temporal-style async job orchestration, and a 30-minute live code defence that hits the candidate's weak area (explaining architecture).

## 2. Hard filters

**(a) India eligibility: `pass` (worldwide wording; India not named).**
- Posting: "This is a remote position available anywhere in the world! Linkedin makes us show a country, but we hire the best people wherever they are." (S1)
- The Ashby structured location is "Global", `workplaceType: Remote` (S4).
- railway.com/careers says: "Work from anywhere — Railway is fully remote." (S5)
- The application form asks only for name, email, resume and "Why Railway?". There is no location or work-authorization question (S10).

**(b) Live today: `pass`.** The posting is in the Ashby job-board API on 2026-10-09 (`publishedAt` 2024-02-07) and is mirrored at railway.com/careers/full-stack (S1, S2). Because the posting is more than two years old, it is probably an always-open pipeline rather than one headcount (inference).

**Employment type:** "FullTime". Benefits are listed as "Great salary, full health benefits including dependents, strong equity grants, equipment stipend" (S1). The legal arrangement for India is not stated.

**Working hours:** No timezone requirement. The posting warns: "the end of your day may overlap with the start of someone else's" (S1).

## 3. Current role requirements

| Item | Label | Evidence |
|---|---|---|
| Seniority: "Senior" title; no years stated | required (title); years: none stated | S1 |
| "An ability to autonomously lead, design, and implement great product experiences, from front to back" | required | S1 |
| "A strong understanding of frontend architecture to build interactivity-rich systems for fetching, mutating, and rendering data effectively" | required | S1 |
| "Experience managing complex asynchronous backend jobs for something like a build/deploy pipeline" | required | S1 |
| Build "TypeScript + GraphQL APIs with strong guarantees around modeling data" | required (responsibility) | S1 |
| Orchestrate workflows with Temporal | required (responsibility); Temporal experience not demanded | S1 |
| "Write Engineering Requirement Documents" (ERDs) from idea to monitoring | required (responsibility) | S1, S6 |
| "Experience with, or at least the desire to learn Rust" for open-source repos (CLI, Nixpacks) | preferred | S1 |
| "Great written and verbal communication skills ... in mostly-asynchronous manner" | required | S1 |
| Whole lifecycle: "research gathering and planning, to implementation and monitoring" | required | S1 |
| Postgres, Node.js, Temporal, TypeScript, GraphQL, ClickHouse | inferred from repeated job language (the Scalability posting repeats TypeScript + GraphQL, Temporal, ERDs, async communication; it also adds on-call) | S3 |
| Testing, security, performance | not stated for this role. The Scalability role asks for a "security and abuse-aware mindset" | S3 |
| AI-assisted development | not stated in any Railway engineering posting | S1, S3, S4 |
| Compensation | not published | S1, S5 |
| Location | worldwide | S1 |

**Other open engineering roles (S4):** 8 postings. Six are senior or infrastructure roles (Storage, Observability, Baremetal Orchestration, Datacenters, Infrastructure Engineer, Senior Product Engineer, Scalability). One is a US-only Growth Content Engineer. No mid-level product role is open.

## 4. Interview stages

Current official process. Steps 5 and 6 come from railway.com/careers/full-stack and the 2026 Scalability posting. The older Ashby text merges them into one "Offer and Details Chat with CEO".

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Talk with us about the role | Open-ended call: "who you are, what you want to do, and where you wanna go" | not stated | unknown | motivation, goals | official | S1, S2 |
| 2 | Small project (take-home) | "Build an application to spin up and spin down a container using our GQL API. Please deploy on Railway before the interview ... The app needs to have a UI component and not just a backend." Submitted before stage 3. "You can, and SHOULD! ask us questions ahead of time." | not stated | unknown (asynchronous, no rule given) | GraphQL API integration, frontend UI, async state (container lifecycle), deployment | official | S1, S2 |
| 3 | Review your solution with the Team | Live, 60 minutes: 0–5 intros; 5–35 "Walking through the code, talking about how you'd extend it"; 35–50 "Noodling on technology, frameworks, how you think about product"; 50–60 your questions. "Looking for: ... How you break down a problem and how you present a solution." | 60 min | unknown | code walkthrough, extensibility, product thinking, communication | official | S1, S2, S3 |
| 4 | Meet the Team | Conversations with "4 people from vastly different sections of the company" | not stated | unknown | collaboration, communication | official | S1, S2 |
| 5 | Chat with CEO | "a 1:1, open ended conversation" | 30 min | unknown | values, ownership, motivation | official | S2, S3 |
| 6 | Offer call | Offer, details, onboarding | not stated | n/a | — | official | S2, S3 |

**Paid work trial: not found.** Neither posting, the careers page, nor the "How We Work" blog series (Volumes I and IV) mentions a paid trial or a paid take-home (S1–S3, S6, S7). Payment for the take-home is not stated.

## 5. Stage-by-stage evaluation targets (brief)

- **Take-home:** Build a small React/Next.js app that calls Railway's public GraphQL API to create or deploy and then delete a service. Handle loading, error and polling states. Deploy it on Railway and write a short README. Ask questions ahead of time, since the posting invites it.
- **60-minute review:** Rehearse a 25-minute narrated walkthrough. Cover why you structured it that way, what breaks at scale, how you would add logs, rollbacks or multi-service support, and how the backend would orchestrate the job (queue or workflow engine; idempotency; retries). This is the candidate's weakest format.
- **Product noodling:** Form opinions on Railway's dashboard, CLI and templates marketplace. Read the Product Engineering team spotlight (linked in S1).
- **Meet the team / CEO:** Prepare stories about ownership, an async written proposal (ERD-style), and working across timezones.

## 6. Competency taxonomy (brief)

- **Frontend:** data fetching and mutation, optimistic UI, real-time status, canvas-style interfaces.
- **Backend:** GraphQL schema and data modelling, long-running async jobs (Temporal), idempotency and retries.
- **Delivery:** ERDs, monitoring, shipping without a manager.
- **Communication:** async writing; live explanation of design.

## 7. Process changes and history

- **2024-02-07 (Ashby text, still shown):** five steps, with the CEO chat merged into the offer step (S1).
- **2026-06-11 (Scalability posting) and the current railway.com page:** six steps, with a separate 30-minute CEO 1:1 and a separate offer call. For the backend role, the take-home is a written system design instead of an app, and two more team members join the review (S2, S3). This was not AI-driven as far as any source says.
- **Company:** Series B of US$100M, announced 2026-01-22 (led by TQ Ventures). The stated plan is to expand the team (S8). No layoffs were found. The posting's "we're 21" headcount is from 2024 and is stale.

## 8. Candidate-report findings

- **None found.** Searches for Railway (railway.com) interview reports on Glassdoor, Reddit, Hacker News and interview databases returned only BNSF Railway and other rail companies. Glassdoor was not fetched directly because it usually returns 403. No candidate claim can be labelled.
- **Applicant pool (inference):** Railway is a prominent developer-tools brand, and this "anywhere in the world" posting has been open for 2.5 years. Expect a large global applicant pool.

## 9. Fit check

**Verdict: `stretch` (preliminary; no hard filter fails).**

| Gap | Evidence |
|---|---|
| Senior title with "autonomously lead, design, and implement" expectations, against about 3 years of experience. No years threshold is stated, so this is not a hard fail. | S1 |
| Complex async backend jobs and workflow orchestration (Temporal). There is no candidate evidence for these. | S1 |
| GraphQL API design. The candidate's stated stack is NestJS, which may cover GraphQL, but this is unverified. | S1 |
| A 30-minute live walkthrough and extension of your own code. This maps directly to the weak areas (explaining aloud; defending architecture). | S1, S2 |
| Pay is unknown, and the location-adjusted pay hint is weak evidence. | S9 |
| Strength: the take-home is a React UI plus API integration plus deployment, which is squarely in the candidate's stack. | S1 |

## 10. Exclusions and unknowns

- India pay level and employment arrangement: unknown.
- Expected time for the take-home and whether it is paid: unknown.
- AI tool rules for the take-home: unknown. Ask in advance (the posting encourages questions).
- The "paid work trial" mentioned in the brief could not be found in any first-party source.
- Candidate reports: none found.

## 11. Source ledger

```yaml
company: "Railway"
anchor: false
match:
  hard_filters:
    eligibility: "pass — 'remote position available anywhere in the world' (S1); India not named but covered; no location question on the form (S10)"
    hiring_now: "pass — https://jobs.ashbyhq.com/railway/6ddcfe47-6cce-469b-ba6d-4f0e83440c9d live 2026-10-09 (evergreen since 2024-02-07)"
  soft_dimensions:
    - dimension: "stack match (React/TypeScript UI + API integration)"
      evidence: ["S1"]
    - dimension: "take-home rather than LeetCode"
      evidence: ["S1", "S2"]
    - dimension: "async, writing-heavy culture (ERDs)"
      evidence: ["S1", "S6"]
fit:
  verdict: "stretch"
  preliminary: true
  gaps:
    - gap: "Senior-titled role expecting autonomous end-to-end product leadership"
      evidence: ["S1"]
    - gap: "Complex async backend jobs / Temporal workflow orchestration"
      evidence: ["S1"]
    - gap: "Live 30-min code walkthrough and extension (weak area: explaining and defending design)"
      evidence: ["S1", "S2"]
    - gap: "Pay unpublished; weak hint of location-adjusted pay"
      evidence: ["S9"]
role:
  title: "Senior Full-Stack Engineer - Product"
  url: "https://jobs.ashbyhq.com/railway/6ddcfe47-6cce-469b-ba6d-4f0e83440c9d"
  seniority: "senior (no years stated)"
  compensation: "not published"
  verified_date: "2026-10-09"
process:
  url: "https://railway.com/careers/full-stack"
  verified_date: "2026-10-09"
  stages:
    - id: "P1"
      name: "Talk with us about the role"
      format: "open-ended call"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["motivation", "career goals"]
      evidence_quality: "official"
      sources: ["S1", "S2"]
    - id: "P2"
      name: "Small project (take-home)"
      format: "async app with UI that spins a container up/down via Railway GQL API, deployed on Railway, submitted before review"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["GraphQL API integration", "frontend UI", "async state", "deployment"]
      evidence_quality: "official"
      sources: ["S1", "S2"]
    - id: "P3"
      name: "Review your solution with the Team"
      format: "live code walkthrough + extension + product/tech discussion"
      timebox: "60 min"
      ai_policy: "unknown"
      competencies: ["problem breakdown", "presenting a solution", "extensibility", "product thinking"]
      evidence_quality: "official"
      sources: ["S1", "S2", "S3"]
    - id: "P4"
      name: "Meet the Team"
      format: "conversations with 4 people from different parts of the company"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["collaboration", "communication"]
      evidence_quality: "official"
      sources: ["S1", "S2"]
    - id: "P5"
      name: "Chat with CEO"
      format: "1:1 open-ended"
      timebox: "30 min"
      ai_policy: "unknown"
      competencies: ["values", "ownership"]
      evidence_quality: "official"
      sources: ["S2", "S3"]
    - id: "P6"
      name: "Offer call"
      format: "offer and onboarding details"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "official"
      sources: ["S2", "S3"]
  changes:
    - date: "2024-02-07 → 2026-06-11"
      change: "CEO chat split into separate 30-min 1:1 plus separate offer call; backend roles get a written system-design take-home and two extra reviewers"
      ai_driven: false
      sources: ["S1", "S2", "S3"]
requirements:
  explicit_required: ["autonomously lead/design/implement front-to-back product", "frontend architecture for data fetch/mutate/render", "complex async backend jobs (build/deploy pipeline)", "TypeScript + GraphQL APIs", "ERDs", "async written + verbal communication"]
  explicit_preferred: ["Rust (or desire to learn) for OSS CLI/Nixpacks"]
  inferred_repeated: ["Temporal", "TypeScript + GraphQL", "ERDs", "ownership/autonomy", "async communication", "Postgres/Node.js (Scalability posting)"]
  ai_expectations: []
uncertainty:
  - claim: "No paid work trial exists"
    reason: "Absent from all first-party sources found; not explicitly denied"
    confidence: "medium"
  - claim: "Pay is location-adjusted"
    reason: "Single tiny Levels.fyi sample"
    confidence: "low"
  - claim: "Take-home AI tool rules"
    reason: "Not stated anywhere"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://jobs.ashbyhq.com/railway/6ddcfe47-6cce-469b-ba6d-4f0e83440c9d"
    title: "Senior Full-Stack Engineer - Product (Ashby posting, via posting API)"
    tier: 1
    published_or_updated: "2024-02-07 (publishedAt)"
    accessed: "2026-10-09"
    freshness: "current (live today)"
    supports: ["eligibility", "requirements", "process"]
  - id: "S2"
    url: "https://railway.com/careers/full-stack"
    title: "Senior Full-Stack Engineer - Product - Careers (railway.com)"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "current (live today)"
    supports: ["process (6 steps, 30-min CEO 1:1)", "location"]
  - id: "S3"
    url: "https://jobs.ashbyhq.com/railway/5f51771e-339f-49f9-8da2-e3c7179c7bad"
    title: "Senior Product Engineer, Scalability (Ashby)"
    tier: 1
    published_or_updated: "2026-06-11"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated language", "process changes"]
  - id: "S4"
    url: "https://api.ashbyhq.com/posting-api/job-board/railway"
    title: "Railway Ashby job board API (8 postings)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["other open roles", "location field Global"]
  - id: "S5"
    url: "https://railway.com/careers"
    title: "Railway careers"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'Work from anywhere — Railway is fully remote'", "no pay numbers"]
  - id: "S6"
    url: "https://blog.railway.com/p/how-we-work"
    title: "How We Work (Jacob Cooper)"
    tier: 2
    published_or_updated: "2021-05-28"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["ERD practice", "async tooling"]
  - id: "S7"
    url: "https://blog.railway.com/p/how-we-work-volume-iv"
    title: "How We Work Volume IV (Jacob Cooper)"
    tier: 2
    published_or_updated: "2025-02-11"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["onboarding expectations; no hiring/trial details"]
  - id: "S8"
    url: "https://siliconangle.com/2026/01/22/intelligent-cloud-infrastructure-startup-railway-gets-100m-simplify-application-deployment/"
    title: "Railway gets $100M (SiliconANGLE)"
    tier: 4
    published_or_updated: "2026-01-22"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Series B funding", "hiring plans"]
  - id: "S9"
    url: "https://www.levels.fyi/companies/railway/salaries"
    title: "Railway salaries (Levels.fyi)"
    tier: 4
    published_or_updated: "2025-12-25"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["sparse pay data; location variation hint"]
  - id: "S10"
    url: "https://jobs.ashbyhq.com/railway/6ddcfe47-6cce-469b-ba6d-4f0e83440c9d/application"
    title: "Application form (Ashby, via public GraphQL)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["form asks only name/email/resume/'Why Railway?'"]
```
