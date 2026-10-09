# Curriculum node schema

Use this structure for each major competency when generating the curriculum.

```yaml
competency_id: SWE.WEB.HTTP.CACHING
name: HTTP caching
category: web-platform
importance: CORE
companies:
  - Company A
  - Company B
market:
  trajectory: stable          # rising | stable | shifting | declining | insufficient-data
  demand_share: "18 of 96 postings (19%), corpus 2026-10-09"
  evidence: [M1]
relevance_decision: keep      # keep | cap | cut, with reason below
relevance_reason: "Tested in Company A's code-review stage; stable demand."
required_depth: D2
assessment:
  measured_depth: D1
  confidence: high            # high | medium | low
  evidence: ["item A3: stale-response diagnosis failed", "item A4: cache-control MCQ passed"]
  gap: 1                      # required_depth − measured_depth, in levels
leverage:
  reach: 0.67                 # share of target companies testing it (stretch-fit at half weight)
  weight: 3                   # 3 CORE/gatekeeper, 2 BRANCH, 1 SUPPORTING
  impact: 2.0                 # reach × weight × gap
  hours_to_close: 4.5         # work units × pace factor
  score: 0.44                 # impact ÷ hours_to_close
  rank: 3
  vital_few: true
coverage:                     # ordered by how often targets test each subskill
  - cache-control
  - freshness
  - validation
  - invalidation
not_covered:
  - CDN vendor internals
  - distributed cache internals beyond interview need
evidence:
  - source_id: S1
    claim: "..."
resources:
  primary:
    title: ""
    url: ""
    verified: ""              # date the URL was confirmed live
    version_or_updated: ""    # tool/framework version or last-updated date
    covers: []
    skip: []
  supplements: []
work_units:
  - id: W1
    activity: "Read/learn ..."
    minutes: 30
  - id: W2
    activity: "Implement ..."
    minutes: 45
practice_ai_mode: both        # with-ai | without-ai | both, per target company AI policy
exit_test:
  criteria:
    - ""
  pass_threshold: "all criteria"
stop_rule: "Pass exit test at target depth; expand only if later evidence reveals a gap."
```
