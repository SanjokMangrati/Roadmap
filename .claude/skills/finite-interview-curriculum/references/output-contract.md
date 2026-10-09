# Output contract

Write to `curriculum/` (assessment exercises live in `assessment/`). Every file opens with the freshness header from SKILL.md. Node format for each competency: `curriculum-schema.md`.

## 1. `curriculum/candidate-assessment.md`
Structure in `assessment-interview.md`, Step 6.

## 2. `curriculum/master-curriculum.md`
- freshness header
- **where you stand:** the summary from the assessment
- **reality check:** demand vs capacity (hours, with calculation); per-company readiness and fit; market notes that change priorities, each with numbers and sources
- target profile; target companies; deadline/budget; assumptions
- **gap ranking:** every gap with its leverage inputs; the vital few; the Pareto line
- finite syllabus: target and measured depth, exact subtopics, `NOT COVERED` for every major topic
- maintenance list (competencies already at target)
- relevance-gate decisions (cuts and caps, with evidence)
- exit test for every CORE/BRANCH topic
- estimated hours with the calculation
- primary resources mapped to nodes
- practice tasks and story-bank practice
- schedule
- company branches (summary)
- deferred topics
- re-verification checklist

## 3. `curriculum/company-branches.md`
Per company: inherited master preparation; readiness; unique stages and their AI policy; unique competencies; branch tasks ranked by leverage; branch hours; branch exit criteria; fit verdict; evidence links.

## 4. `curriculum/study-plan.csv`
`date_or_week, session, competency_id, topic, target_depth, measured_depth, leverage_rank, vital_few, activity, estimated_minutes, prerequisite, exit_test, resource, company_branch, market_trajectory, evidence_ids, status`

## 5. `curriculum/rabbit-hole-parking-lot.md`
Structure in SKILL.md, "Rabbit-hole parking lot".

## 6. `curriculum/coverage-audit.md`
Traceability matrix:

`Company requirement → competency → measured gap → subskills → curriculum unit → practice → exit test → source`

plus the relevance-gate log (what was cut or capped, and the market evidence). Anything untraceable is flagged.
