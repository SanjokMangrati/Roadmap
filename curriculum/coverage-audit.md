---
generated: 2026-10-09
evidence_window: 2024-05 (oldest candidate report used) to 2026-10-09 (posting corpus, first-party postings, resource checks)
reverify_by: 2026-10-29, or before your first scheduled interview if that is earlier
---

> **UNMEASURED.** The "measured gap" column uses priors (`candidate-assessment.md`), not observed results.

# Coverage audit

## 1. Traceability matrix

Columns follow the output contract: company requirement, competency, measured gap, subskills, curriculum unit, practice, exit test, source. Requirement files are in `interview-intelligence/requirements/`; source IDs are the ones each file's ledger uses.

### Hyperproof (realistic)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Required essay on testing and reliability; optional async-communication essay | C16 | D1 to D2 | application essays | C16-W1, C16-W2 | real application submitted Day 1 | XT-C16 | hyperproof.md S2 |
| Take-home technical assessment (Coderbyte per older posting) | C05, C09 | D1 to D2 | easy-medium patterns; unit tests and naming | C05-P1 to P8; C09-W1 to W4 | 24 narrated problems; tests for timed builds | XT-C05, XT-C09 | hyperproof.md S3, S5, S6 |
| React, TypeScript, Node.js, REST | C01, C02, C03 | D1 to D2 each | see master nodes | C01-W1 to W4; C02-W1 to W4; C03-W1 to W5 | timed builds, React drills | XT-C01, XT-C02, XT-C03 | hyperproof.md S1 |
| PostgreSQL modelling, data integrity | C04 | D1 to D2 | schema, indexes, transactions, locks | C04-W1 to W5 | 1M-row lab; race reproduction | XT-C04 | hyperproof.md S1 |
| Three 60-minute one-to-ones: design and technical depth | C06, C15 | D1 to D2; D0 to D2 | delivery framework; narration | C06-W4 (risk register design); C15 | recorded designs; Mock 2 | XT-C06, XT-C15 | hyperproof.md S3, S5 |
| Compliance domain preferred | C18-HP | none to D1 | risk register, inherent vs residual risk, control testing | C18-HP-W1 | schema sketch | XT-C18-HP | hyperproof.md S1, section 6 |
| RBAC, encryption | C12 | at target | access control, hashing vs encryption | C12-M1 | cold test | XT-C12 | hyperproof.md section 6 |
| Azure | C11 | at target | awareness only | C11-M1 | cold test | XT-C11 | hyperproof.md S1 |
| Java Spring Boot or C#/.NET; "4+ years React + Java" screening question | none | not closable | n/a | **not covered** (relevance gate, section 3) | n/a | n/a | hyperproof.md S2 |

