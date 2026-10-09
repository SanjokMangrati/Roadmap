# Assessment interview

Goal: a **measured** picture of where the candidate stands on every competency their targets test, precise enough that each curriculum hour lands on a real gap. The curriculum is built from this file; a sloppy assessment produces a generic plan.

## Contents
- Ground rules and candidate briefing
- Step 1 — Plan
- Step 2 — Artifact review
- Step 3 — Achievement deep-dive
- Step 4 — Adaptive competency probes (depth item table)
- Step 5 — Format probes
- Exercise mechanics
- Scoring (confidence, pace factor)
- Step 6 — Results
- Later updates

## Ground rules

- **Measure, not ask.** Evidence strength, strongest first: observed performance (solved now, tests run) → artifact review (their own code and PRs) → explanation probe → self-rating. Self-ratings from `candidate-profile.md` are only the starting point of the adaptive search.
- **Assess the matrix.** Only competencies that survived the relevance gate. CORE and BRANCH get full adaptive probing; SUPPORTING gets one quick check; OPTIONAL is skipped.
- **Probe up to the target depth, no higher.** Measuring above what the targets test costs time and changes nothing in the plan.
- **Budget:** about 5% of planned prep hours, within 1.5–4 h, split into sessions of at most 90 min. When the budget is tight, use one item per competency at target depth.
- **Rubric first.** Write each item's pass criteria before showing the item, so scoring stays consistent.

Brief the candidate before the first item:
- the purpose: find gaps, so the plan skips what they already know
- no AI tools, notes or search unless an item says so
- "I don't know" is a useful answer; a guess that happens to land hides a gap the plan will then miss
- feedback comes at the end of each section, not item by item

## Step 1 — Plan

Write `assessment/plan.md`: competencies to assess, target depth, prior (self-rating plus profile evidence), item formats, minutes per item, session split. Show the candidate the session count and total time; let them choose when to run each session.

**Done when:** the candidate has agreed to the session plan.

## Step 2 — Artifact review

Needs no candidate time; run it while waiting, if the profile links repos, PRs, a portfolio or writing samples.

Read the code against the competency list: structure, tests, error handling, security, performance awareness, commit and PR descriptions (written communication). Ask the candidate which parts they wrote alone, with others, or with AI help. Artifact evidence alone gives **medium** confidence at most.

## Step 3 — Achievement deep-dive

For each top achievement in the profile, climb this probing ladder, one question at a time:

1. **Ownership:** what exactly did you do, versus the team?
2. **Decisions:** why this approach over the alternatives? What did you reject?
3. **Failure:** what broke, and what would you change now?
4. **Numbers:** scale, latency, users, cost, impact. How were they measured?
5. **Depth floor:** follow the most technical claim one "why" or "how" further each turn until the answers run out. Where they run out is a measured depth for that competency.

Score each achievement on ownership clarity, trade-off reasoning, depth floor reached, and story readiness (a complete situation–action–result story told in 2–3 minutes). This doubles as the behavioral assessment and seeds the story bank.

## Step 4 — Adaptive competency probes

For each competency, find the highest depth the candidate passes:

1. Start one level below the target depth, or at the prior if the prior is lower.
2. Pass → step up, stopping once the target depth is passed.
3. Fail → step down until a pass.
4. Stop when two consistent signals agree. Expect 1–3 items per competency.

Measured depth = the highest level passed.

| Depth | Item type | Pass signal |
|---|---|---|
| D0 | Define it and say when it matters; multiple-choice via AskUserQuestion, always followed by "why?" | Correct answer **and** correct reason |
| D1 | Predict a snippet's output, spot the bug, or write a short function | Correct, idiomatic, names the common failure mode |
| D2 | Timed representative interview problem with tests, then a trade-off follow-up | Tests pass within the timebox; trade-off stated and defended |
| D3 | Ambiguous design or incident scenario, then perturbations (10× load, a dependency fails, a requirement changes) | Names the failure modes, makes and defends trade-offs, adapts to the perturbation |

Write items in the candidate's primary language unless a target requires another. Draw item content from what the target companies actually test (from `requirements/*.md` and candidate reports).

## Step 5 — Format probes

Run one short mini-mock per distinct format in the target processes, for example:
- live coding with think-aloud
- debugging unfamiliar code
- reviewing a diff, including AI-generated code with planted defects
- a system-design micro-prompt
- a written async explanation of a technical decision
- AI-assisted coding, where a target allows it: solve with an assistant, then verify its output

Score format skills separately from knowledge: states assumptions, asks clarifying questions, manages time, tests own code, explains while working, verifies AI output. A candidate who knows the material but fails the format has a format gap, and the fix is rehearsal, not study.

## Exercise mechanics

- Claude writes each hands-on item to `assessment/<item-id>/`: a `README.md` with the task, timebox and allowed tools; starter code; tests.
- The candidate notes start and end times (or Claude uses message timestamps) and replies when done.
- Claude runs the tests, reads the code, and scores against the pre-written rubric.
- For think-aloud items, the candidate types their reasoning as they work.

## Scoring

Each item: `pass` / `partial` / `fail`, plus evidence (answer excerpt, test result, time taken).

Confidence per competency:
- **high:** two or more consistent observed items
- **medium:** one observed item, or artifact evidence
- **low:** explanation or self-report only

**Pace factor** = actual minutes ÷ estimated minutes across hands-on items. It feeds the timeline engine.

## Step 6 — Results

Write `curriculum/candidate-assessment.md`:

1. **Where you stand:** at most 10 lines, numbers only (e.g. `CORE competencies at target depth: 4 of 11`; `largest gaps: SQL query design D1→D2, system design D0→D2`; `pace factor 1.4`).
2. **Competency table:** competency · target depth · measured depth · gap · confidence · evidence · self-rating · self-rating delta.
3. **Calibration:** where self-rating ran above or below the measurement.
4. **Strengths:** at or above target; these get maintenance only (format rehearsal).
5. **Format skills table.**
6. **Story bank readiness:** per achievement.
7. **Per-company readiness:** share of each company's tested competencies already at target depth.
8. **Pace factor.**

Walk the candidate through the summary and the gaps. Any result they dispute gets one re-test item; the re-test result stands.

**Done when:** every assessed competency has a measured depth and confidence, the candidate has reviewed the results, and every dispute is re-tested.

## Later updates

Exit tests during the curriculum update measured depth. A full re-assessment runs only when re-verification finds the target requirements changed.
