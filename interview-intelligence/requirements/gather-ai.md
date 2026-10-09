# Gather AI: Software Development Engineer II, Full Stack, India (remote)

Last verified: 2026-10-09. Researcher notes: Glassdoor and Peerlist returned HTTP 403 to direct fetches, and the WebFetch tool could not reach gather.ai (its pages were read with curl instead). Content from Glassdoor comes only from search-engine snippets and is marked "(snippet)".

## 1. Summary

- **Role.** "Software Development Engineer II - Full Stack - India" on Gather AI's own Greenhouse board. It was first published 2026-09-21 and updated 2026-09-30. Despite the "Full Stack" title, the posting describes backend and platform work: Python plus Node.js/NestJS, PostgreSQL, queues, Redis, Docker, Kubernetes and Azure. It names no frontend framework.
- **Eligibility: pass.** The location is "Remote (India)", and the posting says "We are hiring an SDE II, Full Stack, for our India-based team" and "This is a fully remote … role". The employment type (employee, employer of record or contractor) is not stated.
- **Pay versus target: unknown.** No salary is published, and no Gather AI India pay data was found. The application form has a required question asking for your compensation expectation.
- **Process: undocumented.** There is no official process page. A Glassdoor page with 8 reviews, rated "very negative" overall (snippet), mentions a system design round and a warehouse-inventory JSON-diff coding problem for a React role.
- **AI policy: unknown.** AI-assisted development is listed as "nice to have".
- **Company.** Series B: $40M in February 2026, $74M raised in total, with stated plans to hire engineers.
- **Fit verdict: stretch (preliminary).** Years, PostgreSQL and NestJS match. The required working Python, and Kubernetes plus Azure or AWS, are probable gaps, and the application form screens on both. The candidate's React strength is barely used in this role.

## 2. Hard filters

| Filter | Result | Evidence |
|---|---|---|
| India-based remote allowed | **Pass** | Greenhouse `"location": {"name": "Remote (India)"}`, office "Remote - India". Posting text: "We are hiring an SDE II, Full Stack, for our India-based team." and "This is a fully remote, hands-on engineering role for someone early in their career who already has experience building production software and wants broader ownership." [G1] |
| Live today | **Pass** | The Greenhouse API returned the job on 2026-10-09 (`updated_at` 2026-09-30), and the hosted URL returned HTTP 200 [G1][G3]. |
| Employment type | **Not stated** | No employee, employer-of-record or contractor wording appears in the posting [G1]. The careers-page benefits (401K, US-style medical) read as US-centric [G7]. Ask the recruiter. |
| Years | **Pass** | "2–5 years of professional software engineering experience" [G1]. The candidate has about 3. |
| Education | Pass if the candidate has a CS degree or equivalent experience | "An engineering degree in Computer Science or equivalent practical experience" [G1] |
| Screening (knock-out) questions | Watch these | The required application questions ask for years with **both Python and Node.js/NestJS**, years deploying and troubleshooting on **Kubernetes and Azure or AWS**, PostgreSQL production and tuning experience, compensation expectation, and start date [G2]. |

Open matching postings (Greenhouse, 2026-10-09) [G3]:
- 1 SDE II Full Stack in India (this role).
- 1 SDE II Data Engineer in India (adjacent, not a match).
- Other India roles: Principal Data Engineer and ML Annotation QA Engineer.
- The board has 10 postings in total.

## 3. Current role requirements (labelled)

All items come from [G1] unless another source is cited.

**Seniority and years**
- 2–5 years of professional software engineering: **required**. The posting calls the role "early in their career" mid-level.

**Languages and frameworks**
- "Production experience with Python and Node.js/NestJS, with strong production depth in at least one and working experience with the other": **required**.
- **Inferred from repeated job language:** Python and Node also appear in the Senior/Staff Full Stack posting, which adds Go [G5].

**Frontend and backend scope**
- The role covers the web platforms behind Drone Vision, MHE Vision and SAGE, "from the customer-facing dashboards down to the APIs, Integration layers and data pipelines".
- No frontend framework is named.
- An older Gather AI frontend posting (closed, updated 2024-10-02) asked for React.js and TypeScript with Jest testing, and listed backend work in Python or Node.js as a nice-to-have [G14]. **Inferred:** the dashboards are probably React. That is low confidence and historical.

