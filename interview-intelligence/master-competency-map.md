# Master competency map

Generated 2026-10-09. Normalizes the requirements of the 8 shortlisted companies (Hyperproof, HighLevel, Drivetrain, Gather AI, Dscout, Infisical, Metabase, Automattic) and the reach list (Railway, Supabase, LiveKit, Tarteel AI, vidIQ) into one taxonomy. No study durations here; those belong to `finite-interview-curriculum`.

- **`demand_share`** comes from `skill-demand.csv`, Segment A: remote, non-staff engineering postings open to India-based candidates, N = 264, 145 companies, fetched 2026-10-09. Segment B (full-stack/product/frontend postings at 148 startup and scale-up boards, any location, N = 151) is shown where it differs materially.
- **`market_trajectory`** comes from `market-context.md` section 6.
- **Evidence strength:** `official` = first-party posting or hiring page; `corroborated` = several recent candidate reports; `anecdotal` = one or few reports.
- **Company abbreviations:** HP Hyperproof, HL HighLevel, DT Drivetrain, GA Gather AI, DS Dscout, IN Infisical, MB Metabase, AU Automattic; reach list: RW Railway, SB Supabase, LK LiveKit, TA Tarteel AI, VQ vidIQ.

## Summary table

| ID | Competency | Shortlist companies requiring | Assessed in | Trajectory | Demand share (A, N=264) |
|---|---|---|---|---|---|
| C01 | TypeScript and JavaScript fluency | all 8 | every coding stage | insufficient-data | TS 41%, JS 50% (B: TS 71%) |
| C02 | React frontend engineering | HP, DT, DS, IN, MB (HL accepts React; uses Vue 3) | DT live coding, MB React panel, take-homes | insufficient-data | 36% (B: 70%) |
| C03 | Node.js backend and API design | HP, HL, GA, IN, (DS via GraphQL) | HL timed API build, take-homes, design rounds | insufficient-data | Node 28%, REST/API 66% (broad) |
| C04 | Relational data modelling and PostgreSQL | HP, HL, GA, DS, IN | HL schema discussion, GA tuning knock-out question | insufficient-data | 31% |
| C05 | Data structures and algorithms (live) | DT (high), MB (medium), HL/HP/GA (low–medium) | DT live rounds, MB panels, screens | shifting | not counted in postings |
| C06 | System design and architecture defense | HL, MB, GA, HP, IN, RW | HL 2-hour design round, MB panel, RW walkthrough, HP one-to-ones | insufficient-data | 61% (broad) |
| C07 | Asynchronous processing and reliability | HL, GA, IN, RW | design rounds, take-home extensions | insufficient-data | queues 8%, microservices/distributed 32% |
| C08 | Caching and NoSQL stores | HL, GA, IN | design rounds | insufficient-data | Redis 10%, MongoDB 13% |
| C09 | Testing and code quality | HP, IN, MB, AU, HL | take-homes, code review, HP testing essay | insufficient-data | testing 56%, code review 26% |
| C10 | Debugging and working in existing codebases | AU, MB, HL, GA | AU code test/trial, MB screen, on-call questions | insufficient-data | debugging 36%, observability 41% |
| C11 | Cloud, containers and deployment | GA (screened), HL, HP, IN | GA knock-out questions, design rounds | insufficient-data | AWS 30%, GCP 17%, Docker 30%, K8s 27% |
| C12 | Security fundamentals | IN (domain), HP, GA | IN take-home, design | insufficient-data | 45% (broad) |
| C13 | AI-assisted engineering (direct and verify agents) | HL (required), DS (required), VQ, AU (job language), GA (nice) | HL build round (AI allowed, anecdotal), DS exercises with AGENTS.md | rising | 22% (B: 25%) |
| C14 | LLM product features | DS (required), HL (AI teams), GA (nice), LK | DS team interviews, trade-off notes | rising | LLM 26%, agents 22%, retrieval 11%, evals 5% (B: 38%/42%/5%/8%) |
| C15 | Explaining reasoning aloud | all live rounds; weak area | every live coding and design stage | shifting (more weight in AI-era rounds; first-party Canva, Coinbase) | n/a (interview skill) |
| C16 | Written asynchronous communication | AU (high), MB, GA, HP, IN, RW | AU Slack interview and application, HP essay, take-home write-ups | insufficient-data | 72% (broad) |
| C17 | Product sense and ownership | DS (high), HL, MB, RW, IN | DS team interviews, HL past-work call, CEO/founder chats | insufficient-data | 73% (broad; B: 88%) |
| C18 | Domain knowledge | HL (CRM), HP (compliance/risk), DT (finance spreadsheets), IN (secrets/PKI) | role-specific questions | n/a | n/a |
| C19 | Framework variants outside the core stack | HL (Vue 3), DS (Elixir, GraphQL), AU (PHP), HP (Java Spring Boot/C#), GA (Python) | screening questions, live rounds | insufficient-data | Python 34%, Java 16%, Vue 8%, PHP 3%, Elixir 2% |

## Competency details

### C01 — TypeScript and JavaScript fluency
- **Parent:** languages.
- **Subskills:** type modelling (generics, discriminated unions, narrowing); async/await, promises and event-loop behaviour; module systems; error handling; strict-mode type safety for API contracts.
- **Companies:** all shortlisted; Infisical's Senior role states "TypeScript (3+)"; vidIQ includes JavaScript-to-TypeScript migration.
- **Assessment formats:** live coding (DT, MB), timed build (HL), take-homes (HP, IN, RW).
- **Evidence strength:** official.
- **Role relevance:** core.
- **market_trajectory:** insufficient-data (GitHub Octoverse: TypeScript #1 by contributors, a usage signal, not hiring demand).
- **demand_share:** TypeScript 107 of 264 (41%), JavaScript 131 of 264 (50%), Segment A, 2026-10-09; Segment B TypeScript 107 of 151 (71%).
- **Depth hints:** used daily in every build round; Infisical expects production-grade TypeScript across a Fastify backend and React frontend.

### C02 — React frontend engineering
- **Parent:** frontend.
- **Subskills:** component design and composition; state management (Redux at Metabase; TanStack Query at Infisical; Pinia equivalent at HighLevel); rendering performance with large data (virtualised grids, charts at Drivetrain and Metabase); forms and validation; CSS and design systems (Metabase "a necessity"); accessibility.
- **Companies:** HP, DT, DS, IN, MB; HL accepts React at SDE II but its stack is "primarily Vue 3".
- **Assessment formats:** DT live coding plus UI performance; MB React panel; take-homes with UI (RW requires a UI).
- **Evidence strength:** official.
- **Role relevance:** core.
- **market_trajectory:** insufficient-data.
- **demand_share:** 95 of 264 (36%) Segment A; 106 of 151 (70%) Segment B.
- **Depth hints:** Drivetrain builds spreadsheet-style and data-visualisation components; Metabase requires data-structure manipulation in frontend code and "write fast and performant code".

### C03 — Node.js backend and API design
- **Parent:** backend.
- **Subskills:** REST resource design and status codes; validation; pagination; idempotency keys and retries (HL, GA); authentication and authorization middleware; NestJS modules/DI (HL, GA name NestJS); Fastify (IN); GraphQL schema and resolvers (DS, RW).
- **Companies:** HP, HL, GA, IN; DS (GraphQL API in Elixir).
- **Assessment formats:** HL ~1-hour timed "build a working API" round with schema discussion (corroborated); take-homes (HP, IN, RW).
- **Evidence strength:** official (requirements); corroborated (HL round).
- **Role relevance:** core.
- **market_trajectory:** insufficient-data.
- **demand_share:** Node.js 73 of 264 (28%); NestJS 18 of 264 (7%); REST/API 173 of 264 (66%, broad match); GraphQL 25 of 264 (9%).
- **Depth hints:** HL postings name idempotency, retries and consistency explicitly.

### C04 — Relational data modelling and PostgreSQL
- **Parent:** data.
- **Subskills:** schema design and normalisation; indexes and query plans (EXPLAIN); transactions and isolation; migrations; tuning (GA knock-out question); ORMs and query builders (Knex at IN, TypeORM).
- **Companies:** HP, HL (PostgreSQL alongside MongoDB/Firestore), GA, DS, IN.
- **Assessment formats:** HL schema discussion; GA application screening on PostgreSQL tuning; design rounds.
- **Evidence strength:** official.
- **Role relevance:** core.
- **market_trajectory:** insufficient-data.
- **demand_share:** PostgreSQL 82 of 264 (31%); data modelling/schema phrasing 19 of 264 (7%).
- **Depth hints:** Hyperproof requires PostgreSQL queries plus data modelling for risk registers.

### C05 — Data structures and algorithms (live)
- **Parent:** problem solving.
- **Subskills:** arrays, hash maps, stacks (asteroid collision, min/max stack at DT), recursion, dynamic programming (0/1 knapsack at DT), JSON/object diffing (GA, anecdotal), complexity analysis stated aloud.
- **Companies:** DT (high, corroborated), MB (LeetCode easy/medium, anecdotal), HP (Coderbyte take-home), HL and GA (low–medium).
- **Assessment formats:** live coding on video call; online assessment.
- **Evidence strength:** corroborated (DT); anecdotal (others).
- **Role relevance:** company-specific; decisive at Drivetrain.
- **market_trajectory:** shifting (Canva replaced its fundamentals screen with an AI-assisted round, first-party 2025-06-11; large companies harden algorithm rounds, M3 surveys).
- **demand_share:** not measured from postings.
- **Depth hints:** easy-to-medium level; the risk is narrating while coding, not problem difficulty.

### C06 — System design and architecture defense
- **Parent:** design.
- **Subskills:** requirements and scale estimates; data model; API boundaries; queues and background jobs; caching; consistency and failure handling; trade-off articulation; design-doc writing (IN, HL); defending a submitted take-home (RW 30-minute walkthrough).
- **Companies:** HL (2-hour high-level design + past experience, corroborated), MB (architecture panel, anecdotal), GA (anecdotal), HP (design in one-to-ones), IN (system-design extension, anecdotal), RW (official walkthrough).
- **Assessment formats:** live design round; take-home review with extension questions.
- **Evidence strength:** official (RW); corroborated (HL); anecdotal (others).
- **Role relevance:** core; the candidate's stated weak area.
- **market_trajectory:** insufficient-data (GitHub says weight increasing; M3 only).
- **demand_share:** 160 of 264 (61%, broad match).
- **Depth hints:** mid-level product-system scope (CRM contacts service, booking app at DT, secret-sharing app at IN), not planet-scale.

### C07 — Asynchronous processing and reliability
- **Parent:** distributed systems.
- **Subskills:** message queues (GCP Pub/Sub at HL; Kafka/RabbitMQ/SQS at GA; BullMQ at IN); background jobs and orchestration (Cloud Tasks at HL; Temporal at RW); retries, idempotency, dead-letter handling; at-least-once delivery.
- **Companies:** HL, GA, IN, RW.
- **Assessment formats:** design rounds; take-home extensions.
- **Evidence strength:** official (postings).
- **Role relevance:** important for HL and GA.
- **market_trajectory:** insufficient-data.
- **demand_share:** queues/streaming 21 of 264 (8%); microservices/distributed 84 of 264 (32%).

### C08 — Caching and NoSQL stores
- **Parent:** data.
- **Subskills:** Redis caching and invalidation; MongoDB/Firestore document modelling (HL); Elasticsearch basics (HL).
- **Companies:** HL, GA, IN.
- **Evidence strength:** official.
- **demand_share:** Redis 26 of 264 (10%); MongoDB 35 of 264 (13%); search 21 of 264 (8%).

### C09 — Testing and code quality
- **Parent:** quality.
- **Subskills:** unit and integration tests (Vitest/Jest), end-to-end tests (Playwright at IN), testing for reliability (HP required essay), code review etiquette (MB "giving good feedback"), CI.
- **Companies:** HP, IN, MB, AU, HL.
- **Assessment formats:** take-home grading; HP application essay; code review discussion.
- **Evidence strength:** official.
- **market_trajectory:** insufficient-data.
- **demand_share:** testing 147 of 264 (56%); end-to-end 99 of 264 (38%); code review 69 of 264 (26%).

### C10 — Debugging and working in existing codebases
- **Parent:** operations.
- **Subskills:** reading unfamiliar code; reproducing bugs; logs, metrics and traces; on-call and incidents (IN weekly rotation; HL); browser debugging (DT).
- **Companies:** AU (code test on existing code or trial), MB, HL, GA, IN.
- **Evidence strength:** official.
- **market_trajectory:** insufficient-data (AI-era interviews add debugging AI-generated code; Canva first-party).
- **demand_share:** debugging 96 of 264 (36%); observability 107 of 264 (41%); on-call/incidents 56 of 264 (21%).

### C11 — Cloud, containers and deployment
- **Parent:** infrastructure.
- **Subskills:** Docker; Kubernetes basics (GA knock-out, HL GKE); one major cloud (GCP at HL; Azure at GA and HP; AWS); CI/CD pipelines.
- **Companies:** GA (screened), HL, HP, IN.
- **Evidence strength:** official.
- **market_trajectory:** insufficient-data.
- **demand_share:** AWS 78 of 264 (30%); GCP 45 of 264 (17%); Azure 27 of 264 (10%); Docker 78 of 264 (30%); Kubernetes 70 of 264 (27%).

### C12 — Security fundamentals
- **Parent:** security.
- **Subskills:** authentication and authorization (RBAC at HP and IN), encryption at rest and in transit, secrets handling, OWASP top risks, audit logs; secrets/PKI/KMS domain at IN.
- **Companies:** IN (domain), HP, GA ("secure coding").
- **Evidence strength:** official.
- **demand_share:** 119 of 264 (45%, broad match).

### C13 — AI-assisted engineering
- **Parent:** AI-era engineering.
- **Subskills:** directing coding agents (Claude Code, Cursor, Copilot); agent instruction files (CLAUDE.md, AGENTS.md); verifying and testing generated code; reviewing AI output like a pull request (VQ); explaining which parts were AI-written and why they are correct.
- **Companies:** HL ("AI-native builder" coding with agents daily), DS (AI tools required), VQ (daily use), AU (posting language), GA (nice to have); IN and MB repositories use CLAUDE.md.
- **Assessment formats:** HL build round (AI allowed, anecdotal); DS exercises shipped with AGENTS.md (2026 repositories).
- **Evidence strength:** official (postings); anecdotal (interview use).
- **Role relevance:** rising differentiator.
- **market_trajectory:** rising (Stack Overflow 2026: coding agents top AI use at 66%, M2; DORA 2025 adoption 90%, M2).
- **demand_share:** 58 of 264 (22%); Segment B 37 of 151 (25%).

### C14 — LLM product features
- **Parent:** AI product.
- **Subskills:** LLM API calls and streaming UI (VQ); prompt design; tool calling and agents; retrieval with embeddings/pgvector; evaluations; handling non-deterministic output in UX (DS); LLM-versus-deterministic trade-offs (DS).
- **Companies:** DS (required: "built features on LLM APIs or agents"), HL (Workflow AI, CRM AI teams), GA (nice), LK (agents).
- **Evidence strength:** official.
- **Role relevance:** required at Dscout; differentiator elsewhere.
- **market_trajectory:** rising (Hiring Lab: 37% of US software-posting rebound from AI-titled roles, M2; Octoverse LLM-SDK repositories +178%, M2).
- **demand_share:** LLM integration 69 of 264 (26%); agents/tool calling 57 of 264 (22%); retrieval 28 of 264 (11%); evals 14 of 264 (5%); Segment B LLM 57 of 151 (38%), agents 64 of 151 (42%).

### C15 — Explaining reasoning aloud
- **Parent:** interview communication.
- **Subskills:** narrating approach before coding; stating complexity and trade-offs; structured design walkthrough (requirements → data → API → scale → failure); defending decisions under follow-up; past-project deep dives (HL 30-minute past-work call; HL design round includes past experience).
- **Companies:** every live stage at every shortlisted company; least weight at Automattic (text interview).
- **Evidence strength:** corroborated (HL, DT); official (RW walkthrough agenda).
- **Role relevance:** critical; candidate's stated weak area.
- **market_trajectory:** shifting (AI-era rounds score explanation and control of decisions: Canva 2025-10-20 first-party; Coinbase 2026-07-13 listing).

### C16 — Written asynchronous communication
- **Parent:** collaboration.
- **Subskills:** application answers (AU weights them like an interview step); design docs and RFCs (IN, SB); pull-request descriptions and trade-off notes (GA, DS); Slack text interview (AU); required essays (HP testing essay; VQ AI-workflow essays and recorded video).
- **Companies:** AU (high), MB, GA, HP, IN, RW.
- **Evidence strength:** official.
- **demand_share:** 189 of 264 (72%, broad match); explicit "English" 55 of 264 (21%).

### C17 — Product sense and ownership
- **Parent:** product.
- **Subskills:** scoping ambiguous requirements; talking to users; build-versus-buy and push-back (DS); end-to-end feature ownership; customer communication (IN).
- **Companies:** DS (high), HL, MB ("If your focus is only on code this might not be the best role for you"), RW, IN.
- **Evidence strength:** official.
- **demand_share:** 193 of 264 (73%, broad match); Segment B 133 of 151 (88%).

### C18 — Domain knowledge
- **Subskills by company:** CRM data models (contacts, tags, segmentation, opportunities) at HL; governance, risk and compliance (risk register, inherent/residual risk, control testing, SOC 2, ISO 27001, NIST) at HP; FP&A and spreadsheet modelling at DT; secrets lifecycle, PKI, KMS at IN; warehouse inventory data at GA.
- **Evidence strength:** official.
- **Role relevance:** company branch; HL CRM overlap matches the candidate's CRM project claim.

### C19 — Framework variants outside the core stack
- **Subskills by company:** Vue 3 and Pinia (HL); Elixir/Phoenix and GraphQL/Apollo (DS); PHP and the WordPress plugin model (AU); Java Spring Boot and C#/.NET (HP); production Python (GA, screened); Go (IN nice to have, SB, LK).
- **Evidence strength:** official.
- **demand_share:** Python 90 of 264 (34%); Java 43 of 264 (16%); Go 49 of 264 (19%); Vue 22 of 264 (8%); PHP 9 of 264 (3%); Elixir 4 of 264 (2%).
- **Depth hints:** most of these are learn-on-the-job at mid level, but HP and GA screen on them in application questions.
