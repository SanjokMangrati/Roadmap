# Metabase: Software Engineer (Frontend), plus Software Engineer (Backend)

Researched and verified 2026-10-09.

## 1. Summary

- **Role:** Software Engineer (Frontend), Lever posting first created 2020-05-11. It is an evergreen "multiple positions" posting that is still live today (S1, S2). A sibling posting, Software Engineer (Backend), is also live. **The backend is Clojure**, which the candidate has never used (S3).
- **Eligibility: `unverified`.** Both postings are tagged "Global Remote". The company text says "define your own schedule and work from wherever you want", and "50% outside the US" (S2, S3). No first-party source names India, gives a country list, or says whether non-US hires are employees, employer-of-record (EOR) hires or contractors. One aggregator labels the roles "United States only" (S22), which conflicts with the "Global Remote" tag. The Lever API also shows a default `country: US` field on every posting (S1).
- **Pay vs target:** The US base range is $110K–$210K plus equity. Metabase says "Pay may vary by geographic location" (S2), and **non-US pay is not published.** Any plausible location-adjusted figure would likely be well above the ₹1.5–2 lakh/month take-home target. That is an inference, not data.
- **Process shape:** **No first-party page describes the hiring process.** metabase.com/jobs has no process text, and the handbook and "how-we-hire" URLs return 404 (S10). Candidate reports (Glassdoor, read through search snippets only, anecdotal) describe this sequence: ~30-min coding screen in your own environment, three 1-hour panels (algorithms, React or business logic, architecture or system design), a take-home project, a CEO chat, then the offer (S15–S17). A Metabase GitHub repo, `interview-fe-boilerplate`, created 2019-05-22 (React plus Parcel), backs up the "coding exercise in your own environment" report for frontend (S11).
- **AI policy in interviews: `unknown`.** Metabase discloses that it "may use artificial intelligence (AI) tools to support parts of the hiring process" for screening (S6). Engineering uses AI agents heavily: the main repo has had a `CLAUDE.md` since 2025-04-08 and a `.claude/skills` directory, both updated in October 2026 (S13).
- **Fit: `stretch` (preliminary) for Frontend; `out of reach` in practice for Backend unless the candidate commits to Clojure.** The main gaps are algorithm and data-structure rounds and live architecture defense, which are the candidate's stated weak areas. Eligibility also stays unconfirmed.

## 2. Hard filters

**(a) India eligibility: `unverified`.**
- The Frontend and Backend postings both carry the location "Global Remote" and the commitment "Full-time (remote)" (S1, S2, S3).
- The shared company text says: "We're a global team (50% outside the US), fully distributed (from Thailand to California)… We offer flexibility (define your own schedule and work from wherever you want)" (S2).
- The Engineering Manager posting says: "We're a fully remote global team (in 30 countries and growing)" (S5). The CI Engineer posting (2026-04-21) says: "Fully remote, any timezone — we're serious about async-first culture" (S4).
- The Lever board's location filters are Global Remote, Remote-EU, Remote-North & South America and Remote-US (S6). Some roles are restricted. For example, Analytics Engineer requires "Candidates who operate in UTC-3 -- UTC-8" (S9). The SWE roles carry no such restriction.
- **India is not named anywhere.** I found no country list, no EOR or contractor wording, and no non-US benefits description. The benefits text describes only "a comprehensive US benefits package" (S2).
- Conflict: Himalayas (tier 5) lists both SWE roles as "United States only" (S22). This is probably derived from Lever's default `country: "US"` field, which every Metabase posting carries, including ones explicitly scoped to the EU (S1). The first-party "Global Remote" tag wins, but the conflict stays open until a recruiter confirms India.
- **Employment type for non-US hires: not stated.** "Full-time (remote)" is the only label. Whether India hires are employees, EOR hires or contractors is unknown.

**(b) Live today: `pass`.** Both postings are in the Lever API and return HTTP 200 on 2026-10-09 (S1, S2, S3). Caveat: they were created in May 2020 and are evergreen. A live posting does not prove there is an active req for this quarter.