**APIs and distributed systems**
- "Experience designing and maintaining REST APIs, not only consuming them": **required**.
- Integrating external systems and handling "retries, duplicate processing, failure handling, and unreliable dependencies": **required**.
- Distributed-systems concepts (async processing, queues, retries, consistency, failure recovery): **required**.
- Message queues such as Kafka, RabbitMQ or SQS: **required**.

**Databases**
- Strong SQL and relational experience, including "complex queries, indexing, schema design, and production performance troubleshooting": **required**.
- PostgreSQL in production with connection management and tuning: a responsibility.
- **Inferred from repeated job language:** PostgreSQL is the core store. The Senior/Staff posting mentions PostgreSQL upgrades and "data-access abstractions that control DB connections" [G5], and the SDE II Data Engineer posting is about moving analytics off production PostgreSQL [G4].

**Caching**
- "Understanding of caching, including what to cache, where … and how invalidation is handled" and "Experience with Redis or another caching technology": **required**.

**Cloud and infrastructure**
- "Experience with Azure or another major cloud provider, deploying and debugging, using Docker, Kubernetes, and CI/CD pipelines": **required**.
- **Inferred from repeated job language:** Azure is the house cloud. Other postings say "Kubernetes on Azure" [G5] and "Azure preferred" [G6].

**Testing**
- Testing appears within the software development lifecycle responsibilities. No specific framework is required.

**Security**
- "Secure coding fundamentals including authentication and authorization, secrets handling, injection risks, and data exposure": **required**.

**Performance, debugging and incidents**
- Monitoring with logs, dashboards and metrics, and diagnosing failures across APIs, queues, databases and multi-service workflows: **required**. The posting asks for experience "beyond simply writing code".

**System design**
- "Work closely with senior engineers on technical design and architecture decisions while progressively taking greater ownership": a responsibility.
- **Preferred:** multi-region or geo-distributed systems (nice to have).

**Product orientation**
- Collaboration with Customer Success and Product.
- **Nice to have:** logistics, warehouse management system or robotics domain experience.

**Written communication (emphasised)**
- "Because our team is distributed across multiple time zones, clear written communication, initiative, and the ability to make progress independently are especially important."
- "Strong written and verbal communication skills in English, with the ability to document decisions, explain tradeoffs, write clear PRs and design notes, and raise blockers early": **required**.
- **Inferred from repeated job language:** the same wording appears in the SDE II Data Engineer posting [G4].

**Autonomy**
- "Identify opportunities to improve … rather than only executing assigned work": a responsibility.

**AI-assisted development**
- "Experience incorporating AI-assisted development into the software development lifecycle" and "Exposure to GenAI code-validation practices or engineering guardrails": **nice to have** [G1].
- In other postings: the Data Engineer posting says "use AI-assisted development" [G4], and the Senior/Staff posting asks for "Practical AI-assisted engineering, using tools such as Claude" [G5].

**AI/LLM product work**
- None in this role. The company's own AI is computer vision and ML for drones and forklift cameras.

**Nice to have**
- Data pipelines, dbt, Airflow or Flink, and Metabase or Superset.

**Compensation and location**
- Compensation is not published. The location is India only and remote.

## 4. Interview stages

There is no official process documentation. The posting and careers page describe no stages [G1][G7]. Only candidate-report evidence exists, and it is thin and not specific to India or SDE II.

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Application with knock-out questions | Greenhouse form: years of Python+Node, Kubernetes+Azure/AWS, PostgreSQL tuning, compensation, start date | n/a | n/a | Stack fit | official | G2 |
| 1 | Recruiter screen | Call | unknown | unknown | Background, fit | anecdotal (described as "unstructured" by a marketing candidate) | G12 (snippet) |
| 2 | Coding round | Live coding, domain-flavoured data task: compare current and new warehouse inventory JSON across storage locations, then find changed, unchanged, newly occupied and emptied locations. Follow-ups on optimisation, edge cases and code quality | unknown | unknown | JSON parsing, hash maps, lookup optimisation, time complexity, code quality | anecdotal (Senior React Developer role) | G12 (snippet) |
| 3 | System design | Discussion: requirements gathering, high-level design, APIs, data structures, trade-offs. Another listed question was "Snake Game system design" | unknown | unknown | Design fundamentals, trade-off reasoning | anecdotal | G12 (snippet) |
| 4+ | Later stages (hiring manager, leadership, offer) | Not documented | unknown | unknown | unknown | unknown | none |

## 5. Stage-by-stage evaluation targets

