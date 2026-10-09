# HighLevel: Software Development Engineer II (Fullstack), Contacts / CRM (India, remote)

Last verified: 2026-10-09. Researcher notes: Glassdoor, AmbitionBox, Grapevine and Peerlist returned HTTP 403 to direct fetches. Their content below comes only from search-engine snippets, and each such claim is marked "(snippet)". LeetCode Discuss and Reddit r/developersIndia searches returned no HighLevel-specific reports.

## 1. Summary

- **Role.** Two live SDE II postings on HighLevel's own Lever board fit the candidate: "Software Development Engineer II (Fullstack) - Contacts" (posted 2026-09-16) and "Software Development Engineer II - CRM" (posted 2026-09-17). Both are in the CRM & Automation team. The candidate has built a CRM system, and the Contacts team owns tags, notes, files, contact data and segmentation, so the product-domain overlap is direct.
- **Eligibility: pass.** Both postings list location "India", workplace "remote" and commitment "Employee India", which means direct employment, not an employer of record or a contract.
- **Volume.** On 2026-10-09 the board had 13 open SDE II or SDE III engineering postings for India, all remote: 4 SDE II and 9 SDE III. Six more are titled "Senior SDE".
- **Pay versus target.** No salary is published. For HighLevel SDE II in India, Glassdoor estimates an average of about ₹22 lakh a year (snippet). That is a little below the ₹24–33 lakh cost-to-company that the 1.5–2 lakh a month take-home target roughly needs. The upper quartile (about ₹34 lakh) and recent submissions (₹20–36 lakh) do overlap the target. SDE III pay is probably above the target, but SDE III asks for 4+ years.
- **Process shape (from candidate reports, not official).** A recruiter or HR screen, then a past-work or intro technical call, then a timed "machine coding" round where you build a working API, then a high-level design round combined with a deep dive on past experience, then HR or culture fit. Before mid-2025 the process included a take-home assignment.
- **AI policy: allowed (anecdotal).** Two independent candidate reports (2025 and June 2026) say AI tools could be used in the build round. The SDE II CRM posting says AI is "part of how we build". The company has not published an official interview policy on AI.
- **Fit verdict: realistic (preliminary).** The years and stack match. The gaps are Vue 3 (React is accepted), MongoDB or Firestore, queue and cache depth, on-call experience, and defending design decisions aloud, which is the candidate's self-reported weak area.

## 2. Hard filters

| Filter | Result | Evidence |
|---|---|---|
| India-based remote allowed | **Pass** | Lever JSON for both postings: `"location": "India"`, `"workplaceType": "remote"`, `"commitment": "Employee India"`, `"allLocations": ["India"]`, plus the tag "#LI-Remote" [S1][S2][S3]. Company text in the posting: "HighLevel operates as a global, remote-first organization" [S1]. |
| Live today | **Pass** | Both hosted URLs returned HTTP 200 on 2026-10-09 and appear in the live Lever API listing [S1][S2][S3]. |
| Employment type | **Employee (India)** | The commitment field reads "Employee India" [S1][S2]. |
| Years of experience | **Pass** | Contacts asks for "3+ years of software development experience" [S1]. CRM asks for "2+ years of backend engineering experience" [S2]. The candidate has about 3 years. A third SDE II posting asks for "3–5 years of fullstack development experience" [S4]. |
| Work authorization | Not stated beyond the India location. | [S1][S2] |

Open-postings count (Lever API, 2026-10-09) [S3]:
- **SDE II, India, remote (4):** SDE II (Fullstack) - Contacts; SDE II - CRM; SDE II (general, full stack, posted 2026-09-11); SDE II - Horizontal Platform Growth.
- **SDE III, India, remote (9):** Conversations; Users; Workflow AI; (Backend) - Contacts; CRM - Opportunities; CRM - Opportunities - AI; (Fullstack) - Workflows; Full stack - Wallet (Delhi); Ads Manager (Delhi; created 2024-05-07, so it is probably an evergreen requisition).
- **Adjacent, not counted:** six "Senior SDE" or "Senior Software Development Engineer" postings, plus Lead and Staff roles.

## 3. Current role requirements (labelled)

Sources are the two primary postings [S1][S2], with repeated language checked against the other SDE II and SDE III postings [S4][S5][S7][S8] and the Staff Platform Frontend posting [S6].

**Seniority and years**
- 3+ years of software development (Contacts): **required** [S1].
- 2+ years of backend engineering (CRM): **required** [S2].
- The general SDE II posting asks for 3–5 years: **required** for that posting [S4].
- SDE III postings ask for 4+ years, and Contacts Backend SDE III asks for 5+: **required** for those roles, and out of range for this candidate [S7][S8].

