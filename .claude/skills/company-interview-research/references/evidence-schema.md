# Evidence schema

Use this schema for machine-readable notes inside company requirement files.

```yaml
company: ""
anchor: false            # true if the candidate named this company
match:
  hard_filters:
    eligibility: ""      # pass | fail, with note
    hiring_now: ""       # pass | fail, with posting URL
  soft_dimensions:
    - dimension: ""
      evidence: []       # source ids
fit:
  verdict: ""            # realistic | stretch | out of reach
  preliminary: true      # skill-gap verdicts stay preliminary until the curriculum assessment
  gaps:
    - gap: ""
      evidence: []
role:
  title: ""
  url: ""
  seniority: ""
  compensation: ""       # if published
  verified_date: ""
process:
  url: ""
  verified_date: ""
  stages:
    - id: ""
      name: ""
      format: ""
      timebox: ""
      ai_policy: "allowed|banned|expected|proctored|unknown"
      competencies: []
      evidence_quality: "official|corroborated|anecdotal|stale|conflicting"
      sources: []
  changes:
    - date: ""
      change: ""
      ai_driven: null
      sources: []
requirements:
  explicit_required: []
  explicit_preferred: []
  inferred_repeated: []
  ai_expectations: []
uncertainty:
  - claim: ""
    reason: ""
    confidence: "high|medium|low"
sources:
  - id: "S1"
    url: ""
    title: ""
    tier: 1
    published_or_updated: ""
    accessed: ""
    freshness: "current|recent|old|stale|unknown"
    supports: []
```
