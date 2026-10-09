# LiveKit: Senior Product Engineer

Researched and verified 2026-10-09 (REACH list, lighter pass).

## 1. Summary

- **Role:** Senior Product Engineer. You would build LiveKit's developer-facing web dashboards, CLI, observability and debugging surfaces, mainly in TypeScript, with some Go. The posting is live today (published 2026-05-23) (S1).
- **Eligibility: `unverified`.** The posting is remote with the locations "North America", "APJ", "EMEA" and "San Francisco, CA (Hybrid)". "APJ" is never defined, and India is not named (S1, S2). Supporting signals:
  - The application form asks "Are you legally authorized to work in the US (or country of your residence)?", which implies hiring in the applicant's own country (S3).
  - A LiveKit Developer Support Engineer role was mirrored by Built In as "Hiring Remotely in India" until 2026-07-25 (S5).
  - A job aggregator lists India among LiveKit's hiring countries (S6, tier 5).
- **Pay vs target:** US$135K–300K plus equity, the same band on every R&D role (S1, S2). Whether this band applies to APJ hires is not stated. Even the bottom of the band is far above 1.5–2 lakh INR per month take-home.
- **Process:** LiveKit publishes nothing official. One candidate report (early 2026, US Software Engineer, anecdotal) describes about 5 weeks: recruiter screen → technical interview including "create a voice agent with sub-500ms latency" → system design ("design a support agent ... and refund them") → take-home (S7).
- **AI policy in interviews:** `unknown`.
- **Fit: `out of reach` (final on years).** The posting requires "6+ years of engineering experience"; the candidate has about 3. A better-matched LiveKit role open to APJ is "Software Engineer, Agents". It states no years and uses Python and TypeScript, but it needs LLM and agent-building experience (S2).

## 2. Hard filters

**(a) India eligibility: `unverified`.**
- Ashby structured data: `location: North America`, `secondaryLocations: APJ, San Francisco, CA (Hybrid), EMEA`, `workplaceType: Remote`, `addressCountry: "APJ"` (S1). The posting says: "This role can be based remotely or in our SF HQ" (S1).
- APJ usually means Asia-Pacific and Japan. Whether LiveKit's APJ includes India, and through which entity or employer-of-record, is not stated in any first-party source.
- Form question: "Are you legally authorized to work in the US (or country of your residence)?" plus "Would you now or in the future require sponsorship support?" (S3). This suggests local hiring, but it is not proof.
- An India-specific LiveKit listing existed earlier in 2026, according to Built In Hyderabad (removed 2026-07-25). That was a support role, not engineering (S5).
- **Action:** ask the recruiter to confirm in writing that India is within "APJ", and how hires there are engaged.

**(b) Live today: `pass`.** The role is in the Ashby job-board API on 2026-10-09 (S1).

**Employment type:** "FullTime". Benefits: "Health, dental, and vision benefits; Flexible vacation policy" (S1). The legal arrangement for India is unknown.

## 3. Current role requirements

| Item | Label | Evidence |
|---|---|---|
| "6+ years of engineering experience, with meaningful time spent shipping product end-to-end" | required | S1 |
| "Strong coding skills in TypeScript, with fluency in modern web frameworks" | required | S1 |
| "Comfort with Go is a plus" | preferred | S1 |
| "A track record of building user-facing software that developers or technical users actually adopted" | required | S1 |
| "Strong product sense: you weigh user experience, trade-offs, and value alongside technical implementation" | required | S1 |
| "Comfort with ambiguity. You can take a vague problem, frame it, and start shipping." | required (autonomy) | S1 |
| "Excellent written and verbal communication" | required | S1 |
| "Genuine excitement about agentic AI, voice, and the next generation of developer platforms" | required (motivation) | S1 |
| Developer platforms, SDKs, CLIs or APIs as the primary product | nice to have | S1 |
| Production distributed systems: "Kubernetes-based deployments, analytics/telemetry, and observability" | nice to have | S1 |
| Open source contributions (infra or developer tools) | nice to have; also asked on the form | S1, S3 |
| Realtime, audio/video or AI tooling background | nice to have | S1 |
| Based in or willing to spend time in the San Francisco Bay Area | nice to have | S1 |
| Engage directly with developers and customers; "prototype to production" | required (responsibility) | S1 |
| Testing, security, performance specifics | not stated ("fast, reliable, and right-sized" code) | S1 |
| AI-assisted development | not stated in engineering postings. An aggregator claims a 2026 LiveKit posting described an "AI-first development environment" with Claude Code; this could not be found on the current board | S2, S6 |
| Compensation | US$135K–300K plus equity (published) | S1 |

**Repeated language across R&D roles (S2):** "Contribute to open source alongside world-class engineers"; developer experience and API design; remote across North America, APJ and EMEA for 6 R&D roles. Only the Senior Product Engineer posting states a years threshold. The stack per the postings is TypeScript and Go for product work, plus Python and TypeScript for the Agents framework.

## 4. Interview stages