**Languages and frameworks**
- Strong JavaScript and TypeScript fundamentals, with Node.js on the backend: **required** [S1][S2].
- Contacts frontend: "Vue.js, React, or Angular" is **required**, with Vue 2/3 and Pinia, Redux or similar as **nice to have** [S1].
- CRM frontend: "Proficient in Vue 3 or a similar modern frontend framework", with real state-management experience (Pinia, Vuex or equivalent): **required** [S2].
- NestJS: **nice to have** in Contacts [S1] and "preferred" in Horizontal Platform Growth [S5].
- Go: part of the CRM technical environment ("Node.js (TypeScript), Go"). It is not required ("Node.js, Go, or a comparable language") [S2].
- **Frontend framework verified from a first-party source.** The Staff Engineer - Platform Frontend posting says: "Our stack is primarily Vue 3; strong engineers from React, Angular, or Svelte backgrounds are welcome". It also describes a "module federation topology" (micro-frontends) [S6]. CRM lists "Vue 3, TypeScript, Pinia, Vite, Tailwind" [S2]. **Inferred from repeated job language:** Vue 3 is the house frontend, and React experience is accepted at SDE II.

**Frontend and backend scope**
- Full ownership across the database, API and UI layers: **required** [S1].
- "Build interfaces dealing with lists, filters, search, files, notes, tags, and large datasets" [S1].
- CRM: "Ship Vue 3 UIs that consume your own APIs … realtime updates that don't flicker or drift" [S2].

**APIs and distributed systems**
- Design and consume REST APIs: **required** [S1].
- Working knowledge of queues or async processing (Pub/Sub, Kafka, RabbitMQ), and an interest in delivery semantics, ordering and backpressure: **required** in CRM [S2]. Contacts lists event-driven systems as **nice to have** [S1].
- Distributed-systems basics such as idempotency, retries and consistency trade-offs: **required** in CRM [S2].
- **Inferred from repeated job language:** idempotency and queues appear across SDE II and SDE III postings [S2][S5][S7][S8].

**Databases**
- Relational and/or NoSQL: **required** [S1].
- "Model data, write efficient queries, and reason about indexes": **required** [S2].
- MongoDB and Firestore: **nice to have** in Contacts and **bonus** in CRM [S1][S2]. Both appear in almost every SDE II and III posting, so treat them as **inferred from repeated job language** [S4][S5][S7][S8].
- Elasticsearch/OpenSearch and ClickHouse: nice to have or bonus [S1][S2].
- First-party confirmation: HighLevel engineering described moving most workloads from a document database to Firestore. Their write traffic spikes from hundreds to thousands of requests per second within minutes [S9].
- Redis or another cache: **required** in CRM [S2] and **nice to have** in Contacts [S1].

**Cloud and infrastructure**
- GCP with GKE, Pub/Sub and Cloud Tasks, plus GitHub Actions, Docker and Kubernetes: the stated environment in CRM and SDE III Conversations [S2][S7].
- Docker, Kubernetes and GCP: **nice to have** in Contacts [S1].
- CI/CD and Git: **required** [S1].

**Testing**
- "Experience with Git, CI/CD and automated testing": **required** [S1].
- "You write tests as a habit": **required** [S2].

**Security**
- No explicit requirement at SDE II CRM or Contacts. Horizontal Platform Growth asks for secure code and "strict guardrails" when using AI [S5].

**Performance**
- "Optimize APIs and queries for performance and scalability": a responsibility [S1].

**Debugging and incidents**
- "Good understanding of frontend and backend debugging": **required** [S1].
- "Join the on-call rotation with backup from senior engineers": a responsibility [S2].

**System design**
- "Participate in technical design and API-contract discussions" [S1].
- "Write design docs for your features and defend them in review — clear thinking, honest trade-offs" [S2].
- At SDE II this means designing features and defending them. Full high-level design (HLD and LLD) is required at SDE III [S7].

**Product orientation**
- "Understand product requirements and translate them into technical solutions" [S1].
- The general SDE II posting asks for product intuition and a passion for metrics [S4].

**Written communication**
- "Can put your design thinking into a clear doc": **required** [S2].

**Autonomy**
- "Ability to independently deliver medium-complexity features": **required** [S1].
- "Own well-scoped services and components end to end" [S2].

**AI-assisted development**
- "AI First approach while Design, Development and Debugging": **required** [S1].
- "AI-native builder — you code with agents daily and are pushing to get accurate, production-quality output from them": **required** [S2].
- The CRM posting adds: "We're past the debate. AI is part of how we build … If you're still copy-pasting from a chat window and hoping, this isn't the seat for you." [S2]
- Horizontal Platform Growth names LLMs, Cursor and Claude Code [S5].
- **Inferred from repeated job language:** agentic coding is expected across all engineering levels.

