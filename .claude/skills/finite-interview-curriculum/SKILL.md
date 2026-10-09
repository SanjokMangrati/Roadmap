---
name: finite-interview-curriculum
description: Interview-prep curriculum builder. Runs a measured assessment interview of the candidate, then turns company-interview-research evidence into one personalised, finite, market-grounded study plan that spends hours on the highest-leverage gaps first (80/20), with depth targets, derived time budgets, exit tests, stopping rules, verified resources and company branches. Use when planning interview preparation, assessing where a candidate stands, or building a study schedule for target companies.
---

# Finite Interview Curriculum

## Mission

Measure where the candidate stands, then build one finite plan that closes the gaps between that position and what their target companies test, and that the current market still rewards. Highest-leverage gaps first; what they already know gets maintenance only.

The central optimization:

> maximize interview-relevant, market-relevant competence gained per hour, subject to a hard time budget.

The learner will follow this plan day after day without re-checking it. It must be correct about what matters, honest about what is uncertain, specific to this candidate, and dated so they know when to re-verify.

Every curriculum answers:

1. Where does the candidate measurably stand today?
2. What exactly must be learned to reach the targets, and what evidence says it matters now?
3. Which gaps carry the most interview impact per hour?
4. How deeply, and how much concrete work?
5. What proves a topic is complete, so the learner can stop?

## Principles

### 1. Evidence first

Sources, in order:
- current company role requirements
- current company interview process (including its AI policy)
- market data in `market-context.md` and `skill-demand.csv`
- corroborated recent candidate evidence
- established foundational interview requirements
- only then expert inference, labelled as such

Every non-obvious major item traces to evidence or is marked `baseline` (foundational knowledge every target interview assumes).

### 2. Grounded register

The learner trusts this document with their days, so it is written as a technical plan, not a pep talk.

- Each sentence carries a requirement, a datum, a source, an estimate with its calculation, or an instruction.
- Statements about outcomes stay within what evidence supports: coverage, depth, estimated hours, pass criteria. Offer likelihood and job outcomes are outside the plan's evidence and stay out of it.
- Shortfalls are stated plainly where the learner will see them: capacity below demand, a target role with a thin market, a gap the timeline cannot close.
- Readable over compressed: complete sentences, terms spelled out, outcome first. Chat shorthand, arrow chains and labels coined while building the plan stay out of learner-facing files.

### 3. Measured, not claimed

The plan is built on the candidate's **measured** depth from the assessment interview. Self-ratings and resume claims only seed the assessment. Each topic's study load is sized to its measured gap; a topic already at target depth gets format rehearsal, not study.

### 4. 80/20 leverage

A minority of gaps carries most of the interview impact. Rank gaps by impact per hour, identify the **vital few** that together carry about 80% of the impact, and schedule them first. The same rule applies inside a topic: the most frequently tested subskills come first, and the exit test weights them.

### 5. Market relevance

Every competency carries the `market_trajectory` from research (`rising` / `stable` / `shifting` / `declining` / `insufficient-data`) and its `demand_share`.

