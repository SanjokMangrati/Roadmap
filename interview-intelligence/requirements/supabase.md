# Supabase: Software Engineer - Auth, Software Engineer - Branching, and Supalite Engineer

Researched and verified 2026-10-09 (REACH list, lighter pass).

## 1. Summary

- **Headline: no TypeScript/React/Next.js product-facing role is open.** Of 53 open postings, none is for the dashboard (Studio) or another frontend or full-stack product surface (S1).
  - The two named roles are Go-heavy infrastructure or protocol roles. **Software Engineer - Auth** requires "4+ years ... Go in production" and "2+ years ... on an authentication system" (S2). **Software Engineer - Branching** requires Go and TypeScript, "3+ years ... cloud infrastructure or distributed systems", and AWS (S3).
  - The closest match is **Supalite Engineer**, a TypeScript-native re-implementation of Supabase on SQLite and Postgres. It asks for "substantial backend or full-stack experience with strong fluency in TypeScript" and states no years. It is backend and developer-tooling work, not React (S4).
- **Eligibility: `pass` (global wording; India not named in postings).** Postings say "Fully Remote — We hire globally. We believe you can do your best work from anywhere." (S2–S4). The application form asks for "Passport Country" and "Country of Residence" (S6). A Himalayas company profile lists India among employee countries (S8, tier 4).
- **Pay vs target:** No range is published for these roles. Levels.fyi has a thin sample, with a company median total compensation of US$115,575 (S11). That is far above 1.5–2 lakh INR per month if it applies, but India-specific pay is unknown.
- **Process:** No first-party page describes the interview loop. A "How we hire" text on Supabase's Himalayas profile (likely supplied by the company, but unconfirmed) lists recruiter → technical interview with team lead → second technical with a department lead or peer → founders interview. All calls are "1:1 and usually take between 20-45 minutes", over Google Meet (S8).
- **"GitHub-PR / async hiring style": not verified as a formal step.** First-party evidence shows only that a GitHub profile is a *required* application field and there is an optional open-source contribution question (S6). Postings also stress RFC writing and "working in public repositories on a remote, async team" (S2, S4). No source describes PR-based or async-only interviews.
- **AI policy in interviews:** `unknown` for engineering. A non-engineering posting (Partner Operations & Systems Lead) says candidates "will complete a short build exercise ... show us how you'd use Claude Code (or a similar tool)" (S10). That shows AI-expected exercises exist at Supabase, but this is not evidence for engineering roles.
- **Fit: `out of reach` for Auth and Branching (hard requirements); `stretch` for Supalite (preliminary).**

## 2. Hard filters

**(a) India eligibility: `pass` with a note.**
- Every posting: "Fully Remote. We hire globally. We believe you can do your best work from anywhere. There are no Supabase offices" (S2–S4). Ashby location: "Remote, Global" (S1).
- supabase.com/careers: "We hire globally", team spans "60+ countries" (S7).
- Form: required "Passport Country" and "Country of Residence" fields (S6). These could be used to filter, but they do not exclude anyone on their face.
- India is not named in any first-party source. The Himalayas profile says Supabase "has employees in United States, Australia, Singapore, Ireland, Romania, Japan, Canada, India" (S8; tier 4, undated).

**(b) Live today: `pass`.** Auth (published 2026-04-08), Branching (2026-09-02) and Supalite (2026-07-17) are all in the Ashby API on 2026-10-09 (S1–S4).

**Employment type:** "FullTime". The legal arrangement (employee, employer-of-record or contractor) is not stated. Benefits include ESOP, "100% of health insurance for employees and 80% for dependents, wherever you are", a tech allowance and a co-working allowance (S2).

## 3. Current role requirements

**Software Engineer - Auth (S2, S6)**

| Item | Label |
|---|---|
| "4+ years of professional experience writing and shipping Go in production" | required |
| "2+ years of professional experience working on an authentication system" | required |
| "Strong relational database experience (Postgres or MySQL)" | required |
| Strong TypeScript; web fundamentals (cookies, sessions, JWT, HTTP, browser APIs) | preferred |
| OAuth/OIDC/SAML; cryptography fundamentals | preferred |
| Next.js (or another SSR framework) plus a traditional framework (Rails/Django/Laravel) | preferred; also a required self-rating question on the form |
| RFC writing ("RFC process is an important part") | preferred, repeated |
| Kubernetes, AWS, observability (Prometheus/Grafana/OpenTelemetry), safe migrations at scale | preferred |

**Software Engineer - Branching (S3)**

