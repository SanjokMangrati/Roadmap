---
generated: 2026-10-09
evidence_window: 2024-05 (oldest candidate report used) to 2026-10-09 (posting corpus and first-party postings)
reverify_by: 2026-10-29, or before your first scheduled interview if that is earlier
---

> **UNMEASURED.** Readiness figures below use priors from your profile, not observed results (see `candidate-assessment.md`). They change as exit tests pass.

# Company branches

Each branch is a delta from `master-curriculum.md`, not a second curriculum. Every branch hour listed here is already inside the 19-day schedule in `study-plan.csv`; no branch adds time beyond it.

Order: realistic fit first, then stretch. Within each company, branch tasks are ranked by the leverage score from master section 4.

| Company | Fit | Readiness by prior | Branch-only hours | Gate before branch work |
|---|---|---|---|---|
| Hyperproof | realistic | 2 of 12 (17%) | 2.0 | none |
| HighLevel | realistic | 3 of 16 (19%) | 3.5 | none |
| Drivetrain | realistic | 0 of 6 (0%) | 0.5 | none |
| Gather AI | stretch | 2 of 14 (14%) | 0.0 | knock-out questions on Python and Kubernetes years |
| Dscout | stretch | 1 of 8 (13%) | 2.0 | none (India confirmed; entity unverified) |
| Infisical | stretch | 3 of 15 (20%) | 1.0 | written confirmation of India eligibility |
| Metabase | stretch | 1 of 9 (11%) | 1.0 | written confirmation of India eligibility |
| Automattic | stretch | 0 of 7 (0%) | 1.5 | written confirmation of India eligibility |

---

## 1. Hyperproof: Software Engineer, Risk Management

**Posting:** https://hyperproof.io/job-listings/?gh_jid=4708360005 (updated 2026-09-24; HTTP 200 on 2026-10-09). "This role is open to candidates based in India." Published pay ₹21.37-30 lakh per year.

**Fit verdict: realistic, with one known filter.** A screening question asks for "4+ years React and Java (Spring Boot)"; with 3 years and Node.js, the honest answer is "No". The posting itself asks 3-5 years and accepts Node.js. The plan does not try to close the Java gap (see "Reduced or skipped").

**Inherited master preparation:** C01, C02, C03, C04, C05, C06, C09, C15 and C16 from the master; C11 and C12 as maintenance.

**Readiness:** 2 of 12 tested competencies at target by prior (C11, C12).

**Stages and AI policy** (from `requirements/hyperproof.md` section 4; order unconfirmed):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Application | Screening questions plus a required essay on testing and reliability; optional essay on async communication | unknown | C16-W2 (Day 1) |
| Take-home | Coderbyte platform per an older posting; easy-to-medium coding plus testing | unknown; Coderbyte supports proctoring, use not confirmed | C05-P1 to P8, C09 |
| Talent partner chat | 30 minutes | unknown | C15-W3 story bank |
| Three engineering one-to-ones | 3 x 60 minutes, camera on; technical depth, design, testing, hiring manager | unknown | C06-W4, C09-W4, C15-W6b |

**Unique competencies and branch tasks (ranked by leverage):**

1. **C16-W2, Hyperproof essays** (60 min, Day 1, leverage rank 3 via C16). Essays cover unit, integration and end-to-end layers; test data for edge cases; migrations tested against PostgreSQL; idempotency; preventing data-integrity bugs (the posting says integrity "is not optional"). Submit the real application the same day.
2. **C18-HP-W1, GRC domain** (60 min, Day 1, rank 7). Risk register, inherent versus residual risk (likelihood x impact, reduced by control effectiveness), control testing, SOC 2 versus ISO 27001.
3. **Tailored master unit C06-W4** (Day 12): design a risk register with control-test scheduling, audit trail and RBAC aloud.

**Branch hours:** C16-W2 60 min + C18-HP-W1 60 min = 2.0 hours.

**Branch exit criteria:** XT-C16 (essays submitted), XT-C18-HP (5-minute GRC explanation and the risk-register schema with many-to-many risk-control mapping, test schedule and audit history), and the Design 3 recording (C06-W4) meets the XT-C06 criteria.

