---
name: company-interview-research
description: Interview-target research. Interviews the candidate about goals, experience, achievements and constraints, then finds matching companies and extracts current, evidence-backed role and interview requirements, grounded in live job-posting data and how AI has reshaped the target role and its interviews. Use when choosing target companies, checking what companies currently test, or gauging which skills the market still rewards. Outputs structured evidence for finite-interview-curriculum.
---

# Company Interview Research

## Mission

Find companies that match **this candidate's** goals and profile, then extract what those companies currently require and test. Ground every finding in dated, sourced evidence and in live job-market data, including how AI has changed the target role and its interviews.

A learner will study from the downstream curriculum for weeks. Every claim here must survive a source check; a skill the market has stopped rewarding costs the learner real days.

The research answers:

1. Who is the candidate, what do they want, what have they achieved, and what can they realistically reach?
2. What does the current market for their target role look like, and how has AI changed the job and its interviews?
3. Which companies match the profile, and why?
4. Which current roles at those companies fit?
5. What does each company evaluate at each hiring stage?
6. Which competencies do current role descriptions explicitly require?
7. What is known versus inferred, and what is stable enough to build a curriculum on?

## Grounding rules

These apply to every phase and every output file.

- **Plain findings register.** Each sentence carries a datum, a source, a date, or a decision. Cut sentences that carry none. Report weak markets, skill gaps and out-of-reach targets as plainly as strong ones: an accurate bad-news line serves the candidate; a reassuring one costs them weeks.
- **Numbers carry their provenance:** N, source, date, segment. Example: `41 of 96 postings (43%), Greenhouse/Lever/Ashby boards, fetched 2026-10-09, remote full-stack mid-level, EU-eligible`.
- **Model memory is a search lead, not evidence.** A trend you recall gets verified against a dated source before it enters any output. Unverifiable claims are marked `unverified` and stay out of requirements.
- **Freshness.** Record publication/update date when visible, access date always. Hiring-process and market evidence older than 12 months is `old`; older than 24 months is `stale` (historical only). AI-related claims (tooling, AI interview policy, AI skill demand) age faster: older than 6 months is `old`.
- **Today's date comes from the environment**, never from training data.
- **Readable output.** The candidate reads these files, not your working notes. Write complete sentences with terms spelled out; keep chat shorthand, arrow chains and labels coined mid-research out of output files. Lead each summary with the finding.

## Research tools

Use the strongest tools the session offers. Some load lazily: check deferred tools and load them with ToolSearch before calling. Skip any that are absent and say which were unavailable in `company-landscape.md`.

| Need | Tool |
|---|---|
| JS-rendered careers pages, boards that block plain fetches | Playwright plugin (`mcp__plugin_playwright_*`), or Claude in Chrome after loading its skill |
| Current postings in bulk | Public ATS JSON endpoints (below) via WebFetch or `curl` |
| Is a framework/library version current, what replaced it | context7: `resolve-library-id`, then `query-docs` |
| Multi-source market synthesis | `anthropic-skills:deep-research` skill when an Agent tool exists |
| Per-company deep dives on a shortlist of 5+ | One subagent per company running Phases 3–6 against `references/evidence-schema.md`; keep working on other phases while they run, then merge and resolve conflicts in the main thread |
| Skill-frequency counts over saved postings | Bash/Python script, saved alongside its output |

Record what you learn about sources in `interview-intelligence/research-notes.md`, one line each: working board tokens, endpoints that failed, sites that block fetches, searches that surfaced good companies. Read it first on a re-run.

Public ATS endpoints (confirm each responds before relying on it; fall back to the careers page):

- Greenhouse: `https://boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true`
- Lever: `https://api.lever.co/v0/postings/<company>?mode=json`
- Ashby: `https://api.ashbyhq.com/posting-api/job-board/<name>?includeCompensation=true`
- SmartRecruiters: `https://api.smartrecruiters.com/v1/companies/<id>/postings`

The board token is usually visible in the company's careers URL (e.g. `job-boards.greenhouse.io/<token>`). Respect site terms; prefer official APIs and first-party pages over scraping third-party boards.

## Phase 0 — Intake

Read `references/intake.md` and run it before any company or market research.

The candidate's answers define the search. There is no default anchor company and no default profile. Unanswered fields are recorded as `unspecified`, and the search widens to cover them rather than assuming a value.

**Done when:** `interview-intelligence/candidate-profile.md` exists and the candidate has confirmed or corrected its summary.