**AI/LLM product work**
- Not required at SDE II. It is required in the SDE III Opportunities-AI and Workflow AI postings, for example "Have shipped a customer-facing feature backed by an LLM" [S8].

**Compensation and location**
- Compensation is not published [S1][S2].
- Location is India only, remote, as an employee [S1][S2].

## 4. Interview stages

No official current process page exists. The careers page describes no process [S11], and the current postings do not mention one [S1][S2][S3]. The table combines one historical official posting [S12] with candidate reports.

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Application and recruiter or HR intro call | Phone or video | Not stated | unknown | Motivation, experience fit, logistics | corroborated | S13, S15 (snippet), S14 (snippet) |
| 2 | Technical interview 1: intro, past work, possibly light DSA | Video call with an engineer (an SDE 3 in the June 2026 report) | About 30 min (June 2026 report) | unknown | Past-project depth, fundamentals; 2024 report: 1 DSA question and 1 puzzle | corroborated (stage exists); anecdotal (content) | S12, S13, S14 (snippet) |
| 3 | Machine coding or build-an-API round (earlier: take-home assignment) | Live, timed build of a working API with schema discussion. Variants: social-media-feed machine coding (SDE II), LLD and OOP (Snake and Ladders), API integration assignment (2024) | About 1 h (June 2026). Assignment timebox unknown | allowed (anecdotal: "AI-assisted assignment" 2025; "code using any AI tool" June 2026) | Working code, API design, schema and data modelling, clean modular design, AI-tool fluency | corroborated (practical build round); anecdotal (AI allowed) | S12, S13, S14 (snippet), S15 (snippet), S20 (snippet) |
| 4 | Technical interview 2: high-level design plus past experience | Video discussion | About 2 h combined with past experience (June 2026) | unknown | HLD (for example Uber-style ride booking in 2025; SQS design for a backend role), databases (MVCC, partitioning, sharding), trade-offs, past architecture decisions | corroborated | S12, S13, S14 (snippet) |
| 5 | Final HR or culture-fit round | Video | Not stated | unknown | Culture fit, ownership, expectations, compensation | corroborated | S12, S13 |
| 6 | Offer | Recruiter call | Reports cite about 15 days on average (Glassdoor aggregate) and about 3 weeks (2024) | n/a | n/a | anecdotal | S13, S14 (snippet) |

## 5. Stage-by-stage evaluation targets

1. **Recruiter or HR screen.** Prepare a 90-second story: about 3 years of full stack work, a CRM system you built, Node/NestJS with PostgreSQL, GCP, and daily AI-agent coding. Give a pay expectation grounded in Section 9: ask for a ₹24–33 lakh fixed cost-to-company, not a percentage hike. A 2024 candidate who anchored on a percentage hike received only 9% more [S13].
2. **Intro or past-work technical call.** Be ready to walk through your CRM system end to end. Cover the data model for contacts, tags and notes, how search and filtering on large lists worked, indexes, and what you would change. Expect one easy-to-medium DSA or JavaScript question. Candidate leads mention hash-map counting, flattening a nested object, and for-in versus for-of [S19, low quality].
3. **Machine coding or build-an-API round (the decisive stage).** Practise building a small REST service in Node/TypeScript within 60 minutes, for example a contacts-with-tags API or a feed. It should have a clean module structure, validation, a sensible schema and indexes, idempotent writes, and a few tests. Rehearse driving an AI coding agent while narrating what you accept, reject and verify. The posting penalises unreviewed AI output ("slop-free code") [S2]. Be ready to defend schema choices aloud [S14 snippet].
4. **High-level design plus past experience.** Prepare one design at HighLevel's scale (millions of contacts, bursty writes, queue-backed workflows, a search index). Cover Pub/Sub delivery semantics, retries and idempotency, caching with Redis, MongoDB or Firestore versus PostgreSQL trade-offs, and rate limiting [S2][S9]. A February 2026 candidate said the interviewer steered toward one predefined solution [S14 snippet], so ask clarifying questions early and check direction often.
5. **HR or culture fit.** Prepare evidence of ownership, learning speed, taking feedback, and remote-first communication [S2].

## 6. Competency taxonomy for HighLevel