## 3. Current role requirements

**Software Engineer (Frontend) (S2)**

| Item | Label |
|---|---|
| "Prior experience shipping non-trivial apps using React + Redux (or equivalent)… really strong React and JavaScript knowledge" | required |
| "You've worked on a large and complex JavaScript project… ability to adapt existing code and integrate new code into established systems" | required |
| "experience writing tests, giving good feedback on other people's code, and writing proposals for more complicated problems" | required |
| "computer science-y problems come up frequently… write fast and performant code and deal with a fair bit of data structure manipulation regularly" | required (signals algorithm and data-structure evaluation) |
| "comfort in CSS and familiarity with things like design systems and component libraries is a necessity" | required |
| Product and UX care: "If your focus is only on code this might not be the best role for you" | required |
| Data visualization experience (dc.js, d3.js) | nice to have |
| Open-source contributions | nice to have ("a huge plus") |
| Interest in learning Clojure | nice to have |
| Years of experience | not stated |
| Compensation: "US base salary range… $110K–$210K annually, plus equity and benefits"; "Pay may vary by geographic location" | published (US only) |

**Software Engineer (Backend) (S3)**

| Item | Label |
|---|---|
| "Experience in Clojure (or a strong desire to learn)" | required (learnable, per wording) |
| "We run on a mix of Clojure and JavaScript (and TypeScript)… ship major features end to end across our JavaScript and Clojure codebase" | required |
| "Track record of shipping products of significant complexity" | required |
| "Solid CS background (acquired through either a CS program or shipping software in a production setting)" | required |
| "Able to make good technical judgements and back them up articulately" | required |
| JDBC and database integrations; Java ecosystem and JVM tuning; open source; JS/TS | nice to have |
| Machine learning, compiler theory, big-data infrastructure "would be helpful" | nice to have |
| Compensation: US base $110K–$210K plus equity | published (US only) |

**Repeated language across Metabase engineering postings (S2–S5, S7, S8)** (`inferred from repeated job language`):
- Async written communication and clarity: "communication and clarity are really important" (Frontend); "Strong async written communication skills" (CI); "bias to written communication" (Engineering Manager).
- Defending decisions: "make good technical judgements and back them up articulately" appears in both the Backend and Senior SRE postings.
- Ownership and autonomy without close supervision (CI Engineer, Technical Product Lead).
- Product sensibility and user focus ("relentlessly user-focused") in every posting.
- Stack named across postings: Clojure, TypeScript and React; Cypress, Jest and Clojure test frameworks; GitHub Actions; Docker; a broad database matrix (PostgreSQL, MySQL, Snowflake, BigQuery, Redshift); AWS, Kubernetes and Terraform for Metabase Cloud.

**First-party stack evidence (S12):**
- GitHub language bytes: Clojure 58.0M, TypeScript 38.8M, JavaScript 4.3M.
- `package.json` pins React 18.2, Redux 5 with Redux Toolkit 2.x, Mantine 8, TypeScript 6.0, Rspack 2 alongside webpack 5, ECharts 6, d3 7, Jest 30 and Cypress 15.

**AI-assisted development (`inferred`, not in the SWE postings):**
- The root `CLAUDE.md` routes agents to `.claude/skills` for Clojure REPL evaluation, TypeScript writing and review, and docs. Its first commit was 2025-04-08 and its latest was 2026-10-02; the skills directory changed on 2026-10-08 (S13).
- The repo also has `.coderabbit.yaml` (AI code review) (S12).
- The SWE postings, written in 2020, say nothing about AI. A September 2026 non-engineering posting asks for "fluency with AI tools and know when to apply them" (S1, Marketing Programs & Operations).

## 4. Interview stages

