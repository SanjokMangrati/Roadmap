# Dscout — Software Engineer - India (primary) and Applied AI Engineer - India

Researched 2026-10-09. All access dates are 2026-10-09.

## 1. Summary

- **Role:** Software Engineer - India (full-stack, AI-native product features). Dscout asks for 2–7 years of experience. The company is a US qualitative/UX research platform with headquarters in Chicago and a remote-first workforce. A second India role, Applied AI Engineer - India (2–5 years), wants LLM agents in production plus evaluation harnesses, which is a poor match for the candidate.
- **Eligibility: pass.** The posting's location is "Remote - India" and it is live on Greenhouse today (first published 2026-08-21). The employment structure for India (Dscout's own Indian entity, an employer of record, or a contractor arrangement) is **not stated anywhere** and stays unverified.
- **Pay versus target: unknown.** Dscout does not publish an India range. The application form asks "What are your compensation expectations for your next role?", so the candidate must name a number. No India pay data was found.
- **Process shape (official, generic):** application review, then a 30-minute recruiter screen, then virtual team interviews with the hiring manager and team (which "may" include a brief practical exercise), then a decision. No software-engineer-specific candidate reports exist from the last 12 months.
- **AI policy: unknown officially.** However, the posting *requires* "Comfort using AI coding tools (Cursor, Claude Code, Copilot, or similar) as a real part of your workflow". Dscout's public interview-exercise repository (created September 2026) ships `AGENTS.md` files that brief AI coding agents. This suggests AI use is expected in exercises, but that is an inference.
- **Fit: stretch (preliminary).** Experience years and full-stack scope fit. The gaps are the required production experience of building features on LLM APIs or agents, the product-ownership and user-research expectations, and defending tradeoffs aloud. Dscout's backend is Elixir/Phoenix with a GraphQL (Absinthe) API, **not Ruby on Rails** as assumed, so the candidate's Node/NestJS depth will not transfer directly. The posting does not require Elixir.

## 2. Hard filters

| Filter | Result | Evidence |
|---|---|---|
| India-based remote allowed | **pass** | Greenhouse job record location: "Remote - India" (S1). The posting also says: "Dscout is proud to support a remote-first workforce and enable employees to work from almost anywhere. At this time, however, we are unable to hire in the following locations: Montana, Hawaii, Alaska, and Washington DC." (S1) |
| Posting live today | **pass** | Present in the Greenhouse board API on 2026-10-09 with id 4370266009, first published 2026-08-21 and updated 2026-08-21 (S1, S3). The Applied AI Engineer - India role (4370258009) is also live (S2). |
| Employment type | **unverified** | The posting says only: "Note: Some of the benefits listed below apply only to U.S.-based employees. We offer a similarly competitive benefits program in the UK..." (S1). India is not mentioned. Built In's employer profile lists "India" as an office location with no city (S10). A search for a registered Dscout India private limited company found none (search only; the official company registry was not checked). In April 2026 Dscout absorbed the Userology product and engineering team, whose founders previously worked at Indian companies (S12, S18). That team may be the seed of the India hub, but this is an inference. **Ask the recruiter whether the role is direct employment through an Indian entity, an employer of record (for example Deel or Remote), or a contractor arrangement.** |
| Work authorization | No restriction stated for India. The US-only clause appears only on the Senior DevOps posting (S4). | S1, S4 |

## 3. Current role requirements (Software Engineer - India, S1)

**Seniority and scope**
- `required` 2–7 years of software engineering experience "shipping full-stack product features to real users".
- `required` Comfort working across the frontend and backend, "picking up whatever's needed to ship".
- `required` End-to-end ownership, from "an ambiguous problem statement to shipped, working software".