### HighLevel (realistic)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| ~1-hour build-a-working-API round with schema discussion (decisive stage) | C03, C04 | D1 to D2 | REST, validation, pagination, idempotency keys, schema | C03-W1 to W5; C04 | 4 timed builds | XT-C03 | highlevel.md S12-S15 |
| AI tools allowed in build round (anecdotal); "AI-native builder", "slop-free code" | C13 | D1 to D2 | agent workflow, AGENTS.md, reviewing AI diffs | C13-W1 to W3 | narrated accept/reject in every build | XT-C13 | highlevel.md S1, S2, S14 |
| 30-minute past-work call; past experience in the 2-hour round | C15 | D0 to D2 | project deep-dive, story bank | C15-W3, W4, W5, W6c | Mock 3 | XT-C15 | highlevel.md S13, S14 |
| ~2-hour high-level design | C06 | D1 to D2 | delivery framework, perturbations | C06-W1, W2, W6, W7 | 6 designs aloud; Mock 2 | XT-C06 | highlevel.md S12-S14 |
| LLD variant (Snake and Ladders) | C06 | D1 to D2 | class design | C06-W9 | 2 x 45-minute LLD | XT-C06 (design criteria) | highlevel.md S14 |
| Pub/Sub, Cloud Tasks, idempotency, retries, consistency | C07 | D0 to D2 | at-least-once, idempotent consumer, backoff, DLQ, outbox | C07-W1 to W3 | BullMQ worker; vocabulary map in company-branches.md | XT-C07 | highlevel.md S2 |
| MongoDB/Firestore, Redis | C08 | D0 to D1 | cache-aside, invalidation, embed vs reference | C08-W1 to W3 | cache added to C03-W4 API | XT-C08 | highlevel.md S1, S9 |
| Elasticsearch for search and filters | C08 | D0 to D0 | one-sentence role of an inverted index | C06-W2 (said in design) | none | **partial**: no exit criterion (flag F2) | highlevel.md S1, S9 |
| Vue 3 Composition API and Pinia | C19-HL | D0 to D1 | ref, reactive, computed, watch, Pinia | C19-HL-W1, W2 | autocomplete port | XT-C19-HL | highlevel.md S1, S6 |
| Workflow AI and CRM AI teams | C14 | D0 to D1 | streaming, tool calling, structured output | C14-W1 to W3 | LLM feature build | XT-C14 | highlevel.md S1 |
| Tests, CI, Docker, GKE | C09, C11 | D1 to D2; at target | test layers; Dockerfile, Kubernetes objects | C09; C11-M1 | integration tests; cold test | XT-C09, XT-C11 | highlevel.md S1, S2 |
| On-call debugging | C10 | D1 to D2 | reproduce, debugger, root cause | C10-W1 to W4 | 3 bug fixes | XT-C10 | highlevel.md S2 |
| CRM domain (contacts, tags, segmentation) | C18-HL | at target by prior | n/a | covered by C15-W4 CRM deep-dive | Mock 3 | XT-C15 (deep-dive criterion) | highlevel.md S1, S4 |
| Possibly one easy DSA or JavaScript question | C05, C01 | D1 to D2 | hash maps, flatten object | C05-P1; C01-W3 | narrated problems | XT-C05, XT-C01 | highlevel.md S13, S19 |

### Drivetrain (realistic)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Live DSA round 1: stacks, asteroid collision, min/max stack, 2-D matrix, recursion | C05, C15 | D1 to D2; D0 to D2 | stacks, binary search on matrix, recursion | C05-P3, P4, P5; C15-W1, W2 | LC 735, 155, 74, 78, 46, 39; Mocks 1 and 4 | XT-C05, XT-C15 | drivetrain.md D12, D13 |
| Round 2: 0/1 knapsack DP | C05 | D1 to D2 | 1-D and knapsack DP | C05-P7 | LC 70, 198, 416; LC 322 in Mock 4 | XT-C05 | drivetrain.md D12 |
| Round 2: LLD and HLD of a booking app | C06, C04 | D1 to D2 | seat holds, double-booking prevention | C06-W3, C06-W9, C04-W5, C03-W4 | booking design, race lab, booking API build | XT-C06, XT-C04 | drivetrain.md D12 |
| Spreadsheet-style components and large data in React | C02 | D1 to D2 | virtualisation, memoisation, re-render profiling | C02-W2, W3 | 10,000-row grid | XT-C02 | drivetrain.md D1 |
| Data-visualisation components | none | n/a | charts | **deferred** (master section 13) | none | none | drivetrain.md D1 (flag F1) |
| Browser debugging | C10 | D1 to D2 | DevTools Performance panel | C10-W1 | grid profiling in C02-W3 | XT-C10 | drivetrain.md D1 |
| FP&A product | C18-DT | none to D0 | plan vs actuals, drivers, scenarios | C18-DT-W1 | "why Drivetrain" paragraph | XT-C18-DT | drivetrain.md D1 |