**Reduced or skipped:** Java Spring Boot and C#/.NET (in duties) are not covered: neither reaches a screened level in 20 days, and the posting accepts Node.js. Azure is awareness only (C11). NIST CSF and FedRAMP control catalogues are parked.

**Ask the recruiter:** stage order, whether the take-home is proctored, and whether AI tools are allowed in it.

**Evidence:** `requirements/hyperproof.md` S1 (posting), S2 (application questions), S3 (AI-role process), S5 (candidate report), S6 (older Coderbyte posting).

---

## 2. HighLevel: SDE II (Fullstack), Contacts or CRM

**Postings:** Contacts https://jobs.lever.co/gohighlevel/254ef24c-ff4b-42c9-8b43-603e55e650a3 and CRM https://jobs.lever.co/gohighlevel/92002249-671d-4d08-96b0-e87c1d6082cb (posted 2026-09-16/17). Lever commitment "Employee India", workplace remote. 13 India-remote SDE II/III postings were live on 2026-10-09.

**Fit verdict: realistic.** Direct CRM overlap with your stated CRM project. The CRM posting requires an "AI-native builder" who codes with agents daily.

**Inherited master preparation:** C01, C03, C04, C05 (easy-medium only), C06, C07, C08, C09, C10, C13, C14, C15; C11 and C17 as maintenance; C18-HL (CRM domain) at target by prior.

**Readiness:** 3 of 16 tested competencies at target by prior (C11, C17, C18 CRM).

**Stages and AI policy** (corroborated candidate reports 2024-2026; no official process page):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Recruiter or HR screen | call | unknown | C15-W3 (90-second background story) |
| Past-work call | about 30 minutes with an engineer; possibly one easy DSA or JavaScript question | unknown | C15-W4, C15-W6c, C01 |
| Build-an-API round (decisive stage) | about 1 hour, live, build a working API and discuss the schema; variants: feed machine coding, low-level design (Snake and Ladders) | **allowed** (anecdotal, two reports: May 2025, June 2026) | C03-W1, W3, W4, W5; C13; C06-W9 |
| High-level design plus past experience | about 2 hours | unknown | C06-W2, C06-W6, C06-W7, C07, C08, C15-W6b |
| HR or culture fit | video | n/a | C15-W3 story bank |

**Unique competencies and branch tasks (ranked by leverage):**

1. **Tailored master units** (no extra hours): C03-W1 contacts-with-tags build (Day 2) and C03-W3 social-feed build (Day 4) mirror the reported build-round prompts; C06-W2 (Day 9) is a HighLevel-scale contacts service (millions of contacts, tags, segment search, bulk import); C06-W9 (Day 14) includes Snake and Ladders low-level design; C15-W6c (Day 16) mirrors the past-experience half of the 2-hour round.
2. **C19-HL-W1 and W2, Vue 3 and Pinia** (210 min, Day 17, leverage rank 20). React is accepted at SDE II, so this stays at D1.

**Vocabulary mapping for the design round** (C07 teaches the semantics on BullMQ; HighLevel names GCP services):

| Concept you practise in C07 | BullMQ (what you build) | GCP name HighLevel uses |
|---|---|---|
| at-least-once delivery, redelivery | job retried after a failure or a stalled lock | Pub/Sub: unacknowledged message redelivered after the ack deadline |
| dead-letter handling | failed jobs kept in the failed set, or moved to a separate queue | Pub/Sub dead-letter topic |
| deduplication | custom job ID | Cloud Tasks: task name deduplication |
| retries with backoff | `attempts` plus `backoff` options | Cloud Tasks retry configuration; Pub/Sub retry policy |

**Branch hours:** C19-HL-W1 120 min + C19-HL-W2 90 min = 3.5 hours.

**Branch exit criteria:** XT-C03 (timed build 4) is the stage-specific gate; XT-C19-HL (Vue 3 port with Pinia, React mapping explained); the CRM deep-dive survives five "why?" follow-ups in Mock 3 (XT-C15).

**Reduced or skipped:** MongoDB and Firestore at D1 only (C08); Elasticsearch at one sentence in C06-W2 (deferred); module federation not covered; heavy DSA not covered, because the reports conflict and the build and design rounds carry more weight (`requirements/highlevel.md` section 8, "Conflicting").

