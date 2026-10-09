# Infisical: Full Stack Engineer (primary) and Senior Full Stack Engineer

Researched and verified 2026-10-09.

## 1. Summary

- **Role:** Full Stack Engineer (posted 2026-10-02, live today), plus Senior Full Stack Engineer (same posting text with "TypeScript (3+)"). The team works directly with the Chief Technology Officer on secrets management, PKI (certificates), KMS (key management) and PAM (privileged access) product lines.
- **Eligibility: pass, with a conflict to resolve.** The posting text says "Based in the Americas (US or Canada), Brazil, India, UK, or EU. Must work US hours." But the Ashby location fields list only the US, UK, Brazil and Canada. The required application question is "Do you live and work in the Americas?", and Infisical's Y Combinator job page limits the same role to the Americas. Ask the recruiter to confirm India in writing before investing heavily. You would also have to work US hours.
- **Pay vs target:** No India figure is published. Infisical's Y Combinator listing shows US$100K–180K plus 0.05–0.25% equity for Full Stack Engineer and US$180K–250K for Senior. That listing is scoped to the Americas, so whether India hires are paid on the same band is unknown. Even a steep location discount would likely clear 1.5–2 lakh INR per month, but this is unverified.
- **Process:** No first-party description exists. One anonymous Glassdoor report (June 2025) describes a founder screen, a founder technical discussion, a take-home (build a secret-sharing app), a take-home review with a system-design extension, a founder chat and an in-person "work day" in San Francisco (whether it was paid is not stated). This is anecdotal.
- **AI policy in interviews:** unknown. The codebase is openly AI-assisted (it has CLAUDE.md, AGENTS.md and agent skills, plus Greptile AI review), and the posting asks engineers to "experiment with novel approaches for applying AI".
- **Fit: stretch (preliminary).** The stack is a near match (TypeScript, React, Node, PostgreSQL). The gaps are a self-declared "exceptionally high" bar, security-domain depth, a GitHub link required at application, founder-led architecture defence (a known weak area) and the eligibility ambiguity.

## 2. Hard filters

**(a) India eligibility: explicit in text, contradicted by structured data and the form. Verdict `pass` with a conflict flag.**
- The Ashby posting API description reads: "Based in the Americas (US or Canada), Brazil, India, UK, or EU. Must work US hours." (S1). The rendered careers page at infisical.com/careers/full-stack-engineer repeats it (S2), and the Senior posting has the identical sentence (S1, S3).
- Ashby's structured fields say `location: United States`, with `secondaryLocations: United Kingdom, Brazil, Canada` and `workplaceType: Remote`. India and EU countries are absent (S1).
- The application form for both roles has the required yes/no question "Do you live and work in the Americas?" (S4).
- Infisical's Y Combinator jobs page lists Full Stack Engineer as "San Francisco, CA, US / Remote (US; CA; PA; AR; BR; BO; UY; CL; …)". These are Americas-only country codes. Senior is listed as "Remote (US; CA)" (S5).
- The public company handbook's hiring page lists India among the countries Infisical can legally hire from (S6). That page was last changed 2024-07-16, so it is stale.
- **Resolution:** Following the rule that the current official source wins and role-specific beats generic, the posting text (2026-10-02) is the most specific and current statement, and it names India. The form question and the Y Combinator mirror suggest the Americas are preferred or that the text was edited without updating the form. This stays visible as a conflict. Answering "No" to the Americas question may trigger an automatic filter (inference).

**(b) Live today: `pass`.** Both postings appear in the Ashby job board API on 2026-10-09 with `publishedAt` 2026-10-02 (S1) and on infisical.com/careers (S7).

**Employment type:** The posting says "FullTime". Employee vs employer-of-record vs contractor for India is not stated. The handbook refers to ending "your contract" and to a 3-month probation and severance (S8), which does not settle it. US-only health benefits are stated on the careers page (S7).

**Working hours:** "Must work US hours" is a requirement (S1). The candidate says they have no timezone limits, so this passes, but it means night shifts from India.

## 3. Current role requirements