### Gather AI (stretch)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Live JSON-diff data task (anecdotal) | C05 | D1 to D2 | hash maps, nested-object diff | C05-P1, P8 | custom JSON diff | XT-C05 | gather-ai.md G12 |
| Retries, duplicate processing, unreliable dependencies | C07 | D0 to D2 | idempotency, backoff, DLQ | C07-W1 to W3 | BullMQ worker | XT-C07 | gather-ai.md G1 |
| PostgreSQL tuning (knock-out question) | C04 | D1 to D2 | indexes, EXPLAIN | C04-W2, W3, W5 | 1M-row lab | XT-C04 | gather-ai.md G2 |
| NestJS services, REST | C03 | D1 to D2 | API design | C03 | timed builds | XT-C03 | gather-ai.md G1 |
| Redis caching and invalidation | C08 | D0 to D1 | cache-aside | C08 | cache on C03-W4 API | XT-C08 | gather-ai.md G1 |
| System design (requirements first) | C06 | D1 to D2 | delivery framework | C06 | designs aloud | XT-C06 | gather-ai.md G12 |
| Written design notes and PRs | C16 | D1 to D2 | PR descriptions, design doc | C16-W3, W4 | write-ups | XT-C16 | gather-ai.md G1 |
| Production Python; Kubernetes on Azure (knock-out on years) | none | not closable | n/a | **not covered** (relevance gate) | n/a | n/a | gather-ai.md G2 |

### Dscout (stretch)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Built features on LLM APIs or agents (required) | C14, C14-DS | D0 to D1; D1 to D2 | streaming, tool calls, validation, non-determinism UX, evals | C14-W1 to W3; C14-DS-W1 | LLM feature with 10-case eval | XT-C14, XT-C14-DS | dscout.md S1 |
| AI coding tools in daily use | C13 | D1 to D2 | agent workflow, AGENTS.md | C13 | every timed build | XT-C13 | dscout.md S1, S7, S8 |
| Product judgment, push back, LLM vs deterministic | C17, C14 | at target; D0 to D1 | scoping, trade-off note | C17-M1; C14-W3 | 3 scoping drills | XT-C17, XT-C14 | dscout.md S1 |
| React, TypeScript, GraphQL frontend | C01, C02 | D1 to D2 | see master | C01, C02 | drills | XT-C01, XT-C02 | dscout.md S1 |
| Exercise with ticket breakdown and trade-off notes | C16 | D1 to D2 | design doc, PR notes | C16-W3, W4 | write-ups | XT-C16 | dscout.md S7, S8 |
| GraphQL (Apollo), Elixir/Phoenix | none | n/a | n/a | **not covered**; GraphQL deferred | n/a | n/a | dscout.md S1 |

### Infisical (stretch; eligibility conflicting)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Secret-sharing take-home and review with design extension (anecdotal) | C06, C03, C09, C12 | D1 to D2 | encryption, expiry, view-once, rate limiting | C06-W5; C03; C09 | Design 4 aloud | XT-C06, XT-C03, XT-C09 | infisical.md S14 |
| Secrets, PKI, KMS domain | C18-IN | none to D1 | lifecycle, envelope encryption, dynamic secrets | C18-IN-W1 (gated) | applied to Design 4 | XT-C18-IN | infisical.md S1 |
| Redis and BullMQ | C07, C08 | D0 to D2; D0 to D1 | BullMQ worker, cache-aside | C07-W2; C08 | worker build | XT-C07, XT-C08 | infisical.md S1 |
| Work day in the real monorepo (anecdotal) | C10 | D1 to D2 | navigating unfamiliar code | C10-W2 to W4 | 3 bug fixes | XT-C10 | infisical.md S14 |
| TypeScript, React 18, Fastify, PostgreSQL | C01-C04 | D1 to D2 | see master | C01-C04 | builds and drills | XT-C01 to XT-C04 | infisical.md S1 |
| GitHub profile required; "exceptional ability" bullets | C16 | D1 to D2 | concise written claims | C16 | none specific | **partial**: no unit builds a public GitHub profile (flag F4) | infisical.md S4 |