- **Backend engineering:** Node.js and TypeScript, NestJS modules and DI, REST API design, validation, error handling, pagination, and query optimisation [S1][S2][S5].
- **Async and distributed systems:** GCP Pub/Sub and Cloud Tasks, delivery semantics (at-least-once), ordering, backpressure, idempotency keys, retries with backoff, eventual consistency, and rate limiters [S2].
- **Data:** MongoDB and Firestore schema design and indexes, PostgreSQL, Redis caching and invalidation, and Elasticsearch for search and filters [S1][S2][S9].
- **Frontend:** Vue 3 Composition API, Pinia state, component design, large-list rendering and virtualisation, realtime UI updates, and an awareness of module federation [S1][S2][S6].
- **Delivery and operations:** tests (unit and integration), GitHub Actions CI/CD, Docker and Kubernetes (GKE), monitoring and observability, and on-call debugging [S1][S2].
- **Design communication:** writing feature design docs, defending trade-offs in review, and high-level design aloud [S2][S14].
- **AI-native engineering:** agentic coding workflows, verifying AI output, and producing tested, production-quality code with agents [S1][S2][S5].
- **Product and ownership:** translating requirements, owning a feature end to end, and CRM domain knowledge (contacts, segmentation, tags) [S1][S4].

## 7. Process changes and history (dated)

- **Mid-2024 (historical).** A Bengaluru SDE 3 reported four rounds over about 3 weeks (22 Jul to 12 Aug 2024): a get-to-know round with past work, 1 DSA question and 1 puzzle; an assignment to build an API integration; system design; and a culture fit with HR [S13]. An older Glassdoor review (about 855 days old, so around mid-2024) described a hands-on coding round that turned into endpoints and system design [S14 snippet].
- **Up to June 2025 (official, historical).** The SDE III Reporting posting, removed 2025-06-05, listed the process as "Technical Interview I → Assignment → Technical Interview II → Final HR Interview" [S12].
- **May 2025 (New Delhi).** A candidate reported a projects discussion, an "AI-assisted assignment" built on APIs, and an Uber-style ride-booking design [S14 snippet]. This is the first report of AI tools in the build round.
- **November 2025.** A candidate was given a practical task: reverse-engineer HighLevel's APIs, create a contact, convert it to an opportunity, and verify with Playwright [S14 snippet]. This was probably an SDET (test engineer) role.
- **February 2026.** A round meant to test LLD and machine coding spent 30–40 minutes on HLD, with the interviewer steering toward a predefined answer [S14 snippet].
- **June 2026 (current-most).** A Gurgaon SDE-III reported a 30-minute call with an SDE 3, then a 1-hour machine coding round ("code using any AI tool", build a working API, discuss the schema), then 2 hours of HLD and past experience [S14 snippet].
- **Interpretation (inference).** Between 2024 and 2026 the build round seems to have moved from a take-home assignment to a timed live "machine coding" session where AI tools are allowed. That fits the posting's "We're past the debate. AI is part of how we build" [S2]. This is AI-driven, but the evidence is candidate reports only.

## 8. Candidate-report findings

- **Corroborated.** There is a practical build round (an API or machine coding task) rather than a pure LeetCode loop. Sources: [S13] 2024, [S14] May 2025, Feb 2026 and Jun 2026, [S15] SDE II, and [S12] official "Assignment".
- **Corroborated.** There is an HLD or system design round, often combined with a past-experience deep dive [S12][S13][S14].
- **Corroborated.** Past-project discussion appears in nearly every loop [S13][S14][S15].
- **Anecdotal.** AI tools are allowed in the build round. There are two independent reports (May 2025 and June 2026) [S14 snippet], and no official confirmation. Ask the recruiter.
- **Anecdotal.** The SDE II machine coding round used a "social media feed" problem plus web fundamentals, SEO and performance questions. The Glassdoor SDE II page has only 2 interviews [S15 snippet].
- **Conflicting.** How much DSA matters. Some reports mention one DSA question or a HashMap problem [S13][S14], and one backend loop included a DSA exercise [S14 snippet]. Dataford claims a heavy DSA and Java emphasis [S19], but its method is unclear and it does not match the posting's Node and Vue stack. **Resolution:** prepare easy-to-medium DSA only; the build and design rounds carry more weight.
- **Conflicting (low weight).** The number of stages. Dataford gives both five and six stages [S19]. Candidate reports describe three to four rounds [S13][S14]. **Resolution:** go with the candidate reports and the official 2025 posting (four rounds).
- **Corroborated (experience quality).** Glassdoor's aggregate shows 41.1% positive interview experiences and a difficulty of 2.76/5 across about 124 interviews [S14 snippet]. Several reports mention slow feedback, reschedules or an unprofessional HR contact [S13][S15 snippet].
- **Stale or old.** The 2024 Blind report and the about-855-day-old Glassdoor review describe a take-home assignment. Treat both as historical.
- **Blocked.** Direct pages on Glassdoor, AmbitionBox, Grapevine ("HighLevel Round 2 - Rejected") and Peerlist returned 403, so their full content was not read. LeetCode Discuss and Reddit r/developersIndia had no HighLevel-specific posts in search results. The "specific India loop" the brief mentions is best evidenced as: intro call → machine coding/API build → HLD and past experience → HR.