**AI and LLM work**
- `required` "Working fluency with LLM-based systems: you've built features on top of LLM APIs or agents and understand prompting and non-determinism well enough to design good product experiences around them."
- `required` "Comfort using AI coding tools (Cursor, Claude Code, Copilot, or similar) as a real part of your workflow." The same expectation appears in the Applied AI Engineer, Senior DevOps ("You use AI coding tools daily") and AI Product Manager postings (S2, S4, S5), so it is `inferred from repeated job language` as a company-wide norm.
- `nice to have` Conversational or voice AI features. Familiarity with LLM observability and evaluation tools (the Applied AI posting names Braintrust, LangSmith and Datadog LLM Observability).
- Role duty: build product surfaces "that make AI-driven behavior understandable, controllable, and trustworthy", integrating "LLM-based features and agent outputs into real product flows".

**Product orientation and autonomy**
- `required` A "track record of taking a vague, underspecified problem and shipping something real without a fully-scoped ticket".
- `required` "Strong product judgment: you can reason about tradeoffs (build vs. buy, LLM vs. deterministic logic, speed vs. polish) and push back when a request doesn't serve the user". **This lines up directly with the candidate's weak area of defending decisions.**
- `required` Empathy for users. Making independent smaller UX calls using the design system.
- `required` "High agency and a bias toward shipping."
- Duty: "Talk to users directly when you need to". `nice to have` Running lightweight user research yourself, or partnering with UX research teams.
- Duty: "Ship fast, instrument what you ship, and iterate based on real usage". This implies metrics and observability (`inferred`).

**Stack (from first-party and employer-supplied sources; the posting itself names no stack)**
- Backend: **Elixir** with **Phoenix**. The API is GraphQL through **Absinthe**. Background jobs run on **Oban**. Phoenix Channels and Presence power realtime features. **PostgreSQL** is the main datastore and **AWS** is the hosting platform (S11, an old posting; S10). Dscout's GitHub organization maintains Elixir libraries that were still being pushed in 2026 (`medea`, `samly`, S9).
- Frontend: **React** with **Apollo**, plus **TypeScript** and JavaScript (S10, S11).
- Mobile: Swift and Kotlin (S10). The 2026 mobile interview exercise uses Kotlin Compose Multiplatform with a Node/Express backend (S7).
- Other: Python for AI and data work (the 2026 AI data engineering exercise uses Python, DuckDB and pandas, and targets Snowflake, S8). WebRTC handles live video (S11). CircleCI/RWX, Docker and Terraform appear in the DevOps posting (S4).
- **Ruby on Rails: not supported by current evidence.** The GitHub organization's only Ruby repositories date from 2013–2014 (S9). Nothing current mentions Rails.

**Not mentioned in the posting** (so the expectation is unknown): system design depth, specific database skills, testing, security, on-call, and written communication. The DevOps posting notes the team "deploy[s] to production many times a day" (S4), which implies continuous delivery (`inferred`).

**Compensation:** Not published. The posting promises "A strong and competitive compensation package with a built-in bonus and equity program", but its benefits list (401k, US holidays) is US-centric.

