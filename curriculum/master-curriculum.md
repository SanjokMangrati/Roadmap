---
generated: 2026-10-09
evidence_window: 2024-05 (oldest candidate report used) to 2026-10-09 (posting corpus, profile, resource checks)
reverify_by: 2026-10-29, or before your first scheduled interview if that is earlier
---

> **UNMEASURED.** You declined the assessment interview on 2026-10-09. Every "measured" depth in this plan is a **prior** estimated from your profile, with low confidence. The plan measures you as it goes: Day 1 and Day 2 open with cold exit tests ("test-outs") for C01, C02, C03 and C04, and every exit test result replaces its prior. A passed test-out removes that competency's learning units and returns their hours to the buffer.

# Master curriculum

Companion files: `candidate-assessment.md` (priors and readiness), `study-plan.csv` (every unit, day by day), `company-branches.md` (per-company deltas), `rabbit-hole-parking-lot.md` (tempting topics kept out), `coverage-audit.md` (traceability from each company requirement to its exit test).

## 1. Where you stand

- Measured by observation: 0 of 20 competencies. All depths below are priors.
- Gaps: 21 gap rows (14 master competencies plus 7 company-branch rows); 3 competencies at target by prior (C11, C12, C17) get maintenance only.
- Largest gaps by prior: explaining reasoning aloud (C15, D0 to D2) and asynchronous reliability (C07, D0 to D2). Every other gap is one level.
- Because the priors are nearly uniform, the ranking below is driven by how many targets test each competency and at which stage, not by your actual weak spots. The Day 1-2 test-outs are the first chance to correct that.
- Pace factor: 1.0 (default). Recalibrate after Day 3 (section 12).

## 2. Reality check

### Demand versus capacity

- Capacity: 7 hours per day x 20 days (2026-10-09 to 2026-10-29) = **140 hours**. Units are scheduled on 19 days, 2026-10-10 to 2026-10-28; 2026-10-29 is unscheduled.
- Scheduled work: 79 units, 6,114 minutes = **101.9 hours gross** (99.4 h closing gaps + 2.5 h maintenance).
- Planned hours = 101.9 h x pace 1.0 x 1.2 buffer = **122.3 hours**. The 20% buffer (20.4 h) pays for exit-test retakes and overruns; it is the default, not an assessment-based figure, because nothing was measured.
- Slack: 140 - 122.3 = **17.7 hours**. The schedule fits while the observed pace stays at or below 140 / (101.9 x 1.2) = **1.145**.
- Daily load: scheduled days hold 165 to 365 minutes (2.8 to 6.1 hours); the remaining time each day is buffer and retake time, not free time.
- Not in these hours: job applications, recruiter emails, and interviews themselves. The three eligibility emails (section 11) take about 15 minutes and should be sent on Day 1.

### Per-company readiness and fit (readiness by prior, low confidence)

| Company | Fit | Readiness by prior | Gatekeeper stage this plan targets first | India eligibility |
|---|---|---|---|---|
| Hyperproof | realistic | 2 of 12 (17%) | written essay at application (C16-W2, Day 1); take-home (C05, C09) | confirmed in posting |
| HighLevel | realistic | 3 of 16 (19%) | timed API build (C03); past-work call (C15-W4, Day 2) | confirmed (Employee India) |
| Drivetrain | realistic | 0 of 6 (0%) | live algorithms round 1 (C05, C15) | confirmed (Lever location India) |
| Gather AI | stretch | 2 of 14 (14%) | application knock-outs on Python and Kubernetes years: **not closable by study** | confirmed |
| Dscout | stretch | 1 of 8 (13%) | recruiter screen; requires a shipped LLM feature (C14, C14-DS) | confirmed; employing entity unverified |
| Infisical | stretch | 3 of 15 (20%) | founder screen; GitHub profile required | **conflicting**: confirm before C18-IN |
| Metabase | stretch | 1 of 9 (11%) | coding screen in your own environment (C05) | **unverified**: confirm before C02-MB |
| Automattic | stretch | 0 of 7 (0%) | weighted written application (C16-AU) | **likely**, India not named: confirm before C16-AU |

Readiness percentages are low because priors put most competencies one level below target, not because a test found gaps.

### Market findings that change priorities

1. **India access, not skill, is the binding filter.** 22 of 197 non-staff full-stack or frontend postings (11%) on 148 startup and scale-up boards were open beyond named non-India regions (M1, 2026-10-09). Consequence: the plan spends nothing on companies outside the verified shortlist, and gates three branches on eligibility emails.
2. **AI-assisted engineering is rising**: 22% of Segment A postings (N = 264) and 25% of Segment B (N = 151); Stack Overflow 2026 reports coding agents as the top AI use (66%). Consequence: C13 is kept at D2 and practised inside every timed build.
3. **LLM product work is rising**: LLM integration 26% and agents 22% of Segment A; 38% and 42% of Segment B. Consequence: C14 enters at D1 for all, D2 only for Dscout, where it is required.
4. **Algorithm rounds are shifting, not disappearing**: Canva replaced its fundamentals screen with an AI-assisted round (first-party, 2025-06-11), but Drivetrain's current rounds are algorithm-led (corroborated 2025 reports). Consequence: C05 stays at D2 because a gatekeeper stage tests it, and is capped at easy-medium.
5. **Practical build rounds dominate the shortlist**: 6 of 9 processes use a take-home, timed build, trial or practical exercise (company-landscape.md s7). Consequence: C03, C09, C10 and C13 are practised as timed builds and bug fixes rather than as reading.
6. **Remote work availability is declining** (Indeed: US remote-or-hybrid software share 30.8% on 2026-08-31, from 33.7% a year earlier). This is a market condition, not a skill, and changes no depth target.

## 3. Target, deadline and assumptions

- **Target profile:** mid-level (2-5 years) full-stack engineer, remote from India, US/EU seed to scale-up companies; TypeScript, React, Node.js, PostgreSQL.
- **Targets and weights used in reach:** Hyperproof, HighLevel, Drivetrain (realistic, weight 1.0 each); Gather AI, Dscout, Infisical, Metabase, Automattic (stretch, 0.5 each). Total weight 5.5. Railway (reach list) is not weighted; its take-home and walkthrough are covered by C03, C06 and C15.
- **Deadline and budget:** interview-ready 2026-10-29; 7 hours per day; free resources only.
- **Assumptions:** (a) priors from the profile stand in for measurement until each exit test runs; (b) your primary language for exercises is TypeScript; (c) no learning-format preference was stated, so units mix reading, building and recorded practice; (d) a free LLM API (Gemini free tier) or a local model (Ollama) is available for C14; (e) Docker runs on your machine for C04, C07 and C09.

## 4. Gap ranking

Inputs: reach = sum of company weights testing the competency / 5.5; weight = 3 for CORE or gatekeeper-tested, 2 for BRANCH, 1 for SUPPORTING; impact = reach x weight x gap; hours = scheduled minutes / 60 x pace 1.0 (before buffer); leverage = impact / hours. These scores rank work; they do not measure you. Challenge any weight and the ranking is recomputed.

| Rank | ID | Competency | Companies testing | Reach | Weight | Gap | Impact | Hours | Leverage | Cumulative impact | Vital few |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C18-DT | FP&A domain awareness (Drivetrain branch) | DT | 1.0/5.5 = 0.18 | 2 | 1 | 0.36 | 0.50 | 0.727 | 1% | yes: top of ranking to 80% of impact |
| 2 | C01 | TypeScript and JavaScript fluency | HP HL DT GA DS IN MB AU | 5.5/5.5 = 1.00 | 3 | 1 | 3.00 | 5.33 | 0.562 | 11% | yes: top of ranking to 80% of impact |
| 3 | C16 | Written asynchronous communication | HP GA IN MB AU | 3.0/5.5 = 0.55 | 3 | 1 | 1.64 | 3.00 | 0.545 | 17% | yes: top of ranking to 80% of impact |
| 4 | C15 | Explaining reasoning aloud | HP HL DT GA DS IN MB AU | 5.5/5.5 = 1.00 | 3 | 2 | 6.00 | 11.50 | 0.522 | 37% | yes: top of ranking to 80% of impact |
| 5 | C09 | Testing and code quality | HP HL IN MB AU | 3.5/5.5 = 0.64 | 3 | 1 | 1.91 | 4.50 | 0.424 | 44% | yes: top of ranking to 80% of impact |
| 6 | C07 | Asynchronous processing and reliability | HL GA IN | 2.0/5.5 = 0.36 | 2 | 2 | 1.45 | 4.00 | 0.364 | 49% | yes: top of ranking to 80% of impact |
| 7 | C18-HP | GRC domain: risk register (Hyperproof branch) | HP | 1.0/5.5 = 0.18 | 2 | 1 | 0.36 | 1.00 | 0.364 | 50% | yes: top of ranking to 80% of impact |
| 8 | C13 | AI-assisted engineering (direct and verify) | HL GA DS AU | 2.5/5.5 = 0.45 | 2 | 1 | 0.91 | 2.58 | 0.352 | 53% | yes: top of ranking to 80% of impact |
| 9 | C03 | Node.js backend and API design | HP HL GA DS IN | 3.5/5.5 = 0.64 | 3 | 1 | 1.91 | 6.00 | 0.318 | 60% | yes: top of ranking to 80% of impact |
| 10 | C04 | Relational data modelling and PostgreSQL | HP HL GA DS IN | 3.5/5.5 = 0.64 | 3 | 1 | 1.91 | 6.23 | 0.306 | 66% | yes: top of ranking to 80% of impact |
| 11 | C10 | Debugging and working in existing codebases | HL GA IN MB AU | 3.0/5.5 = 0.55 | 2 | 1 | 1.09 | 3.75 | 0.291 | 70% | yes: top of ranking to 80% of impact |
| 12 | C02 | React frontend engineering | HP DT DS IN MB | 3.5/5.5 = 0.64 | 3 | 1 | 1.91 | 7.08 | 0.270 | 76% | yes: top of ranking to 80% of impact |
| 13 | C06 | System design and architecture defense | HP HL DT GA IN MB | 4.5/5.5 = 0.82 | 3 | 1 | 2.45 | 11.50 | 0.213 | 85% | yes: top of ranking to 80% of impact |
| 14 | C18-IN | Secrets, PKI and KMS basics (Infisical branch) | IN | 0.5/5.5 = 0.09 | 2 | 1 | 0.18 | 1.00 | 0.182 | 85% | no |
| 15 | C02-MB | Redux Toolkit (Metabase branch) | MB | 0.5/5.5 = 0.09 | 2 | 1 | 0.18 | 1.00 | 0.182 | 86% | no |
| 16 | C16-AU | Automattic written application and WordPress awareness | AU | 0.5/5.5 = 0.09 | 3 | 1 | 0.27 | 1.50 | 0.182 | 87% | yes: gatekeeper stage |
| 17 | C08 | Caching and NoSQL stores | HL GA IN | 2.0/5.5 = 0.36 | 1 | 1 | 0.36 | 2.25 | 0.162 | 88% | no |
| 18 | C14 | LLM product features | HL GA DS | 2.0/5.5 = 0.36 | 2 | 1 | 0.73 | 4.50 | 0.162 | 91% | no |
| 19 | C05 | Data structures and algorithms (easy-medium, live) | HP HL DT GA MB | 4.0/5.5 = 0.73 | 3 | 1 | 2.18 | 16.67 | 0.131 | 98% | yes: gatekeeper stage |
| 20 | C19-HL | Vue 3 and Pinia (HighLevel branch) | HL | 1.0/5.5 = 0.18 | 2 | 1 | 0.36 | 3.50 | 0.104 | 99% | no |
| 21 | C14-DS | LLM features to interview depth (Dscout branch) | DS | 0.5/5.5 = 0.09 | 2 | 1 | 0.18 | 2.00 | 0.091 | 100% | no |