## Phase 1 — Market scan

Read `references/market-research.md` and run it for the role families and segment in the profile.

**Done when:** `market-context.md` and `skill-demand.csv` exist; every target role family has a demand snapshot from a posting corpus with stated N; every major skill family has a trajectory verdict; the AI shift is summarised separately for the job and for the interview, each claim sourced and dated.

## Phase 2 — Company discovery

**Anchors.** If the candidate named target companies, research them as anchors and use their verified traits to find similar companies. If not, build the similarity model directly from the profile.

**Hard filters** (a company failing one is excluded, with the reason logged):
- Location / work-authorization eligibility for the candidate, verified per role. Never assume eligibility.
- Currently hiring for a matching role: at least one live first-party posting, or documented recurring hiring for that role within the last 6 months.

**Soft match dimensions** (derive weights from the profile, not from prestige or brand):
- role family and seniority alignment
- tech-stack overlap with the candidate's experience and stated goals
- work mode (remote/async/hybrid/onsite)
- company stage, size and domain preferences
- interview style (work sample, take-home, paid trial, live coding, algorithm-heavy, system design) against the candidate's strengths and stated preferences
- AI posture: AI-product company, AI-assisted engineering expectations, AI policy in interviews, where the candidate cares
- company hiring trajectory: layoffs, freezes, growth, from dated sources

A company is a match only when it passes all hard filters and at least two soft dimensions are supported by evidence. A single shared trait ("remote", "uses React") is never enough.

**Candidate pool sources:** companies appearing in the Phase 1 posting corpus; the candidate's named companies; ATS boards; several search families generated from the profile (e.g. `"<role> <stack> <work mode> <region> hiring"`, `"<domain> engineering hiring process"`, `"<role> interview process take-home OR work sample"`, `"companies hiring <role> visa sponsorship <country>"`).

Default shortlist: 5–8 matches plus an optional reach list. Adjust to the candidate's request.

**Done when:** every shortlisted company has a live first-party matching posting (URL + fetch date) and a written match rationale citing the evidence for each soft dimension claimed.

## Phase 3 — Role requirements

For each relevant current role, extract:

- seniority and years/level expectations, if stated
- languages/frameworks (check version currency with context7 where it matters)
- backend / frontend / full-stack scope
- APIs and distributed-systems expectations
- databases/storage
- cloud/infrastructure
- testing/quality
- security
- performance
- debugging / incident response
- system design / architecture
- product/customer orientation
- collaboration and written communication
- autonomy/ownership
- AI-assisted development expectations (AI coding tools, reviewing/verifying generated code)
- AI/LLM product work (API integration, retrieval, evals, agents), when stated
- compensation range, when published
- location/work-authorization restrictions

Keep each item labelled `required`, `preferred`, `nice to have`, or `inferred from repeated job language`.

## Phase 4 — Interview process

Map every known stage in order, from application questions through reference checks. For every stage record: format; duration/timebox if published; artifact or task type; competencies evaluated; explicit company guidance; **AI policy** (AI tools allowed / banned / expected / unknown); source; confidence.

Record format changes and their dates, especially ones driven by AI (take-home replaced by live coding, new AI-assisted rounds, proctoring). Keep current and historical processes as separate, dated entries. Map only stages a source supports.

## Phase 5 — Candidate reports

Candidate reports supply practical detail official docs omit: recurring question patterns, task shape, unexpected areas, recent changes. They are secondary evidence; weight the last 12 months.

Label each claim:
- `corroborated`: several recent independent reports
- `anecdotal`: one or very few reports
- `stale`: old process, historical only
- `conflicting`: current sources disagree

One report stays anecdotal regardless of how detailed it is.

## Phase 6 — Resolve conflicts

1. Current official company source wins.
2. Role-specific material beats company-wide generic material.
3. Newer beats older when the process is known to change.
4. Unresolved conflicts stay visible, with both sides cited.

## Phase 7 — Fit check

For each shortlisted role, compare the candidate profile with the role and interview requirements:

| Verdict | Meaning |
|---|---|
| `realistic` | Meets hard requirements; gaps are closable within the candidate's stated timeline |
| `stretch` | Meets hard requirements; gaps likely exceed the timeline or hours |
| `out of reach` | Fails a hard requirement (work authorization, years, required credential) |

Each verdict lists the specific gaps and the evidence for each. Out-of-reach roles move to the reach list only when the candidate asked for one.