No first-party process document exists. Every stage below is from candidate reports, so the evidence quality is anecdotal.

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 0 | Application and AI-assisted screening | Lever form; Metabase "may use… AI tools to support… reviewing applications, analyzing resumes… identifying potential inconsistencies" | n/a | unknown for candidate (company uses AI in screening) | résumé fit, consistency | official (disclosure only) | S6 |
| 1 | Initial call with team member and quick coding exercise | Video call; code in your own dev environment (one frontend candidate used Node.js); some report LeetCode easy/medium | ~30 min (20 min coding reported) | unknown | basic coding fluency, algorithms | anecdotal | S11, S15, S16 |
| 2 | Three technical panels | 3 × 1-hour live panels. Frontend: "architectural design", "React programming", "more algorithmic programming". Another SWE report: "algo coding, business logic coding, system design". Backend: two database panels plus LeetCode-medium | 3 × 60 min | unknown | React depth, algorithms and data structures, system or architecture design, databases (backend) | anecdotal | S15, S16 |
| 3 | Take-home project | Practical project ("a practical problem you might actually face on the job", from an Engineering Manager report); one report ~3.5 h | ~3.5 h reported, not confirmed | unknown | real-world engineering, code quality, communication | anecdotal | S15, S17 |
| 4 | CEO chat | 1:1 with CEO (sometimes also VP Engineering) | unknown | unknown | values, product thinking, motivation | anecdotal | S15, S17 |
| 5 | Offer | not documented | — | — | — | not sourced | — |

Process length reports: Glassdoor estimates an average of 41 days to hire for SWE (4 submissions). Several reviewers call the process long, opaque and slow to give feedback (S15, S17).

## 5. Stage-by-stage evaluation targets

1. **Application:** Lead with a large React/TypeScript codebase you adapted, not greenfield work. Show product and UX care, tests and code review (S2). Assume AI screening checks consistency between résumé and answers (S6).
2. **Coding screen:** Have a local React and TypeScript scaffold ready, because the exercise runs in your own environment (S11, S16). Practise LeetCode easy/medium array, hash-map and string problems while narrating your approach aloud. This directly targets the candidate's weakness.
3. **Panels:**
   - React: rendering and performance, state management (Redux Toolkit), and building data-heavy UI such as tables, filters and charts (S2, S12).
   - Algorithms: medium-level data-structure manipulation (S2 "data structure manipulation regularly").
   - Architecture: design a frontend feature end to end and defend the tradeoffs. One example is drill-through on a chart or dashboard filters with embedded analytics theming (S2 "types of problems"). Another is a query-builder state model.
   - Backend variant: SQL and database design.
4. **Take-home:** Treat it as production code. Include tests, a README with tradeoffs and clean commits. Written clarity counts (S2 "writing proposals… thoughtful and clear").
5. **CEO chat:** Know the product (open-source BI, embedded analytics, Metabase AI). Have a view on what makes data tools usable, and explain why async remote work suits you.

## 6. Competency taxonomy

- **Frontend engineering:** React 18 hooks and rendering; Redux and Redux Toolkit; TypeScript; CSS, design systems and Mantine-style component libraries; data visualization (ECharts, d3); performance on large datasets; testing with Jest, React Testing Library and Cypress.
- **CS fundamentals:** arrays, maps, trees, sorting and searching; complexity analysis; data transformation (pivoting, grouping).
- **System and architecture design:** frontend state architecture; API contracts with a Clojure backend; embedding and SDK design; trade-off articulation.
- **Backend (Backend role only):** Clojure, the JVM, JDBC, SQL across many databases, query compilation (the "compiler theory" hint).
- **Product sense:** UX details, copy, user workflows in BI.
- **Async written communication:** proposals, code-review feedback, status updates without prompting.
- **AI-assisted development:** working inside an agent-configured repo (CLAUDE.md, skills). This is inferred.

## 7. Process changes and history