## 9. Fit check

**Verdict: realistic (preliminary)** for SDE II (Contacts or CRM). SDE III postings are **out of reach on years**: they require 4+ or 5+ years against the candidate's about 3 years, and that verdict is final.

**Hard requirements (final):**
- India remote as an employee: pass.
- Years: pass (2+ or 3+ needed, about 3 held).

**Pay (inference, see the note below):**
- Glassdoor HighLevel SDE II average is about ₹22 lakh a year (25th–75th percentile ₹16.5–34.25 lakh). Recent submissions: ₹20–24 lakh (1–3 years, Jul 2025), ₹23–27 lakh (4–6 years, Jan 2026), ₹31–36 lakh (1–3 years, Gurgaon) [S16 snippet].
- Levels.fyi, all levels in India: median total compensation ₹34.6 lakh, average ₹35.9 lakh, from 36 submissions (page updated 2026-10-09) [S17].
- 6figr, all software engineer titles: average ₹28.2 lakh [S18].
- **How the target was converted (estimate, not sourced):** under India's new tax regime with standard provident-fund deductions, a take-home of 1.5–2 lakh a month needs roughly ₹24–33 lakh fixed cost-to-company. With minimal provident fund it is about ₹22–29 lakh.
- **Conclusion:** the typical SDE II offer sits at or slightly below the bottom of the target. A strong negotiation, or a level-up later, is needed to reach the upper half.