### Metabase (stretch; eligibility unverified)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| React panel; performance on large data | C02 | D1 to D2 | rendering, memoisation, virtualisation | C02 | grid, drills | XT-C02 | metabase.md S2, S15 |
| Redux | C02-MB | D0 to D1 | slices, selectors | C02-MB-W1 (gated) | grid state refactor | XT-C02-MB | metabase.md S2, S12 |
| Algorithms panel and coding screen | C05 | D1 to D2 | easy-medium patterns | C05 | 24 problems | XT-C05 | metabase.md S11, S15, S16 |
| Architecture panel | C06 | D1 to D2 | frontend feature design | C06 | designs aloud | XT-C06 | metabase.md S15 |
| Take-home with tests and write-up | C09, C16 | D1 to D2 | tests, README trade-offs | C09; C16-W3 | integration tests | XT-C09, XT-C16 | metabase.md S15, S17 |
| Code review, "giving good feedback" | C13, C09 | D1 to D2 | review comments | C13-W3 | 3 AI-diff reviews | XT-C13 | metabase.md S2 |
| CSS and design systems ("a necessity") | none | n/a | n/a | **deferred** until eligibility confirmed | none | none | metabase.md S2 (flag F3) |

### Automattic (stretch; eligibility likely, unconfirmed)

| Company requirement | Competency | Gap (prior) | Subskills | Curriculum unit | Practice | Exit test | Source |
|---|---|---|---|---|---|---|---|
| Application answers weighted as a hiring step | C16-AU | D0 to D1 | concrete stories with numbers | C16-AU-W1 (gated) | answers drafted | XT-C16-AU | automattic.md S1, S2 |
| Slack text interview | C16 | D1 to D2 | written reasoning | C16 | write-ups | XT-C16 | automattic.md S2 |
| Code test on existing code or trial up to 20 hours | C10 | D1 to D2 | unfamiliar code, PR description | C10-W2 to W4 | 3 bug fixes | XT-C10 | automattic.md S2 |
| PHP and the WordPress plugin model | C16-AU (awareness) | D0 to D1 | hooks, actions vs filters | C16-AU-W1 | none | XT-C16-AU (criterion 2) | automattic.md S1 |
| Skills assessment (format not described) | unknown | unknown | unknown | **untraceable** (flag F5) | none | none | automattic.md S2 |

## 2. Flags: requirements without a full trace

| Flag | Requirement | Status | Why | What would close it |
|---|---|---|---|---|
| F1 | Drivetrain data-visualisation components | deferred | Named in the posting; no reported round tests it | Recruiter confirms a frontend machine-coding round |
| F2 | HighLevel Elasticsearch | partial (one sentence in C06-W2, no exit criterion) | No report shows search internals tested | Interviewer raises search in an earlier round |
| F3 | Metabase CSS and design systems | deferred | Eligibility unverified | Written confirmation of India eligibility |
| F4 | Infisical public GitHub profile | not in plan | Building a portfolio is outside the 20-day study budget; the timed builds could be published, but quality for an "exceptionally high" bar is not assessed here | You choose to publish the C03 and C14 builds; eligibility confirmed |
| F5 | Automattic skills assessment | untraceable | Format not described anywhere | Recruiter describes the format |
| F6 | Every company's interview AI policy | unknown | No target published one | Ask each recruiter (re-verification checklist) |

## 3. Relevance-gate log

Every competency row, its trajectory, the decision, and the evidence. No item a target company currently tests was cut on market grounds alone.