Hard-requirement verdicts (authorization, years, credentials) are final here. Skill-gap verdicts rest on self-reported depth, so label them `preliminary`: `finite-interview-curriculum` measures actual depth in its assessment interview and replaces them.

## Evidence rules

Every material claim has a source. Company source tiers:

- Tier 1: official careers page / job description / hiring documentation
- Tier 2: official engineering handbook / blog / interviewer documentation
- Tier 3: official employee statements hosted by the company
- Tier 4: reputable current candidate reports / interview databases
- Tier 5: community discussions / social posts (leads only; never the sole basis for a requirement)

Market source tiers (M1–M4) live in `references/market-research.md`.

For each source record: URL, title, tier, publication/update date, access date, claims supported, freshness (`current` / `recent` / `old` / `stale` / `unknown`).

## Clustering

Cluster related job-description phrases into competency families ("performance", "profiling", "optimization", "scalability" → one family with concrete subskills). Keep enough subtopics that curriculum coverage stays auditable; a label like "backend knowledge" is too coarse to audit.

## Output contract

Write to `interview-intelligence/` in the working directory unless the user names another location.

1. **`candidate-profile.md`**: schema in `references/intake.md`.
2. **`market-context.md`**: structure in `references/market-research.md`.
3. **`skill-demand.csv`**: columns in `references/market-research.md`.
4. **`raw/postings/<company-slug>-<YYYY-MM-DD>.json`** plus the extraction script: the corpus behind every demand number, so it can be re-run.
5. **`company-landscape.md`**: candidate summary; matching method; shortlist with match rationale; fit verdicts and gaps; reach list; current role links; hiring-process summary; notable differences; evidence quality; tools used/unavailable; unresolved uncertainty. Describe fit along dimensions; no overall ranking.
6. **`company-matrix.csv`**: columns
   `company, anchor, match_dimensions, fit_verdict, fit_gaps, role_title, role_url, open_matching_postings, seniority, location_eligibility_notes, process_url, stages, ai_interview_policy, ai_skill_expectations, technical_competencies, nontechnical_competencies, work_sample_type, leetcode_emphasis, system_design_emphasis, written_communication_emphasis, trial_or_work_sample, evidence_quality, last_verified`
7. **`requirements/<company-slug>.md`**: current role requirements; interview stages with AI policy; stage-by-stage evaluation targets; competency taxonomy; explicit exclusions/unknowns; source ledger (YAML per `references/evidence-schema.md`).
8. **`master-competency-map.md`**: all company requirements normalized into one taxonomy, without curriculum durations. Each competency: `competency_id`, name, parent, subskills, companies requiring it, assessment formats, evidence strength, role relevance, `market_trajectory` (from Phase 1), `demand_share` (from `skill-demand.csv`, with N and date), known depth hints.

## Quality checks

Before finishing, verify each item and fix failures. When an Agent tool exists, give the checklist and the output directory to a fresh subagent: it re-fetches a sample of cited URLs (at least one per shortlisted company), confirms each supports its claim, and reports failures; you fix them. A fresh-context check catches what self-review misses. Without an Agent tool, run the checklist yourself.

- [ ] The candidate confirmed `candidate-profile.md`; no profile field was filled by assumption.
- [ ] Every demand number states N, source, date and segment; the raw corpus and script are saved.
- [ ] Every trajectory verdict cites its evidence or reads `insufficient-data`.
- [ ] The AI shift is covered for both the role and the interview, with dated sources.
- [ ] Every shortlisted company passes both hard filters, with a live first-party posting URL.
- [ ] Every match rationale cites evidence for at least two soft dimensions.
- [ ] Every claimed interview stage has a source and an AI-policy value (`unknown` allowed).
- [ ] Current and historical processes are separate and dated.
- [ ] Candidate reports never override available official evidence.
- [ ] Role requirements and interview requirements are represented separately.
- [ ] Every role has a fit verdict with listed gaps.
- [ ] Uncertainty is explicit.
- [ ] The files are usable as inputs to `finite-interview-curriculum`.

## Final behavior

This skill researches. Study schedules, durations and resource picks belong to `finite-interview-curriculum`; hand off the evidence, the market context and the normalized competencies.

Close with a message to the candidate that opens with the outcome (shortlist size, fit verdicts, the market finding that most changes their plan), then names anything only they can resolve. Report only work a tool result from this session backs; say plainly what was skipped or could not be verified.