**Skill gaps (preliminary, because the candidate's stack depth is self-reported):**
1. **Vue 3 and Pinia.** The house stack is Vue 3 [S6]. React is accepted at SDE II [S1][S2]. Learning enough Vue 3 to work in it is a quick win.
2. **MongoDB or Firestore.** These are nice-to-have or bonus items but appear in nearly every posting [S1][S2][S9]. The candidate's database experience is PostgreSQL.
3. **Queues (Pub/Sub) and Redis.** Required in CRM [S2]. The candidate's depth is unknown, though GCP experience (1 year) helps.
4. **On-call and incident debugging.** A CRM responsibility [S2]. Unknown.
5. **Defending design docs and HLD aloud.** Required [S2] and tested in round 4 [S14]. This is the candidate's self-reported weak area, so it is the highest-leverage gap.
6. **Strength: AI-native coding.** The candidate has 1.5 years of AI-assisted coding, which matches the expectation [S1][S2].
7. **Strength: CRM domain overlap.** The candidate has built a CRM system, which maps directly to the Contacts team's scope (tags, notes, files, segmentation, large lists) [S1].

**Company signals:**
- **Funding.** PeakEquity-led $60M round (Nov 2021) [S22]. General Atlantic minority growth investment, announced 2024-04-11 with terms undisclosed [S21].
- **Size.** "Over 2,000 team members across 10+ countries" [S1].
- **Layoffs and hiring freezes.** None found in searches covering 2025–2026. Absence of reports is not proof.
- **Applicant pool (inference).** Likely crowded. HighLevel is a well-known remote employer in India, there are 13 open SDE II or III postings, Glassdoor has about 124 interview reports, and postings are syndicated to many aggregators. LinkedIn applicant counts could not be fetched.

## 10. Exclusions and unknowns

- There is no official current interview-process page. Stage timeboxes come from one June 2026 report.
- No official AI-in-interview policy exists. "Allowed" rests on two candidate reports.
- Glassdoor, AmbitionBox, Grapevine and Peerlist were blocked (403). Their figures are search-engine snippets and could not be verified on the page.
- No AmbitionBox HighLevel salary or interview data could be read. The brief asked for AmbitionBox pay data; it is unavailable here.
- Levels.fyi gives no SDE II-specific India breakdown.
- Dataford [S19] and hiredvoices [S20] were used only as leads.
- The general SDE II posting [S4] lists React and Vue.js at once. It is treated as generic.

## 11. Source ledger

```yaml
company: "HighLevel"
anchor: false
match:
  hard_filters:
    eligibility: "pass — Lever location India, workplaceType remote, commitment 'Employee India' (S1, S2)"
    hiring_now: "pass — https://jobs.lever.co/gohighlevel/254ef24c-ff4b-42c9-8b43-603e55e650a3 and https://jobs.lever.co/gohighlevel/92002249-671d-4d08-96b0-e87c1d6082cb live 2026-10-09"
  soft_dimensions:
    - dimension: "Full-stack Node.js/TypeScript + Vue 3 (React accepted at SDE II)"
      evidence: [S1, S2, S6]
    - dimension: "CRM product-domain overlap (contacts, tags, notes, segmentation)"
      evidence: [S1]
    - dimension: "AI-native agentic coding expected"
      evidence: [S1, S2, S5]
    - dimension: "GCP stack (GKE, Pub/Sub, Cloud Tasks), MongoDB/Firestore"
      evidence: [S2, S7, S9]
    - dimension: "Pay overlaps lower half of 1.5–2 lakh/month take-home target"
      evidence: [S16, S17, S18]
    - dimension: "Open volume: 4 SDE II + 9 SDE III India remote postings"
      evidence: [S3]
fit:
  verdict: "realistic (SDE II); SDE III out of reach on years"
  preliminary: true
  gaps:
    - gap: "Vue 3 / Pinia (house stack; React accepted)"
      evidence: [S1, S2, S6]
    - gap: "MongoDB/Firestore data modelling"
      evidence: [S1, S2, S9]
    - gap: "Queues (Pub/Sub) delivery semantics, Redis caching"
      evidence: [S2]
    - gap: "On-call / production incident experience"
      evidence: [S2]
    - gap: "Defending design docs and HLD aloud (self-reported weak area)"
      evidence: [S2, S14]
    - gap: "Typical SDE II pay at or slightly below take-home target"
      evidence: [S16, S17]
role:
  title: "Software Development Engineer II (Fullstack) - Contacts; Software Development Engineer II - CRM"
  url: "https://jobs.lever.co/gohighlevel/254ef24c-ff4b-42c9-8b43-603e55e650a3"
  seniority: "SDE II (2+ / 3+ years)"
  compensation: "not published; Glassdoor SDE II India avg ~₹22 LPA (snippet); levels.fyi India all-levels median ₹34.6 LPA"
  verified_date: "2026-10-09"
process:
  url: "https://builtin.com/job/software-development-engineer-iii-reporting/4599082"
  verified_date: "2026-10-09"
  stages:
    - id: "hl-1"
      name: "Recruiter / HR intro"
      format: "phone/video"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["motivation", "experience fit", "expectations"]
      evidence_quality: "corroborated"
      sources: [S13, S14, S15]
    - id: "hl-2"
      name: "Technical interview 1 (intro / past work / light DSA)"
      format: "video with engineer"
      timebox: "~30 min (Jun 2026 report)"
      ai_policy: "unknown"
      competencies: ["past-project depth", "JS/Node fundamentals", "easy DSA"]
      evidence_quality: "corroborated"
      sources: [S12, S13, S14]
    - id: "hl-3"
      name: "Machine coding / build-an-API (formerly take-home assignment)"
      format: "live timed build of working API + schema discussion; earlier take-home API integration"
      timebox: "~1 h (Jun 2026 report)"
      ai_policy: "allowed"
      competencies: ["API design", "schema/data modelling", "clean modular code", "AI-tool fluency", "LLD/OOP"]
      evidence_quality: "corroborated"
      sources: [S12, S13, S14, S15, S20]
    - id: "hl-4"
      name: "Technical interview 2: HLD + past experience"
      format: "video design discussion"
      timebox: "~2 h combined (Jun 2026 report)"
      ai_policy: "unknown"
      competencies: ["high-level design", "databases (sharding, MVCC)", "queues", "trade-off defence"]
      evidence_quality: "corroborated"
      sources: [S12, S13, S14]
    - id: "hl-5"
      name: "Final HR / culture fit"
      format: "video"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["culture fit", "ownership", "compensation alignment"]
      evidence_quality: "corroborated"
      sources: [S12, S13]
  changes:
    - date: "2024-08 (report dated 2024-08-13)"
      change: "Loop: get-to-know (past work + DSA + puzzle) → API-integration assignment → system design → HR culture fit"
      ai_driven: false
      sources: [S13]
    - date: "2025-06-05 (posting removed)"
      change: "Official listed process: Technical Interview I → Assignment → Technical Interview II → Final HR"
      ai_driven: false
      sources: [S12]
    - date: "2025-05"
      change: "First report of an 'AI-assisted assignment' built on APIs"
      ai_driven: true
      sources: [S14]
    - date: "2026-06"
      change: "Timed 1-hour machine coding round with any AI tool allowed; 2-hour HLD + past experience"
      ai_driven: true
      sources: [S14]
requirements:
  explicit_required:
    - "3+ years software development (Contacts) / 2+ years backend (CRM)"
    - "Strong JavaScript/TypeScript; Node.js backend"
    - "Vue.js, React or Angular (Contacts); Vue 3 or similar with state management (CRM)"
    - "Design/consume REST APIs"
    - "Relational and/or NoSQL databases; data modelling and indexes"
    - "Queues/async processing (Pub/Sub, Kafka, RabbitMQ) (CRM)"
    - "Redis or other cache (CRM)"
    - "Distributed-systems basics: idempotency, retries, consistency (CRM)"
    - "Git, CI/CD, automated testing; tests as a habit"
    - "Frontend and backend debugging"
    - "Independently deliver medium-complexity features"
    - "Design docs, defended in review"
    - "AI-first / AI-native development with agents"
  explicit_preferred:
    - "Vue 2/3 + Pinia/Redux"
    - "NestJS"
    - "MongoDB/Firestore, Redis, Elasticsearch/OpenSearch, ClickHouse"
    - "Docker/Kubernetes/GCP"
    - "Micro-frontend architecture"
    - "Event-driven systems; messaging/automation systems"
    - "High-scale SaaS experience"
    - "Accessibility and internationalization"
  inferred_repeated:
    - "Vue 3 is the house frontend (Staff Platform Frontend posting)"
    - "MongoDB/Firestore + GCP Pub/Sub across SDE II/III postings"
    - "End-to-end feature ownership incl. on-call"
    - "AI-assisted engineering expected at every level"
  ai_expectations:
    - "Codes with agents daily; produces accurate, tested, production-quality output (S2)"
    - "AI-first approach in design, development, debugging (S1)"
    - "Uses LLMs, Cursor, Claude Code with guardrails (S5)"
uncertainty:
  - claim: "AI tools allowed in machine coding round"
    reason: "Two candidate reports via search snippets; no official policy"
    confidence: "medium"
  - claim: "Current stage order and timeboxes"
    reason: "Single June 2026 SDE-III report gives timeboxes; SDE II may differ"
    confidence: "medium"
  - claim: "SDE II pay ~₹22 LPA average"
    reason: "Glassdoor blocked; figures from search snippets with small samples"
    confidence: "low"
  - claim: "Target take-home equals ₹24–33 LPA CTC"
    reason: "Own estimate using new tax regime and standard PF; actual structure unknown"
    confidence: "medium"
  - claim: "No layoffs in last 12 months"
    reason: "Absence of search results, not a positive source"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://jobs.lever.co/gohighlevel/254ef24c-ff4b-42c9-8b43-603e55e650a3"
    title: "Software Development Engineer II (Fullstack) - Contacts"
    tier: 1
    published_or_updated: "2026-09-16 (Lever createdAt)"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["eligibility", "requirements", "AI expectation", "CRM domain", "company size"]
  - id: "S2"
    url: "https://jobs.lever.co/gohighlevel/92002249-671d-4d08-96b0-e87c1d6082cb"
    title: "Software Development Engineer II - CRM"
    tier: 1
    published_or_updated: "2026-09-17"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["eligibility", "requirements", "tech environment", "On AI section", "on-call", "design docs"]
  - id: "S3"
    url: "https://api.lever.co/v0/postings/gohighlevel?mode=json"
    title: "HighLevel Lever postings API (91 postings)"
    tier: 1
    published_or_updated: "live"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["open posting counts", "workplace/commitment fields"]
  - id: "S4"
    url: "https://jobs.lever.co/gohighlevel/b4f73bb7-d3ec-4886-9509-3feaf28a7d60"
    title: "Software Development Engineer II"
    tier: 1
    published_or_updated: "2026-09-11"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated language", "3–5 years", "product intuition"]
  - id: "S5"
    url: "https://jobs.lever.co/gohighlevel/75ce4a5c-f6f9-4f96-b886-e714744bc7ab"
    title: "Software Development Engineer II - Horizontal Platform Growth"
    tier: 1
    published_or_updated: "2026-09-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["NestJS preferred", "Vue preferred", "AI tools named", "Pub/Sub"]
  - id: "S6"
    url: "https://jobs.lever.co/gohighlevel/5b51c71b-a61e-41e4-82e3-7fa4deb2678a"
    title: "Staff Engineer - Platform Frontend"
    tier: 1
    published_or_updated: "2026-09-24"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'Our stack is primarily Vue 3'", "module federation"]
  - id: "S7"
    url: "https://jobs.lever.co/gohighlevel/4ec92bca-2593-4081-85fb-c8288147939d"
    title: "Software Development Engineer III - Conversations"
    tier: 1
    published_or_updated: "2025-12-18"
    accessed: "2026-10-09"
    freshness: "recent"
    supports: ["tech environment GCP GKE Pub/Sub Cloud Tasks", "SDE III 4+ years"]
  - id: "S8"
    url: "https://jobs.lever.co/gohighlevel/a718fab2-3fc6-4acd-b364-883f5fc59cac"
    title: "Software Development Engineer III (CRM - Opportunities - AI)"
    tier: 1
    published_or_updated: "2026-09-17"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["SDE III requirements", "LLM product work at SDE III", "stack incl. Istio, Kafka/Pub-Sub"]
  - id: "S9"
    url: "https://cloud.google.com/blog/products/databases/highlevel-migrates-workloads-to-firestore"
    title: "HighLevel migrates workloads to Firestore (Google Cloud blog, by HighLevel engineering)"
    tier: 2
    published_or_updated: "2024-12 (per search snippet)"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["Firestore as primary store", "bursty write traffic", "Firestore vector search for Conversation AI"]
  - id: "S10"
    url: "https://github.com/GoHighLevel"
    title: "GoHighLevel GitHub organization"
    tier: 2
    published_or_updated: "repos pushed up to 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["TypeScript SDK", "Vue widget repos", "Flutter mobile"]
  - id: "S11"
    url: "https://www.gohighlevel.com/careers"
    title: "HighLevel Careers"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["no hiring process described"]
  - id: "S12"
    url: "https://builtin.com/job/software-development-engineer-iii-reporting/4599082"
    title: "HighLevel SDE III - Reporting (mirror of official posting, removed 2025-06-05)"
    tier: 1
    published_or_updated: "removed 2025-06-05"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["official process: Technical Interview I, Assignment, Technical Interview II, Final HR"]
  - id: "S13"
    url: "https://www.teamblind.com/post/highlevel-sde-3-negative-interview-experience-p23z5dij"
    title: "HighLevel SDE 3 Negative Interview Experience (Blind)"
    tier: 5
    published_or_updated: "2024-08-13"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["2024 loop", "assignment round", "offer 35L vs 32L current", "slow feedback"]
  - id: "S14"
    url: "https://www.glassdoor.co.in/Interview/highlevel-Interview-Questions-E3453927.htm"
    title: "highlevel Interview Questions (Glassdoor) — direct fetch 403; snippets only"
    tier: 4
    published_or_updated: "reports dated 2025-05, 2025-11, 2026-02, 2026-06, 2026-08"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["machine coding with AI tool", "HLD + past experience", "41.1% positive, 2.76/5, ~15 days"]
  - id: "S15"
    url: "https://static.glassdoor.co.in/Interview/highlevel-Software-Development-Engineer-SDE-II-Interview-Questions-EI_IE3453927.0,9_KO10,46.htm"
    title: "highlevel SDE II interview questions (Glassdoor) — 403; snippets only"
    tier: 4
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["HR intro, resume interview, machine coding (social media feed)", "web fundamentals/SEO/performance"]
  - id: "S16"
    url: "https://www.glassdoor.co.in/Salary/highlevel-Software-Development-Engineer-SDE-II-Salaries-E3453927_DAO.htm?filter.jobTitleExact=Software+Development+Engineer+%28SDE%29+II"
    title: "highlevel SDE II Salaries (Glassdoor) — 403; snippets only"
    tier: 4
    published_or_updated: "submissions 2025-07 to 2026-01"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["SDE II avg ~₹22 LPA, 25th–75th ₹16.5–34.25 LPA"]
  - id: "S17"
    url: "https://www.levels.fyi/companies/highlevel/salaries/software-engineer"
    title: "HighLevel Software Engineer Salaries (Levels.fyi)"
    tier: 4
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["India median total ₹3.46M, 36 submissions"]
  - id: "S18"
    url: "https://6figr.com/in/salary/highlevel--software-engineer"
    title: "HighLevel Software Engineer Salaries (6figr) — snippet"
    tier: 5
    published_or_updated: "2026"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["avg ₹28.2 LPA across 25 profiles"]
  - id: "S19"
    url: "https://dataford.io/interview-guides/highlevel/software-engineer"
    title: "highlevel Software Engineer Interview Guide (Dataford)"
    tier: 5
    published_or_updated: "2026"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["lead only: question topics; stage counts conflict"]
  - id: "S20"
    url: "https://hiredvoices.com/main/experiences/gohighlevel/sde"
    title: "Gohighlevel Software Engineer Interview Experiences (HiredVoices) — page body empty; snippet only"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["machine coding: Snake and Ladders with SOLID/OOP"]
  - id: "S21"
    url: "https://www.paulweiss.com/insights/client-news/general-atlantic-invests-in-highlevel"
    title: "General Atlantic Invests in HighLevel (Paul, Weiss)"
    tier: 4
    published_or_updated: "2024-04-11"
    accessed: "2026-10-09"
    freshness: "old"
    supports: ["minority growth investment, terms undisclosed"]
  - id: "S22"
    url: "https://www.clay.com/dossier/highlevel-funding"
    title: "How Much Did HighLevel Raise? (Clay)"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["$60M round led by PeakEquity, Nov 2021"]
```