**Pareto line.** The top 13 gaps reach 85% of total impact (29.36) with 67% of gap hours. Two gatekeeper gaps join them regardless of rank: C16-AU (Automattic's written application is a scored hiring step) and C05 (Drivetrain round 1, Hyperproof take-home). **Vital few: 15 of 21 gaps, 93% of impact, 86% of gap hours (85.2 of 99.4 h).**

The split is flat (15 of 21 gaps carry 93% of impact) because the priors are uniform. When the Day 1-2 test-outs pass or fail, gaps change and this ranking is recomputed; expect it to sharpen.

## 5. Maintenance list (at target by prior)

Each gets one cold exit test and a refresh of only the failed items. A failed maintenance test turns the competency into a gap and it is ranked like the others.

| ID | Competency | Target | Prior | Unit | Minutes |
|---|---|---|---|---|---|
| C11 | Cloud, containers and deployment | D1 | D1 (prior) | C11-M1 (2026-10-26) | 60 |
| C12 | Security fundamentals | D1 | D1 (prior) | C12-M1 (2026-10-28) | 60 |
| C17 | Product sense and ownership | D1 | D1 (prior) | C17-M1 (2026-10-28) | 30 |
| C18-HL | CRM domain (HighLevel) | D1 | D1 (prior: you built a CRM) | none; your CRM deep-dive (C15-W4) covers it | 0 |

## 6. Relevance-gate decisions

Full log with evidence: `coverage-audit.md`, section 3. Nothing a target company currently tests was cut on market grounds. No competency in scope has a `declining` verdict; the two `declining` verdicts in the research are market conditions (remote availability, entry-level hiring), not skills.

| Item | Decision | Reason |
|---|---|---|
| C07 asynchronous reliability | cap at D2, subset only | Postings name idempotency, retries and delivery semantics; broker internals are not evidenced as tested. |
| C08 caching and NoSQL | cap at D1 | Appears in stacks and design rounds only; 10-13% of Segment A. |
| C14 LLM features | cap at D1 (D2 in Dscout branch) | Rising (M2 sources), but required only at Dscout. |
| C05 algorithms | keep at D2, cap at easy-medium | Trajectory `shifting`, but Drivetrain tests it now; no target reports Hard problems. |
| C19 framework variants | Vue 3 to D1 (HighLevel); all others cut to not covered | Vue 3 is HighLevel's main frontend; Java Spring Boot, C#, Elixir, PHP and Python cannot reach a screened level in 20 days and are learn-on-the-job at mid level. |
| Gather AI Python and Kubernetes knock-outs | not covered | They screen on years of experience, which study cannot change. |
| C11, C12, C17 | maintenance only | At target by prior; one cold exit test each. |

## 7. Schedule

Vital-few units fill the earliest days; Day 1 starts with the gatekeepers (Hyperproof essay, narration diagnostic) and the cold test-outs. Full detail in `study-plan.csv`.

| Day | Date | Minutes | Competencies (units) |
|---|---|---|---|
| 1 | 2026-10-10 | 300 | C15-W1, C15-W2, C01-W1, C04-W1, C02-W1, C16-W1, C16-W2, C18-HP-W1, C18-DT-W1 |
| 2 | 2026-10-11 | 365 | C05-P1, C15-W4, C01-W2, C03-W1 |
| 3 | 2026-10-12 | 365 | C05-P2, C01-W3, C01-W4 |
| 4 | 2026-10-13 | 330 | C05-P3, C03-W2, C13-W1, C13-W2, C03-W3 |
| 5 | 2026-10-14 | 305 | C05-P4, C09-W1, C09-W2 |
| 6 | 2026-10-15 | 335 | C05-P5, C04-W2, C04-W3, C04-W5 |
| 7 | 2026-10-16 | 312 | C07-W1, C07-W2, C07-W3, C04-W4a |
| 8 | 2026-10-17 | 347 | C05-P6, C15-W3, C04-W4b |
| 9 | 2026-10-18 | 335 | C06-W1, C06-W2, C13-W3, C10-W1 |
| 10 | 2026-10-19 | 325 | C05-P7, C10-W2, C10-W3, C06-W3 |
| 11 | 2026-10-20 | 360 | C02-W2, C02-W3, C16-W4, C15-W5 |
| 12 | 2026-10-21 | 250 | C06-W4, C03-W4, C16-AU-W1 |
| 13 | 2026-10-22 | 365 | C15-W6a, C06-W5, C16-W3, C09-W3, C09-W4, C10-W4 |
| 14 | 2026-10-23 | 330 | C06-W6, C06-W7, C06-W9, C03-W5 |
| 15 | 2026-10-24 | 335 | C02-W4, C05-P8, C15-W6b |
| 16 | 2026-10-25 | 345 | C15-W6c, C14-W1, C14-W2, C14-W3 |
| 17 | 2026-10-26 | 330 | C19-HL-W1, C19-HL-W2, C02-MB-W1, C11-M1 |
| 18 | 2026-10-27 | 315 | C08-W1, C08-W2, C08-W3, C14-DS-W1, C18-IN-W1 |
| 19 | 2026-10-28 | 165 | C15-W6d, C12-M1, C17-M1 |
| 20 | 2026-10-29 | 0 | unscheduled: retakes, reopened subskills, applications |
| | **Total** | **6,114** | 79 units = 101.9 h gross; 122.3 h planned with buffer |

## 8. Finite syllabus

One node per gap, in leverage order, in the format of `curriculum-schema.md`. Hours = sum of unit minutes x pace 1.0; the 20% buffer is pooled, not per node. Every resource URL was fetched on 2026-10-09 and returned HTTP 200 with the named page title, except LeetCode pages, which block scripts (HTTP 403 challenge page); each of the 28 LeetCode problems was instead confirmed through LeetCode's public GraphQL endpoint (ID, title, free, difficulty).

### C18-DT. FP&A domain awareness (Drivetrain branch)

```yaml
competency_id: C18-DT
name: FP&A domain awareness (Drivetrain branch)
category: domain
importance: BRANCH
companies: [Drivetrain]
market:
  trajectory: n/a
  demand_share: "n/a"
  evidence: "domain knowledge"
relevance_decision: keep
relevance_reason: "Drivetrain builds FP&A software; hiring-manager round covers motivation."
required_depth: D0
assessment:
  measured_depth: none (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.18
  weight: 2
  impact: 0.36
  hours_to_close: 0.50
  score: 0.727
  rank: 1
  vital_few: true
coverage:   # most frequently tested first
  - "plan versus actuals and variance"
  - "driver-based planning and scenarios"
  - "why spreadsheet-style grids matter in the product"
not_covered:
  - "accounting standards"
  - "financial modelling technique"
evidence:
  - "requirements/drivetrain.md D1"
resources:
  - role: primary
    title: "Drivetrain FP&A product page"
    url: [https://www.drivetrain.ai/solutions/financial-planning-analysis-software]
    verified: 2026-10-09
    covers: [C18-DT-W1]
    skip: "none; read in full (single page)"
work_units:
  - id: C18-DT-W1
    date: 2026-10-10
    activity: "Learn FP&A vocabulary (plan vs actuals, driver-based models) from Drivetrain's product page; apply to Drivetrain"
    minutes: 30
hours_calculation: "(30) min = 30 min x pace 1.0 = 0.50 h"
practice_ai_mode: "without-ai"
exit_test:
  id: XT-C18-DT
  criteria:
    - "Define plan versus actuals, variance, driver-based model and scenario in one sentence each."
    - "Write one paragraph on why Drivetrain, naming one product feature that maps to your grid work (C02-W3)."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C01. TypeScript and JavaScript fluency

```yaml
competency_id: C01
name: TypeScript and JavaScript fluency
category: languages
importance: CORE
companies: [Hyperproof, HighLevel, Drivetrain, Gather AI, Dscout, Infisical, Metabase, Automattic]
market:
  trajectory: insufficient-data
  demand_share: "TypeScript 107 of 264 (41%), JavaScript 131 of 264 (50%), Segment A, 2026-10-09; Segment B TypeScript 71%"
  evidence: "skill-demand.csv; market-context.md s6 (TypeScript #1 by GitHub contributors is usage, not hiring demand)"
relevance_decision: keep
relevance_reason: "Used in every coding stage at all 8 targets."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 1.00
  weight: 3
  impact: 3.00
  hours_to_close: 5.33
  score: 0.562
  rank: 2
  vital_few: true
coverage:   # most frequently tested first
  - "async/await, promise combinators, event loop (microtasks vs macrotasks)"
  - "async error handling"
  - "implementing utilities from scratch (debounce, throttle, deepEqual, flattenObject, promiseAll, retryWithBackoff)"
  - "TypeScript narrowing and discriminated unions"
  - "generics and utility types"
  - "strict-mode typing of API contracts"
not_covered:
  - "type-level programming (conditional and mapped types beyond utility types)"
  - "decorators and reflect-metadata internals"
  - "JavaScript engine internals (V8 hidden classes, JIT)"
  - "module bundler configuration"
  - "Deno and Bun specifics"
evidence:
  - "master-competency-map.md C01"
  - "all 8 requirement files (TypeScript or JavaScript in every posting)"
resources:
  - role: primary
    title: "javascript.info: Promises, async/await and Event loop"
    url: [https://javascript.info/async, https://javascript.info/event-loop]
    verified: 2026-10-09
    covers: [C01-W2, C01-W3]
    skip: "the two named chapters only"
  - role: supplement
    title: "TypeScript Handbook: Narrowing, Generics, Utility Types"
    url: [https://www.typescriptlang.org/docs/handbook/2/narrowing.html]
    verified: 2026-10-09
    covers: [C01-W4]
    skip: "Narrowing, Generics, Utility Types only; skip declaration files and decorators"
work_units:
  - id: C01-W1
    date: 2026-10-10
    activity: "Test-out: C01 exit test cold (pass = skip C01-W2 to W4)"
    minutes: 20
  - id: C01-W2
    date: 2026-10-11
    activity: "Learn event loop, microtasks vs macrotasks, promise combinators, async error handling"
    minutes: 60
  - id: C01-W3
    date: 2026-10-12
    activity: "Implement from scratch with tests: debounce, throttle, flattenObject, deepEqual, promiseAll, retryWithBackoff"
    minutes: 150
  - id: C01-W4
    date: 2026-10-12
    activity: "Learn TypeScript narrowing, discriminated unions, generics, utility types; type the C01-W3 utilities strictly"
    minutes: 90
hours_calculation: "(20 + 60 + 150 + 90) min = 320 min x pace 1.0 = 5.33 h"
practice_ai_mode: "without-ai for test-out and drills; with-ai inside timed builds"
exit_test:
  id: XT-C01
  criteria:
    - "Predict the output order of 5 promise/timer snippets and explain each with microtask versus macrotask rules (all 5 correct)."
    - "Implement promiseAll or retryWithBackoff in 15 minutes, handling rejection and empty input, with your own tests passing."
    - "Type a discriminated-union API response and narrow it exhaustively under `strict` with no `any` (compiles, `never` check present)."
    - "Find and explain at least 3 of 4 planted bugs (lost `this`, closure over a loop variable, floating promise, loose equality)."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C16. Written asynchronous communication

```yaml
competency_id: C16
name: Written asynchronous communication
category: collaboration
importance: CORE (gatekeeper at Hyperproof application)
companies: [Hyperproof, Gather AI, Infisical, Metabase, Automattic]
market:
  trajectory: insufficient-data
  demand_share: "written communication 189 of 264 (72%, broad match); explicit "English" 55 of 264 (21%)"
  evidence: "skill-demand.csv (broad regular-expression match overcounts)"
relevance_decision: keep
relevance_reason: "Hyperproof requires an essay at application (a gatekeeper); Automattic weights written answers as a hiring step; take-home write-ups at Metabase, Infisical, Railway."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.55
  weight: 3
  impact: 1.64
  hours_to_close: 3.00
  score: 0.545
  rank: 3
  vital_few: true
coverage:   # most frequently tested first
  - "application essays (Hyperproof testing-and-reliability essay, async-communication essay)"
  - "pull-request descriptions: what, why, trade-offs, how verified"
  - "design doc: context, goals, non-goals, design, alternatives, risks"
not_covered:
  - "RFC processes of specific companies"
  - "technical blogging"
  - "documentation sites and docs-as-code tooling"
evidence:
  - "master-competency-map.md C16"
  - "requirements/hyperproof.md S2 (essay questions)"
  - "requirements/automattic.md S1, S2"
resources:
  - role: primary
    title: "Design Docs at Google"
    url: [https://www.industrialempathy.com/posts/design-docs-at-google/]
    verified: 2026-10-09
    covers: [C16-W1, C16-W3, C16-W4]
    skip: "none; read in full (single page)"
  - role: supplement
    title: "Hyperproof posting (essay questions)"
    url: [https://hyperproof.io/job-listings/?gh_jid=4708360005]
    verified: 2026-10-09
    covers: [C16-W2]
    skip: "none; read in full (single page)"
work_units:
  - id: C16-W1
    date: 2026-10-10
    activity: "Learn: design-doc structure and Hyperproof/Automattic application formats"
    minutes: 30
  - id: C16-W2
    date: 2026-10-10
    activity: "Write Hyperproof testing-and-reliability essay and async-communication essay; submit the real application"
    minutes: 60
  - id: C16-W4
    date: 2026-10-20
    activity: "Write PR descriptions for timed builds 1 and 2 and bug fix 1: what, why, trade-offs, how verified"
    minutes: 30
  - id: C16-W3
    date: 2026-10-22
    activity: "Write a 1-2 page design doc from Design 1 (context, goals, non-goals, design, alternatives, risks)"
    minutes: 60
hours_calculation: "(30 + 60 + 30 + 60) min = 180 min x pace 1.0 = 3.00 h"
practice_ai_mode: "without-ai for the final text (Metabase discloses AI screening for inconsistencies; essays must be your own words)"
exit_test:
  id: XT-C16
  criteria:
    - "The Hyperproof essays are submitted, each answering the question asked in its first two sentences."
    - "Each PR description (C16-W4) is under 200 words and states what changed, why, one trade-off, and how it was verified."
    - "The design doc (C16-W3) fits in 2 pages and lists at least 2 rejected alternatives with reasons and at least 3 risks."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C15. Explaining reasoning aloud

```yaml
competency_id: C15
name: Explaining reasoning aloud
category: interview communication
importance: CORE (format skill in every live stage)
companies: [Hyperproof, HighLevel, Drivetrain, Gather AI, Dscout, Infisical, Metabase, Automattic]
market:
  trajectory: shifting
  demand_share: "n/a (interview skill; not counted in postings)"
  evidence: "market-context.md s4-s5: Canva (2025-10-20, first-party) and Coinbase (2026-07-13 listing) score explanation and control of decisions"
relevance_decision: keep
relevance_reason: "Tested in every live stage at all 8 targets; stated weak area; trajectory shifting toward more weight."
required_depth: D2
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 2
leverage:
  reach: 1.00
  weight: 3
  impact: 6.00
  hours_to_close: 11.50
  score: 0.522
  rank: 4
  vital_few: true
coverage:   # most frequently tested first
  - "narrating approach before coding (clarify, examples, brute force, optimise, complexity, test)"
  - "stating complexity and trade-offs unprompted"
  - "past-project deep dive: architecture, 5 decisions with rejected alternatives, one failure, numbers (HighLevel past-work call)"
  - "behavioral story bank: 6 STAR stories, 2-3 minutes each"
  - "structured design walkthrough (shared with C06)"
  - "defending a decision under follow-up questions"
not_covered:
  - "public-speaking or presentation courses"
  - "accent or language coaching"
  - "negotiation scripts (outside the plan)"
  - "more than 4 full mocks"
evidence:
  - "master-competency-map.md C15"
  - "requirements/highlevel.md S14 (past-work call, 2-hour design plus past experience)"
  - "requirements/drivetrain.md D12 (interviewer ended a round early despite an acknowledged approach)"
  - "market-context.md s5"
resources:
  - role: primary
    title: "Tech Interview Handbook: Coding interview techniques"
    url: [https://www.techinterviewhandbook.org/coding-interview-techniques/]
    verified: 2026-10-09
    covers: [C15-W1]
    skip: "the named page only; skip the resume and negotiation sections"
  - role: supplement
    title: "LeetCode problem pages (free; problem IDs in activity)"
    url: [https://leetcode.com/problems/]
    verified: 2026-10-09
    covers: [C15-W2, C15-W6a, C15-W6d]
    skip: "skip the editorial and discussion tabs until after your attempt; NeetCode videos only for a problem you failed after 25 minutes"
  - role: supplement
    title: "Tech Interview Handbook: Behavioral interviews"
    url: [https://www.techinterviewhandbook.org/behavioral-interview/]
    verified: 2026-10-09
    covers: [C15-W3, C15-W4, C15-W5, C15-W6c]
    skip: "the named page only; skip the resume and negotiation sections"
  - role: supplement
    title: "Hello Interview: System Design Delivery Framework"
    url: [https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery]
    verified: 2026-10-09
    covers: [C15-W6b]
    skip: "free pages only; skip premium mock-interview offers"
work_units:
  - id: C15-W1
    date: 2026-10-10
    activity: "Learn the narration protocol: clarify, examples, brute force, optimise, complexity, test"
    minutes: 30
  - id: C15-W2
    date: 2026-10-10
    activity: "Diagnostic: solve Valid Parentheses (LC 20) aloud while screen- and voice-recording; review the recording against the protocol"
    minutes: 30
  - id: C15-W4
    date: 2026-10-11
    activity: "Write past-project deep-dive scripts for the CRM and SaaS products: architecture sketch, 5 decisions with rejected alternatives, one failure, numbers"
    minutes: 120
  - id: C15-W3
    date: 2026-10-17
    activity: "Write a 6-story bank (STAR, 2-3 min each): CRM build, SaaS build, conflict, failure, ownership beyond scope, learning fast"
    minutes: 150
  - id: C15-W5
    date: 2026-10-20
    activity: "Rehearse the story bank and project deep-dives aloud, recorded, two passes; cut each to under 3 minutes"
    minutes: 60
  - id: C15-W6a
    date: 2026-10-22
    activity: "Mock 1, coding (60 min + 15 review): Decode String (394) and Word Search (79), recorded, narrated, no AI"
    minutes: 75
  - id: C15-W6b
    date: 2026-10-24
    activity: "Mock 2, design (60 min + 15 review): unseen prompt (URL shortener with analytics), recorded, with 3 perturbations"
    minutes: 75
  - id: C15-W6c
    date: 2026-10-25
    activity: "Mock 3, past-project and behavioral (60 min + 15 review): deep-dive follow-ups to the depth floor, recorded"
    minutes: 75
  - id: C15-W6d
    date: 2026-10-28
    activity: "Mock 4, final coding (= C05 exit test): Generate Parentheses (22) and Coin Change (322), 45 min, narrated, no AI"
    minutes: 75
hours_calculation: "(30 + 30 + 120 + 150 + 60 + 75 + 75 + 75 + 75) min = 690 min x pace 1.0 = 11.50 h"
practice_ai_mode: "without-ai (Drivetrain live rounds); with-ai narration in timed builds (C03)"
exit_test:
  id: XT-C15
  criteria:
    - "In two consecutive recorded mocks (one coding, one design), you ask at least two clarifying questions before writing code or drawing boxes."
    - "You state the plan before implementing, and the recording has no silence longer than 60 seconds while you work."
    - "You state time and space complexity (coding) or two trade-offs with rejected alternatives (design) without being asked."
    - "Each of the 6 stories runs under 3 minutes and names your own role, one decision, and one number."
    - "The CRM and SaaS deep-dives survive five consecutive "why?" follow-ups in Mock 3 without "I don't remember" on a decision you claim."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C09. Testing and code quality

```yaml
competency_id: C09
name: Testing and code quality
category: quality
importance: CORE
companies: [Hyperproof, HighLevel, Infisical, Metabase, Automattic]
market:
  trajectory: insufficient-data
  demand_share: "testing 147 of 264 (56%); end-to-end 99 of 264 (38%); code review 69 of 264 (26%)"
  evidence: "skill-demand.csv; code review of generated code is `shifting` (market-context.md s6)"
relevance_decision: keep
relevance_reason: "Hyperproof testing essay and take-home; Infisical and Metabase take-home grading; HighLevel build round asks for tests."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.64
  weight: 3
  impact: 1.91
  hours_to_close: 4.50
  score: 0.424
  rank: 5
  vital_few: true
coverage:   # most frequently tested first
  - "test layers and what each catches (unit, integration, end-to-end)"
  - "naming tests by behaviour; arrange-act-assert"
  - "what to mock and what to run for real (real PostgreSQL in Docker for integration)"
  - "Vitest and Supertest"
  - "one Playwright end-to-end test"
not_covered:
  - "test-driven development as a methodology"
  - "property-based and mutation-testing frameworks"
  - "visual regression"
  - "load testing"
  - "contract testing (Pact)"
evidence:
  - "master-competency-map.md C09"
  - "requirements/hyperproof.md S2 (testing essay), S5 (unit-test naming question)"
resources:
  - role: primary
    title: "Vitest guide ; Testing Trophy"
    url: [https://vitest.dev/guide/, https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications]
    verified: 2026-10-09
    covers: [C09-W1, C09-W2]
    skip: "Getting Started and mocking pages only"
  - role: supplement
    title: "Playwright docs"
    url: [https://playwright.dev/docs/intro]
    verified: 2026-10-09
    covers: [C09-W3]
    skip: "none; read in full (single page)"
work_units:
  - id: C09-W1
    date: 2026-10-14
    activity: "Learn test layers (unit, integration, end-to-end), naming, arrange-act-assert, what to mock"
    minutes: 60
  - id: C09-W2
    date: 2026-10-14
    activity: "Write unit and integration tests (Vitest + Supertest against a Dockerised PostgreSQL) for the C03-W3 API"
    minutes: 120
  - id: C09-W3
    date: 2026-10-22
    activity: "Write one Playwright end-to-end test for the C02-W3 grid"
    minutes: 45
  - id: C09-W4
    date: 2026-10-22
    activity: "C09 exit test (see exit tests)"
    minutes: 45
hours_calculation: "(60 + 120 + 45 + 45) min = 270 min x pace 1.0 = 4.50 h"
practice_ai_mode: "both; generated tests count only after you have seen each one fail"
exit_test:
  id: XT-C09
  criteria:
    - "On an unseen small module plus endpoint, write unit tests for its boundaries and one integration test against real PostgreSQL in 30 minutes."
    - "All 3 planted mutations (off-by-one, wrong status code, missing transaction) make at least one of your tests fail."
    - "Explain in 5 minutes what you mocked, what you did not, and which of your tests you would delete first and why."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C07. Asynchronous processing and reliability

```yaml
competency_id: C07
name: Asynchronous processing and reliability
category: distributed systems
importance: BRANCH
companies: [HighLevel, Gather AI, Infisical]
market:
  trajectory: insufficient-data
  demand_share: "queues/streaming 21 of 264 (8%); microservices/distributed 84 of 264 (32%)"
  evidence: "skill-demand.csv"
relevance_decision: cap
relevance_reason: "Capped at D2 for idempotency, retries and at-least-once delivery only; HighLevel postings name these explicitly. Broker internals are out."
required_depth: D2 (capped subset)
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 2
leverage:
  reach: 0.36
  weight: 2
  impact: 1.45
  hours_to_close: 4.00
  score: 0.364
  rank: 6
  vital_few: true
coverage:   # most frequently tested first
  - "at-least-once delivery and why exactly-once is an effect, not a transport guarantee"
  - "idempotent consumers with an idempotency-key table"
  - "retries with exponential backoff and jitter"
  - "dead-letter handling and replay"
  - "transactional outbox for dual writes"
  - "one working implementation: BullMQ on Redis"
not_covered:
  - "Kafka partitions, consumer groups, offsets"
  - "RabbitMQ exchanges and routing"
  - "stream processing (Flink, Kafka Streams)"
  - "saga orchestration frameworks"
  - "Temporal workflows"
evidence:
  - "master-competency-map.md C07"
  - "requirements/highlevel.md S2 (idempotency, retries, Pub/Sub, Cloud Tasks)"
  - "requirements/gather-ai.md G1"
resources:
  - role: primary
    title: "AWS: Timeouts, retries and backoff with jitter ; Transactional outbox"
    url: [https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter, https://microservices.io/patterns/data/transactional-outbox.html]
    verified: 2026-10-09
    covers: [C07-W1]
    skip: "none; read in full (single page)"
  - role: supplement
    title: "BullMQ docs"
    url: [https://docs.bullmq.io/]
    verified: 2026-10-09
    covers: [C07-W2]
    skip: "none; read in full (single page)"
work_units:
  - id: C07-W1
    date: 2026-10-16
    activity: "Learn at-least-once delivery, idempotent consumers, retries with exponential backoff and jitter, dead-letter queues, transactional outbox"
    minutes: 90
  - id: C07-W2
    date: 2026-10-16
    activity: "Implement a BullMQ worker (Redis in Docker) with retries, backoff, idempotency key table and a dead-letter path; test duplicate delivery"
    minutes: 120
  - id: C07-W3
    date: 2026-10-16
    activity: "Exit rehearsal: explain aloud two failure scenarios (consumer crash mid-job; duplicate webhook) and the fix"
    minutes: 30
hours_calculation: "(90 + 120 + 30) min = 240 min x pace 1.0 = 4.00 h"
practice_ai_mode: "with-ai for the worker build; without-ai for the explanation"
exit_test:
  id: XT-C07
  criteria:
    - "Explain aloud in 10 minutes without notes: at-least-once delivery, idempotent consumer, backoff with jitter (and why jitter), dead-letter queue and replay, transactional outbox."
    - "Your BullMQ worker test that delivers the same job twice shows exactly one side effect."
    - "Walk through two failure scenarios (consumer crash mid-job; duplicate webhook) and state the fix for each."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C18-HP. GRC domain: risk register (Hyperproof branch)

```yaml
competency_id: C18-HP
name: GRC domain: risk register (Hyperproof branch)
category: domain
importance: BRANCH
companies: [Hyperproof]
market:
  trajectory: n/a
  demand_share: "n/a"
  evidence: "domain knowledge; not a market skill family"
relevance_decision: keep
relevance_reason: "Hyperproof posting prefers compliance-domain experience; Risk Management team builds the risk register."
required_depth: D1
assessment:
  measured_depth: none (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.18
  weight: 2
  impact: 0.36
  hours_to_close: 1.00
  score: 0.364
  rank: 7
  vital_few: true
coverage:   # most frequently tested first
  - "risk register entities"
  - "inherent versus residual risk (likelihood x impact, reduced by control effectiveness)"
  - "control testing and its schedule"
  - "SOC 2 versus ISO 27001 at one-sentence level"
not_covered:
  - "auditor-level SOC 2 criteria"
  - "NIST CSF and FedRAMP control catalogues"
  - "quantitative risk models (FAIR)"
evidence:
  - "requirements/hyperproof.md S1, S2, section 6"
resources:
  - role: primary
    title: "Hyperproof: Risk register guide ; Inherent vs residual risk"
    url: [https://hyperproof.io/resource/risk-register-key-benefits/, https://hyperproof.io/resource/inherent-risk-vs-residual-risk/]
    verified: 2026-10-09
    covers: [C18-HP-W1]
    skip: "none; read in full (single page)"
work_units:
  - id: C18-HP-W1
    date: 2026-10-10
    activity: "Learn risk register, inherent vs residual risk, control testing; sketch a risk-register schema"
    minutes: 60
hours_calculation: "(60) min = 60 min x pace 1.0 = 1.00 h"
practice_ai_mode: "without-ai"
exit_test:
  id: XT-C18-HP
  criteria:
    - "Explain in 5 minutes: risk register, inherent versus residual risk, control testing, and SOC 2 versus ISO 27001."
    - "Your schema sketch has risks, controls, a many-to-many risk-control mapping, a control-test schedule, and audit history."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C13. AI-assisted engineering (direct and verify)

```yaml
competency_id: C13
name: AI-assisted engineering (direct and verify)
category: AI-era engineering
importance: BRANCH
companies: [HighLevel, Gather AI, Dscout, Automattic]
market:
  trajectory: rising
  demand_share: "58 of 264 (22%); Segment B 37 of 151 (25%)"
  evidence: "market-context.md s6: Stack Overflow 2026 coding agents 66% (M2); DORA 2025 90% adoption (M2)"
relevance_decision: keep
relevance_reason: "Required at HighLevel ("AI-native builder") and Dscout; AI reportedly allowed in HighLevel build round (anecdotal); rising."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.45
  weight: 2
  impact: 0.91
  hours_to_close: 2.58
  score: 0.352
  rank: 8
  vital_few: true
coverage:   # most frequently tested first
  - "plan first, constrain scope, use tests as the verification oracle"
  - "agent instruction file (AGENTS.md or CLAUDE.md)"
  - "reviewing AI-generated diffs like a pull request"
  - "stating which code was AI-written and how it was verified"
not_covered:
  - "building your own coding agent"
  - "MCP server development"
  - "comparing AI tool vendors"
  - "prompt-engineering courses"
evidence:
  - "master-competency-map.md C13"
  - "requirements/highlevel.md S1, S2 ("slop-free code")"
  - "requirements/dscout.md S1, S7, S8"
resources:
  - role: primary
    title: "Claude Code best practices"
    url: [https://code.claude.com/docs/en/best-practices]
    verified: 2026-10-09
    covers: [C13-W1, C13-W3]
    skip: "none; read in full (single page)"
  - role: supplement
    title: "AGENTS.md format"
    url: [https://agents.md/]
    verified: 2026-10-09
    covers: [C13-W2]
    skip: "none; read in full (single page)"
work_units:
  - id: C13-W1
    date: 2026-10-13
    activity: "Learn agent workflow: plan first, constrain scope, tests as the verification oracle, reading diffs"
    minutes: 45
  - id: C13-W2
    date: 2026-10-13
    activity: "Write an AGENTS.md / CLAUDE.md for the build-practice repo (stack, commands, conventions, test rule)"
    minutes: 20
  - id: C13-W3
    date: 2026-10-18
    activity: "Review three AI-generated diffs with planted defects (generate with an assistant, then hide 3 defects each via a second prompt; find them blind)"
    minutes: 90
hours_calculation: "(45 + 20 + 90) min = 155 min x pace 1.0 = 2.58 h"
practice_ai_mode: "with-ai (the subject of the competency)"
exit_test:
  id: XT-C13
  criteria:
    - "Given a fresh AI-generated diff with 3 planted defects, find all 3 in 20 minutes and write a review comment for each."
    - "In timed build 4 (C03-W5), for every accepted AI chunk you can name the test or check that verified it."
    - "Your AGENTS.md lists stack, run and test commands, conventions, and a rule that changes need passing tests."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C03. Node.js backend and API design

```yaml
competency_id: C03
name: Node.js backend and API design
category: backend
importance: CORE
companies: [Hyperproof, HighLevel, Gather AI, Dscout, Infisical]
market:
  trajectory: insufficient-data
  demand_share: "Node.js 73 of 264 (28%); NestJS 18 (7%); REST/API 173 (66%, broad); GraphQL 25 (9%)"
  evidence: "skill-demand.csv"
relevance_decision: keep
relevance_reason: "HighLevel timed build-an-API round is the decisive stage there (corroborated); take-homes at Hyperproof, Infisical, Railway."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.64
  weight: 3
  impact: 1.91
  hours_to_close: 6.00
  score: 0.318
  rank: 9
  vital_few: true
coverage:   # most frequently tested first
  - "REST resource naming and status codes"
  - "validation and a consistent error shape"
  - "cursor pagination"
  - "idempotency keys on writes"
  - "module structure for a 60-minute build"
  - "schema and index choices explained aloud"
not_covered:
  - "GraphQL server design (Dscout D0 only)"
  - "NestJS internals beyond modules and DI"
  - "API gateways"
  - "gRPC"
  - "OpenAPI code generation"
evidence:
  - "master-competency-map.md C03"
  - "requirements/highlevel.md S2, S12-S15 (build round)"
resources:
  - role: primary
    title: "Zalando RESTful API Guidelines ; Stripe idempotency"
    url: [https://opensource.zalando.com/restful-api-guidelines/, https://stripe.com/blog/idempotency]
    verified: 2026-10-09
    covers: [C03-W2, C03-W3, C03-W4]
    skip: "sections on naming, HTTP status codes, errors, pagination and compatibility only; skip events and the Zalando-specific JSON rules"
work_units:
  - id: C03-W1
    date: 2026-10-11
    activity: "Test-out: 60-min timed build of a contacts-with-tags REST API in Node/TypeScript, AI allowed, narrated (pass = skip C03-W2 to W4)"
    minutes: 60
  - id: C03-W2
    date: 2026-10-13
    activity: "Learn REST conventions: resource naming, status codes, errors, cursor pagination, validation, idempotency keys"
    minutes: 60
  - id: C03-W3
    date: 2026-10-13
    activity: "Timed build 2 (60 min + 20 review): social-feed API with cursor pagination, AI allowed, narrate accept/reject decisions"
    minutes: 80
  - id: C03-W4
    date: 2026-10-21
    activity: "Timed build 3 (60 min + 20 review): booking API with seat hold expiry and idempotent confirm"
    minutes: 80
  - id: C03-W5
    date: 2026-10-23
    activity: "C03 exit test: HighLevel-style timed build 4 (see exit tests)"
    minutes: 80
hours_calculation: "(60 + 60 + 80 + 80 + 80) min = 360 min x pace 1.0 = 6.00 h"
practice_ai_mode: "with-ai (HighLevel build round, anecdotal policy); narrate accept/reject decisions"
exit_test:
  id: XT-C03
  criteria:
    - "Timed build 4 (60 minutes plus 20 review, AI allowed) on an unseen spec: all endpoints work end to end."
    - "Invalid input returns 400 with a consistent error body; list endpoint uses cursor pagination; POST honours an Idempotency-Key header."
    - "At least 5 tests pass, including one for the idempotent retry."
    - "When asked, you explain the schema and two indexes in under 5 minutes."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C04. Relational data modelling and PostgreSQL

```yaml
competency_id: C04
name: Relational data modelling and PostgreSQL
category: data
importance: CORE
companies: [Hyperproof, HighLevel, Gather AI, Dscout, Infisical]
market:
  trajectory: insufficient-data
  demand_share: "PostgreSQL 82 of 264 (31%); data modelling phrasing 19 (7%)"
  evidence: "skill-demand.csv"
relevance_decision: keep
relevance_reason: "HighLevel schema discussion; Gather AI PostgreSQL tuning knock-out question; Hyperproof data modelling."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.64
  weight: 3
  impact: 1.91
  hours_to_close: 6.23
  score: 0.306
  rank: 10
  vital_few: true
coverage:   # most frequently tested first
  - "schema design and normalisation with keys and constraints"
  - "B-tree, composite and partial indexes; column order"
  - "EXPLAIN / EXPLAIN ANALYZE reading"
  - "isolation levels, MVCC at the level of what each isolation level permits"
  - "row locks (SELECT ... FOR UPDATE) and unique constraints against races"
  - "joins, aggregates, window functions"
not_covered:
  - "PostgreSQL internals (WAL, vacuum tuning, storage format)"
  - "replication and failover setup"
  - "sharding implementation (concept only, in C06)"
  - "stored procedures and PL/pgSQL"
  - "non-PostgreSQL SQL dialects"
evidence:
  - "master-competency-map.md C04"
  - "requirements/hyperproof.md S1"
  - "requirements/gather-ai.md G2 (knock-out question)"
resources:
  - role: primary
    title: "Use The Index, Luke"
    url: [https://use-the-index-luke.com/]
    verified: 2026-10-09
    covers: [C04-W2]
    skip: "chapters 1-2 and 5 only; skip vendor-specific sections for Oracle, MySQL and SQL Server"
  - role: supplement
    title: "PostgreSQL 18 docs: Using EXPLAIN, Transaction Isolation, Explicit Locking"
    url: [https://www.postgresql.org/docs/current/using-explain.html]
    verified: 2026-10-09
    covers: [C04-W3, C04-W5]
    skip: "Using EXPLAIN, Transaction Isolation, Explicit Locking only"
  - role: supplement
    title: "PostgreSQL Exercises"
    url: [https://pgexercises.com/]
    verified: 2026-10-09
    covers: [C04-W4a, C04-W4b]
    skip: "none; read in full (single page)"
work_units:
  - id: C04-W1
    date: 2026-10-10
    activity: "Test-out: C04 exit test cold (pass = skip C04-W2 to W5)"
    minutes: 20
  - id: C04-W2
    date: 2026-10-15
    activity: "Learn B-tree indexes, composite and partial indexes, index-only scans (Use The Index, Luke ch. 1-2, 5)"
    minutes: 90
  - id: C04-W3
    date: 2026-10-15
    activity: "Learn EXPLAIN / EXPLAIN ANALYZE, isolation levels, MVCC, row locks (SELECT ... FOR UPDATE)"
    minutes: 60
  - id: C04-W5
    date: 2026-10-15
    activity: "Lab: 1M-row contacts table in Docker PostgreSQL; compare plans before/after indexes; reproduce a double-booking race and fix it"
    minutes: 60
  - id: C04-W4a
    date: 2026-10-16
    activity: "SQL practice part 1: pgexercises Joins and Aggregates sections, timed"
    minutes: 72
  - id: C04-W4b
    date: 2026-10-17
    activity: "SQL practice part 2: pgexercises Modifying Data and window-function exercises, timed"
    minutes: 72
hours_calculation: "(20 + 90 + 60 + 60 + 72 + 72) min = 374 min x pace 1.0 = 6.23 h"
practice_ai_mode: "without-ai for SQL drills and test-out"
exit_test:
  id: XT-C04
  criteria:
    - "Design a contacts-tags-notes schema with keys and constraints in 8 minutes."
    - "Given an EXPLAIN ANALYZE output with a sequential scan, propose a composite index, justify its column order, and predict the new plan."
    - "Write one join-plus-aggregate query and one window-function query that are correct on first run."
    - "Explain a double-booking race and fix it with a row lock or a unique constraint, naming the isolation level involved."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C10. Debugging and working in existing codebases

```yaml
competency_id: C10
name: Debugging and working in existing codebases
category: operations
importance: BRANCH
companies: [HighLevel, Gather AI, Infisical, Metabase, Automattic]
market:
  trajectory: insufficient-data
  demand_share: "debugging 96 of 264 (36%); observability 107 (41%); on-call 56 (21%)"
  evidence: "skill-demand.csv; Canva first-party: debugging AI-generated code (market-context.md s4)"
relevance_decision: keep
relevance_reason: "Automattic code test on existing code or trial; Infisical work day in the real monorepo; Metabase screen."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.55
  weight: 2
  impact: 1.09
  hours_to_close: 3.75
  score: 0.291
  rank: 11
  vital_few: true
coverage:   # most frequently tested first
  - "reproduce first with a failing test"
  - "Node inspector breakpoints"
  - "Chrome DevTools Performance panel"
  - "reading an unfamiliar repository: entry points, tests, recent commits"
  - "writing the PR description for the fix"
not_covered:
  - "observability stacks (OpenTelemetry, Grafana) beyond reading logs"
  - "production incident command"
  - "memory-leak heap analysis"
  - "kernel or network-level debugging"
evidence:
  - "master-competency-map.md C10"
  - "requirements/automattic.md S2"
  - "requirements/infisical.md S14"
  - "requirements/metabase.md S11, S16"
resources:
  - role: primary
    title: "Node.js: Debugging ; Chrome DevTools Performance"
    url: [https://nodejs.org/learn/getting-started/debugging, https://developer.chrome.com/docs/devtools/performance]
    verified: 2026-10-09
    covers: [C10-W1]
    skip: "none; read in full (single page)"
work_units:
  - id: C10-W1
    date: 2026-10-18
    activity: "Learn Node inspector breakpoints and Chrome DevTools Performance panel"
    minutes: 45
  - id: C10-W2
    date: 2026-10-19
    activity: "Timeboxed bug fix 1 (60 min) in an unfamiliar open-source TypeScript repo: reproduce, locate, fix, test"
    minutes: 60
  - id: C10-W3
    date: 2026-10-19
    activity: "Timeboxed bug fix 2 (60 min), different repo; write the PR description"
    minutes: 60
  - id: C10-W4
    date: 2026-10-22
    activity: "C10 exit test: timeboxed bug fix 3 (60 min) narrated"
    minutes: 60
hours_calculation: "(45 + 60 + 60 + 60) min = 225 min x pace 1.0 = 3.75 h"
practice_ai_mode: "without-ai for the exit test; with-ai allowed in bug fixes 1-2 if you narrate verification"
exit_test:
  id: XT-C10
  criteria:
    - "Bug fix 3 in an unfamiliar repository within 60 minutes, narrated: a failing test reproduces the bug before any fix."
    - "You locate the root cause with the debugger or logs, not by trial edits."
    - "The fix passes the test suite and has a PR description that states cause, fix and verification."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C02. React frontend engineering

```yaml
competency_id: C02
name: React frontend engineering
category: frontend
importance: CORE
companies: [Hyperproof, Drivetrain, Dscout, Infisical, Metabase]
market:
  trajectory: insufficient-data
  demand_share: "95 of 264 (36%) Segment A; 106 of 151 (70%) Segment B"
  evidence: "skill-demand.csv"
relevance_decision: keep
relevance_reason: "Drivetrain spreadsheet-style and data-visualisation components; Metabase React panel; take-homes with UI."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.64
  weight: 3
  impact: 1.91
  hours_to_close: 7.08
  score: 0.270
  rank: 12
  vital_few: true
coverage:   # most frequently tested first
  - "effects pitfalls ("you might not need an effect")"
  - "state preservation and keys"
  - "memo, useMemo, useCallback: when they help and when not"
  - "rendering 10,000 rows with virtualisation"
  - "machine-coding drills: debounced autocomplete, filterable list with URL state, accessible modal"
not_covered:
  - "React Server Components and Next.js App Router internals"
  - "charts and data-visualisation libraries (parked; see rabbit-hole parking lot)"
  - "CSS architecture and design systems beyond using one (parked; Metabase only)"
  - "React Native"
  - "animation libraries"
evidence:
  - "master-competency-map.md C02"
  - "requirements/drivetrain.md D1"
  - "requirements/metabase.md S2, S15, S16"
resources:
  - role: primary
    title: "react.dev: You Might Not Need an Effect; Preserving and Resetting State; memo"
    url: [https://react.dev/learn/you-might-not-need-an-effect]
    verified: 2026-10-09
    covers: [C02-W2, C02-W4]
    skip: "the three named pages only"
  - role: supplement
    title: "TanStack Virtual docs"
    url: [https://tanstack.com/virtual/latest/docs/introduction]
    verified: 2026-10-09
    covers: [C02-W3]
    skip: "none; read in full (single page)"
work_units:
  - id: C02-W1
    date: 2026-10-10
    activity: "Test-out: C02 exit test cold (pass = skip C02-W2 to W4)"
    minutes: 20
  - id: C02-W2
    date: 2026-10-20
    activity: "Learn effects pitfalls, state preservation and keys, memo/useMemo/useCallback, rendering lists"
    minutes: 90
  - id: C02-W3
    date: 2026-10-20
    activity: "Build a 10,000-row spreadsheet-style grid: virtualised rows (TanStack Virtual), sort, filter, inline edit; profile re-renders"
    minutes: 180
  - id: C02-W4
    date: 2026-10-24
    activity: "Three timed React machine-coding drills (45 min each): debounced autocomplete, filterable list with URL state, accessible modal"
    minutes: 135
hours_calculation: "(20 + 90 + 180 + 135) min = 425 min x pace 1.0 = 7.08 h"
practice_ai_mode: "without-ai for drills (Drivetrain and Metabase policy unknown); with-ai for the grid build"
exit_test:
  id: XT-C02
  criteria:
    - "Fix a list component with 3 planted issues (index keys, effect used for derived state, needless re-render of every row) in 20 minutes and explain each."
    - "Explain without notes when memo, useMemo and useCallback help and when they do not, with one example each."
    - "Build a debounced autocomplete with loading, error and empty states and keyboard navigation in 45 minutes, without AI (the first C02-W4 drill). The 20-minute test-out C02-W1 runs criteria 1 and 2 only."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C06. System design and architecture defense

```yaml
competency_id: C06
name: System design and architecture defense
category: design
importance: CORE
companies: [Hyperproof, HighLevel, Drivetrain, Gather AI, Infisical, Metabase]
market:
  trajectory: insufficient-data
  demand_share: "160 of 264 (61%, broad match)"
  evidence: "skill-demand.csv; GitHub commentary says weight is increasing (M3 only)"
relevance_decision: keep
relevance_reason: "HighLevel 2-hour design round; Drivetrain LLD plus HLD; Metabase architecture panel; Hyperproof one-to-ones; Infisical take-home extension; stated weak area."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.82
  weight: 3
  impact: 2.45
  hours_to_close: 11.50
  score: 0.213
  rank: 13
  vital_few: true
coverage:   # most frequently tested first
  - "delivery framework: requirements (with numbers), core entities, API, high-level design, deep dives"
  - "back-of-envelope estimates"
  - "data store choice and partition-key choice"
  - "queues and background jobs (from C07)"
  - "caching (from C08)"
  - "concurrency: double booking, seat holds"
  - "failure handling and perturbations (10x load, dependency failure, requirement change)"
  - "low-level design: classes for a booking system, Snake and Ladders"
not_covered:
  - "planet-scale designs (global replication, multi-region active-active)"
  - "consensus algorithms (Raft, Paxos)"
  - "CAP proofs and formal consistency models"
  - "designs outside mid-level product scope (YouTube, Google Search)"
evidence:
  - "master-competency-map.md C06"
  - "requirements/highlevel.md S12-S14"
  - "requirements/drivetrain.md D12"
  - "requirements/metabase.md S15"
resources:
  - role: primary
    title: "Hello Interview: System Design Delivery Framework"
    url: [https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery]
    verified: 2026-10-09
    covers: [C06-W1, C06-W2, C06-W4, C06-W5]
    skip: "free pages only; skip premium mock-interview offers"
  - role: supplement
    title: "Hello Interview: Design Ticketmaster"
    url: [https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster]
    verified: 2026-10-09
    covers: [C06-W3]
    skip: "free pages only; skip premium mock-interview offers"
  - role: supplement
    title: "Hello Interview: Design News Feed"
    url: [https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed]
    verified: 2026-10-09
    covers: [C06-W6]
    skip: "free pages only; skip premium mock-interview offers"
  - role: supplement
    title: "Hello Interview: Distributed Rate Limiter"
    url: [https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter]
    verified: 2026-10-09
    covers: [C06-W7]
    skip: "free pages only; skip premium mock-interview offers"
work_units:
  - id: C06-W1
    date: 2026-10-18
    activity: "Learn the delivery framework: requirements, core entities, API, high-level design, deep dives; back-of-envelope estimates"
    minutes: 120
  - id: C06-W2
    date: 2026-10-18
    activity: "Design 1 aloud (60 min + 20 review): HighLevel-style contacts service, millions of contacts, tags, segment search, bulk import"
    minutes: 80
  - id: C06-W3
    date: 2026-10-19
    activity: "Design 2 aloud: Drivetrain-style booking app, seat holds and double-booking prevention (HLD), then compare with the Ticketmaster breakdown"
    minutes: 80
  - id: C06-W4
    date: 2026-10-21
    activity: "Design 3 aloud: Hyperproof-style risk register with control-test scheduling, audit trail, RBAC"
    minutes: 80
  - id: C06-W5
    date: 2026-10-22
    activity: "Design 4 aloud: Infisical-style one-time secret-sharing app (encryption, expiry, access audit)"
    minutes: 80
  - id: C06-W6
    date: 2026-10-23
    activity: "Design 5 aloud: news feed / notifications fan-out, then compare with the News Feed breakdown"
    minutes: 80
  - id: C06-W7
    date: 2026-10-23
    activity: "Design 6 aloud: rate limiter for a public API, then compare with the rate-limiter breakdown"
    minutes: 80
  - id: C06-W9
    date: 2026-10-23
    activity: "Low-level design, 2 x 45 min: booking system classes; Snake and Ladders (HighLevel-reported)"
    minutes: 90
hours_calculation: "(120 + 80 + 80 + 80 + 80 + 80 + 80 + 90) min = 690 min x pace 1.0 = 11.50 h"
practice_ai_mode: "without-ai (live design rounds)"
exit_test:
  id: XT-C06
  criteria:
    - "In Mock 2 (unseen prompt, 60 minutes, recorded): functional and non-functional requirements with numbers inside the first 8 minutes."
    - "Entities, API and a high-level design with a justified data-store choice; deep dive on 2 bottlenecks."
    - "Each of the 3 perturbations gets a concrete design change, stated aloud."
    - "At least 2 trade-offs named with the rejected alternative and why."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C18-IN. Secrets, PKI and KMS basics (Infisical branch)

```yaml
competency_id: C18-IN
name: Secrets, PKI and KMS basics (Infisical branch)
category: domain
importance: BRANCH
companies: [Infisical]
market:
  trajectory: n/a
  demand_share: "n/a"
  evidence: "domain knowledge"
relevance_decision: keep (eligibility gate)
relevance_reason: "Infisical is a secrets-management company; the take-home is a secret-sharing app (anecdotal). Do only after India eligibility is confirmed."
required_depth: D1
assessment:
  measured_depth: none (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.09
  weight: 2
  impact: 0.18
  hours_to_close: 1.00
  score: 0.182
  rank: 14
  vital_few: false
coverage:   # most frequently tested first
  - "secret lifecycle: create, rotate, revoke"
  - "envelope encryption (data key and key-encryption key)"
  - "dynamic secrets"
  - "what a PKI, an X.509 certificate and a KMS do"
not_covered:
  - "ACME, EST and KMIP protocols"
  - "FIPS deployment"
  - "HSM hardware"
  - "SAML and SCIM details"
evidence:
  - "requirements/infisical.md S1, S4, S14, section 6"
resources:
  - role: primary
    title: "Infisical docs"
    url: [https://infisical.com/docs/documentation/getting-started/introduction]
    verified: 2026-10-09
    covers: [C18-IN-W1]
    skip: "secrets, rotation and KMS concept pages only; skip self-hosting guides"
work_units:
  - id: C18-IN-W1
    date: 2026-10-27
    activity: "Infisical branch: secrets lifecycle, rotation, envelope encryption, PKI/KMS terms"
    minutes: 60
hours_calculation: "(60) min = 60 min x pace 1.0 = 1.00 h"
practice_ai_mode: "without-ai"
exit_test:
  id: XT-C18-IN
  criteria:
    - "Explain in 10 minutes: secret lifecycle, envelope encryption, dynamic secrets, PKI and KMS roles."
    - "Apply envelope encryption and rotation to your Design 4 (C06-W5) aloud."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C02-MB. Redux Toolkit (Metabase branch)

```yaml
competency_id: C02-MB
name: Redux Toolkit (Metabase branch)
category: frontend
importance: BRANCH
companies: [Metabase]
market:
  trajectory: insufficient-data
  demand_share: "not separately counted"
  evidence: "n/a"
relevance_decision: keep (eligibility gate)
relevance_reason: "Metabase frontend uses Redux; do only after India eligibility is confirmed."
required_depth: D1
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.09
  weight: 2
  impact: 0.18
  hours_to_close: 1.00
  score: 0.182
  rank: 15
  vital_few: false
coverage:   # most frequently tested first
  - "slices and reducers"
  - "memoised selectors"
  - "Redux state versus local state versus server cache"
not_covered:
  - "RTK Query"
  - "redux-saga"
  - "middleware authoring"
evidence:
  - "requirements/metabase.md S2, S12"
resources:
  - role: primary
    title: "Redux Essentials"
    url: [https://redux.js.org/tutorials/essentials/part-1-overview-concepts]
    verified: 2026-10-09
    covers: [C02-MB-W1]
    skip: "parts 1-2 only"
work_units:
  - id: C02-MB-W1
    date: 2026-10-26
    activity: "Learn Redux Toolkit essentials (slices, selectors); refactor grid filter state to RTK"
    minutes: 60
hours_calculation: "(60) min = 60 min x pace 1.0 = 1.00 h"
practice_ai_mode: "with-ai allowed"
exit_test:
  id: XT-C02-MB
  criteria:
    - "Grid filter state lives in an RTK slice with memoised selectors and the grid still passes its tests."
    - "Explain when state belongs in Redux, in a component, or in a server cache such as TanStack Query."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C16-AU. Automattic written application and WordPress awareness

```yaml
competency_id: C16-AU
name: Automattic written application and WordPress awareness
category: collaboration
importance: BRANCH (gatekeeper: written application)
companies: [Automattic]
market:
  trajectory: insufficient-data
  demand_share: "n/a"
  evidence: "n/a"
relevance_decision: keep (eligibility gate)
relevance_reason: "Automattic says application answers "are a significant part of the hiring process". Do only after India eligibility is confirmed."
required_depth: D1
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.09
  weight: 3
  impact: 0.27
  hours_to_close: 1.50
  score: 0.182
  rank: 16
  vital_few: true
coverage:   # most frequently tested first
  - "weighted application answers with a debugging or quality story and a number"
  - "WordPress plugin model: hooks, actions versus filters"
not_covered:
  - "PHP language study"
  - "Gutenberg block development"
  - "WordPress core internals"
evidence:
  - "requirements/automattic.md S1, S2"
resources:
  - role: primary
    title: "Automattic: Work with us (hiring process) ; WordPress Plugin Handbook"
    url: [https://automattic.com/work-with-us/, https://developer.wordpress.org/plugins/]
    verified: 2026-10-09
    covers: [C16-AU-W1]
    skip: "none; read in full (single page)"
work_units:
  - id: C16-AU-W1
    date: 2026-10-21
    activity: "Automattic branch: write weighted application answers; read the plugin handbook introduction"
    minutes: 90
hours_calculation: "(90) min = 90 min x pace 1.0 = 1.50 h"
practice_ai_mode: "without-ai for the answers"
exit_test:
  id: XT-C16-AU
  criteria:
    - "Each application answer is under 250 words and contains one concrete story with a number."
    - "Explain in 5 minutes how a plugin hooks into WordPress, and the difference between an action and a filter."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C08. Caching and NoSQL stores

```yaml
competency_id: C08
name: Caching and NoSQL stores
category: data
importance: SUPPORTING
companies: [HighLevel, Gather AI, Infisical]
market:
  trajectory: insufficient-data
  demand_share: "Redis 26 of 264 (10%); MongoDB 35 (13%); search 21 (8%)"
  evidence: "skill-demand.csv"
relevance_decision: cap
relevance_reason: "Capped at D1: appears in HighLevel, Gather AI and Infisical stacks and design rounds, not as a separate stage."
required_depth: D1
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.36
  weight: 1
  impact: 0.36
  hours_to_close: 2.25
  score: 0.162
  rank: 17
  vital_few: false
coverage:   # most frequently tested first
  - "Redis cache-aside read and write paths"
  - "TTLs and invalidation on write"
  - "cache stampede protection"
  - "MongoDB embed versus reference and indexes"
not_covered:
  - "Redis Cluster and persistence tuning"
  - "Firestore specifics"
  - "Elasticsearch beyond "an inverted index serves segment search" (said in C06-W2)"
  - "DynamoDB single-table design"
evidence:
  - "master-competency-map.md C08"
  - "requirements/highlevel.md S1, S9"
resources:
  - role: primary
    title: "Redis: Cache-aside pattern"
    url: [https://redis.io/tutorials/howtos/solutions/microservices/caching/]
    verified: 2026-10-09
    covers: [C08-W1, C08-W3]
    skip: "none; read in full (single page)"
  - role: supplement
    title: "MongoDB Manual: Data Modeling"
    url: [https://www.mongodb.com/docs/manual/data-modeling/]
    verified: 2026-10-09
    covers: [C08-W2]
    skip: "none; read in full (single page)"
work_units:
  - id: C08-W1
    date: 2026-10-27
    activity: "Learn Redis cache-aside, TTLs, invalidation, stampede protection"
    minutes: 45
  - id: C08-W2
    date: 2026-10-27
    activity: "Learn MongoDB embed-vs-reference modelling and indexes"
    minutes: 45
  - id: C08-W3
    date: 2026-10-27
    activity: "Add cache-aside with invalidation to the C03-W4 API; measure hit rate"
    minutes: 45
hours_calculation: "(45 + 45 + 45) min = 135 min x pace 1.0 = 2.25 h"
practice_ai_mode: "with-ai allowed for C08-W3"
exit_test:
  id: XT-C08
  criteria:
    - "Explain the cache-aside read and write paths and two invalidation strategies, and name one stampede mitigation."
    - "Choose embed or reference for two MongoDB scenarios with a reason each."
    - "C08-W3 reports a measured hit rate and shows a stale read does not survive an update."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C14. LLM product features

```yaml
competency_id: C14
name: LLM product features
category: AI product
importance: BRANCH
companies: [HighLevel, Gather AI, Dscout]
market:
  trajectory: rising
  demand_share: "LLM integration 69 of 264 (26%); agents 57 (22%); retrieval 28 (11%); evals 14 (5%); Segment B LLM 38%, agents 42%"
  evidence: "market-context.md s6: Hiring Lab 37% of US software-posting rebound from AI-titled roles (M2); Octoverse LLM-SDK repositories +178% (M2)"
relevance_decision: cap
relevance_reason: "Capped at D1 in the master; D2 only in the Dscout branch, where shipped LLM features are required."
required_depth: D1
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.36
  weight: 2
  impact: 0.73
  hours_to_close: 4.50
  score: 0.162
  rank: 18
  vital_few: false
coverage:   # most frequently tested first
  - "streaming a model response to a React page"
  - "one tool call against your own API"
  - "structured output validated with zod"
  - "failure and invalid-output fallback"
  - "LLM versus deterministic decision note"
not_covered:
  - "retrieval and vector databases (parked)"
  - "fine-tuning"
  - "agent frameworks (LangChain, LlamaIndex)"
  - "model hosting"
  - "eval frameworks beyond a 10-case script (Dscout branch)"
evidence:
  - "master-competency-map.md C14"
  - "requirements/dscout.md S1"
resources:
  - role: primary
    title: "AI SDK docs (+ Gemini API free tier or Ollama"
    url: [https://ai-sdk.dev/docs/introduction, https://ai.google.dev/gemini-api/docs/pricing, https://ollama.com/)]
    verified: 2026-10-09
    covers: [C14-W1, C14-W2]
    skip: "streaming, tool calling and structured output pages only"
work_units:
  - id: C14-W1
    date: 2026-10-25
    activity: "Learn LLM API basics: streaming, tool calling, structured output with schema validation (AI SDK; Gemini free tier or local Ollama)"
    minutes: 60
  - id: C14-W2
    date: 2026-10-25
    activity: "Build a React page that streams an LLM answer, makes one tool call against your API, validates output with zod, handles failure"
    minutes: 180
  - id: C14-W3
    date: 2026-10-25
    activity: "Write a half-page note: where this feature should be LLM vs deterministic, and how you would evaluate it"
    minutes: 30
hours_calculation: "(60 + 180 + 30) min = 270 min x pace 1.0 = 4.50 h"
practice_ai_mode: "with-ai allowed"
exit_test:
  id: XT-C14
  criteria:
    - "The C14-W2 page streams an answer, makes one tool call, validates output with zod, and shows a fallback when the model fails or returns invalid output."
    - "The half-page note decides LLM versus deterministic for at least 2 parts of the feature with reasons, and names one evaluation metric."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C05. Data structures and algorithms (easy-medium, live)

```yaml
competency_id: C05
name: Data structures and algorithms (easy-medium, live)
category: problem solving
importance: BRANCH, gatekeeper (Drivetrain round 1; Hyperproof take-home)
companies: [Hyperproof, HighLevel, Drivetrain, Gather AI, Metabase]
market:
  trajectory: shifting
  demand_share: "not measured from postings"
  evidence: "market-context.md s5-s6: Canva replaced its fundamentals screen (first-party); large companies harden algorithm rounds (M3)"
relevance_decision: keep
relevance_reason: "Drivetrain rounds are algorithm-led (corroborated); gatekeeper stages at Drivetrain and Hyperproof. Shifting trend does not override a current test."
required_depth: D2
assessment:
  measured_depth: D1 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.73
  weight: 3
  impact: 2.18
  hours_to_close: 16.67
  score: 0.131
  rank: 19
  vital_few: true
coverage:   # most frequently tested first
  - "arrays and hash maps"
  - "two pointers and sliding window"
  - "stacks including monotonic stacks (Asteroid Collision, Min Stack: Drivetrain-reported)"
  - "binary search"
  - "recursion and backtracking"
  - "BFS/DFS on grids and trees"
  - "1-D and 0/1-knapsack dynamic programming (Drivetrain-reported)"
  - "intervals, heaps, nested-object diff (Gather AI-reported)"
not_covered:
  - "LeetCode Hard problems"
  - "advanced graphs (Dijkstra, union-find, topological sort)"
  - "tries, segment trees, Fenwick trees"
  - "bit manipulation"
  - "competitive-programming speed"
evidence:
  - "master-competency-map.md C05"
  - "requirements/drivetrain.md D12, D13"
  - "requirements/metabase.md S15, S16"
  - "requirements/gather-ai.md G12"
resources:
  - role: primary
    title: "NeetCode roadmap (free video per problem) ; LeetCode problems"
    url: [https://neetcode.io/roadmap]
    verified: 2026-10-09
    covers: [C05-P1, C05-P2, C05-P3, C05-P4, C05-P5, C05-P6, C05-P7, C05-P8]
    skip: "skip the editorial and discussion tabs until after your attempt; NeetCode videos only for a problem you failed after 25 minutes"
work_units:
  - id: C05-P1
    date: 2026-10-11
    activity: "Pattern 1, arrays and hash maps (20 min) + Two Sum (1), Group Anagrams (49), Top K Frequent Elements (347), narrated, no AI"
    minutes: 125
  - id: C05-P2
    date: 2026-10-12
    activity: "Pattern 2, two pointers and sliding window + 3Sum (15), Longest Substring Without Repeating Characters (3), Container With Most Water (11)"
    minutes: 125
  - id: C05-P3
    date: 2026-10-13
    activity: "Pattern 3, stacks incl. monotonic + Min Stack (155), Asteroid Collision (735), Daily Temperatures (739)"
    minutes: 125
  - id: C05-P4
    date: 2026-10-14
    activity: "Pattern 4, binary search + Search a 2D Matrix (74), Find Minimum in Rotated Sorted Array (153), Koko Eating Bananas (875)"
    minutes: 125
  - id: C05-P5
    date: 2026-10-15
    activity: "Pattern 5, recursion and backtracking + Subsets (78), Permutations (46), Combination Sum (39)"
    minutes: 125
  - id: C05-P6
    date: 2026-10-17
    activity: "Pattern 6, BFS/DFS on grids and trees + Number of Islands (200), Binary Tree Level Order Traversal (102), Rotting Oranges (994)"
    minutes: 125
  - id: C05-P7
    date: 2026-10-19
    activity: "Pattern 7, 1-D and 0/1-knapsack DP + Climbing Stairs (70), House Robber (198), Partition Equal Subset Sum (416)"
    minutes: 125
  - id: C05-P8
    date: 2026-10-24
    activity: "Pattern 8, intervals, heaps, nested-object work + Merge Intervals (56), Kth Largest Element (215), custom JSON diff of two nested objects"
    minutes: 125
hours_calculation: "(125 + 125 + 125 + 125 + 125 + 125 + 125 + 125) min = 1000 min x pace 1.0 = 16.67 h"
practice_ai_mode: "without-ai (no target has stated AI is allowed in algorithm rounds)"
exit_test:
  id: XT-C05
  criteria:
    - "Mock 4: two unseen mediums in 45 minutes, narrated, no AI. Pass: both solved, or one solved and the other with a correct brute force in code plus the optimal approach and its complexity stated."
    - "You ask clarifying questions, state complexity for each solution, and test your own code with at least 2 edge cases."
    - "Each pattern block ends with its last problem solved unaided in 25 minutes or less; a miss reopens only that pattern."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C19-HL. Vue 3 and Pinia (HighLevel branch)

```yaml
competency_id: C19-HL
name: Vue 3 and Pinia (HighLevel branch)
category: frontend
importance: BRANCH
companies: [HighLevel]
market:
  trajectory: insufficient-data
  demand_share: "Vue 22 of 264 (8%)"
  evidence: "skill-demand.csv"
relevance_decision: cap
relevance_reason: "HighLevel frontend is "primarily Vue 3"; React is accepted at SDE II, so capped at D1."
required_depth: D1
assessment:
  measured_depth: D0 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.18
  weight: 2
  impact: 0.36
  hours_to_close: 3.50
  score: 0.104
  rank: 20
  vital_few: false
coverage:   # most frequently tested first
  - "Composition API: ref, reactive, computed, watch"
  - "Pinia stores"
  - "mapping each to its React equivalent"
not_covered:
  - "Nuxt"
  - "Options API"
  - "Vue internals and reactivity implementation"
  - "module federation"
evidence:
  - "requirements/highlevel.md S1, S6"
resources:
  - role: primary
    title: "Vue.js guide: Essentials"
    url: [https://vuejs.org/guide/essentials/application.html]
    verified: 2026-10-09
    covers: [C19-HL-W1]
    skip: "Essentials section only"
  - role: supplement
    title: "Pinia: Defining a Store"
    url: [https://pinia.vuejs.org/core-concepts/]
    verified: 2026-10-09
    covers: [C19-HL-W2]
    skip: "none; read in full (single page)"
work_units:
  - id: C19-HL-W1
    date: 2026-10-26
    activity: "Learn Vue 3 essentials, Composition API, Pinia stores"
    minutes: 120
  - id: C19-HL-W2
    date: 2026-10-26
    activity: "Port the C02-W4 autocomplete to Vue 3 + Pinia"
    minutes: 90
hours_calculation: "(120 + 90) min = 210 min x pace 1.0 = 3.50 h"
practice_ai_mode: "with-ai allowed"
exit_test:
  id: XT-C19-HL
  criteria:
    - "The ported autocomplete works in Vue 3 with a Pinia store."
    - "Explain ref versus reactive, computed versus watch, and store versus component state, each mapped to React."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### C14-DS. LLM features to interview depth (Dscout branch)

```yaml
competency_id: C14-DS
name: LLM features to interview depth (Dscout branch)
category: AI product
importance: BRANCH
companies: [Dscout]
market:
  trajectory: rising
  demand_share: "see C14"
  evidence: "see C14"
relevance_decision: keep
relevance_reason: "Dscout requires "built features on LLM APIs or agents" and asks about LLM versus deterministic logic."
required_depth: D2
assessment:
  measured_depth: D1 after C14 (prior)
  confidence: low
  evidence: ["prior from candidate-profile.md; no item observed"]
  gap: 1
leverage:
  reach: 0.09
  weight: 2
  impact: 0.18
  hours_to_close: 2.00
  score: 0.091
  rank: 21
  vital_few: false
coverage:   # most frequently tested first
  - "UX for non-deterministic output: retry, edit, confidence cues"
  - "a 10-case evaluation script with a pass rate"
  - "answering LLM-versus-deterministic and push-back questions aloud"
not_covered:
  - "LLM-as-judge pipelines"
  - "Elixir/Phoenix"
  - "GraphQL (Apollo) depth"
evidence:
  - "requirements/dscout.md S1, S6, S7, S8"
resources:
  - role: primary
    title: "AI SDK docs (+ Gemini API free tier or Ollama"
    url: [https://ai-sdk.dev/docs/introduction, https://ai.google.dev/gemini-api/docs/pricing, https://ollama.com/)]
    verified: 2026-10-09
    covers: [C14-DS-W1]
    skip: "streaming, tool calling and structured output pages only"
work_units:
  - id: C14-DS-W1
    date: 2026-10-27
    activity: "Dscout branch: add non-deterministic-output UX (retry, edit, confidence cues) and a 10-case eval script to the C14-W2 feature"
    minutes: 120
hours_calculation: "(120) min = 120 min x pace 1.0 = 2.00 h"
practice_ai_mode: "with-ai allowed"
exit_test:
  id: XT-C14-DS
  criteria:
    - "The 10-case eval script runs and reports a pass rate."
    - "The UI shows retry, edit and confidence states."
    - "Answer three Dscout-style questions aloud in 15 minutes (LLM versus deterministic, handling non-determinism, a push-back story), each with a concrete example."
  pass_threshold: all criteria
stop_rule: "Pass the exit test at target depth, then stop. A failed criterion reopens only its subskill; retest after the reopened unit. Curiosity beyond the coverage list goes to rabbit-hole-parking-lot.md."
```

### Maintenance nodes (C11, C12, C17)

**C11. Cloud, containers and deployment** (SUPPORTING; target D1; prior D1 (prior); trajectory insufficient-data; demand AWS 30%, GCP 17%, Azure 10%, Docker 30%, Kubernetes 27% of 264). Exit test XT-C11, taken cold:
- Write a multi-stage Dockerfile for the C03 API in 10 minutes.
- Explain Pod, Deployment, Service, ConfigMap and Secret in one sentence each.
- Describe a CI pipeline (lint, test, build, deploy) in GitHub Actions terms.
NOT COVERED: Kubernetes operators, Helm chart authoring; Terraform; cloud certifications; Azure-specific services (Gather AI, Hyperproof use Azure; awareness only).

**C12. Security fundamentals** (SUPPORTING; target D1; prior D1 (prior); trajectory insufficient-data; demand 119 of 264 (45%, broad match)). Exit test XT-C12, taken cold:
- Explain 5 categories of the OWASP Top 10:2025 most relevant to web APIs, with one mitigation each.
- Find the planted insecure direct object reference in a code snippet and fix it with an authorization check.
- Explain password hashing versus encryption and where an RBAC check belongs in a request path.
NOT COVERED: penetration testing; cryptographic algorithm internals; compliance frameworks (C18-HP covers awareness).

**C17. Product sense and ownership** (SUPPORTING (BRANCH at Dscout); target D1; prior D1 (prior); trajectory insufficient-data; demand 193 of 264 (73%, broad match); Segment B 88%). Exit test XT-C17, taken cold:
- In 10 minutes, scope an ambiguous feature: users, problem, smallest useful version, 2 deliberate exclusions, one success metric. Pass 2 of 3 consecutive attempts.
NOT COVERED: product-management frameworks; user-research methods; metrics design beyond one success metric.

## 9. Practice tasks and story-bank practice

Each practice task mirrors a target company's documented format. No target published an official interview AI policy, so the AI mode follows the best available evidence and you should ask each recruiter.

| Task | Units | Format mirrored | AI mode |
|---|---|---|---|
| 4 timed API builds (60 min + 20 review) | C03-W1, W3, W4, W5 | HighLevel build-an-API round (corroborated); Railway and Infisical take-homes | with AI, narrated |
| 8 algorithm pattern blocks, 24 problems | C05-P1 to P8 | Drivetrain live rounds; Metabase screen; Hyperproof take-home | without AI, narrated |
| 4 recorded mocks | C15-W6a to W6d | Drivetrain coding; HighLevel 2-hour design plus past experience | without AI |
| 6 designs aloud plus 2 low-level designs | C06-W2 to W7, W9 | HighLevel contacts service; Drivetrain booking app; Hyperproof risk register; Infisical secret sharing | without AI |
| 3 timeboxed bug fixes in unfamiliar repositories | C10-W2 to W4 | Automattic code test; Infisical work day | AI allowed in fixes 1-2; not in the exit test |
| 3 AI-diff reviews with planted defects | C13-W3 | HighLevel "slop-free" review expectation; Canva-style AI-output review | with AI to generate, without AI to review |
| 3 React machine-coding drills (45 min) | C02-W4 | Drivetrain and Metabase React rounds | without AI |
| Written: 2 Hyperproof essays, PR descriptions, 1 design doc, Automattic answers | C16-W2, W3, W4, C16-AU-W1 | Hyperproof application; Automattic application; take-home write-ups | your own words |

**Story bank.** C15-W4 (Day 2) turns your CRM and SaaS products into deep-dive scripts: an architecture sketch, 5 decisions with the alternatives you rejected, one failure, and numbers (users, records, latency, team size). Your profile leaves scale, outcome and role unspecified, so this unit is where you supply them; HighLevel's 30-minute past-work call and every loop's project deep-dive test exactly this. C15-W3 (Day 8) adds 4 more STAR stories (conflict, failure, ownership beyond scope, learning fast); C15-W5 (Day 11) rehearses all 6 aloud, recorded, cut to under 3 minutes; Mock 3 (Day 16) tests them under follow-up.

## 10. Resource map

One primary resource per competency; supplements only where a unit needs them. All free.

| Resource | Nodes and units | Verified |
|---|---|---|
| Tech Interview Handbook: Coding interview techniques https://www.techinterviewhandbook.org/coding-interview-techniques/ | C15-W1 | 2026-10-09 |
| LeetCode problem pages (free; problem IDs in activity) https://leetcode.com/problems/ | C15-W2, C15-W6a, C15-W6d | 2026-10-09 (GraphQL check; site blocks scripts) |
| Design Docs at Google https://www.industrialempathy.com/posts/design-docs-at-google/ | C16-W1, C16-W4, C16-W3 | 2026-10-09 |
| Hyperproof posting (essay questions) https://hyperproof.io/job-listings/?gh_jid=4708360005 | C16-W2 | 2026-10-09 |
| Hyperproof: Risk register guide https://hyperproof.io/resource/risk-register-key-benefits/ + Inherent vs residual risk https://hyperproof.io/resource/inherent-risk-vs-residual-risk/ | C18-HP-W1 | 2026-10-09 |
| Drivetrain FP&A product page https://www.drivetrain.ai/solutions/financial-planning-analysis-software | C18-DT-W1 | 2026-10-09 |
| NeetCode roadmap (free video per problem) https://neetcode.io/roadmap + LeetCode problems | C05-P1, C05-P2, C05-P3, C05-P4, C05-P5, C05-P6, C05-P7, C05-P8 | 2026-10-09 |
| Tech Interview Handbook: Behavioral interviews https://www.techinterviewhandbook.org/behavioral-interview/ | C15-W4, C15-W3, C15-W5, C15-W6c | 2026-10-09 |
| javascript.info: Promises, async/await https://javascript.info/async and Event loop https://javascript.info/event-loop | C01-W2, C01-W3 | 2026-10-09 |
| TypeScript Handbook: Narrowing, Generics, Utility Types https://www.typescriptlang.org/docs/handbook/2/narrowing.html | C01-W4 | 2026-10-09 |
| Zalando RESTful API Guidelines https://opensource.zalando.com/restful-api-guidelines/ + Stripe idempotency https://stripe.com/blog/idempotency | C03-W2, C03-W3, C03-W4 | 2026-10-09 |
| Claude Code best practices https://code.claude.com/docs/en/best-practices | C13-W1, C13-W3 | 2026-10-09 |
| AGENTS.md format https://agents.md/ | C13-W2 | 2026-10-09 |
| Vitest guide https://vitest.dev/guide/ + Testing Trophy https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications | C09-W1, C09-W2 | 2026-10-09 |
| Use The Index, Luke https://use-the-index-luke.com/ | C04-W2 | 2026-10-09 |
| PostgreSQL 18 docs: Using EXPLAIN, Transaction Isolation, Explicit Locking https://www.postgresql.org/docs/current/using-explain.html | C04-W3, C04-W5 | 2026-10-09 |
| AWS: Timeouts, retries and backoff with jitter https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter + Transactional outbox https://microservices.io/patterns/data/transactional-outbox.html | C07-W1 | 2026-10-09 |
| BullMQ docs https://docs.bullmq.io/ | C07-W2 | 2026-10-09 |
| PostgreSQL Exercises https://pgexercises.com/ | C04-W4a, C04-W4b | 2026-10-09 |
| Hello Interview: System Design Delivery Framework https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery | C06-W1, C06-W2, C06-W4, C06-W5, C15-W6b | 2026-10-09 |
| Node.js: Debugging https://nodejs.org/learn/getting-started/debugging + Chrome DevTools Performance https://developer.chrome.com/docs/devtools/performance | C10-W1 | 2026-10-09 |
| Hello Interview: Design Ticketmaster https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster | C06-W3 | 2026-10-09 |
| react.dev: You Might Not Need an Effect; Preserving and Resetting State; memo https://react.dev/learn/you-might-not-need-an-effect | C02-W2, C02-W4 | 2026-10-09 |
| TanStack Virtual docs https://tanstack.com/virtual/latest/docs/introduction | C02-W3 | 2026-10-09 |
| Automattic: Work with us (hiring process) https://automattic.com/work-with-us/ + WordPress Plugin Handbook https://developer.wordpress.org/plugins/ | C16-AU-W1 | 2026-10-09 |
| Playwright docs https://playwright.dev/docs/intro | C09-W3 | 2026-10-09 |
| Hello Interview: Design News Feed https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed | C06-W6 | 2026-10-09 |
| Hello Interview: Distributed Rate Limiter https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter | C06-W7 | 2026-10-09 |
| AI SDK docs https://ai-sdk.dev/docs/introduction (+ Gemini API free tier https://ai.google.dev/gemini-api/docs/pricing or Ollama https://ollama.com/) | C14-W1, C14-W2, C14-DS-W1 | 2026-10-09 |
| Vue.js guide: Essentials https://vuejs.org/guide/essentials/application.html | C19-HL-W1 | 2026-10-09 |
| Pinia: Defining a Store https://pinia.vuejs.org/core-concepts/ | C19-HL-W2 | 2026-10-09 |
| Redux Essentials https://redux.js.org/tutorials/essentials/part-1-overview-concepts | C02-MB-W1 | 2026-10-09 |
| Docker Get started https://docs.docker.com/get-started/ + Kubernetes basics https://kubernetes.io/docs/tutorials/kubernetes-basics/ | C11-M1 | 2026-10-09 |
| Redis: Cache-aside pattern https://redis.io/tutorials/howtos/solutions/microservices/caching/ | C08-W1, C08-W3 | 2026-10-09 |
| MongoDB Manual: Data Modeling https://www.mongodb.com/docs/manual/data-modeling/ | C08-W2 | 2026-10-09 |
| Infisical docs https://infisical.com/docs/documentation/getting-started/introduction | C18-IN-W1 | 2026-10-09 |
| OWASP Top 10:2025 https://top10.owasp.org/ | C12-M1 | 2026-10-09 |

## 11. Company branches (summary)

Full deltas in `company-branches.md`. Branch hours are already inside the schedule.

| Company | Branch-only units | Branch hours | Master units tailored to it |
|---|---|---|---|
| Hyperproof | C16-W2, C18-HP-W1 | 2.0 | C06-W4 |
| HighLevel | C19-HL-W1, C19-HL-W2 | 3.5 | C03-W1 to W5, C06-W2, C06-W9, C15-W4, C15-W6c |
| Drivetrain | C18-DT-W1 | 0.5 | C05-P3, C05-P7, C06-W3, C02-W3, C15-W6a, C15-W6d |
| Gather AI | none | 0.0 | C05-P8 (JSON diff), C07, C04 |
| Dscout | C14-DS-W1 | 2.0 | C14-W1 to W3, C13 |
| Infisical | C18-IN-W1 | 1.0 | C06-W5, C07-W2, C10 |
| Metabase | C02-MB-W1 | 1.0 | C02, C05 |
| Automattic | C16-AU-W1 | 1.5 | C10, C16 |

**Eligibility emails (Day 1, outside study hours).** Ask Infisical, Metabase and Automattic recruiters in writing whether the role can be done as an India-based employee, through an employer of record, or as a contractor. If there is no written yes by the day a branch unit is scheduled (C18-IN Day 18, C02-MB Day 17, C16-AU Day 12), skip the unit and return its minutes to the buffer.

## 12. Progress, recalibration and cuts

**States per competency:** not_started, learning, practicing, assessment_due, complete, maintenance, reopened, deferred. Update the `status` column in `study-plan.csv`.

**Test-out rule.** C01-W1, C02-W1, C04-W1 (Day 1) and C03-W1 (Day 2) are the exit tests taken cold. Pass: mark complete, skip that competency's learning units, and use the freed minutes for the next-ranked gap or the buffer. Fail: the failed criteria decide which learning units run; units covering only passed criteria are skipped.

**Recalibration after Day 3.** observed_pace = actual minutes / estimated minutes over Days 1-3 (1,030 estimated minutes). Replace the 1.0 pace, recompute planned hours, keep this version visible for comparison, and apply the cut list if needed:

| Step | Cut (bottom of ranking first, in the skill's order) | Gross hours saved | Remaining gross hours | Fits 140 h up to pace |
|---|---|---|---|---|
| 1 | `declining` items not tested by a target | 0.00 | 101.90 | 1.145 |
| 2 | OPTIONAL items (none scheduled; C19 variants already excluded) | 0.00 | 101.90 | 1.145 |
| 3 | SUPPORTING, lowest leverage first: C08 (rank 17) | 2.25 | 99.65 | 1.171 |
| 4a | BRANCH for stretch companies: C14-DS (Dscout) | 2.00 | 97.65 | 1.195 |
| 4b | BRANCH for stretch companies: C02-MB (Metabase, eligibility unverified) | 1.00 | 96.65 | 1.207 |
| 4c | BRANCH for stretch companies: C18-IN (Infisical, eligibility conflicting) | 1.00 | 95.65 | 1.220 |
| 5a | Lower depth outside the vital few: C19-HL to D0 (drop C19-HL-W2) | 1.50 | 94.15 | 1.239 |
| 5b | Lower depth outside the vital few: C14 to D0 (drop C14-W2 build) | 3.00 | 91.15 | 1.280 |

After all cuts, 91.15 gross hours remain: the vital few (85.15 h), maintenance (2.50 h) and the D0 remnants of C19-HL and C14 (3.50 h). Dropping the remnants too leaves 87.65 h, which fits 140 hours up to a pace of 1.331. Above that, the vital few alone exceed capacity and the choice is yours: extend the interview-ready date, add hours per day, or drop the stretch-company units inside the vital few (C16-AU-W1, C05-P8 and C06-W5; 4.9 gross hours).

## 13. Deferred topics

Deferred means in scope but not scheduled before 2026-10-29; each re-enters only through its trigger.

| Topic | Why deferred | Trigger to schedule it |
|---|---|---|
| Charts and data-visualisation components (Drivetrain, Metabase postings) | Named in postings; no report shows them tested in an interview stage | A Drivetrain or Metabase recruiter describes a frontend machine-coding round |
| CSS architecture and design systems (Metabase "a necessity") | Metabase eligibility unverified | Metabase confirms India eligibility in writing |
| GCP Pub/Sub and Cloud Tasks specifics (HighLevel) | C07 teaches the semantics on BullMQ; vocabulary mapping is in `company-branches.md` | HighLevel design round is scheduled |
| Elasticsearch basics (HighLevel) | Only "an inverted index serves segment search" is said in C06-W2 | HighLevel interviewer asks about search internals in an earlier stage |
| GraphQL (Dscout, Railway) | D0 awareness only; no stage evidence | Dscout or Railway exercise brief mentions GraphQL |
| Infisical monorepo practice run | Covered generically by C10 | Infisical invites you to a take-home or work day |

## 14. Re-verification checklist

Run before 2026-10-29 or before your first scheduled interview, whichever is earlier. A changed fact reopens only the affected nodes.

- [ ] Each target posting is still open and unchanged: Hyperproof (gh_jid 4708360005), HighLevel Contacts and CRM (Lever), Drivetrain (Lever), Gather AI (5243582007), Dscout (4370266009), Infisical (Ashby), Metabase (Lever), Automattic (5862239). Affects: the company's branch and its reach weight.
- [ ] Each recruiter has told you the interview stages and the AI policy for coding rounds. Affects: `practice_ai_mode` of C03, C05, C13.
- [ ] India eligibility answered in writing by Infisical, Metabase and Automattic. Affects: C18-IN, C02-MB, C16-AU and their reach weights.
- [ ] Hyperproof screening question ("4+ years React + Java Spring Boot") unchanged. Affects: Hyperproof fit.
- [ ] The `rising` verdicts for AI-assisted engineering and LLM product work still hold (re-run `raw/extract_skills.py` on a fresh corpus 4-8 weeks after 2026-10-09). Affects: C13 and C14 depth.
- [ ] The `shifting` verdict for algorithms has not become "removed" at Drivetrain. Affects: C05 hours.
- [ ] Observed pace recorded after Day 3 and the cut list applied if above 1.145.