| Item | Label |
|---|---|
| "Go and Typescript required" | required |
| "3+ years of experience building and operating cloud infrastructure or distributed systems at scale" | required |
| "familiarity with AWS constructs is required"; AWS SDKs and IaC (Pulumi/Terraform) | required / strongly preferred |
| CI/CD runner orchestration on EKS/ECS, job scheduling, retries and timeouts, observability | required (responsibilities) |
| Async or globally distributed team experience; ownership | preferred |

**Supalite Engineer (S4) — closest match**

| Item | Label |
|---|---|
| "Substantial backend or full-stack experience with strong fluency in TypeScript"; has built or contributed to a backend system, framework or developer platform | required (no years stated) |
| Read unfamiliar code (GoTrue in Go, PostgREST in Haskell) and match its behaviour in TypeScript | required |
| SQL and relational databases; Postgres vs SQLite differences | required |
| Conformance tests and specs; "bias toward compatibility and correctness" | required |
| CLI, local tooling and docs; developer experience | required |
| "Comfortable working in public repositories on a remote, async team"; clear writing | required |
| Supabase stack, developer CLIs, open-source maintenance | nice to have |

**Repeated language across engineering postings (S1):** async remote work; written communication and RFCs; open source and the community (GitHub, Discord); Postgres; operating at scale and on-call. Most engineering roles are Postgres, Go, Rust or infrastructure. TypeScript appears in Auth, Branching, Functions, Supalite and Compute Capacity. React and Next.js appear only as client-library context in Auth. Compensation is unpublished except for one Bay Area product manager role (US$200K–270K).

## 4. Interview stages

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Application | Ashby form: GitHub profile (required), LinkedIn, open-source contributions (optional), passport and residence country, role-specific self-ratings (Auth: auth experience, Go/TypeScript proficiency, web frameworks) | — | unknown | open-source track record, stack depth | official | S6 |
| 1 | Recruiter interview | 1:1 video (Google Meet); career path and goals | 20–45 min | unknown | motivation, fit | company-supplied text on a third-party site (treat as semi-official) | S8 |
| 2 | Technical interview with team lead | 1:1 video; hard skills and problem-solving | 20–45 min (stated for all calls) | unknown | role-specific technical depth | semi-official | S8 |
| 3 | Second technical with department lead or peer | 1:1 video; deeper skills and role expectations | 20–45 min | unknown | technical depth, collaboration | semi-official | S8 |
| 4 | Founders interview | Meet the co-founders; values, mission, vision | 20–45 min | unknown | values, culture | semi-official | S8 |
| ? | Take-home (4–6 h, "most senior/staff roles") | Extend an open-source library or build on Supabase foundations; write-up weighted | 4–6 h | unknown | code quality, documentation | unverified (tier-5 guide with no citations) | S9 |

## 5. Stage-by-stage evaluation targets (brief)

- **Application:** A public GitHub with real TypeScript and Postgres work is effectively required. An open-source contribution to a Supabase repository (for example supabase-js or the CLI) is the strongest signal the form invites.
- **Technical rounds:** Be ready for role-specific depth: Postgres (row-level security, migrations), TypeScript API design and, for Supalite, behavioural compatibility testing.
- **Founders:** Prepare to talk about open source, async work and ownership.

## 6. Competency taxonomy (brief)

- **Database:** Postgres internals, row-level security, migrations, SQL vs SQLite semantics.
- **Backend:** TypeScript services, REST compatibility (PostgREST), auth protocols (JWT, OAuth).
- **Infrastructure (Auth and Branching):** Go, AWS, Kubernetes, observability.
- **Working style:** RFCs, public repositories, async collaboration, community support.

## 7. Process changes and history

- No dated first-party process page was found, so no changes can be recorded.
- **Company:** "Over $1B raised (including our $500M Series F)", about 400 team members in 60+ countries (S2). No layoffs were found.

## 8. Candidate-report findings

| Claim | Label | Source |
|---|---|---|
| A take-home of 4–6 hours for senior and staff roles, with the write-up weighted | anecdotal at best (guide sites; no cited reports) | S9 |
| Timelines vary widely (support about 7 days; senior engineering roles up to about 70 days) | anecdotal (search summary of Glassdoor) | S12 |
| Glassdoor interview pages | blocked (HTTP 403 on .com and .co.in); content not used | S12 |
| Supabase "hires like an open-source organization" | CEO statement in an investor interview; culture, not a process step | S13 |

**Applicant pool (inference):** Supabase is a top developer brand with "Remote, Global" roles, so pools are very large. The role-specific self-rating questions on the form suggest automated or quick screening on hard requirements.