No first-party process exists. The only stages listed are from one candidate report.

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Application | Ashby form: why this role, "a project you're proud of", GitHub or LinkedIn link, open-source yes/no, work authorization | — | unknown | motivation, project ownership | official | S3 |
| 1 | Recruiter screen | Call; recruiter gave useful prep guidance | not stated | unknown | background, "Why LiveKit?" | anecdotal | S7 |
| 2 | Technical interview | Practical build: "create a voice agent with sub-500ms latency" | not stated | unknown | realtime voice agents, latency | anecdotal | S7 |
| 3 | System design | "Design a support agent that is able to help customers with their problems and refund them" | not stated | unknown | agent architecture, tool calls, safety | anecdotal | S7 |
| 4 | Take-home | Listed; scope not described | not stated | unknown | — | anecdotal | S7 |

The overall loop took about 5 weeks and was rated "Difficult". The report was for a US onsite Software Engineer role, not Product Engineer, so it may not match this role (S7). An interview guide (S8) presents its stage list as an estimate; it is not used as evidence.

## 5. Stage-by-stage evaluation targets (brief)

- **Application:** The two long-text answers and the GitHub link carry weight. Show a shipped developer-facing feature.
- **Technical build (anecdotal):** Build a small voice agent with the open-source LiveKit Agents framework. Measure end-to-end latency and be able to explain where the time goes.
- **Design (anecdotal):** Practise designing an LLM support agent with tools (refund API), guardrails, human hand-off and observability.
- **Product sense (from the posting):** Prepare opinions on LiveKit Cloud dashboard and CLI developer experience.

## 6. Competency taxonomy (brief)

- **Product engineering:** TypeScript, a modern web framework (React or Next.js inferred), dashboards, CLI developer experience.
- **Platform:** observability and telemetry UIs, Kubernetes basics, Go.
- **AI and realtime:** voice-agent pipelines (speech-to-text, LLM, text-to-speech), latency budgets, WebRTC concepts.
- **Behaviour:** ownership, customer contact, written communication.

## 7. Process changes and history

- No dated first-party process exists, so no changes can be recorded.
- **Company:** US$100M Series C at a US$1B valuation, announced 2026-01-22, led by Index Ventures (S9). An unconfirmed "Series C-1" in August 2026 is reported by one source only and is not used. No layoffs were found.

## 8. Candidate-report findings

| Claim | Label | Source |
|---|---|---|
| Loop is recruiter screen → technical → system design → take-home, about 5 weeks | anecdotal (one report) | S7 |
| A practical voice-agent build with a sub-500 ms latency target | anecdotal (one report; S6 repeats the same report, so it does not corroborate) | S7, S6 |
| A system design question about a support agent issuing refunds | anecdotal | S7 |
| Glassdoor | not fetched (usually 403); search summaries say there are very few reviews | — |

**Applicant pool (inference):** LiveKit is a high-profile AI-infrastructure company (it powers ChatGPT Advanced Voice), with a US$135K–300K band open to three continents. Expect heavy competition.

## 9. Fit check

**Verdict: `out of reach` (hard requirement on years, final).**

| Gap | Evidence |
|---|---|
| "6+ years of engineering experience" required, against about 3 years | S1 |
| Track record of developer-adopted software required; no candidate evidence | S1 |
| No Go, no realtime/voice/WebRTC and no agentic AI work in the profile | S1, S7 |
| India eligibility unverified | S1, S3 |
| Alternative: "Software Engineer, Agents" (APJ, no years stated, Python and TypeScript) requires "Experienced building LLM-based applications and agentic systems". It is a stretch at best and is not researched in depth here. | S2 |

## 10. Exclusions and unknowns

- APJ country list, India legal arrangement and India pay: unknown.
- Official interview stages and AI policy: unknown.
- An India-paid Forward Deployed Engineer listing (INR figures appeared in a search snippet) could not be verified. The page now shows "This role has been filled", closed 2026-10-02. It is not used.

## 11. Source ledger