## 4. Interview stages

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Application review | Recruiter screens the profile. The application asks for compensation expectations, and the cover letter is optional. | — | unknown | Experience fit, compensation fit | official | S6, S1 |
| 2 | Initial screening | "30 min conversation with our recruiter to share more about the role and to discuss your experience" | 30 min | unknown | Background, motivation, compensation, logistics | official | S6 |
| 3 | Team interviews | "virtual interview, you'll connect with the hiring manager and team members to explore your experience and fit". Candidates "may also complete a brief exercise to showcase your skills in a practical, real-world context". | not stated | unknown. Expected use of AI agents is suggested by the 2026 exercise repository (inference). | Experience depth, team fit, practical skill | official (generic, not role-specific) | S6 |
| 3a | Practical exercise (role-specific variant unknown) | The 2026 public exercises are realistic repositories with AGENTS.md briefs. The mobile "partner challenge" asks for a feature plan (architecture approach, ticket breakdown, release plan) on a deliberately uneven codebase. The AI data engineering round 1 is a take-home Python/SQL file "send back... with any notes on tradeoffs or assumptions". **No Software Engineer exercise was found.** | not stated | unknown (AGENTS.md suggests agents are used; inference) | Planning under ambiguity, tradeoffs, edge cases, debuggability, testing approach | anecdotal (inferred from the company's own repositories, not linked to this role) | S7, S8 |
| 4 | Decision | "thoughtfully review everything you've shared"; offer or a personal follow-up | — | — | — | official | S6 |

## 5. Stage-by-stage evaluation targets

- **Recruiter screen (30 min):** Have a two-minute story ready about shipping a full-stack feature from a vague request. Give a compensation figure. Using the candidate's 1.5–2 lakh INR/month take-home target, quote a gross annual cost-to-company, since the application asks this before any call. Also ask about the employment structure (entity, employer of record or contractor) and about the team and time-zone overlap.
- **Team interviews:** Expect probing on (a) one LLM-powered feature you built: prompting, how you handled non-deterministic output, error and empty states, and how you decided LLM versus deterministic logic. The posting phrases this exact tradeoff, and it is the candidate's biggest gap. (b) A time you pushed back on a request for user reasons. (c) How you instrument and iterate after launch. Practise saying the reasoning aloud, because the "product judgment" and "push back" requirements are tested by talking.
- **Practical exercise:** Based on Dscout's 2026 exercise style (S7, S8), prepare for a realistic, deliberately messy codebase or dataset where you must (1) read a requirements document plus a half-finished plan, (2) resolve open questions such as whether logic runs on the client or the server, and how the release is ordered, (3) write a ticket breakdown and release plan, and (4) say how you would test it. Practise directing an AI coding agent through a repository via AGENTS.md-style instructions while checking its output.

## 6. Competency taxonomy for Dscout

- **AI-native product engineering:** LLM API integration, prompt and context design, handling non-determinism in the UI (confidence cues, editability, fallbacks), the LLM-versus-rules decision, basic evaluation awareness.
- **Full-stack delivery:** React/TypeScript UI with GraphQL (Apollo) data fetching; backend APIs (Elixir/Phoenix at Dscout, but the posting is stack-agnostic); PostgreSQL; instrumentation.
- **Product judgment:** scoping ambiguous problems, build-versus-buy, speed-versus-polish, user empathy, independent UX calls within a design system, talking to users.
- **Craft:** edge cases, error states, interaction details.
- **Execution habits:** daily use of AI coding tools with verification, shipping small and iterating, high agency.
- **Communication:** explaining tradeoffs and pushback, writing tradeoff and assumption notes (the exercises ask for them).

## 7. Process changes and history

- **2026-07-17:** Dscout created public interview repositories `dscout-interview-aide` (AI data engineering round 1, a Python plus SQL take-home) and `dscout-interview-mle` (empty) (S8, S9).
- **2026-09-16 to 2026-10-05:** Dscout created `dscout-interview`, which groups exercises by department (mobile "partner challenge", DevOps "build concurrency"). Each exercise includes `AGENTS.md` instructions for AI coding agents (S7). This looks like an AI-era shift towards realistic, agent-assisted work samples. It is AI-driven by inference (high confidence for those departments, unknown for Software Engineer - India).
- **2026-04-14:** The Userology team joined Dscout to launch Dscout AI Studio (S12). The India product roles were first published 2026-08-21 (S1–S3, S5).
- **Historical (2018–2019, stale):** Glassdoor excerpts for Chicago Research Advisor roles describe a long process with several conversations and a project (S16). Not engineering, and not current.

## 8. Candidate-report findings

- **No software engineering candidate reports were found for 2025–2026.** Glassdoor returned HTTP 403 when fetched. Search excerpts showed only 2018–2019 non-engineering reports (`stale`). No reports were found on Reddit, Blind or LeetCode Discuss.
- A Dataford "interview guide" lists generic questions (structured debugging, synchronous versus asynchronous programming). It is an aggregator with no sourcing, so it is used as a lead only (tier 5, `anecdotal`).
- Because the India roles are new (August 2026), the absence of reports is expected.

## 9. Fit check

**Verdict: stretch (preliminary).** Hard requirements pass: years (3 is within 2–7) and India location.

| Gap | Evidence | Severity |
|---|---|---|
| Built features on LLM APIs or agents in production (required) | S1 "Working fluency with LLM-based systems: you've built features on top of LLM APIs or agents". The candidate profile lists AI-assisted *coding*, not LLM *product* work. | High. Build one real LLM feature (streaming, structured output, fallbacks) before applying. |
| Product judgment and pushing back, said aloud | S1 "Strong product judgment... push back when a request doesn't serve the user". The candidate self-reports weakness defending decisions. | High |
| Backend stack mismatch (Elixir/Phoenix/GraphQL versus Node/NestJS/REST) | S10, S11 | Medium. The posting is stack-agnostic, but daily work will be in Elixir. Learning GraphQL basics is cheap. |
| User-research and design-system UX calls | S1 | Low to medium |
| Pay unknown, applicant pool | No India pay data. Inference: a US brand with "Remote - India" engineering roles on Greenhouse plus mirrors on Built In, freehire and workopia will draw a large applicant pool. | Unknown |

The Applied AI Engineer - India role is **out of reach (preliminary)**. It requires production LLM agents plus evaluation harnesses (offline evaluation sets, LLM-as-judge) and experiments run in production (S2), which are absent from the candidate's profile.

## 10. Exclusions and unknowns

- Employment structure for India (entity, employer of record or contractor) is unknown. India pay band is unknown. Whether the Software Engineer exercise is a take-home or live is unknown. The number of interview rounds within "team interviews" is unknown. The official AI policy during interviews is unknown.
- Glassdoor (403) and Wellfound were not fetched. Levels.fyi has no Dscout engineering data.
- Funding: the last known round is a $70M Series C in March 2022 led by Guidepost Growth Equity (search excerpt; no newer round found). Headcount estimates range from about 180 (Built In) to about 269 (Revelio, March 2026, -0.2% year over year). TrueUp lists no known layoffs. No layoffs or hiring freezes were found for the last 12 months, but the absence of reports is not proof.

## 11. Source ledger

```yaml
company: "Dscout"
anchor: false
match:
  hard_filters:
    eligibility: "pass — Greenhouse location 'Remote - India'; employment structure (entity/EOR/contractor) unverified"
    hiring_now: "pass — https://job-boards.greenhouse.io/dscout/jobs/4370266009 live in board API 2026-10-09 (published 2026-08-21)"
  soft_dimensions:
    - dimension: "US company, remote-first, Series C (2022)"
      evidence: [S6, S10, S13]
    - dimension: "Full-stack mid-level scope (2-7 yrs)"
      evidence: [S1]
    - dimension: "AI-native product work; AI coding tools required"
      evidence: [S1, S2, S4, S5]
fit:
  verdict: "stretch"
  preliminary: true
  gaps:
    - gap: "Production LLM/agent feature experience required"
      evidence: [S1]
    - gap: "Product-judgment tradeoff defense and push-back, verbally"
      evidence: [S1]
    - gap: "Backend is Elixir/Phoenix/GraphQL, not Node"
      evidence: [S10, S11]
    - gap: "Pay band unknown; must state comp expectation on application"
      evidence: [S1]
role:
  title: "Software Engineer - India"
  url: "https://job-boards.greenhouse.io/dscout/jobs/4370266009"
  seniority: "2-7 years (mid)"
  compensation: "not published; 'competitive... bonus and equity'"
  verified_date: "2026-10-09"
process:
  url: "https://dscout.com/careers"
  verified_date: "2026-10-09"
  stages:
    - id: "1"
      name: "Application review"
      format: "Recruiter review; application asks comp expectations"
      timebox: ""
      ai_policy: "unknown"
      competencies: ["experience fit"]
      evidence_quality: "official"
      sources: [S6, S1]
    - id: "2"
      name: "Recruiter screen"
      format: "Video/phone conversation"
      timebox: "30 min"
      ai_policy: "unknown"
      competencies: ["background", "motivation", "comp"]
      evidence_quality: "official"
      sources: [S6]
    - id: "3"
      name: "Team interviews (+ possible brief practical exercise)"
      format: "Virtual interviews with hiring manager and team; may include practical exercise"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["experience depth", "fit", "practical skill"]
      evidence_quality: "official"
      sources: [S6]
    - id: "3a"
      name: "Practical exercise (format for SWE unknown)"
      format: "Realistic repo or take-home with AGENTS.md; planning/tradeoff notes (seen for mobile, devops, AI data eng)"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["ambiguity handling", "tradeoffs", "release planning", "edge cases", "testing"]
      evidence_quality: "anecdotal"
      sources: [S7, S8]
    - id: "4"
      name: "Decision"
      format: "Offer or personal follow-up"
      timebox: ""
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "official"
      sources: [S6]
  changes:
    - date: "2026-07-17"
      change: "Public interview repo for AI data engineering round 1 (Python+SQL take-home)"
      ai_driven: null
      sources: [S8]
    - date: "2026-09-16/2026-10-05"
      change: "Public interview-exercise repo grouped by department; exercises ship AGENTS.md for AI coding agents"
      ai_driven: true
      sources: [S7]
requirements:
  explicit_required: ["2-7 yrs full-stack shipping", "frontend+backend", "ambiguous-problem ownership", "LLM API/agent feature experience", "product judgment and tradeoffs", "user empathy", "design-system UX calls", "AI coding tools in workflow", "high agency"]
  explicit_preferred: ["conversational/voice AI", "LLM observability/eval tooling", "UX research partnership", "talking to users"]
  inferred_repeated: ["AI coding tools daily across all roles", "non-determinism framing", "ship fast and instrument", "deploy many times a day"]
  ai_expectations: ["Build product UX around non-deterministic LLM output", "Cursor/Claude Code/Copilot as real workflow", "know LLM vs deterministic tradeoff"]
uncertainty:
  - claim: "India employment is via an Indian entity or EOR"
    reason: "Not stated anywhere; Built In lists India office without city; no entity found in search"
    confidence: "low"
  - claim: "SWE exercise is agent-assisted"
    reason: "Inferred from other departments' 2026 exercise repos"
    confidence: "medium"
  - claim: "Stack is Elixir/Phoenix + React/Apollo/TS, not Rails"
    reason: "Employer-supplied Built In profile + old Elixir posting + active Elixir OSS; no current SWE posting names stack"
    confidence: "high"
sources:
  - id: "S1"
    url: "https://job-boards.greenhouse.io/dscout/jobs/4370266009"
    title: "Software Engineer - India (Greenhouse; API boards-api.greenhouse.io/v1/boards/dscout/jobs/4370266009)"
    tier: 1
    published_or_updated: "2026-08-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["eligibility", "requirements", "AI tools", "benefits note", "application asks comp"]
  - id: "S2"
    url: "https://job-boards.greenhouse.io/dscout/jobs/4370258009"
    title: "Applied AI Engineer - India"
    tier: 1
    published_or_updated: "2026-08-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated AI language", "Applied AI requirements"]
  - id: "S3"
    url: "https://boards-api.greenhouse.io/v1/boards/dscout/jobs"
    title: "Dscout Greenhouse board (10 open jobs)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["open postings", "India roles list"]
  - id: "S4"
    url: "https://job-boards.greenhouse.io/dscout/jobs/4402627009"
    title: "Senior DevOps Engineer (Remote - US)"
    tier: 1
    published_or_updated: "2026-09-25"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["AWS, Terraform, CircleCI/RWX", "deploy many times a day", "AI tools daily"]
  - id: "S5"
    url: "https://job-boards.greenhouse.io/dscout/jobs/4370272009"
    title: "AI Product Manager - India"
    tier: 1
    published_or_updated: "2026-08-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated AI-native language"]
  - id: "S6"
    url: "https://dscout.com/careers"
    title: "Dscout Careers (interview process, remote-first, HQ Chicago)"
    tier: 1
    published_or_updated: "undated (footer 2026)"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["process stages", "remote-first"]
  - id: "S7"
    url: "https://github.com/dscout/dscout-interview"
    title: "dscout/dscout-interview (branches partner-challenge/mobile, devops-challenge/build-concurrency)"
    tier: 2
    published_or_updated: "2026-10-05"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["exercise style", "AGENTS.md", "planning/release tasks"]
  - id: "S8"
    url: "https://github.com/dscout/dscout-interview-aide"
    title: "Dscout AI Data Engineering Interview: Round 1"
    tier: 2
    published_or_updated: "2026-08-03"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["take-home format with tradeoff notes", "Python/DuckDB/Snowflake"]
  - id: "S9"
    url: "https://github.com/dscout"
    title: "Dscout GitHub organization"
    tier: 2
    published_or_updated: "2026-10-06"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Elixir libraries active", "Ruby repos only 2013-2014"]
  - id: "S10"
    url: "https://builtin.com/company/dscout"
    title: "Dscout on Built In (employer profile: tech stack, offices, 180 employees)"
    tier: 3
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["stack: Elixir, Phoenix, React, Apollo, TypeScript, Kotlin, Swift, Python", "India office"]
  - id: "S11"
    url: "https://www.workingnomads.com/jobs/lead-software-engineer-elixir-dscout"
    title: "Lead Software Engineer - Elixir (expired repost)"
    tier: 4
    published_or_updated: "~2024 ('posted 2 years ago')"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["Elixir, Absinthe GraphQL, Phoenix channels, Oban, PostgreSQL, AWS, React"]
  - id: "S12"
    url: "https://dscout.com/people-nerds/introducing-dscout-ai-studio"
    title: "Introducing Dscout AI Studio (Userology team joins)"
    tier: 2
    published_or_updated: "2026-04-14"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Userology acquisition/team join"]
  - id: "S13"
    url: "https://beringea.com/news/in-the-news/dscout-raises-usd70m-to-accelerate-growth-empower-organizations-to-deliver-human-insight-at-enterprise-scale"
    title: "Dscout raises USD70M (Series C, Guidepost; via search excerpt)"
    tier: 4
    published_or_updated: "2022-03"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["funding stage"]
  - id: "S14"
    url: "https://trueup.io/co/dscout"
    title: "TrueUp Dscout (no known layoffs; via search excerpt)"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["no layoffs found"]
  - id: "S15"
    url: "https://www.reveliolabs.com/companies/dscout/employees"
    title: "Revelio Labs Dscout headcount (~269, Mar 2026; via search excerpt)"
    tier: 4
    published_or_updated: "2026-03"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["headcount stable"]
  - id: "S16"
    url: "https://www.glassdoor.com/Interview/dscout-Interview-Questions-E1311226.htm"
    title: "Glassdoor Dscout interviews (HTTP 403; excerpts show 2018-2019 non-engineering only)"
    tier: 4
    published_or_updated: "2019"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["no SWE reports"]
  - id: "S17"
    url: "https://dataford.io/interview-guides/dscout/software-engineer"
    title: "Dataford Dscout SWE guide (aggregator)"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["lead only"]
  - id: "S18"
    url: "https://www.everydev.ai/developers/userology"
    title: "Userology founders profile (via search excerpt)"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["Userology founders' Indian-company backgrounds (lead only)"]
```