**Ask the recruiter:** whether AI tools are allowed in the build round; whether the 2-hour round is design plus past experience in one session.

**Evidence:** `requirements/highlevel.md` S1, S2 (postings), S6, S9 (stack), S12 (historical official posting), S13, S14, S15, S20 (candidate reports).

---

## 3. Drivetrain: Frontend Engineer (India)

**Posting:** https://jobs.lever.co/drivetrain/cd39cc4e-056e-444c-8c17-9f97e34ddbce. Lever workplace remote, location India.

**Fit verdict: realistic, with a format risk.** The band (1-3 years React plus data structures) fits; the reported rounds are live, narrated algorithm coding, which is your stated weak area. The posting has been reposted since 2024 and may be an evergreen pipeline.

**Inherited master preparation:** C01, C02, C05, C06, C15.

**Readiness:** 0 of 6 tested competencies at target by prior.

**Stages and AI policy** (Glassdoor excerpts only; no first-party process):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Technical round 1 (gatekeeper) | about 60 minutes live DSA on Google Meet: asteroid collision, min/max stack, 2-D matrix, recursion | unknown; plan assumes not allowed | C05-P3 (Asteroid Collision 735, Min Stack 155), C05-P4 (Search a 2D Matrix 74), C05-P5, C15-W6a, C15-W6d |
| Technical round 2 | 0/1 knapsack DP, then low-level and high-level design of a movie or concert booking app | unknown | C05-P7 (Partition Equal Subset Sum 416), C06-W3, C06-W9, C03-W4 |
| Rounds 3, hiring manager, HR | not described | unknown | C15-W3 story bank; C18-DT-W1 |

**Unique competencies and branch tasks (ranked by leverage):**

1. **C18-DT-W1, FP&A vocabulary** (30 min, Day 1, leverage rank 1).
2. **Tailored master units** (no extra hours): C02-W3 (Day 11) builds a 10,000-row spreadsheet-style grid, the posting's stated scope; C06-W3 (Day 10) designs the booking app with seat holds and double-booking prevention; C04-W5 (Day 6) reproduces and fixes a double-booking race; Mocks 1 and 4 use Drivetrain-style problems.

**Branch hours:** 0.5 hours.

**Branch exit criteria:** XT-C05 (Mock 4) is the stage-specific gate; XT-C18-DT; the Design 2 recording (C06-W3) meets XT-C06.

**Reduced or skipped:** charts and data-visualisation components are deferred (named in the posting, not reported in any round); the Java/Spring backend role is out of scope.

**Ask the recruiter:** whether the frontend loop includes a React machine-coding round; whether the role is actively hiring this quarter.

**Evidence:** `requirements/drivetrain.md` D1 (posting), D12, D13 (candidate reports).

---

## 4. Gather AI: SDE II Full Stack, India

**Posting:** https://job-boards.greenhouse.io/gatherai/jobs/5243582007 (updated 2026-09-30). "Remote (India)."

**Fit verdict: stretch, gated by experience questions.** The application form knocks out on years of production Python plus Node, and Kubernetes plus Azure or AWS. Study cannot change years of experience; answer honestly and count any real Python or Kubernetes work.

**Inherited master preparation:** C01, C03, C04, C05, C06, C07, C08, C10, C13, C14, C15, C16; C11 and C12 as maintenance.

**Readiness:** 2 of 14 tested competencies at target by prior (C11, C12).

**Stages and AI policy** (anecdotal, from a different role):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Application | knock-out questions: Python+Node years, Kubernetes+cloud years, PostgreSQL tuning | n/a | C04 (tuning vocabulary for the answer) |
| Coding round | live data task: diff two warehouse-inventory JSON snapshots by location | unknown | C05-P8 (custom JSON diff), C05-P1 (hash maps) |
| System design | requirements, high-level design, APIs, trade-offs | unknown | C06, C07 (idempotent ingestion with retries), C08 |

**Unique competencies and branch tasks:** none beyond tailored master units. C05-P8 (Day 15) ends with a custom nested-object diff; C07 covers the posting's retries and duplicate processing.

**Branch hours:** 0.