| Competency | Trajectory | Demand share (Segment A, N = 264, 2026-10-09) | Decision | Evidence and reason |
|---|---|---|---|---|
| C01 TypeScript and JavaScript | insufficient-data | TS 41%, JS 50% | keep D2 | Tested at all 8 targets |
| C02 React | insufficient-data | 36% (Segment B 70%) | keep D2 | Drivetrain, Metabase panels; take-homes |
| C03 Node.js and API design | insufficient-data | Node 28%, REST 66% (broad) | keep D2 | HighLevel build round (corroborated) |
| C04 PostgreSQL | insufficient-data | 31% | keep D2 | HighLevel schema discussion; Gather AI knock-out |
| C05 Algorithms | shifting | not counted | keep D2, cap easy-medium | Drivetrain tests now (corroborated); Canva replaced its screen (first-party 2025-06-11); large companies harden rounds (M3). Interview reality wins. |
| C06 System design | insufficient-data | 61% (broad) | keep D2 | HighLevel, Drivetrain, Metabase, Hyperproof, Infisical; stated weak area |
| C07 Async reliability | insufficient-data | queues 8% | cap D2 to a subset | HighLevel postings name idempotency and retries; broker internals have no stage evidence |
| C08 Caching and NoSQL | insufficient-data | Redis 10%, MongoDB 13% | cap D1 | Stack and design-round mentions only |
| C09 Testing | insufficient-data | 56% | keep D2 | Hyperproof essay and take-home |
| C10 Debugging | insufficient-data | 36% | keep D2 | Automattic code test; Infisical work day |
| C11 Cloud and containers | insufficient-data | AWS 30%, Docker 30%, K8s 27% | maintenance (D1) | At target by prior |
| C12 Security | insufficient-data | 45% (broad) | maintenance (D1) | At target by prior |
| C13 AI-assisted engineering | rising | 22% (Segment B 25%) | keep D2 | Stack Overflow 2026 (M2); HighLevel and Dscout require it |
| C14 LLM product features | rising | LLM 26%, agents 22% | cap D1; D2 Dscout branch | Hiring Lab, Octoverse (M2); required only at Dscout |
| C15 Explaining reasoning aloud | shifting | n/a | keep D2 | Every live stage; Canva and Coinbase score explanation |
| C16 Written communication | insufficient-data | 72% (broad) | keep D2 | Hyperproof essay; Automattic application |
| C17 Product sense | insufficient-data | 73% (broad) | maintenance (D1) | At target by prior |
| C18 Domain (per company) | n/a | n/a | keep D0-D1 per branch | Company postings |
| C19 Vue 3 (HighLevel) | insufficient-data | Vue 8% | cap D1 | HighLevel frontend; React accepted |
| C19 Java Spring Boot, C# | insufficient-data | Java 16% | cut to not covered | Hyperproof accepts Node.js; not reachable to a screened level in 20 days |
| C19 Python (production) | insufficient-data | 34% | cut to not covered | Gather AI screens on years; study cannot change years |
| C19 Elixir, PHP, Go | insufficient-data | 2%, 3%, 19% | cut to not covered | No shortlisted stage tests them; Go only at out-of-reach companies |
| Remote work availability (market condition) | declining | n/a | no curriculum effect | Not a skill |
| Entry-level hiring (market condition) | declining | n/a | no curriculum effect | Not a skill; target is mid-level |

## 4. Unit-to-gap check

All 79 units in `study-plan.csv` carry a `competency_id` that maps to a ranked gap in master section 4 or to a maintenance row (C11, C12, C17). No unit exists without a gap or maintenance need.

| Check | Result |
|---|---|
| Units total | 79 |
| Units mapped to a ranked gap | 76 |
| Units mapped to maintenance | 3 (C11-M1, C12-M1, C17-M1) |
| Units without a gap or maintenance need | 0 |
| Sum of unit minutes | 6,114 (101.9 hours gross; 122.3 hours planned at pace 1.0 with 20% buffer) |
| Resource URLs fetched 2026-10-09 | 47 distinct; 46 returned HTTP 200 with the named page; LeetCode returned a 403 challenge page to scripts, and all 28 problems were confirmed free via LeetCode's GraphQL endpoint |