- **Interview reality wins.** If a target company's current process tests it, it stays for that company's branch, whatever the trend.
- `declining` items not tested by any target company are cut, or capped at D0, with the evidence cited.
- `shifting` items are taught in their current form (e.g. if coding rounds now allow AI tools, practice both solving with an assistant and verifying its output, matching each company's policy).
- `rising` items enter at the depth target postings and processes evidence, never higher.
- AI-era competencies (AI-assisted development, reviewing generated code, LLM integration, evals) are included at the depth the evidence supports, like any other topic.

### 6. Finite by construction

Every topic is a bounded set of subskills plus an exit test. Write "HTTP caching: cache-control, validation, invalidation; exit test below", never "learn databases deeply", "master distributed systems", or "do lots of LeetCode".

### 7. Depth levels

Exactly four:

- **D0 — Awareness:** know the terminology and when it matters. No implementation.
- **D1 — Working knowledge:** explain it, use it in normal code, recognize common failure modes.
- **D2 — Interview-ready:** solve representative problems, reason about trade-offs, debug mistakes, explain decisions without notes.
- **D3 — Production-depth:** design/debug complex systems; reason about failure modes, performance, security and trade-offs under ambiguity.

D3 requires evidence that a target role or process tests that depth.

### 8. Explicit exclusions

Every major section has a `NOT COVERED` list, so the learner knows what to skip.

### 9. Exit before expansion

A topic expands only after its exit test is failed, and only for the failed subskill.

### 10. Time is derived

Estimate from concrete work units: concepts × minutes + exercises × minutes + assessments + review buffer, multiplied by the candidate's measured pace factor. Use ranges, show the calculation, and call it a planning model, not a fact about the learner.

`(8 concepts × 30 min + 6 exercises × 40 min + 1 assessment × 60 min) × pace 1.3 × 1.2 buffer = 14.0 h`

### 11. Competency, not consumption

Complete means the learner performed the target behavior, not that they read or watched something.

## Inputs

Read from `interview-intelligence/`:
- `candidate-profile.md`: role, level, goals, achievements, deadline, hours/week, constraints, weak areas
- `market-context.md`, `skill-demand.csv`
- `master-competency-map.md`, `company-matrix.csv`, `requirements/*.md`

If `interview-intelligence/` is missing, run `company-interview-research` first. If the user declines that, run its intake (`company-interview-research/references/intake.md`), build from baseline requirements plus whatever evidence the user supplies, and label the curriculum `UNGROUNDED: no company or market evidence` at the top of every output file.

For scheduling, use the profile's deadline and hours/week. If absent, produce a parameterized schedule (hours per week as the variable) rather than inventing a deadline.

## Curriculum construction

### Phase 1 — Coverage matrix

Combine the competency map, company requirements and market data:

| Competency | Required by | Assessment modes | Gatekeeper stage? | Importance | Market trajectory | Demand share (N, date) | Evidence |
|---|---|---|---|---|---|---|---|

A **gatekeeper stage** is an early stage that ends the process on a fail (screens, online assessments).

Importance labels, for triage only:
- **CORE:** required across several targets, or central to the target role
- **BRANCH:** important for one or a subset of target companies
- **SUPPORTING:** improves performance; not a primary requirement
- **OPTIONAL:** low-confidence or low-frequency

CORE competencies stay visible however hard they are.

### Phase 2 — Relevance gate

Apply Principle 5 to every row. Record each removal or depth cap, with its evidence, in `coverage-audit.md`.

**Done when:** every row has a trajectory, a relevance decision (keep / cap / cut) and its evidence.

### Phase 3 — Deduplicate and cluster

Merge equivalent topics into shared master topics; keep company-unique assessments as branch items.

Example: Company A tests unfamiliar-codebase debugging plus security review; Company B tests code review plus production readiness; Company C tests product-minded coding on a take-home. Shared: practical debugging and code review (D2). Branches: A's security review, B's change-management discussion, C's take-home rehearsal.

Distinct skills stay distinct even when merging would shorten the plan.

### Phase 4 — Target depths

Per competency: target depth; required subskills, ordered by how often targets test them; excluded subskills; evidence for the depth. Use the minimum sufficient depth. When uncertain, choose the lower depth and add a validation checkpoint.

### Phase 5 — Assessment interview

Read `references/assessment-interview.md` and run it against the target depths from Phase 4. This is a live, multi-session interview with the candidate; the plan that follows is only as personal as this measurement is precise.

**Done when:** `curriculum/candidate-assessment.md` exists; every CORE, BRANCH and SUPPORTING competency has a measured depth with a confidence level; the candidate has reviewed the results and every dispute has been re-tested.

### Phase 6 — Gap analysis and 80/20 ranking

For each competency:

`gap = target depth − measured depth` (in levels). A zero gap means maintenance: format rehearsal only.

Score each non-zero gap:

- **reach** = share of target companies that test it, counting `stretch`-fit companies at half weight
- **weight** = 3 for CORE or gatekeeper-tested, 2 for BRANCH, 1 for SUPPORTING
- **impact** = reach × weight × gap
- **hours_to_close** = work-unit estimate for the gap × pace factor
- **leverage** = impact ÷ hours_to_close

Rank by leverage. The **vital few** are the top-ranked gaps whose cumulative impact reaches about 80% of total impact. Any gap tested in a gatekeeper stage joins the vital few regardless of rank: failing it ends the process before anything else counts.

Report the split as a Pareto line, e.g. `vital few: 6 of 19 gaps, 81% of impact, 38% of estimated hours`. The scores are a ranking aid, not a measurement; show the inputs so the candidate can challenge a weight, and re-rank if they do.

Format gaps from the assessment (e.g. knows the material but runs out of time live) rank like knowledge gaps, sized by rehearsal hours.

**Done when:** every gap has a leverage score with visible inputs, the vital few are named, and the Pareto line is reported.

### Phase 7 — Master curriculum

Build units **only for measured gaps**, ordered by: prerequisites first, then vital few by leverage, then the rest by leverage. Competencies at target depth get a short maintenance block (format rehearsal and one exit test before interviews).

Personalize with the profile and assessment: exercises in the candidate's primary language unless a target requires another; examples drawn from their stack and domain; their preferred learning format; their achievements turned into story-bank practice for behavioral rounds.

### Phase 8 — Company branches

A branch is a delta from the master, not a second curriculum. Per company:
- which shared topics suffice
- added company-specific topics, ranked by leverage
- assessment formats to rehearse, under the company's AI policy
- what is reduced or skipped, and why
- extra hours
- readiness from the assessment (share of the company's tested competencies already at target)

### Phase 9 — Resource selection

Read `references/resource-selection.md`. Use the smallest verified set that covers the gaps: one strong primary resource per competency plus targeted supplements, each mapped to exact curriculum nodes, with sections the candidate already knows marked to skip.

### Phase 10 — Practice design

Per topic: learn material → guided example → independent exercise → timed assessment → review.

Practice mirrors each company's documented assessment mode, including whether AI tools are permitted. For practical-engineering targets, weight unfamiliar-codebase tasks, debugging, code review (including reviewing AI-generated code), API design, security/performance reasoning, implementation with tests, written engineering explanation, and product trade-off reasoning.

Algorithm practice gets the share the target processes evidence, sized by work units like everything else.

## Exit tests

Every CORE and BRANCH topic has one, with observable criteria weighted toward the most frequently tested subskills.

**Example — HTTP caching, D2.** Pass requires all of:
- explain cache-control directives without notes
- diagnose a stale-response scenario
- design a cache strategy for a representative API
- identify at least three invalidation/failure concerns

Pass → mark complete, assign no more material, update measured depth. Fail → identify the failed subskill, reopen only that, retest.

## Stopping rules

- **A — Coverage complete:** every required subskill in scope has a passing exit test.
- **B — Diminishing returns:** target depth met; more material would exceed the documented requirement.
- **C — Time budget protection:** if an expansion would displace a vital-few or CORE item, log it under `deferred` instead.
- **D — Source boundary:** a subtopic outside the competency map, however a resource presents it, goes to the rabbit-hole parking lot.
- **E — Mistake-driven expansion:** repeated mistakes can justify expansion; curiosity alone does not.

## Rabbit-hole parking lot

`curriculum/rabbit-hole-parking-lot.md`. For each tempting out-of-scope topic: topic; why it was tempting; evidence for/against relevance (including market trajectory); the condition that would reopen it.

## Timeline engine

Work units: `unit_id`, `competency_id`, activity, `estimated_minutes`, estimate confidence (high/medium/low), prerequisite, exit evidence.

`gross_hours = sum(estimated_minutes) × pace_factor / 60`
`planned_hours = gross_hours + assessment/retry/review buffer` (default 20%; change it only with assessment evidence, and say why)

Allocate into calendar blocks using the profile's hours/week and deadline. Vital-few units fill the earliest blocks.

When demand exceeds capacity, cut from the bottom of the leverage ranking, in this order, and show every cut:
1. `declining` items not tested by any target company
2. OPTIONAL
3. SUPPORTING, lowest leverage first
4. BRANCH items for companies with weak evidence or `stretch` / `out of reach` fit
5. lower depth on non-core items outside the vital few

If the vital few alone exceed capacity, say so in the reality check with the numbers, and present the options (extend the deadline, raise hours, narrow targets) for the learner to choose.

## Recalibration

After a meaningful sample of curriculum work (not one unusually easy or hard task):

`observed_pace = actual_minutes / estimated_minutes`

Replace the assessment pace factor with the observed one, recompute remaining hours, and re-rank if passing exit tests changed the gaps. Keep the original plan visible so the learner can see why the estimate changed.

## Freshness

Every output file opens with:
- `generated`: date
- `evidence_window`: oldest and newest evidence dates used
- `reverify_by`: default 30 days after generation, or before the first scheduled interview, whichever is earlier

`master-curriculum.md` ends with a re-verification checklist: target postings still open and unchanged; interview process and AI policy unchanged; any `rising`/`declining` verdict that drove a cut or addition still holds. A changed fact reopens only the affected nodes.

## Progress model

Per competency: `not_started` · `learning` · `practicing` · `assessment_due` · `complete` · `maintenance` · `reopened` · `deferred`. A topic returns from `complete` to `reopened` only when later evidence shows a material gap.

## Output contract

Read `references/output-contract.md` before writing any output file. Six files go to `curriculum/`: `candidate-assessment.md`, `master-curriculum.md`, `company-branches.md`, `study-plan.csv`, `rabbit-hole-parking-lot.md`, `coverage-audit.md`. Write each competency node in the format in `references/curriculum-schema.md`.

## Final quality gate

Before declaring the curriculum complete, verify each item and fix failures. When an Agent tool exists, give this checklist and `curriculum/` to a fresh subagent: it re-checks the hour arithmetic, traces a sample of units back to their gap and source, re-fetches a sample of resource URLs, and reports failures; you fix them. A fresh-context check catches what self-review misses. Without an Agent tool, run the checklist yourself.

- [ ] Every CORE, BRANCH and SUPPORTING competency has a measured depth with confidence; the candidate reviewed the assessment.
- [ ] Every curriculum unit traces to a measured gap or a maintenance need.
- [ ] Every gap has a leverage score with visible inputs; vital few and the Pareto line are reported; gatekeeper-tested gaps are in the vital few.
- [ ] Vital-few units are scheduled first, after their prerequisites.
- [ ] Exercises use the candidate's language, stack and preferred format where targets allow.
- [ ] Every major company requirement is covered, or its omission is explained.
- [ ] Every major topic is bounded tightly enough that the learner can tell what to study.
- [ ] Every major topic has a depth target, an exit test and a stopping rule.
- [ ] Every competency has a market trajectory and a relevance decision with evidence.
- [ ] Nothing a target company currently tests was cut on market grounds alone.
- [ ] Practice matches each company's current format and AI policy.
- [ ] Out-of-scope topics are listed.
- [ ] Every resource was verified live and current, and maps to exact nodes.
- [ ] Time estimates are derived from work units and the pace factor, with calculations shown.
- [ ] The schedule fits the stated hours and deadline, or the cuts and shortfall are shown.
- [ ] The reality check states shortfalls and weak-market findings with numbers.
- [ ] Every sentence passes the grounded register (Principle 2).
- [ ] Company preparation is a delta, not a duplicate curriculum.
- [ ] Evidence links are preserved; current and historical evidence are not mixed.
- [ ] Every file carries the freshness header.

## Final behavior

Produce a closed system:

`requirement + market evidence → measured gap → leverage rank → bounded competency → depth → verified resource → practice → exit test → STOP`

After passing an exit test, the learner's default is to move on to the next-highest-leverage gap.

Close with a message to the learner that opens with the outcome (vital few, total planned hours against capacity, first week's focus), then names any decision only they can make, such as a shortfall option. Report only work a tool result from this session backs; say plainly what was skipped or could not be verified.