**Branch exit criteria:** XT-C05 and XT-C07 cover the reported stages.

**Reduced or skipped:** production Python, Kafka and RabbitMQ internals, Kubernetes on Azure, dbt and Airflow: not covered (parked).

**Evidence:** `requirements/gather-ai.md` G1 (posting), G2 (application form), G12 (candidate report, snippet).

---

## 5. Dscout: Software Engineer, India

**Posting:** https://job-boards.greenhouse.io/dscout/jobs/4370266009 (published 2026-08-21). "Remote - India"; employing entity unverified.

**Fit verdict: stretch.** The posting requires shipped features on LLM APIs or agents; your profile has none. C14 plus C14-DS produces one working LLM feature with an evaluation script to discuss.

**Inherited master preparation:** C01, C02, C03, C04, C13, C14, C15; C17 as maintenance.

**Readiness:** 1 of 8 tested competencies at target by prior (C17).

**Stages and AI policy** (official, generic):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Recruiter screen | 30 minutes; the application asks for compensation before any call | unknown | C15-W3 |
| Team interviews | hiring manager and team; LLM feature probing; product judgment and push-back | unknown | C14-W3 note, C14-DS-W1, C17-M1 |
| Possible practical exercise | 2026 public exercises are repositories with AGENTS.md briefs, ticket breakdowns, trade-off notes | unknown; AGENTS.md suggests agents are expected (inference) | C13-W2 (AGENTS.md), C16-W3 |

**Unique competencies and branch tasks (ranked by leverage):**

1. **C14-DS-W1** (120 min, Day 18, leverage rank 21): add retry, edit and confidence cues to the C14-W2 feature, and a 10-case evaluation script.

**Branch hours:** 2.0 hours.

**Branch exit criteria:** XT-C14-DS (eval script runs with a pass rate; UI states present; three Dscout-style questions answered aloud with concrete examples).

**Reduced or skipped:** Elixir/Phoenix and GraphQL (Apollo) at awareness only; not scheduled.

**Ask the recruiter:** employing entity (direct, employer of record, or contractor) and time-zone overlap.

**Evidence:** `requirements/dscout.md` S1 (posting), S6 (process page), S7, S8 (2026 exercise repositories).

---

## 6. Infisical: Full Stack Engineer

**Posting:** https://jobs.ashbyhq.com/infisical/351240fc-0dd3-48c3-a46e-e8861cae27cd (published 2026-10-02).

**Gate: India eligibility is conflicting.** The text lists India; the structured locations omit it; a required form question asks "Do you live and work in the Americas?". Do not run C18-IN-W1 (Day 18) without a written yes; if none arrives, skip it and return 60 minutes to the buffer.

**Fit verdict: stretch.** "Exceptionally high" bar; GitHub profile required.

**Inherited master preparation:** C01, C02, C03, C04, C06, C07, C08, C09, C10, C15, C16; C11, C12, C17 as maintenance.

**Readiness:** 3 of 15 tested competencies at target by prior (C11, C12, C17).

**Stages and AI policy** (one anecdotal 2025 report):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Application | GitHub URL, three "exceptional ability" bullets, optional Loom | unknown | C16 |
| Founder screens | two calls | unknown | C15-W3 |
| Take-home | build a secret-sharing application | unknown | C06-W5 (Day 13), C03, C09 |
| Take-home review and design extension | defend and extend the take-home | unknown | C06-W5, C15-W6b |
| Work day (in person in San Francisco in the report) | audit-log refactor, frontend bug fix, CLI feature | unknown | C10-W2 to W4 |

**Unique competencies and branch tasks:**

1. **C18-IN-W1** (60 min, Day 18, leverage rank 14): secret lifecycle, envelope encryption, dynamic secrets, PKI and KMS roles.

**Branch hours:** 1.0 hour.

**Branch exit criteria:** XT-C18-IN; Design 4 (C06-W5) meets XT-C06 with envelope encryption and rotation applied.

**Reduced or skipped:** ACME, EST, KMIP, FIPS and SAML/SCIM detail parked; a dedicated run of the Infisical monorepo is deferred until a take-home or work day is offered.

**Evidence:** `requirements/infisical.md` S1, S4 (posting and form), S14 (candidate report).

---