- **2019-02-16:** The CEO's Discourse post for Software Engineer lists "Experience in Clojure or a strong desire to learn", "Solid CS background", and "History of open source contributions strongly preferred". It gives no process (S14). Stale.
- **2019-05-22:** Metabase created the public repo `metabase/interview-fe-boilerplate` (React 16 plus Parcel, "Hello world"). This is the only first-party interview artifact found. Its last push was 2019-05-22, so it may no longer be used (S11).
- **2020-05-11 / 2020-05-19:** The current Frontend and Backend postings were created. The wording still references React + Redux "(or equivalent)", which reflects their 2020 origin (S1).
- **2021-06-17:** The Engineering Manager posting gives "30 countries" (S5).
- **2026-04-21:** The CI Engineer posting gives "engineering team of ~70 people" and "Fully remote, any timezone" (S4).
- **Undated (observed 2026-10-09):** The Lever board added an AI-in-hiring disclosure (S6). AI-driven: yes, on the screening side.
- **No dated official change to the interview loop was found.**

## 8. Candidate-report findings

Glassdoor returned HTTP 403 to direct fetches, so the content below comes from search-engine snippets and summaries of Glassdoor pages. Review dates are partly unclear in those snippets. No Reddit, Blind or LeetCode Discuss threads about Metabase were found.

- **Short coding screen, then three 1-hour panels:** `corroborated (weakly)`. Several SWE and Frontend reports describe this shape (S15, S16).
- **Algorithm content at LeetCode easy/medium:** `anecdotal`. One or two reports; one says "at or slightly below LeetCode Medium" (S15).
- **Frontend panel topics (architecture, React, algorithms):** `anecdotal`. One report (S16).
- **Take-home after the panels:** `corroborated` across roles (SWE, Engineering Manager, Success Engineer, Product Manager) (S15, S17). Length for engineering is `anecdotal` (~3.5 h).
- **Final CEO conversation:** `corroborated` across roles (S15, S17).
- **Long, opaque process with little feedback:** `corroborated` (several reviewers) (S15, S17).
- **"Canned" screening question:** `anecdotal`. One Frontend reviewer (S16).

## 9. Fit check

**Verdict (Frontend): `stretch`, preliminary.** Eligibility is `unverified`, so it is not final.
- **Gap: algorithm rounds.** Data-structure manipulation is explicitly required, and LeetCode easy/medium rounds are reported (S2, S15). The candidate's algorithm skill is unmeasured.
- **Gap: live architecture defense.** An architecture or system design panel is reported, and "back them up articulately" recurs across postings (S3, S7, S16). These are the candidate's self-reported weak areas.
- **Gap: Redux and data-visualization depth.** Next.js experience does not cover the Redux Toolkit or ECharts and d3 work in Metabase's frontend (S2, S12).
- **Strength:** 3 years of React and Node match the "large and complex JavaScript project" requirement on paper. The posting states no minimum years (S2).
- **Competition (inference):** a 49.6k-star open-source product (S10), an evergreen posting since 2020 and "Global Remote" scope suggest a crowded pool. No applicant counts were found.

**Verdict (Backend): `out of reach`, preliminary.** The candidate has no Clojure, JVM or JDBC experience. The posting's "strong desire to learn" softens the requirement, but "ship major features end to end across our JavaScript and Clojure codebase" plus database panels make it unrealistic within 20 days (S3, S15).

**Company signals:**
- Funding: "$30M Series B" (S2), dated May 2021 and led by Insight Partners per Clay (S21, tier 5).
- Headcount: about 119 in March 2026, up about 2% year on year, per Revelio (S19, tier 5).
- No known layoffs (S20, tier 5).
- Pay data: Levels.fyi has US-only data, with a median SWE total compensation of about $209K (S18). There is no India data.

## 10. Exclusions and unknowns

- **India eligibility and employment vehicle:** unknown. Confirm with the recruiter before investing prep time.
- **How Metabase pays outside the US:** unknown. The postings say only that pay "may vary by geographic location" (S2).
- **No first-party hiring-process page, blog post or handbook was found.** The only first-party interview artifact is the 2019 boilerplate repo (S11).
- AI-tool rules for the coding screen and take-home: unknown.
- Take-home length and topic for engineering: not confirmed.
- The Glassdoor content could not be fetched directly. All Glassdoor-derived claims are snippet-level.

## 11. Source ledger