```yaml
company: "LiveKit"
anchor: false
match:
  hard_filters:
    eligibility: "unverified — locations North America/APJ/EMEA; APJ undefined; India not named; form asks authorization in 'country of your residence' (S3); prior India-remote support listing (S5)"
    hiring_now: "pass — https://jobs.ashbyhq.com/livekit/463e2769-bb85-4429-96a3-3a175eb228cd live 2026-10-09"
  soft_dimensions:
    - dimension: "TypeScript product engineering on developer surfaces"
      evidence: ["S1"]
    - dimension: "published high pay band"
      evidence: ["S1"]
fit:
  verdict: "out of reach"
  preliminary: false
  gaps:
    - gap: "6+ years required vs ~3"
      evidence: ["S1"]
    - gap: "No Go / realtime / voice-agent / agentic AI experience evidenced"
      evidence: ["S1", "S7"]
    - gap: "India eligibility unverified"
      evidence: ["S1", "S3", "S5"]
role:
  title: "Senior Product Engineer"
  url: "https://jobs.ashbyhq.com/livekit/463e2769-bb85-4429-96a3-3a175eb228cd"
  seniority: "senior (6+ years)"
  compensation: "US$135K–300K + equity (band not stated as location-specific)"
  verified_date: "2026-10-09"
process:
  url: ""
  verified_date: "2026-10-09"
  stages:
    - id: "P0"
      name: "Application"
      format: "Ashby form with two long-text answers, GitHub/LinkedIn, OSS yes/no, work authorization"
      timebox: "n/a"
      ai_policy: "unknown"
      competencies: ["motivation", "project ownership"]
      evidence_quality: "official"
      sources: ["S3"]
    - id: "P1"
      name: "Recruiter screen"
      format: "call"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["background", "why LiveKit"]
      evidence_quality: "anecdotal"
      sources: ["S7"]
    - id: "P2"
      name: "Technical interview"
      format: "practical build: voice agent with sub-500ms latency"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["realtime voice agents", "latency"]
      evidence_quality: "anecdotal"
      sources: ["S7"]
    - id: "P3"
      name: "System design"
      format: "design a support agent that resolves problems and issues refunds"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: ["agent architecture", "tool use", "safety"]
      evidence_quality: "anecdotal"
      sources: ["S7"]
    - id: "P4"
      name: "Take-home"
      format: "not described"
      timebox: "not stated"
      ai_policy: "unknown"
      competencies: []
      evidence_quality: "anecdotal"
      sources: ["S7"]
  changes: []
requirements:
  explicit_required: ["6+ years engineering", "strong TypeScript + modern web frameworks", "developer-adopted user-facing software", "product sense", "comfort with ambiguity", "excellent written/verbal communication", "excitement about agentic AI/voice"]
  explicit_preferred: ["Go", "developer platforms/SDKs/CLIs/APIs", "production distributed systems (Kubernetes, telemetry, observability)", "open source", "realtime/audio/video/AI tooling", "Bay Area presence"]
  inferred_repeated: ["open source contribution", "developer experience / API design", "remote NA/APJ/EMEA"]
  ai_expectations: ["enthusiasm for agentic AI products (posting); no explicit AI-coding-tool expectation found"]
uncertainty:
  - claim: "India is inside LiveKit's APJ hiring region"
    reason: "APJ undefined; only indirect signals (form wording, removed India support listing, tier-5 aggregator)"
    confidence: "low"
  - claim: "Interview stages"
    reason: "Single candidate report for a different SWE role"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://jobs.ashbyhq.com/livekit/463e2769-bb85-4429-96a3-3a175eb228cd"
    title: "Senior Product Engineer (Ashby posting, via posting API)"
    tier: 1
    published_or_updated: "2026-05-23"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["requirements", "locations", "pay band"]
  - id: "S2"
    url: "https://api.ashbyhq.com/posting-api/job-board/livekit?includeCompensation=true"
    title: "LiveKit Ashby job board API (29 postings)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["repeated language", "APJ roles", "Software Engineer, Agents alternative"]
  - id: "S3"
    url: "https://jobs.ashbyhq.com/livekit/463e2769-bb85-4429-96a3-3a175eb228cd/application"
    title: "Application form (Ashby, via public GraphQL)"
    tier: 1
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["authorization question wording", "application questions"]
  - id: "S4"
    url: "https://livekit.com/careers"
    title: "LiveKit careers"
    tier: 1
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["'Engineered and designed worldwide'; no process or pay"]
  - id: "S5"
    url: "https://builtinhyderabad.in/job/developer-support-engineer/8795755"
    title: "LiveKit Developer Support Engineer (Built In Hyderabad mirror)"
    tier: 4
    published_or_updated: "removed 2026-07-25"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["LiveKit has hired 'remotely in India' for at least one role"]
  - id: "S6"
    url: "https://matcha.fm/company/livekit"
    title: "LiveKit Careers: Remote Jobs, Culture and Where They Hire (Matcha)"
    tier: 5
    published_or_updated: "unknown (pay data 'as of September 2026')"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["lead only: lists India among hiring countries; repeats S7"]
  - id: "S7"
    url: "https://www.aced.io/experiences/livekit-software-engineer-interview-00f76f"
    title: "LiveKit Software Engineer interview report (Aced, formerly Exponent)"
    tier: 4
    published_or_updated: "submitted ~5 months before capture; interview ~early 2026"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["anecdotal stages", "voice-agent build", "support-agent design"]
  - id: "S8"
    url: "https://www.techinterview.org/companies/livekit-interview-guide/"
    title: "LiveKit Interview Guide (2026) (techinterview.org)"
    tier: 5
    published_or_updated: "2026 (no exact date)"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["self-described estimate; not used as evidence"]
  - id: "S9"
    url: "https://fortune.com/press-releases/livekit-raises-100m-1b-valuation-voice-first-computing-2026-01-22"
    title: "LiveKit raises $100M at $1B valuation (press release)"
    tier: 2
    published_or_updated: "2026-01-22"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Series C funding"]
```