| Item | Label | Evidence |
|---|---|---|
| "Deep technical mastery of the JavaScript ecosystem, particularly React.js, Node.js, and TypeScript" | required | S1 |
| Senior role adds "TypeScript (3+)" years | required (Senior only) | S1 |
| Years of experience for Full Stack Engineer: none stated. The Y Combinator listing says "Any (new grads ok)" | required: none; Senior listing on Y Combinator says 3+ years | S1, S5 |
| "Exceptional attention to detail and eager to learn" | required | S1 |
| "Bias toward action—able to make decisions with incomplete information, iterate quickly, and take calculated risks" | required (autonomy) | S1 |
| Location (see hard filters) and "Must work US hours" | required | S1 |
| GitHub/GitLab (or equivalent) URL; a number for years of experience; "up to three bullets showing exceptional ability" | required at application | S4 |
| Optional 1–2 minute Loom video on why Infisical | optional | S4 |
| Expertise in Go | nice to have | S1 |
| "Some understanding of devops/developer tools" | nice to have | S1 |
| Founder or startup experience | nice to have | S1 |
| Open-source or developer-tools building (professional or personal) | nice to have | S1 |
| "Excellent written and oral communication skills to interact with customers directly" | nice to have in the list, but the role description says "communicating directly with enterprise customers", so effectively expected | S1 |
| Security domain work: secret rotation, dynamic secrets, gateways to private resources, EST and KMIP protocols, cloud secret syncs, PKI, PAM, KMS | inferred from the job description's examples of past work | S1 |
| AI-assisted development: the repo ships CLAUDE.md, AGENTS.md, `.agents/skills`, and Greptile AI review configuration (updated 2026-10-06/08) | inferred from first-party engineering sources | S9 |
| AI and large-language-model product work: "Experiment with novel approaches for applying AI to secrets management"; backend depends on the Vercel `ai` SDK and `@ai-sdk/anthropic` | preferred / inferred | S1, S10 |
| Compensation: Full Stack US$100K–180K, equity 0.05–0.25%; Senior US$180K–250K (Y Combinator listing, Americas scope) | published, scope unclear for India | S5, S11 |
| Testing: the codebase uses Vitest unit and e2e suites, Playwright e2e that gates production deploys, and a Go blackbox suite | inferred from first-party repo | S9 |
| Incidents: a weekly 24x7 on-call rotation from Thursday to Thursday, covering pager alerts and customer support tickets | inferred from the engineering handbook (2025-01) | S12 |
| System design: design documents are required for features over 1 engineering week or "high-security" work | inferred from the engineering handbook (2025-07) | S13 |

**Repeated language across Infisical's 10 open postings:** "exceptional talent", "open source security infrastructure stack for the AI era", remote with a San Francisco presence, and US or EST hours. The Technical Recruiter posting says the company will "run a fast, rigorous interview process" and "use and build AI tools across sourcing, outreach, and screening" (S1). Expect AI-assisted screening of applications (inference).

**Actual tech stack (first-party, GitHub `Infisical/infisical`, 29.7k stars, pushed 2026-10-09; S9, S10):**
- **Backend:** TypeScript, Fastify 4 (not NestJS), PostgreSQL via Knex (raw query builder, migrations, Zod schemas generated from the database), Redis/ioredis, BullMQ queues, OpenTelemetry, CASL for permissions, and many cloud SDKs (AWS, GCP KMS, OCI).
- **Partial Go rewrite:** `backend-go/` uses chi and pgx against the same database. Go is 1.2M bytes vs 45.6M bytes of TypeScript.
- **Frontend:** a React 18 single-page app (not Next.js) built with Vite, TanStack Router, React Query and Table, react-hook-form with Zod, Tailwind CSS v4, and Radix UI.
- **Other:** Rust crates compiled to WebAssembly, Helm charts, Docker, a FIPS 140-2 image, and Mintlify docs.
- **Code quality rules** in `backend/CODE_QUALITY.md` cover explicit validation on every input, pagination of third-party APIs, short transactions on a small connection pool, REST-aligned interfaces and readable audit logs.

## 4. Interview stages

No first-party process document exists. The handbook hiring page covers strategy and geography only. The table maps only what sources support.

| Order | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Application | Ashby form: GitHub URL (required), years, Americas yes/no, three "exceptional ability" bullets, optional Loom | none | unknown (the recruiter role uses AI screening tools) | Track record, open-source signal, written concision | official | S4, S1 |
| 1 | Founder screen | Call with one co-founder | unknown | unknown | Motivation, background | anecdotal (1 report, June 2025) | S14 |
| 2 | Technical discussion | Conversation with a second founder | unknown | unknown | Technical depth | anecdotal | S14 |
| 3 | Take-home | "Build a secret sharing application" | unknown | unknown | Full-stack build, security basics (encryption, expiry, access) | anecdotal | S14 |
| 4 | Take-home review and system design | Walk through the take-home, then model and extend it | unknown | unknown | Defending design decisions, extension design | anecdotal | S14 |
| 5 | Founder chat | Casual talk with the third founder | unknown | unknown | Culture and values | anecdotal | S14 |
| 6 | Work day | In person at the San Francisco office: audit-log refactor proposal and implementation, a frontend bug fix, and a new CLI feature. No fixed end time | about one day | unknown | Real-codebase navigation, prioritization, shipping speed | anecdotal | S14 |