```yaml
company: "Metabase"
anchor: false
match:
  hard_filters:
    eligibility: "unverified - postings say 'Global Remote' and 'work from wherever you want', team '50% outside the US', '30 countries'; India not named; no EOR/contractor info; Himalayas says 'United States only' (conflict, likely Lever default country field)"
    hiring_now: "pass - https://jobs.lever.co/metabase/8f02d3fa-edf4-4433-a6d1-4f9e517ac8f9 live in Lever API 2026-10-09 (evergreen since 2020-05-11)"
  soft_dimensions:
    - dimension: "React/TypeScript frontend, large codebase"
      evidence: ["S2", "S12"]
    - dimension: "async-first written communication"
      evidence: ["S2", "S4", "S5"]
    - dimension: "open source"
      evidence: ["S2", "S12"]
    - dimension: "AI-assisted development culture (inferred)"
      evidence: ["S13"]
fit:
  verdict: "stretch (Frontend); out of reach (Backend, Clojure)"
  preliminary: true
  gaps:
    - gap: "Algorithm/data-structure rounds (LeetCode easy/medium reported)"
      evidence: ["S2", "S15"]
    - gap: "Live architecture/system-design defense"
      evidence: ["S3", "S7", "S16"]
    - gap: "Redux Toolkit and data-visualization depth"
      evidence: ["S2", "S12"]
    - gap: "Clojure/JVM for backend role"
      evidence: ["S3"]
    - gap: "India eligibility unconfirmed"
      evidence: ["S1", "S2", "S22"]
role:
  title: "Software Engineer (Frontend)"
  url: "https://jobs.lever.co/metabase/8f02d3fa-edf4-4433-a6d1-4f9e517ac8f9"
  seniority: "not stated; 'multiple positions'; US base range implies mid-to-senior"
  compensation: "US base $110K-$210K + equity; non-US pay not published; 'Pay may vary by geographic location'"
  verified_date: "2026-10-09"
process:
  url: "none first-party; https://jobs.lever.co/metabase (AI screening disclosure only)"
  verified_date: "2026-10-09"
  stages:
    - id: "P0"
      name: "Application + AI-assisted screening"
      format: "Lever application; AI tools may review applications"
      timebox: "n/a"
      ai_policy: "unknown"
      competencies: ["resume fit"]
      evidence_quality: "official"
      sources: ["S6"]
    - id: "P1"
      name: "Initial call + quick coding exercise"
      format: "video call, coding in own dev environment"
      timebox: "~30 min"
      ai_policy: "unknown"
      competencies: ["coding fluency", "algorithms"]
      evidence_quality: "anecdotal"
      sources: ["S11", "S15", "S16"]
    - id: "P2"
      name: "Three technical panels"
      format: "3 x 1h live: architecture/system design, React or business-logic coding, algorithms (backend: databases)"
      timebox: "3 x 60 min"
      ai_policy: "unknown"
      competencies: ["React", "algorithms", "system design", "databases"]
      evidence_quality: "anecdotal"
      sources: ["S15", "S16"]
    - id: "P3"
      name: "Take-home project"
      format: "practical take-home"
      timebox: "~3.5 h reported"
      ai_policy: "unknown"
      competencies: ["practical engineering", "code quality", "written communication"]
      evidence_quality: "anecdotal"
      sources: ["S15", "S17"]
    - id: "P4"
      name: "CEO chat"
      format: "1:1 conversation"
      timebox: "unknown"
      ai_policy: "unknown"
      competencies: ["values", "product thinking"]
      evidence_quality: "anecdotal"
      sources: ["S15", "S17"]
  changes:
    - date: "2019-05-22"
      change: "Public interview-fe-boilerplate repo created (React 16 + Parcel) for frontend coding exercise in own environment"
      ai_driven: false
      sources: ["S11"]
    - date: "undated (observed 2026-10-09)"
      change: "Lever board discloses AI tools may be used to review applications and detect inconsistencies"
      ai_driven: true
      sources: ["S6"]
requirements:
  explicit_required: ["strong React + JavaScript (React+Redux or equivalent)", "large complex JS codebase experience", "tests, code review, written proposals", "performant code and data-structure manipulation", "CSS, design systems, component libraries", "product/UX care"]
  explicit_preferred: ["data visualization (d3/dc.js)", "open-source contributions", "interest in Clojure"]
  inferred_repeated: ["async written communication", "defend technical judgements articulately", "ownership/autonomy", "user focus"]
  ai_expectations: ["none stated in SWE postings; repo has CLAUDE.md + .claude/skills since 2025-04 (inferred AI-agent workflow)"]
uncertainty:
  - claim: "India-based hire allowed"
    reason: "Only 'Global Remote' wording; no country list; aggregator says US-only"
    confidence: "medium"
  - claim: "Interview loop shape"
    reason: "Only Glassdoor snippets via search; direct fetch blocked; no first-party process page"
    confidence: "low"
  - claim: "Non-US pay level"
    reason: "Not published; Levels.fyi has US data only"
    confidence: "low"
sources:
  - id: "S1"
    url: "https://api.lever.co/v0/postings/metabase?mode=json"
    title: "Metabase Lever postings API (18 postings)"
    tier: 1
    published_or_updated: "createdAt per posting; FE 2020-05-11, BE 2020-05-19"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["live postings", "Global Remote tag", "country field US default", "creation dates"]
  - id: "S2"
    url: "https://jobs.lever.co/metabase/8f02d3fa-edf4-4433-a6d1-4f9e517ac8f9"
    title: "Software Engineer (Frontend)"
    tier: 1
    published_or_updated: "created 2020-05-11; live 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["requirements", "US pay range", "global team text", "Series B"]
  - id: "S3"
    url: "https://jobs.lever.co/metabase/85f454d8-e795-4978-8a2b-4b8bfa7d7c37"
    title: "Software Engineer (Backend)"
    tier: 1
    published_or_updated: "created 2020-05-19; live 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["Clojure backend", "back up judgements articulately", "US pay range"]
  - id: "S4"
    url: "https://jobs.lever.co/metabase/ee8203b5-2cf7-4eae-afd6-3f9724761ad9"
    title: "CI Engineer"
    tier: 1
    published_or_updated: "2026-04-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["~70 engineers", "any timezone", "async written comms", "test stack"]
  - id: "S5"
    url: "https://jobs.lever.co/metabase/5bf3233d-a162-47b2-8d85-d3650b176c6e"
    title: "Engineering Manager"
    tier: 1
    published_or_updated: "2021-06-17"
    accessed: "2026-10-09"
    freshness: "current (live)"
    supports: ["30 countries", "bias to written communication"]
  - id: "S6"
    url: "https://jobs.lever.co/metabase"
    title: "Metabase Lever job board (AI-in-hiring disclosure, location filters)"
    tier: 1
    published_or_updated: "undated"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["AI screening disclosure", "location filter set"]
  - id: "S7"
    url: "https://jobs.lever.co/metabase/1b702919-4d0b-4085-baec-8947f9b7e4ee"
    title: "Senior SRE/DevOps Engineer"
    tier: 1
    published_or_updated: "2020-05-11"
    accessed: "2026-10-09"
    freshness: "current (live)"
    supports: ["repeated 'back them up articulately'", "AWS/Kubernetes/Terraform"]
  - id: "S8"
    url: "https://jobs.lever.co/metabase/428505ba-d14f-4675-832f-385af863093e"
    title: "Technical Product Lead"
    tier: 1
    published_or_updated: "2026-04-21"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["autonomy", "product led by CEO"]
  - id: "S9"
    url: "https://jobs.lever.co/metabase/5eca795c-48dd-496a-be23-2181068a5450"
    title: "Analytics Engineer (UTC-3 to UTC-8 restriction)"
    tier: 1
    published_or_updated: "2020-11-19"
    accessed: "2026-10-09"
    freshness: "current (live)"
    supports: ["some roles timezone-restricted; SWE roles not"]
  - id: "S10"
    url: "https://www.metabase.com/jobs"
    title: "Work at Metabase"
    tier: 1
    published_or_updated: "(c) 2026"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["no process info", "49.6k GitHub stars in header", "/handbook and /blog/how-we-hire return 404"]
  - id: "S11"
    url: "https://github.com/metabase/interview-fe-boilerplate"
    title: "metabase/interview-fe-boilerplate"
    tier: 2
    published_or_updated: "created 2019-05-22; last push 2019-05-22"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["frontend coding exercise in own environment"]
  - id: "S12"
    url: "https://github.com/metabase/metabase"
    title: "metabase/metabase repo (languages API, package.json, root files)"
    tier: 2
    published_or_updated: "master as of 2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["tech stack", ".coderabbit.yaml"]
  - id: "S13"
    url: "https://github.com/metabase/metabase/blob/master/CLAUDE.md"
    title: "Metabase Development Guide (CLAUDE.md) and .claude/skills"
    tier: 2
    published_or_updated: "first commit 2025-04-08; last 2026-10-02; skills 2026-10-08"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["AI-agent development workflow (inferred expectation)"]
  - id: "S14"
    url: "https://discourse.metabase.com/t/software-engineer-at-metabase/5447"
    title: "Software Engineer at Metabase (post by sameer)"
    tier: 2
    published_or_updated: "2019-02-16"
    accessed: "2026-10-09"
    freshness: "stale"
    supports: ["historic requirements"]
  - id: "S15"
    url: "https://www.glassdoor.com/Interview/Metabase-CA-Software-Engineer-Interview-Questions-EI_IE6095700.0,11_KO12,29.htm"
    title: "Metabase (CA) Software Engineer interview reviews (via search snippets; direct fetch 403)"
    tier: 4
    published_or_updated: "2025-2026 per page title; individual dates unclear"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["screen + 3 panels + take-home + CEO", "LeetCode easy/medium", "41-day average"]
  - id: "S16"
    url: "https://www.glassdoor.com/Interview/Metabase-CA-Software-Engineer-Frontend-Interview-Questions-EI_IE6095700.0,11_KO12,38.htm"
    title: "Metabase (CA) Software Engineer Frontend interview reviews (via search snippets; direct fetch 403)"
    tier: 4
    published_or_updated: "dates unclear (one snippet says June 2026)"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["coding exercise in own environment", "architecture/React/algorithms panels", "'canned' question"]
  - id: "S17"
    url: "https://www.glassdoor.com/Interview/Metabase-CA-Interview-Questions-E6095700.htm"
    title: "Metabase (CA) interview reviews, all roles (via search snippets)"
    tier: 4
    published_or_updated: "2026 per page title"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["take-home + CEO across roles", "slow/opaque process"]
  - id: "S18"
    url: "https://www.levels.fyi/companies/metabase/salaries/software-engineer"
    title: "Levels.fyi Metabase Software Engineer salaries"
    tier: 4
    published_or_updated: "2026-10-09"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["US median ~ $209K; no India data"]
  - id: "S19"
    url: "https://www.reveliolabs.com/companies/metabase/employees"
    title: "Revelio Labs Metabase headcount"
    tier: 5
    published_or_updated: "2026-03"
    accessed: "2026-10-09"
    freshness: "current"
    supports: ["~119 employees"]
  - id: "S20"
    url: "https://trueup.io/co/metabase"
    title: "TrueUp Metabase"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["no known layoffs"]
  - id: "S21"
    url: "https://www.clay.com/dossier/metabase-funding"
    title: "How Much Did Metabase Raise?"
    tier: 5
    published_or_updated: "unknown"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["Series B May 2021, Insight Partners"]
  - id: "S22"
    url: "https://himalayas.app/companies/metabase/jobs"
    title: "Himalayas Metabase jobs"
    tier: 5
    published_or_updated: "relative dates only"
    accessed: "2026-10-09"
    freshness: "unknown"
    supports: ["conflict: lists SWE roles as United States only"]
```