## 7. Metabase: Software Engineer (Frontend)

**Posting:** https://jobs.lever.co/metabase/8f02d3fa-edf4-4433-a6d1-4f9e517ac8f9 (evergreen since 2020).

**Gate: India eligibility is unverified.** "Global Remote" and "work from wherever you want", but India is not named and one aggregator says US only. Do not run C02-MB-W1 (Day 17) without a written yes.

**Fit verdict: stretch.**

**Inherited master preparation:** C01, C02, C05, C06, C09, C10, C15, C16; C17 as maintenance.

**Readiness:** 1 of 9 tested competencies at target by prior (C17).

**Stages and AI policy** (anecdotal):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Application | Metabase discloses AI-assisted screening for inconsistencies | n/a | C16 (your own words) |
| Coding screen | about 30 minutes in your own environment; LeetCode easy/medium reported | unknown | C05, C02-W4 (have a local React + TypeScript scaffold ready) |
| Three panels | React, algorithms, architecture; 3 x 60 minutes | unknown | C02, C05, C06 |
| Take-home | about 3.5 hours reported | unknown | C03, C09, C16-W3 |
| CEO chat | values and product thinking | n/a | C17-M1 |

**Unique competencies and branch tasks:**

1. **C02-MB-W1** (60 min, Day 17, leverage rank 15): Redux Toolkit slices and memoised selectors applied to the C02-W3 grid.

**Branch hours:** 1.0 hour.

**Branch exit criteria:** XT-C02-MB.

**Reduced or skipped:** CSS architecture and design systems (the posting calls them "a necessity") and chart libraries are deferred until eligibility is confirmed; Clojure backend not covered.

**Evidence:** `requirements/metabase.md` S2 (posting), S6 (AI-screening disclosure), S11, S12, S15, S16, S17 (candidate reports).

---

## 8. Automattic: Experienced Software Engineer

**Posting:** https://job-boards.greenhouse.io/automatticcareers/jobs/5862239 (updated 2026-09-21). Pay "$70,000-$170,000 USD… global, regardless of location… paid in local currency".

**Gate: India eligibility is likely but not named** ("engineers worldwide", 83 countries). Do not run C16-AU-W1 (Day 12) without a written yes.

**Fit verdict: stretch.** PHP and experience at scale are asked; the research file is abbreviated (candidate reports and layoffs not researched).

**Inherited master preparation:** C01, C09, C10, C13, C15, C16.

**Readiness:** 0 of 7 tested competencies at target by prior.

**Stages and AI policy** (official process page):

| Stage | Format | AI policy | Master units that rehearse it |
|---|---|---|---|
| Application (gatekeeper) | answers are "a significant part of the hiring process" | unknown | C16-AU-W1 |
| Skills assessment | format not described | unknown | none specific |
| Initial interview | Slack text interview for most roles, or 30-60-minute video | unknown | C16 (written reasoning in real time) |
| Code test or trial | code test on existing code (such as a WordPress plugin) or a trial up to 20 hours | unknown | C10-W2 to W4 |
| Final review | executive interview; CEO approval | n/a | C15-W3 |

**Unique competencies and branch tasks:**

1. **C16-AU-W1** (90 min, Day 12, leverage rank 16, vital few as a gatekeeper): weighted application answers, plus the plugin model (hooks, actions versus filters).

**Branch hours:** 1.5 hours.

**Branch exit criteria:** XT-C16-AU.

**Reduced or skipped:** PHP language study and Gutenberg block development not covered; the text-based interview lowers the weight of C15 here, but C15 is not reduced because the other 7 targets test it live.

**Evidence:** `requirements/automattic.md` S1 (posting), S2 (work-with-us process page, https://automattic.com/work-with-us/, HTTP 200 on 2026-10-09).

---

## Reach list (not weighted, no branch hours)

| Company | Verdict | Covered by master |
|---|---|---|
| Railway, Senior Full-Stack Engineer, Product | stretch (senior title) | Take-home app plus 60-minute code walkthrough: C03, C06, C15. GraphQL API use deferred. |
| Supabase | stretch (no React role open) | none specific |
| LiveKit, Tarteel AI, vidIQ | out of reach (5-6+ years required) | none |
