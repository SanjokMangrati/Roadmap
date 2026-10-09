# Brief for per-company research agents (Phases 3–6)

Today is 2026-10-09 (take dates from this, not training data). Output directory: `C:\Users\Sanjok\Downloads\Roadmap\interview-intelligence\`.

## Candidate (from candidate-profile.md, confirmed 2026-10-09)
India-based full-stack engineer, about 3 years professional experience, targeting mid-level remote roles at US/EU seed–Series C+ companies that allow working from India (employee, employer-of-record or contractor all acceptable). No timezone limits. Self-reported stack (claims only, unmeasured): React/Next.js 3y, Node/NestJS 3y, PostgreSQL 3y, GCP 1y, AWS 0.5y, AI-assisted coding 1.5y. Weak areas: explaining thought process aloud; explaining/defending architecture decisions. Pay target: take-home about 1.5–2 lakh INR per month. Interview-ready deadline 2026-10-29 (20 days, ~7 h/day). Free resources only.

## Your job for each assigned company
Write `requirements/<company-slug>.md` and return a compact summary (under 300 words) plus one CSV row (columns below).

1. **Hard filters.** Fetch the live first-party posting (URL given). Confirm (a) India-based remote work is explicitly allowed for this role (quote the sentence) and (b) the posting is live today. If India eligibility is not explicit, say so and mark `eligibility: unverified`. Note employment type (employee / EOR / contractor) if stated.
2. **Role requirements (Phase 3).** Extract and label each item `required`, `preferred`, `nice to have` or `inferred from repeated job language`: seniority/years, languages/frameworks, frontend/backend scope, APIs/distributed systems, databases, cloud/infra, testing, security, performance, debugging/incidents, system design, product orientation, written communication, autonomy, AI-assisted development expectations, AI/LLM product work, compensation (if published), location/work-authorization restrictions. Also check other open engineering postings at the same company for repeated language. Note the company's actual tech stack from first-party engineering sources (engineering blog, GitHub org, handbook) when the posting is vague.
3. **Interview process (Phase 4).** Map every stage in order from application to offer: format, duration/timebox, artifact/task type, competencies evaluated, explicit company guidance, **AI policy** (`allowed|banned|expected|proctored|unknown`), source, confidence. Look first for first-party sources: the posting itself, careers page "our hiring process", engineering handbook (e.g. public handbooks), blog posts by the company about hiring. Record format changes with dates (especially AI-driven ones). Keep current vs historical processes as separate dated entries. Only map stages a source supports.
4. **Candidate reports (Phase 5).** Search Glassdoor, Blind, Reddit, LeetCode Discuss, interview databases, personal blogs, YouTube descriptions. Weight the last 12 months. Label each claim `corroborated` (several recent independent reports), `anecdotal` (one or few), `stale` (old process), `conflicting`. One report stays anecdotal however detailed. Glassdoor often blocks fetches; note blocked sources rather than guessing their content.
5. **Resolve conflicts (Phase 6).** Current official source wins; role-specific beats generic; newer beats older; unresolved conflicts stay visible with both sides cited.
6. **Signals for the candidate's goals:** published pay or pay data (levels.fyi, Glassdoor India, posting ranges) versus the 1.5–2 lakh INR/month take-home target; company stage/funding and any layoffs/hiring freezes in the last 12 months (dated sources); how crowded the applicant pool likely is (any data: applicant counts shown on LinkedIn/Wellfound, brand prominence) — mark inference as inference.
7. **Preliminary fit.** Verdict `realistic` / `stretch` / `out of reach` against the candidate profile with specific gaps and evidence. Hard-requirement verdicts (authorization, years, credentials) are final; skill-gap verdicts are `preliminary` (self-reported depth only).

## Rules
- Load tools first: ToolSearch `select:WebSearch,WebFetch`. Use WebSearch mode "standard" first; "extended" for thin/niche results. Public ATS JSON endpoints work: Greenhouse `https://boards-api.greenhouse.io/v1/boards/<token>/jobs/<id>`, Ashby `https://api.ashbyhq.com/posting-api/job-board/<name>`, Lever `https://api.lever.co/v0/postings/<company>/<id>`. You may use curl via Bash.
- Model memory is a search lead, not evidence. Every material claim has a URL, title, tier, publication/update date (if visible), access date 2026-10-09, freshness (`current` <6 months for AI claims / <12 months otherwise; `recent`; `old` >12 months (>6 for AI-related); `stale` >24 months; `unknown`).
- Company source tiers: 1 official careers/job description/hiring docs; 2 official handbook/blog/interviewer docs; 3 employee statements hosted by the company; 4 reputable candidate reports/interview databases; 5 community/social posts (leads only; never the sole basis for a requirement).
- Write complete, readable sentences with terms spelled out. Report bad news plainly (e.g. role is senior-only, pay below target, India not eligible). Lead each section with the finding.
- Do not fabricate. Say plainly what you could not verify or could not fetch.

## `requirements/<slug>.md` structure
1. Summary (5–8 lines: role, eligibility verdict, pay vs target, process shape, AI policy, fit verdict).
2. Hard filters (with quotes and URLs).
3. Current role requirements (labelled list).
4. Interview stages (table: order, stage, format, timebox, AI policy, competencies, evidence quality, sources).
5. Stage-by-stage evaluation targets (what to prepare for each stage, tied to evidence).
6. Competency taxonomy for this company (families → concrete subskills).
7. Process changes and history (dated).
8. Candidate-report findings (labelled corroborated/anecdotal/stale/conflicting).
9. Fit check (verdict, preliminary flag, gaps with evidence).
10. Exclusions and unknowns.
11. Source ledger: YAML block following the evidence schema below.

```yaml
company: ""
anchor: false
match:
  hard_filters:
    eligibility: ""      # pass | fail | unverified, with note
    hiring_now: ""       # pass | fail, with posting URL
  soft_dimensions:
    - dimension: ""
      evidence: []       # source ids
fit:
  verdict: ""
  preliminary: true
  gaps:
    - gap: ""
      evidence: []
role:
  title: ""
  url: ""
  seniority: ""
  compensation: ""
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
    accessed: "2026-10-09"
    freshness: ""
    supports: []
```

## CSV row to return (one per company, do not write the CSV yourself)
`company, anchor, match_dimensions, fit_verdict, fit_gaps, role_title, role_url, open_matching_postings, seniority, location_eligibility_notes, process_url, stages, ai_interview_policy, ai_skill_expectations, technical_competencies, nontechnical_competencies, work_sample_type, leetcode_emphasis, system_design_emphasis, written_communication_emphasis, trial_or_work_sample, evidence_quality, last_verified`
Use semicolons inside fields; quote fields containing commas.