0. **Application.** Answer the knock-out questions honestly but completely. Count any production Python (scripts, services, data jobs) and any Kubernetes or AWS deployment work. These answers are probably used for automatic or recruiter filtering [G2].
1. **Recruiter screen.** Be ready to explain end-to-end ownership, production debugging stories, and async written collaboration across time zones [G1]. Have a compensation figure ready, in rupees of fixed cost-to-company (see Section 9).
2. **Coding round.** Practise data-reconciliation problems in Python or TypeScript: diffing two JSON snapshots keyed by location, hash-map lookups, O(n) versus O(n²) trade-offs, and edge cases such as duplicates, missing keys and empty locations [G12]. Narrate your reasoning aloud, because the candidate's self-reported weak area is explaining thought process.
3. **System design.** Prepare an integration-heavy design: ingest warehouse management system data from external systems with retries and idempotency (deduplication), a queue (Kafka, RabbitMQ or SQS), a PostgreSQL schema with indexes, a Redis caching and invalidation plan, and Kubernetes deployment with observability [G1][G5]. Practise requirements gathering first; the report says it was evaluated [G12].
4. **Written-communication signal (throughout).** Bring a sample design note or PR description. The posting stresses documenting decisions and trade-offs [G1].

## 6. Competency taxonomy for Gather AI

- **Backend services:** Python and Node.js/NestJS services, REST API design, and integrations with external warehouse management systems (WMS) [G1][G5].
- **Reliability patterns:** retries, duplicate processing (idempotency), failure handling, unreliable dependencies, and failure recovery [G1].
- **Data:** PostgreSQL schema design, complex queries, indexing, connection management and performance tuning, plus Redis caching and invalidation [G1][G4].
- **Async:** message queues (Kafka, RabbitMQ, SQS), async workflows and consistency [G1].
- **Infrastructure and operations:** Docker, Kubernetes, CI/CD on Azure (or another major cloud), logs, metrics and dashboards, and incident diagnosis across services [G1][G5][G6].
- **Security:** authentication and authorization, secrets, injection risks and data exposure [G1].
- **Communication:** written design notes, PRs and trade-off explanations, and raising blockers early in a distributed team [G1][G4].
- **Coding fundamentals (from the report):** JSON processing, hash maps, complexity analysis and edge cases [G12].
- **Nice to have:** data pipelines (dbt, Airflow), BI tools, domain knowledge, and AI-assisted development with guardrails [G1].

## 7. Process changes and history (dated)

- **2024-10 (historical).** Gather AI hired a remote "Software Engineer, Frontend" (React, TypeScript, Jest). That posting is now closed [G14]. It suggests earlier frontend hiring that targeted React.
- **2026-02-09.** Gather AI raised a $40M Series B led by Smith Point Capital Management. Coverage says the money will be used partly to hire engineers [G9][G10].
- **2026-05-29.** The Glassdoor interview page was last updated, with 8 reviews and an overall "very negative interview experience" rating [G12 snippet].
- **2026-07 to 2026-09.** The company is building an India engineering team. India-remote postings: Principal Data Engineer (published 2026-07-14), ML Annotation QA Engineer (2026-09-04), SDE II Full Stack (2026-09-21) and SDE II Data Engineer (2026-09-30) [G3].
- **AI-driven interview changes:** none documented.

## 8. Candidate-report findings

- **Anecdotal.** A coding round used a warehouse-inventory JSON comparison problem, with optimisation, edge-case and code-quality follow-ups. It was for a Senior React Developer role, with date and location unknown [G12 snippet].
- **Anecdotal.** The system design round evaluated requirements gathering, HLD, APIs, data structures and trade-offs. "Snake Game system design" was also listed [G12 snippet].
- **Anecdotal.** The overall interview experience is rated "very negative". A Product Marketing Manager candidate described the recruiter screen as unstructured [G12 snippet].
- **Anecdotal (employee reviews, not interviews).** Glassdoor shows a 3.9 average from 7 reviews. Implementation engineers complained of "very low compensation compared to industry standards" and of leadership being out of touch. These are US field roles, not India engineering [G13 snippet].
- **Not found.** No Reddit, Blind, LeetCode Discuss or India-specific candidate reports exist for Gather AI engineering. Scoutify's "Gather" page is generic and possibly refers to a different company, so it was excluded.

## 9. Fit check

**Verdict: stretch (preliminary).**