## 9. Fit check

**Verdict: `out of reach` for Auth and Branching (final, years and hard skills); `stretch` for Supalite (preliminary).**

| Gap | Evidence |
|---|---|
| Auth: no Go and no professional auth-system experience; "4+ years Go" and "2+ years auth" are required | S2 |
| Branching: Go required; 3+ years cloud infrastructure or distributed systems; AWS required (candidate has 0.5 years AWS) | S3 |
| Supalite: TypeScript and Postgres match, but it needs developer-platform or framework-building experience, reading Go and Haskell reference code, and spec and conformance-testing discipline. No candidate evidence for any of these. | S4 |
| No React/Next.js product role is open, so the candidate's frontend strength is not used | S1 |
| A GitHub profile is required; the candidate supplied no portfolio | S6 |

## 10. Exclusions and unknowns

- Official engineering interview loop, take-home existence and AI rules: unknown.
- The "GitHub-PR-based hiring" claim: not verified in any first-party source.
- India pay level and employment arrangement: unknown.
- Studio/dashboard roles: none open today. Re-check the Ashby board periodically.

## 11. Source ledger

```yaml
company: "Supabase"
anchor: false
match:
  hard_filters:
    eligibility: "pass — 'We hire globally ... from anywhere' (S2–S4); India not named in first-party sources; form collects passport and residence country (S6)"
    hiring_now: "pass — Auth https://jobs.ashbyhq.com/supabase/e569b7f7-fa8f-4139-86f6-4f52b456882d ; Branching https://jobs.ashbyhq.com/supabase/06752423-eebb-472c-95b5-c7ff2559fd60 ; Supalite https://jobs.ashbyhq.com/supabase/b75ba81e-54cc-4393-a575-bc41776b0113 (all live 2026-10-09)"
  soft_dimensions:
    - dimension: "TypeScript + Postgres overlap (Supalite)"
      evidence: ["S4"]
    - dimension: "open-source / GitHub signal at application"
      evidence: ["S6"]
fit:
  verdict: "out of reach (Auth, Branching); stretch (Supalite)"
  preliminary: true
  gaps:
    - gap: "Auth requires 4+ yrs Go and 2+ yrs auth systems"
      evidence: ["S2"]
    - gap: "Branching requires Go, 3+ yrs infra/distributed systems, AWS"
      evidence: ["S3"]
    - gap: "Supalite needs developer-platform/framework building and cross-language spec reading"
      evidence: ["S4"]
    - gap: "No React/Next.js product role open"
      evidence: ["S1"]
role:
  title: "Software Engineer - Auth; Software Engineer - Branching; Supalite Engineer"
  url: "https://jobs.ashbyhq.com/supabase/b75ba81e-54cc-4393-a575-bc41776b0113"
  seniority: "Auth: 4+ yrs Go; Branching: 3+ yrs infra; Supalite: unstated ('substantial')"
  compensation: "not published (Levels.fyi company median TC ~US$115.6K, thin sample)"
  verified_date: "2026-10-09"
process:
  url: "https://himalayas.app/companies/supabase"
  verified_date: "2026-10-09"
  stages:
    - id: "P0"
      name: "Application"
      format: "Ashby form: GitHub required, OSS question, passport/residence country, self-ratings"
      timebox: "n/a"
      ai_policy: "unknown"
      competencies: ["open source", "stack depth"]
      evidence_quality: "official"
      sources: ["S6"]
    - id: "P1"
      name: "Recruiter interview"
      format: "1:1 Google Meet"
      timebox: "20-45 min"
      ai_policy: "unknown"
      competencies: ["motivation", "career goals"]
      evidence_quality: "anecdotal"
      sources: ["S8"]
    - id: "P2"
      name: "Technical interview (team lead)"
      format: "1:1 video"
      timebox: "20-45 min"
      ai_policy: "unknown"
      competencies: ["hard skills", "problem solving"]
      evidence_quality: "anecdotal"
      sources: ["S8"]
    - id: "P3"
      name: "Technical interview (department lead or peer)"
      format: "1:1 video"
      timebox: "20-45 min"
      ai_policy: "unknown"
      competencies: ["technical depth", "role expectations"]
      evidence_quality: "anecdotal"
      sources: ["S8"]
    - id: "P4"
      name: "Founders interview"
      format: "1:1 video with co-founders"
      timebox: "20-45 min"
      ai_policy: "unknown"
      competencies: ["values", "mission fit"]
      evidence_quality: "anecdotal"
      sources: ["S8"]
  changes: []
requirements:
  explicit_required: ["Auth: 4+ yrs Go, 2+ yrs auth systems, relational DB", "Branching: Go + TypeScript, 3+ yrs infra/distributed, AWS", "Supalite: substantial backend/full-stack with strong TypeScript, SQL, reading unfamiliar code, tests/specs, async public-repo work, clear writing"]
  explicit_preferred: ["TypeScript + Next.js/SSR (Auth)", "RFC writing", "Kubernetes/AWS/observability", "IaC (Pulumi/Terraform)", "Supabase stack / CLI / OSS maintenance"]
  inferred_repeated: ["async remote work", "written communication / RFCs", "open source + community", "Postgres", "operating at scale"]
  ai_expectations: ["none stated for engineering roles; a non-engineering role's exercise expects Claude Code use (S10)"]
uncertainty:
  - claim: "Supabase uses a GitHub-PR / async-oriented interview process"
    reason: "No first-party source; only GitHub-required form field and async culture language"
    confidence: "low"
  - claim: "Four-stage 1:1 process"
    reason: "Text on Himalayas profile; first-person but not confirmed company-authored; undated"
    confidence: "medium"
  - claim: "Take-home for senior roles"
    reason: "Only uncited guide sites"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://api.ashbyhq.com/posting-api/job-board/supabase"
    title: "Supabase Ashby job board API (53 postings)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["no frontend/Studio role open", "repeated language"]
  - id: "S2"
    url: "https://jobs.ashbyhq.com/supabase/e569b7f7-fa8f-4139-86f6-4f52b456882d"
    title: "Software Engineer - Auth"
    tier: 1
    published_or_updated: "2026-04-08"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Auth requirements", "global remote wording", "benefits", "company size/funding"]
  - id: "S3"
    url: "https://jobs.ashbyhq.com/supabase/06752423-eebb-472c-95b5-c7ff2559fd60"
    title: "Software Engineer - Branching"
    tier: 1
    published_or_updated: "2026-09-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Branching requirements"]
  - id: "S4"
    url: "https://jobs.ashbyhq.com/supabase/b75ba81e-54cc-4393-a575-bc41776b0113"
    title: "Supalite Engineer"
    tier: 1
    published_or_updated: "2026-07-17"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["closest TypeScript full-stack role"]
  - id: "S5"
    url: "https://jobs.ashbyhq.com/supabase/3ab0b926-c9b5-4197-aff2-88d5bf009e13"
    title: "Software Engineer - Functions (Compute)"
    tier: 1
    published_or_updated: "2026-05-13"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["5+ yrs Rust + TypeScript; not a fit"]
  - id: "S6"
    url: "https://jobs.ashbyhq.com/supabase/e569b7f7-fa8f-4139-86f6-4f52b456882d/application"
    title: "Auth application form (Ashby, via public GraphQL)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["GitHub required", "OSS question", "passport/residence fields", "self-rating screens"]
  - id: "S7"
    url: "https://supabase.com/careers"
    title: "Supabase careers"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'We hire globally'", "60+ countries", "no process or pay"]
  - id: "S8"
    url: "https://himalayas.app/companies/supabase"
    title: "Supabase company profile — 'How we hire' (Himalayas)"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["4-stage 1:1 process, 20-45 min calls", "India among employee countries"]
  - id: "S9"
    url: "https://www.techinterview.org/companies/supabase/"
    title: "Supabase Interview Guide 2026 (techinterview.org)"
    tier: 5
    published_or_updated: "2026-07-03"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["lead only: take-home claim (uncited)"]
  - id: "S10"
    url: "https://jobs.ashbyhq.com/supabase"
    title: "Partner Operations & Systems Lead posting (Ashby board)"
    tier: 1
    published_or_updated: "2026-09-03"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["company uses Claude-Code build exercise for a non-engineering role"]
  - id: "S11"
    url: "https://www.levels.fyi/companies/supabase/salaries"
    title: "Supabase salaries (Levels.fyi)"
    tier: 4
    published_or_updated: "2026-03-18 to 2026-08-30 (snapshots)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["median TC ~US$115.6K, thin sample"]
  - id: "S12"
    url: "https://www.glassdoor.com/Interview/Supabase-Interview-Questions-E7639911.htm"
    title: "Supabase interviews (Glassdoor)"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["blocked (403); timeline figures via search summary only"]
  - id: "S13"
    url: "https://www.felicis.com/blog/supabase-paul-copplestone-ant-wilson"
    title: "How Supabase Built a $10B Open-Source Postgres Company (Felicis)"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["CEO: hire 'like an open-source organization' (culture, not process)"]
```