Glassdoor's aggregate says the process averages 10 days across 3 interviews (all roles); that comes from search snippets because the page itself returned 403 (S14). The single software engineer report says 2 weeks. Whether India candidates do the work day in person or remotely is unknown.

## 5. Stage-by-stage evaluation targets

- **Application (official):** Have a GitHub profile that shows real TypeScript, React and Node work, ideally one security or developer-tool project. Write three quantified "exceptional ability" bullets. Record the optional Loom. It is cheap and the founders ask for it. Decide how to answer "Do you live and work in the Americas?" honestly ("No"), and mention India eligibility, quoting the posting text, in the bullets or Loom.
- **Founder screens (anecdotal):** Prepare a 2-minute story on why secrets management and open source matter to you. Have one example of shipping with incomplete information, since bias to action is a stated requirement.
- **Take-home "secret sharing app" (anecdotal):** Practise building a one-time-secret app in TypeScript with React, Node (Fastify is a bonus) and PostgreSQL. Cover client-side or at-rest encryption, expiry, view-once semantics, rate limiting, input validation and tests. Mirror the repo's CODE_QUALITY.md rules.
- **Take-home review and system design (anecdotal):** This is the candidate's weakest area. Practise defending choices aloud: key management, where encryption happens, how to scale reads, audit logging, multi-tenant permissions, and how you would add rotation or sharing to teams. Read Infisical's docs on secret rotation, dynamic secrets and KMS so your vocabulary matches theirs.
- **Work day (anecdotal):** Practise cloning `Infisical/infisical`, running `docker-compose.dev.yml`, and making a small fix in both the frontend and backend. That exact skill (navigating a large, partly documented TypeScript monorepo quickly) is what the report describes. Ask up front whether it is paid, remote, and timeboxed.

## 6. Competency taxonomy

- **TypeScript full-stack:** React 18 single-page app patterns (TanStack Router and Query, react-hook-form with Zod); Node with Fastify (plugins, hooks, schema validation); PostgreSQL with Knex (migrations, transactions, pagination, connection-pool limits); Redis and BullMQ job queues.
- **Security engineering:** secrets lifecycle (rotation, dynamic secrets, sync); encryption at rest and in transit; PKI and certificates (X.509, ACME, EST); KMS and KMIP basics; RBAC and ABAC (CASL); audit logging; SAML, OIDC and SCIM authentication.
- **Systems and operations:** Docker, Helm and Kubernetes basics; self-hosted deployment constraints (FIPS); OpenTelemetry metrics; on-call incident response.
- **Product and customer:** talking directly to enterprise customers; writing lightweight design docs (overview, context, solution, diagrams).
- **AI:** working fluently with Claude Code or similar inside an AGENTS.md/CLAUDE.md codebase; ideas for applying large language models to secrets or security workflows.
- **Nice to have:** Go (chi, pgx), CLI development, open-source contribution etiquette.

## 7. Process changes and history

- **2024-07-16:** The handbook hiring page states "100% inbound" recruiting and a hiring-country list that includes India (S6). Stale.
- **2025-06:** A Glassdoor report describes the 6-stage founder-led process with a take-home and work day (S14). Old by the brief's 12-month rule.
- **2025-06-06:** Series A of $16M led by Elad Gil; total raised about $19M (S15, S5).
- **2026-04-28:** A third-party article on the Full Stack Engineer role reports "US, Canada or LATAM" only (S16). That conflicts with today's posting.
- **2026-10-02:** Current postings published with India named in the text (S1).
- **2026-10 (ongoing):** A Technical Recruiter is being hired to "run a fast, rigorous interview process" with AI screening tools (S1). The process is likely to be re-formalised soon (inference). No AI-driven interview format change has been documented.

## 8. Candidate-report findings