**Hard requirements (final):**
- India remote: pass.
- Years (2–5 needed, about 3 held): pass.
- Degree or equivalent: assumed pass.
- Employment type: unverified.

**Skill gaps (preliminary, because the candidate's stack depth is self-reported):**
1. **Python in production.** It is required as at least "working experience" alongside Node/NestJS, and the application form screens on years with both [G1][G2]. The candidate reports no Python. This is the biggest gap.
2. **Kubernetes and Azure (or AWS).** Required, and screened in the form [G1][G2]. The candidate has GCP 1 year and AWS 0.5 years, with Docker and Kubernetes depth unknown. Azure is the house cloud [G5][G6].
3. **Message queues (Kafka, RabbitMQ, SQS) and Redis.** Required [G1]. The candidate's depth is unknown.
4. **Production operations.** Monitoring, incident diagnosis and post-incident improvement are required [G1]. Unknown.
5. **Written trade-off documentation.** Required, and emphasised for a distributed team [G1]. The candidate's weak area is explaining and defending architecture decisions.
6. **Strengths.** PostgreSQL 3 years, a direct match for the core store [G1]. Node/NestJS 3 years, which can serve as the "strong depth" language [G1]. AI-assisted coding is a nice-to-have bonus [G1]. React is barely relevant: no frontend framework is listed, and only a 2024 posting suggests React dashboards [G14].

**Pay:**
- No published range and no Gather AI India pay data was found (Levels.fyi, Glassdoor and AmbitionBox searches turned up nothing).
- The candidate's take-home target of 1.5–2 lakh a month is roughly ₹24–33 lakh fixed cost-to-company (estimate, under the new tax regime with standard provident fund). If Gather AI hires through an employer of record or as contractors, the cost-to-company structure differs; a contractor pays their own tax and receives no provident fund.
- Employee reviews mention low pay for US field roles [G13]. That is weak evidence about India engineering pay.
- **Pay versus target is unknown.** Ask early, since the form requires your expectation.

**Company signals:**
- Series B: $40M on 2026-02-09, $74M raised in total, bookings "2.5x year over year" [G8][G9][G10].
- No layoffs or hiring freeze found for 2025–2026; absence of reports is not proof.
- Headcount is small. Crunchbase lists 101–250 employees [G16].
- The CTO is Andrew Hoffman, formerly of Kiva Systems and Amazon Robotics [G8].

**Applicant pool (inference):**
- Moderate. Gather AI has low brand recognition in India compared with HighLevel.
- The posting is syndicated to Peerlist, Remoteleaf and Built In India mirrors, which widens reach. Applicant counts could not be fetched.

## 10. Exclusions and unknowns

- Employment type (employee, employer of record or contractor) for India is unknown.
- No published pay and no third-party pay data for India.
- The frontend framework for this role is unknown. React is inferred only from a 2024 posting.
- The interview process is undocumented officially, and candidate evidence is limited to one Glassdoor page read through snippets, with no SDE II or India reports.
- The AI-in-interview policy is unknown.
- Built In India mirrors (Hyderabad and Bengaluru) returned 404. An in-office Hyderabad annotation listing seen in snippets could not be verified.
- The Greenhouse metadata names an internal hiring manager. It is deliberately not reproduced here.

## 11. Source ledger

```yaml
company: "Gather AI"
anchor: false
match:
  hard_filters:
    eligibility: "pass — 'Remote (India)'; 'for our India-based team'; 'fully remote'. Employment type not stated (G1)"
    hiring_now: "pass — https://job-boards.greenhouse.io/gatherai/jobs/5243582007 live 2026-10-09 (updated 2026-09-30)"
  soft_dimensions:
    - dimension: "Backend-heavy: Python + Node.js/NestJS, PostgreSQL, queues, Redis"
      evidence: [G1, G5]
    - dimension: "Azure + Docker/Kubernetes + CI/CD operations"
      evidence: [G1, G5, G6]
    - dimension: "Strong written-communication emphasis for distributed team"
      evidence: [G1, G4]
    - dimension: "Series B, hiring engineers in India"
      evidence: [G3, G8, G9]
fit:
  verdict: "stretch"
  preliminary: true
  gaps:
    - gap: "Production Python (required alongside Node/NestJS; screened in form)"
      evidence: [G1, G2]
    - gap: "Kubernetes + Azure/AWS deployment and troubleshooting (screened in form)"
      evidence: [G1, G2, G5]
    - gap: "Message queues (Kafka/RabbitMQ/SQS) and Redis"
      evidence: [G1]
    - gap: "Production ops / incident diagnosis"
      evidence: [G1]
    - gap: "Written/spoken trade-off explanation (self-reported weak area)"
      evidence: [G1]
    - gap: "Pay unknown vs target"
      evidence: [G1, G2]
role:
  title: "Software Development Engineer II - Full Stack - India"
  url: "https://job-boards.greenhouse.io/gatherai/jobs/5243582007"
  seniority: "SDE II (2–5 years)"
  compensation: "not published; compensation expectation required on application"
  verified_date: "2026-10-09"
process:
  url: "https://job-boards.greenhouse.io/gatherai/jobs/5243582007"
  verified_date: "2026-10-09"
  stages:
    - id: "ga-0"
      name: "Application with knock-out questions"
      format: "Greenhouse form"
      timebox: "n/a"
      ai_policy: "unknown"
      competencies: ["Python+Node years", "Kubernetes+Azure/AWS years", "PostgreSQL tuning", "comp expectation"]
      evidence_quality: "official"
      sources: [G2]
    - id: "ga-1"
      name: "Recruiter screen"
      format: "call"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["background", "fit"]
      evidence_quality: "anecdotal"
      sources: [G12]
    - id: "ga-2"
      name: "Coding round (warehouse inventory JSON diff)"
      format: "live coding"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["JSON parsing", "hash maps", "complexity", "edge cases", "code quality"]
      evidence_quality: "anecdotal"
      sources: [G12]
    - id: "ga-3"
      name: "System design"
      format: "discussion"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["requirements gathering", "HLD", "APIs", "data structures", "trade-offs"]
      evidence_quality: "anecdotal"
      sources: [G12]
  changes:
    - date: "2026-07 to 2026-09"
      change: "India-remote engineering hiring begins (Principal Data Engineer, SDE II Full Stack, SDE II Data Engineer)"
      ai_driven: false
      sources: [G3]
requirements:
  explicit_required:
    - "2–5 years professional software engineering"
    - "CS degree or equivalent practical experience"
    - "Production Python and Node.js/NestJS (strong in one, working in other)"
    - "Production APIs/microservices through deployment and operation"
    - "Strong SQL/relational: complex queries, indexing, schema design, performance troubleshooting"
    - "Design and maintain REST APIs"
    - "External integrations: retries, duplicate processing, failure handling"
    - "Distributed-systems concepts: async, queues, retries, consistency, recovery"
    - "Caching and invalidation; Redis or similar"
    - "Message queues: Kafka, RabbitMQ, SQS or equivalent"
    - "Azure or other major cloud with Docker, Kubernetes, CI/CD"
    - "Git and code review workflows"
    - "Secure coding: authn/authz, secrets, injection, data exposure"
    - "Production operations: monitoring, performance investigation, incident response"
    - "Strong written and verbal English; document decisions and trade-offs"
  explicit_preferred:
    - "Data pipelines, backfills, data quality"
    - "dbt, warehouse/lakehouse modelling, ETL/ELT"
    - "Airflow, Flink or similar"
    - "Metabase, Superset or similar BI"
    - "Multi-region / geo-distributed systems"
    - "Logistics, WMS, robotics domain"
    - "AI-assisted development in SDLC"
    - "GenAI code-validation practices / guardrails"
  inferred_repeated:
    - "Azure is the house cloud (Kubernetes on Azure; Azure preferred)"
    - "PostgreSQL is the core production database"
    - "Written communication across time zones stressed in India postings"
    - "AI-assisted delivery with tools such as Claude expected at senior levels"
  ai_expectations:
    - "Nice to have: AI-assisted development across SDLC and GenAI code-validation guardrails (G1)"
uncertainty:
  - claim: "Interview stages for SDE II India"
    reason: "Only Glassdoor snippets for other roles; no official process"
    confidence: "low"
  - claim: "Frontend framework is React"
    reason: "Inferred from a closed 2024 posting; current posting names none"
    confidence: "low"
  - claim: "Employment type for India"
    reason: "Not stated anywhere found"
    confidence: "low"
  - claim: "Pay vs target"
    reason: "No published range or third-party data"
    confidence: "low"
sources:
  - id: "G1"
    url: "https://boards-api.greenhouse.io/v1/boards/gatherai/jobs/5243582007"
    title: "Software Development Engineer II - Full Stack - India (Greenhouse API)"
    tier: 1
    published_or_updated: "first published 2026-09-21; updated 2026-09-30"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["eligibility", "requirements", "written communication", "AI nice-to-have"]
  - id: "G2"
    url: "https://boards-api.greenhouse.io/v1/boards/gatherai/jobs/5243582007?questions=true"
    title: "Application questions for SDE II Full Stack India"
    tier: 1
    published_or_updated: "2026-09-30"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["knock-out screening questions", "compensation expectation required"]
  - id: "G3"
    url: "https://boards-api.greenhouse.io/v1/boards/gatherai/jobs?content=true"
    title: "Gather AI Greenhouse job board (10 postings)"
    tier: 1
    published_or_updated: "live"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["open postings count", "India hiring timeline"]
  - id: "G4"
    url: "https://job-boards.greenhouse.io/gatherai/jobs/5252951007"
    title: "Software Development Engineer II – Data Engineer"
    tier: 1
    published_or_updated: "2026-09-30"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated language", "production PostgreSQL", "AI-assisted development"]
  - id: "G5"
    url: "https://job-boards.greenhouse.io/gatherai/jobs/5185947007"
    title: "Senior/Staff Full Stack Engineer (Hybrid)"
    tier: 1
    published_or_updated: "first published 2026-07-14; updated 2026-09-30"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["stack: Python, Go, Node.js, PostgreSQL, Kubernetes on Azure", "Claude AI-assisted engineering"]
  - id: "G6"
    url: "https://job-boards.greenhouse.io/gatherai/jobs/5186046007"
    title: "Principal Data Engineer (Remote India)"
    tier: 1
    published_or_updated: "first published 2026-07-14; updated 2026-09-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Azure preferred", "data platform build-out"]
  - id: "G7"
    url: "https://www.gather.ai/careers"
    title: "Careers at Gather AI"
    tier: 1
    published_or_updated: "2026 (footer)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["fully remote or remote-flexible", "equity from day one", "US-style benefits", "no process described"]
  - id: "G8"
    url: "https://www.gather.ai/company"
    title: "About Gather AI"
    tier: 1
    published_or_updated: "2026 (footer)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["$74M raised", "2.5x YoY bookings", "Series B", "CTO Andrew Hoffman"]
  - id: "G9"
    url: "https://technical.ly/entrepreneurship/gather-ai-series-b-raise.md"
    title: "Gather AI Series B raise (Technical.ly)"
    tier: 4
    published_or_updated: "2026-02"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["$40M Series B", "plans to hire engineers"]
  - id: "G10"
    url: "https://www.gather.ai/press/gather-ai-raises-40m-led-by-smith-point-capital-management-to-scale-its-physical-ai-platform-for-global-logistics"
    title: "Gather AI raises $40M led by Smith Point Capital Management (press release; direct fetch 404, snippet only)"
    tier: 1
    published_or_updated: "2026-02-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Series B details", "global expansion"]
  - id: "G11"
    url: "https://www.cbinsights.com/company/gather-ai/financials"
    title: "Gather AI financials (CB Insights) — snippet"
    tier: 4
    published_or_updated: "2026"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["$74.53M over 9 rounds"]
  - id: "G12"
    url: "https://www.glassdoor.com/Interview/Gather-AI-Interview-Questions-E7666654.htm"
    title: "Gather AI Interview Questions (Glassdoor) — 403; snippets only"
    tier: 4
    published_or_updated: "2026-05-29"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["8 reviews, very negative", "inventory JSON diff coding", "system design", "unstructured recruiter screen"]
  - id: "G13"
    url: "https://www.glassdoor.com/Reviews/Gather-AI-Reviews-E7666654.htm"
    title: "Gather AI Reviews (Glassdoor) — snippets only"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["3.9 avg from 7 reviews", "low pay complaints from implementation engineers"]
  - id: "G14"
    url: "https://dynamitejobs.com/company/gatherai/remote-job/software-engineer-frontend"
    title: "Gather AI Software Engineer, Frontend (closed; mirror)"
    tier: 5
    published_or_updated: "2024-10-02"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["React.js, TypeScript, Jest frontend (historical)"]
  - id: "G16"
    url: "https://www.crunchbase.com/organization/gather-ai"
    title: "Gather AI (Crunchbase) — snippet"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["101–250 employees", "Pittsburgh HQ"]
```
