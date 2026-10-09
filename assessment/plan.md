---
generated: 2026-10-09
evidence_window: 2024-05 (oldest candidate report used) to 2026-10-09 (posting corpus)
reverify_by: 2026-10-29 (the profile's interview-ready deadline; earlier than generated + 30 days)
---

# Assessment plan

Purpose: measure where you stand on each competency your target companies test, so the 20-day plan spends its hours only on real gaps. Self-ratings in `candidate-profile.md` are all "unspecified", so every prior below starts at the level a 3-year full-stack engineer typically holds, and the probes move up or down from there.

## Budget

- Planned prep: about 140 hours (7 hours per day, 2026-10-09 to 2026-10-29).
- Assessment budget rule: about 5% of prep hours, capped at 4 hours. 5% of 140 h = 7 h, so the cap applies: **3 sessions, about 3 h 50 min in total, none longer than 90 minutes.**
- No GitHub, portfolio or resume was supplied, so the artifact review is skipped. If you share a repository you wrote most of, it adds evidence at no session cost.

## Target companies and weights used for scoring later

| Company | Fit | Weight in reach calculation |
|---|---|---|
| Hyperproof, HighLevel, Drivetrain | realistic | 1.0 each |
| Gather AI, Dscout, Infisical, Metabase, Automattic | stretch | 0.5 each |
| Railway (reach list) | stretch, senior title | noted, not weighted |

## Competencies, target depths and how each is measured

Depth levels: D0 awareness, D1 working knowledge, D2 interview-ready, D3 production depth. Target = the minimum depth the evidence supports; where uncertain, the lower depth.

| ID | Competency | Importance | Target | Prior | Items (session) | Minutes |
|---|---|---|---|---|---|---|
| C01 | TypeScript and JavaScript fluency | CORE | D2 | D1 | A1 predict-output and bug-spot set (S1); observed again in A5, A6 | 12 |
| C02 | React frontend engineering | CORE | D2 | D1 | A7 React rendering and large-list bug fix (S2) | 20 |
| C03 | Node.js backend and API design | CORE | D2 | D1 | A6 timed API build, AI allowed (S2) | 40 |
| C04 | Relational data modelling and PostgreSQL | CORE | D2 | D1 | A2 schema plus query plus index item (S1); achievement probes | 18 |
| C05 | Data structures and algorithms, easy to medium | BRANCH, gatekeeper (Drivetrain round 1, Hyperproof take-home) | D2 | D1 | A5 live coding with think-aloud, no AI (S2) | 25 |
| C06 | System design and architecture defense | CORE | D2 | D1 | A8 design micro-prompt with perturbations (S3); achievement probes | 30 |
| C07 | Asynchronous processing and reliability | BRANCH | D2 (idempotency, retries, at-least-once only) | D0 | inside A8 perturbations; A3 quick check (S1) | in A8 + 3 |
| C08 | Caching and NoSQL stores | SUPPORTING | D1 | D0 | A3 quick check (S1) | 3 |
| C09 | Testing and code quality | CORE | D2 | D1 | tests written in A6; A9 diff review (S3) | in A6, A9 |
| C10 | Debugging existing codebases | BRANCH | D2 | D1 | A9 debug and review unfamiliar code (S3) | 20 |
| C11 | Cloud, containers and deployment | SUPPORTING | D1 | D1 | A3 quick check (S1) | 3 |
| C12 | Security fundamentals | SUPPORTING | D1 | D1 | A3 quick check (S1); planted defect in A9 | 3 |
| C13 | AI-assisted engineering (direct and verify) | BRANCH | D2 | D1 | A6 with AI allowed; A9 includes an AI-written diff with planted defects | in A6, A9 |
| C14 | LLM product features | BRANCH (required at Dscout) | D1 (master), D2 Dscout branch | D0 | A3 quick check plus one design question (S3) | 8 |
| C15 | Explaining reasoning aloud | CORE format skill, every live stage | D2 | D0 (stated weak area) | scored in A4, A5, A6, A8 | in others |
| C16 | Written asynchronous communication | CORE (Hyperproof essay at application, Automattic) | D2 | D1 | A10 written decision note (S3) | 15 |
| C17 | Product sense and ownership | SUPPORTING (BRANCH at Dscout) | D1 | D1 | achievement deep-dive (S1); A8 clarifying questions | in A4 |
| C18 | Domain knowledge (CRM, GRC, FP&A, secrets) | BRANCH per company | D0 to D1 | D0 to D1 | not assessed; CRM overlap measured in A4 | 0 |
| C19 | Framework variants (Vue 3, Python, Java, PHP, Elixir) | OPTIONAL to BRANCH | D0 (Vue 3 D1 for HighLevel) | D0 | not assessed; scheduled as D0/D1 learning only | 0 |

Not assessed: C18 and C19. Both are awareness-level targets where a short study block costs less than measuring.

## Session split

Each item's pass criteria are written before you see the item and stay in `assessment/<item-id>/rubric.md` until scoring.

**Session 1: about 75 minutes. Conversation in chat; no coding environment needed.**
- Briefing (5 min).
- A4 achievement deep-dive: CRM system and SaaS product, one question at a time (35 min). Measures ownership, trade-off reasoning, technical depth floor, and how ready each story is for behavioral rounds.
- A1 TypeScript/JavaScript predict-output and bug-spot set (12 min).
- A2 PostgreSQL schema, query and index item (18 min).
- A3 quick checks: queues, caching, cloud, security, LLM features; multiple choice, each followed by "why?" (10 min, about 6 questions).

**Session 2: about 90 minutes. Your editor and terminal (Node 24 and TypeScript 5.9 are installed on this machine).**
- A5 live coding with think-aloud, no AI tools: one easy-to-medium stack or hash-map problem of the kind Drivetrain asks (25 min). You type your reasoning as you work.
- A6 timed API build, AI tools allowed, modelled on HighLevel's build round: small contacts-with-tags REST service with validation and tests (40 min). Afterwards you explain what the AI produced and how you verified it.
- A7 React item: fix the rendering and performance bugs in a small list component (20 min).

**Session 3: about 75 minutes. Mixed.**
- A8 system design micro-prompt at mid-level product scope, then three perturbations: 10x load, a dependency fails, a requirement changes (30 min).
- A9 unfamiliar-code debugging plus review of an AI-generated diff containing planted defects (20 min).
- A10 written async note explaining a technical decision (15 min).
- Results walkthrough (10 min), then re-tests for any disputed result.

Total: about 240 minutes (4 h 0 min) including the walkthrough.

## Rules during the assessment

- The purpose is to find gaps, so the plan can skip what you already know.
- No AI tools, notes or search unless an item says so (only A6 allows AI).
- "I don't know" is a useful answer. A lucky guess hides a gap the plan will then miss.
- Feedback comes at the end of each section, not after each item.
- Times are taken from message timestamps; you may also note your own start and end times.