- **Founder-led screens:** anecdotal (1 report, Glassdoor, June 2025, via search snippet; page blocked with 403).
- **Take-home: secret-sharing app:** anecdotal (same report).
- **Take-home review plus system-design extension:** anecdotal.
- **In-person work day with an open-ended scope (audit-log refactor, frontend bug, CLI feature):** anecdotal. The reviewer was negative and called it "cheap labor" and "unstructured".
- **Average 10-day process:** anecdotal (Glassdoor aggregate of 3 interviews, all roles).
- No Reddit, Blind, LeetCode Discuss or YouTube reports were found. Glassdoor (.com and .com.mx) was blocked for direct fetch, so content comes from search-engine snippets only.

## 9. Fit check

**Verdict: `stretch`, preliminary.** The hard filters pass with a conflict on eligibility. Years: none required for Full Stack, and the candidate's 3 years matches Senior's "TypeScript (3+)". Skill verdicts rest on self-reported depth only.

Gaps:
1. **Eligibility ambiguity.** The text names India, but the form and Y Combinator mirror say Americas (S1, S4, S5). This could end the application at screening.
2. **"Exceptionally high" bar.** The company says it with "exceptional ability" bullets and a GitHub link required (S1, S4). The candidate's public GitHub strength is unknown.
3. **Security domain depth.** PKI, KMS, KMIP, EST and secret rotation are the daily work (S1). The candidate profile shows no security specialisation.
4. **Architecture defence and thinking aloud.** These are the candidate's stated weak areas. The reported take-home review, system-design extension and founder technical discussion lean on exactly this (S14).
5. **Stack deltas.** Fastify instead of NestJS, a Vite React single-page app instead of Next.js, Knex instead of an ORM, and optional Go (S9). These are small deltas.
6. **US-hours requirement** (S1). The candidate accepts it, but it is a sustained night shift in India.
7. **Crowded pool (inference).** A 29.7k-star open-source brand, Y Combinator, a remote US$100K+ band and Hacker News visibility suggest heavy applicant volume. No applicant counts were found.

## 10. Exclusions and unknowns

- No first-party interview process or AI-use policy for interviews.
- No India-specific salary band, and no statement of employment model (employee, employer-of-record or contractor) for India.
- Whether the work day is paid, remote-eligible or still used.
- No Levels.fyi or Glassdoor salary data points (the Levels.fyi page had none; Glassdoor was blocked).
- No layoffs or hiring freeze found in the last 12 months (search on 2026-10-09). Absence of news is not proof.
- Team size is 50 per the Y Combinator page (S5).

## 11. Source ledger

```yaml
company: "Infisical"
anchor: false
match:
  hard_filters:
    eligibility: "pass (conflicting) - posting text: 'Based in the Americas (US or Canada), Brazil, India, UK, or EU. Must work US hours.' But structured locations = US/UK/BR/CA, required form question 'Do you live and work in the Americas?', YC mirror Americas-only. Confirm with recruiter."
    hiring_now: "pass - https://jobs.ashbyhq.com/infisical/351240fc-0dd3-48c3-a46e-e8861cae27cd (published 2026-10-02, in API 2026-10-09)"
  soft_dimensions:
    - dimension: "Stack match: TypeScript/React/Node/PostgreSQL"
      evidence: ["S1", "S9", "S10"]
    - dimension: "Remote from India with US hours"
      evidence: ["S1", "S6"]
    - dimension: "Pay likely above target (unverified for India)"
      evidence: ["S5", "S11"]
    - dimension: "Seed-Series A startup, cash-flow positive per press"
      evidence: ["S15"]
fit:
  verdict: "stretch"
  preliminary: true
  gaps:
    - gap: "India eligibility contradicted by application form and YC mirror"
      evidence: ["S1", "S4", "S5"]
    - gap: "Exceptionally high bar; GitHub required; exceptional-ability bullets"
      evidence: ["S1", "S4"]
    - gap: "Security domain (PKI, KMS, KMIP, EST, rotation) not in profile"
      evidence: ["S1"]
    - gap: "Defending architecture aloud (take-home review + system design, founder technical talk)"
      evidence: ["S14"]
    - gap: "Fastify/Knex/Vite SPA vs NestJS/Next.js; Go nice-to-have"
      evidence: ["S9", "S1"]
role:
  title: "Full Stack Engineer (also Senior Full Stack Engineer)"
  url: "https://jobs.ashbyhq.com/infisical/351240fc-0dd3-48c3-a46e-e8861cae27cd"
  seniority: "Mid (no minimum years; YC says new grads OK). Senior variant: TypeScript 3+ years"
  compensation: "YC listing (Americas scope): FSE $100K-$180K + 0.05-0.25% equity; Senior $180K-$250K. India band unpublished."
  verified_date: "2026-10-09"
process:
  url: "none first-party; https://www.glassdoor.com/Interview/Infisical-Interview-Questions-E9917816.htm (blocked, snippets only)"
  verified_date: "2026-10-09"
  stages:
    - id: "INF-0"
      name: "Application form"
      format: "Ashby form: GitHub URL, years, Americas Y/N, 3 exceptional-ability bullets, optional Loom"
      timebox: "n/a"
      ai_policy: "unknown"
      competencies: ["track record", "open-source signal", "written concision"]
      evidence_quality: "official"
      sources: ["S4"]
    - id: "INF-1"
      name: "Founder screen"
      format: "call"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["motivation", "background"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
    - id: "INF-2"
      name: "Founder technical discussion"
      format: "conversation"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["technical depth"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
    - id: "INF-3"
      name: "Take-home: secret sharing application"
      format: "take-home build"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["full-stack build", "security basics"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
    - id: "INF-4"
      name: "Take-home review + system design extension"
      format: "discussion"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["design defence", "data modelling", "extensibility"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
    - id: "INF-5"
      name: "Third founder chat"
      format: "casual conversation"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["culture fit"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
    - id: "INF-6"
      name: "In-person work day (San Francisco)"
      format: "real-codebase tasks: audit-log refactor, frontend bug fix, CLI feature"
      timebox: "about one day, no fixed end"
      ai_policy: "unknown"
      competencies: ["codebase navigation", "prioritisation", "shipping speed"]
      evidence_quality: "anecdotal"
      sources: ["S14"]
  changes:
    - date: "2024-07-16"
      change: "Handbook hiring page: 100% inbound strategy; India on hiring-country list"
      ai_driven: false
      sources: ["S6"]
    - date: "2026-04-28"
      change: "Third-party report: FSE role limited to US/Canada/LATAM"
      ai_driven: false
      sources: ["S16"]
    - date: "2026-10-02"
      change: "Current FSE/Senior postings name India in text"
      ai_driven: false
      sources: ["S1"]
    - date: "2026-10"
      change: "Hiring a Technical Recruiter to run a 'fast, rigorous' process using AI sourcing/screening tools"
      ai_driven: true
      sources: ["S1"]
requirements:
  explicit_required: ["Deep mastery of React.js, Node.js, TypeScript", "Senior: TypeScript 3+ years", "Attention to detail, eager to learn", "Bias toward action", "Americas/Brazil/India/UK/EU and US hours", "GitHub URL at application"]
  explicit_preferred: ["Go", "devops/developer tools", "founder/startup experience", "open source/dev tools", "excellent written and oral communication with customers"]
  inferred_repeated: ["exceptional talent / high hiring bar", "direct enterprise-customer communication", "security infrastructure domain (secrets, PKI, KMS, PAM)", "remote with SF presence", "on-call rotation", "design docs for >1 week or high-security work"]
  ai_expectations: ["Experiment with applying AI to secrets management/security infrastructure", "Codebase built for AI agents (CLAUDE.md, AGENTS.md, agent skills, Greptile review)", "Backend uses Vercel AI SDK with Anthropic provider"]
uncertainty:
  - claim: "India-based candidates are eligible"
    reason: "Text says yes; structured locations, required Americas question and YC mirror say Americas"
    confidence: "medium"
  - claim: "Interview stages (founder screens, secret-sharing take-home, work day)"
    reason: "Single anonymous Glassdoor report from June 2025, read via snippets"
    confidence: "low"
  - claim: "Pay for India hires"
    reason: "Only an Americas-scoped USD band is published"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://api.ashbyhq.com/posting-api/job-board/infisical"
    title: "Infisical Ashby job board API (Full Stack Engineer, Senior Full Stack Engineer, Technical Recruiter, Design Engineer)"
    tier: 1
    published_or_updated: "2026-10-02 (engineering postings)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["requirements", "location text", "structured locations", "live status", "AI experimentation", "recruiter AI screening"]
  - id: "S2"
    url: "https://infisical.com/careers/full-stack-engineer"
    title: "Full Stack Engineer - Infisical careers"
    tier: 1
    published_or_updated: "2026-10-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["location text", "no salary on page"]
  - id: "S3"
    url: "https://infisical.com/careers/senior-full-stack-engineer"
    title: "Senior Full Stack Engineer - Infisical careers"
    tier: 1
    published_or_updated: "2026-10-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Senior location text", "TypeScript 3+", "optional Loom"]
  - id: "S4"
    url: "https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobPosting (infisical, 351240fc..., 3c9ae12c...)"
    title: "Ashby application form for both roles"
    tier: 1
    published_or_updated: "2026-10-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'Do you live and work in the Americas?' required", "GitHub URL required", "exceptional-ability bullets", "optional Loom"]
  - id: "S5"
    url: "https://www.ycombinator.com/companies/infisical/jobs"
    title: "Jobs at Infisical - Y Combinator"
    tier: 1
    published_or_updated: "unknown (live 2026-10-09)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["FSE $100K-$180K, any experience", "Senior $180K-$250K, 3+ years", "Americas-only location lists", "team size 50", "$19M raised", "W23"]
  - id: "S6"
    url: "https://github.com/Infisical/infisical/blob/main/company/handbook/hiring.mdx"
    title: "Infisical Handbook - Hiring"
    tier: 2
    published_or_updated: "2024-07-16"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["100% inbound recruiting", "India on hiring-country list"]
  - id: "S7"
    url: "https://infisical.com/careers"
    title: "Infisical Careers"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["remote or office", "US-only health benefits", "10 open roles", "15+ countries"]
  - id: "S8"
    url: "https://github.com/Infisical/infisical/blob/main/company/handbook/compensation.mdx"
    title: "Infisical Handbook - Compensation"
    tier: 2
    published_or_updated: "2024-11-18"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["3-month probation", "10 weeks severance", "contract wording"]
  - id: "S9"
    url: "https://github.com/Infisical/infisical/blob/main/CLAUDE.md"
    title: "Infisical repo CLAUDE.md (architecture, testing, code quality)"
    tier: 2
    published_or_updated: "2026-10-08"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Fastify/Knex/PostgreSQL/BullMQ", "React 18 + Vite + TanStack", "Go partial rewrite", "Rust WASM", "test suites", "AI-agent tooling (AGENTS.md, .agents, .greptile)"]
  - id: "S10"
    url: "https://github.com/Infisical/infisical (backend/package.json, frontend/package.json, languages API)"
    title: "Infisical GitHub repository"
    tier: 2
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["dependency stack incl. ai + @ai-sdk/anthropic", "29.7k stars", "TypeScript-dominant"]
  - id: "S11"
    url: "https://ecosistemastartup.com/infisical-18-8m-contrata-full-stack-engineers-remotos/"
    title: "Infisical $18.8M: contrata Full Stack Engineers remotos"
    tier: 5
    published_or_updated: "2026-04-28"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["$100K-$180K + 0.05-0.25% equity (corroborates S5)"]
  - id: "S12"
    url: "https://github.com/Infisical/infisical/blob/main/company/documentation/engineering/oncall.mdx"
    title: "Infisical - On call rotation"
    tier: 2
    published_or_updated: "2025-01-13"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["weekly 24x7 on-call, support tickets"]
  - id: "S13"
    url: "https://github.com/Infisical/infisical/blob/main/company/documentation/engineering/how-to-write-design-doc.mdx"
    title: "Infisical - How to write a design document"
    tier: 2
    published_or_updated: "2025-07-16"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["design docs for >1 week or high-security features"]
  - id: "S14"
    url: "https://www.glassdoor.com/Interview/Infisical-Interview-Questions-E9917816.htm"
    title: "Infisical Interview Experience & Questions - Glassdoor (403 on fetch; read via search snippets)"
    tier: 4
    published_or_updated: "review dated 2025-06"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["founder screens", "secret-sharing take-home", "review + system design", "in-person work day", "10-day average"]
  - id: "S15"
    url: "https://fortune.com/2025/06/06/infisical-raises-16-million-series-a-led-by-elad-gil-to-safeguard-secrets"
    title: "Infisical raises $16 million Series A led by Elad Gil - Fortune"
    tier: 4
    published_or_updated: "2025-06-06"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["Series A $16M", "investors"]
  - id: "S16"
    url: "https://ecosistemastartup.com/infisical-18-8m-contrata-full-stack-engineers-remotos/"
    title: "Infisical $18.8M: contrata Full Stack Engineers remotos (location claim)"
    tier: 5
    published_or_updated: "2026-04-28"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["earlier FSE posting limited to US/Canada/LATAM"]
```
