# Company landscape: remote full-stack roles workable from India

Generated 2026-10-09. Inputs: `candidate-profile.md` (confirmed 2026-10-09), `market-context.md`, `company-matrix.csv`, and one file per company in `requirements/`. Fit verdicts on skill gaps are **preliminary**: they rest on self-reported depth and are replaced by the assessment in `finite-interview-curriculum`.

## 1. Outcome

- **3 realistic roles, all verified as open to India-based remote work:** Hyperproof (Software Engineer, Risk Management; ₹21.4–30 lakh published), HighLevel (SDE II Full-stack, CRM and Contacts teams; 13 India-remote SDE II/III openings), Drivetrain (Frontend Engineer, India).
- **5 stretch roles:** Gather AI and Dscout (India-remote verified), plus Infisical, Metabase and Automattic, where India eligibility is conflicting, unverified or not named and must be confirmed with a recruiter before investing preparation time.
- **Reach list:** Railway is a stretch (senior title, anywhere-in-the-world posting); Supabase has no React/Next.js role open; LiveKit, Tarteel AI and vidIQ require 5–6+ years and are out of reach.
- **The market finding that most changes the plan:** India access, not skills, is the binding filter. Only 22 of 197 non-staff full-stack/frontend postings (11%) on 148 startup and scale-up boards were open beyond named non-India regions (M1, 2026-10-09). The realistic roles are concentrated in less-famous companies with explicit India postings, which also fits the goal of avoiding the most crowded applicant pools.

## 2. Candidate summary

India-based full-stack engineer with about 3 years' professional experience (React/Next.js, Node/NestJS, PostgreSQL, GCP; AI-assisted coding; all self-reported and unmeasured). Targets mid-level remote roles at US/EU seed-to-scale-up companies; employee, employer-of-record or contractor all acceptable; no timezone limits. Take-home target ₹1.5–2 lakh per month. Interview-ready by 2026-10-29 at about 7 hours per day. Stated weak areas: explaining thought process aloud, and explaining and defending architecture decisions. Free resources only.

## 3. Matching method

1. **Candidate pool.** 148 company ATS boards (Greenhouse, Ashby, Lever) probed from three hand-built lists of remote-friendly startups, scale-ups, open-source and developer-tool companies; plus the Himalayas public search API filtered to `country=India` with 10 full-stack/TypeScript queries. Indian IT-services and staffing firms were excluded because they pay services-market rates and are not US/EU product companies.
2. **Hard filters.** (a) India-based remote work allowed for the specific role, checked against the first-party posting text, location tags and application questions; (b) a live first-party posting on 2026-10-09 (all 14 role URLs returned HTTP 200 on 2026-10-09; Hyperproof's site blocks scripted requests, so its posting was confirmed through the Greenhouse API instead).
3. **Soft dimensions** (weights from the profile): stack overlap (TypeScript, React, Node, PostgreSQL); mid-level band (2–5 years); fully remote and asynchronous; seed to late-stage private; pay against the take-home target; interview style against stated weak areas; AI posture; hiring trajectory; and smaller brand prominence as a proxy for a less crowded applicant pool (inference; no applicant counts exist).
4. **Match rule.** Pass both hard filters plus at least two evidenced soft dimensions.
5. **Deep research.** Each shortlisted company was researched against first-party postings, company hiring pages, engineering sources (GitHub, blogs) and candidate reports; details and source ledgers are in `requirements/<company>.md`.

## 4. Shortlist with match rationale

Ordered by verdict tier, not ranked within tiers.

### Realistic

**Hyperproof — Software Engineer, Risk Management** ([posting](https://hyperproof.io/job-listings/?gh_jid=4708360005), updated 2026-09-24)
- Eligibility: "This role is open to candidates based in India." Fully remote.
- Pay: ₹21.37–30 lakh per year, published first-party; meets the target (about ₹1.6–2.1 lakh per month take-home as an employee).
- Stack: React, TypeScript, one of Java Spring Boot / Node.js / Python, PostgreSQL, REST; 3–5 years.
- Stage: Series B ($40M, 2023), compliance (governance, risk and compliance) SaaS.
- Gaps: an application screening question asks for "4+ years … React … and Java (Spring Boot)", conflicting with the posting's 3–5 years; C#/.NET in duties; compliance domain preferred; Azure.
- Process: take-home (Coderbyte per an older posting) → 30-minute talent-partner call → three 60-minute one-to-ones including the hiring manager (official for a sibling role, applied here by inference). AI policy unknown.
- Caution: a third-party headcount estimate fell from 221 to 195; one 2025 report says hiring paused after interviews.

**HighLevel — SDE II (Fullstack) Contacts / SDE II CRM** ([Contacts](https://jobs.lever.co/gohighlevel/254ef24c-ff4b-42c9-8b43-603e55e650a3), [CRM](https://jobs.lever.co/gohighlevel/92002249-671d-4d08-96b0-e87c1d6082cb), posted 2026-09-16/17)
- Eligibility: Lever location India, workplace remote, commitment "Employee India".
- Volume: 13 India-remote SDE II/III engineering postings live (4 SDE II, 9 SDE III; SDE III asks 4+ years).
- Domain: direct CRM overlap (Contacts team owns tags, notes, files, segmentation); the candidate built a CRM.
- Stack: Node/TypeScript, NestJS, Vue 3 (React accepted at SDE II), MongoDB/Firestore, Redis, Elasticsearch, GCP (GKE, Pub/Sub, Cloud Tasks).
- AI: the CRM posting requires an "AI-native builder" who codes with agents daily.
- Pay: not published; Glassdoor snippet estimate for SDE II about ₹22 lakh (25th–75th percentile ₹16.5–34 lakh); typical offer at or slightly below the target (inference).
- Process (corroborated candidate reports 2024–2026): recruiter screen → 30-minute past-work call → about 1-hour timed machine-coding round building a working API → about 2-hour high-level design plus past experience → HR. AI tools reportedly allowed in the build round (anecdotal, two reports).

**Drivetrain — Frontend Engineer (India)** ([posting](https://jobs.lever.co/drivetrain/cd39cc4e-056e-444c-8c17-9f97e34ddbce))
- Eligibility: Lever workplace type remote, location India; "remote-first company headquartered in the San Francisco Bay Area".
- Band: 1–3 years React plus data structures; data-visualisation and spreadsheet-style components.
- Stage: Series A ($15M, October 2022), FP&A SaaS, US headquarters.
- Pay: not published; Levels.fyi median about $28,300 total compensation (about ₹24–25 lakh), low end of target.
- Process (corroborated): live data-structures-and-algorithms coding on Google Meet (stack problems, recursion, knapsack); some loops add low-level and high-level design. No take-home.
- Caution: postings created in 2024 and reposted; may be an evergreen pipeline. Live narrated algorithm coding hits the candidate's weak area directly.

### Stretch

**Gather AI — SDE II Full Stack, India** ([posting](https://job-boards.greenhouse.io/gatherai/jobs/5243582007), updated 2026-09-30)
- Eligibility: "Remote (India)"; "We are hiring an SDE II, Full Stack, for our India-based team"; employment type unstated.
- Fit: 2–5 years, NestJS and PostgreSQL tuning match; but backend-heavy, requires production Python plus Node, Kafka/RabbitMQ/SQS, Redis, Kubernetes on Azure or another major cloud; application form knocks out on Python and Kubernetes years.
- Stage: Series B $40M on 2026-02-09; building its India team now.
- Pay: unknown. Process: anecdotal only (JSON-diff coding problem, system design, for a different role).

**Dscout — Software Engineer, India** ([posting](https://job-boards.greenhouse.io/dscout/jobs/4370266009), published 2026-08-21)
- Eligibility: "Remote - India"; employing entity unverified.
- Fit: 2–7 years full-stack; React/TypeScript/GraphQL frontend, Elixir/Phoenix backend; requires shipped LLM or agent features, AI coding tools in daily use, and strong product judgment ("LLM vs deterministic… push back").
- Pay: unpublished. Process (official, generic): recruiter call → team interviews with a possible brief exercise; public 2026 exercise repositories include AGENTS.md files and planning/trade-off write-ups.

**Infisical — Full Stack Engineer** ([posting](https://jobs.ashbyhq.com/infisical/351240fc-0dd3-48c3-a46e-e8861cae27cd), published 2026-10-02)
- Eligibility **conflicting**: text says "Based in the Americas (US or Canada), Brazil, India, UK, or EU. Must work US hours", but structured locations omit India and a required form question asks "Do you live and work in the Americas?". Confirm in writing first.
- Fit: TypeScript, Fastify, React 18, PostgreSQL, Redis/BullMQ; security domain (secrets, PKI, KMS); "exceptionally high" bar with GitHub required.
- Process: one anecdotal 2025 report (founder screens, secret-sharing take-home, review with system-design extension, in-person work day in San Francisco).

**Metabase — Software Engineer (Frontend)** ([posting](https://jobs.lever.co/metabase/8f02d3fa-edf4-4433-a6d1-4f9e517ac8f9))
- Eligibility **unverified**: "Global Remote", "50% outside the US", "work from wherever you want"; India not named; one aggregator says US only.
- Fit: strong React/JavaScript, Redux, CSS/design systems, data-structure manipulation; open-source BI; US range $110–210k.
- Process (anecdotal): coding screen in own environment → three 60-minute panels (React, algorithms, architecture) → take-home about 3.5 hours → CEO chat. Evergreen posting since 2020.

**Automattic — Experienced Software Engineer** ([posting](https://job-boards.greenhouse.io/automatticcareers/jobs/5862239), updated 2026-09-21)
- Eligibility **likely**: "engineers worldwide", 83 countries; India not named. Travel 3–4 weeks per year.
- Pay: "$70,000-$170,000 USD… global, regardless of location… paid in local currency", far above target.
- Fit: PHP and JavaScript; experience at scale; weighted written application.
- Process (official): application → skills assessment → Slack text interview or 30–60-minute video → code test or trial up to 20 hours → executive interview and CEO approval. The text-based format reduces the weight of explaining aloud. File is abbreviated (research stopped early); candidate reports and layoffs not researched.

## 5. Reach list

| Company / role | Verdict | Reason |
|---|---|---|
| Railway — Senior Full-Stack Engineer, Product | stretch | "remote position available anywhere in the world"; official process: take-home app using Railway's GraphQL API → 60-minute code walkthrough → team → CEO. Senior title; pay unpublished. |
| Supabase — Supalite Engineer | stretch | "We hire globally… from anywhere"; TypeScript and SQL, developer-platform work. No React/Next.js product role open; Auth and Branching roles need Go and 3–4+ years. |
| LiveKit — Senior Product Engineer | out of reach | 6+ years required; "APJ" includes India only by inference. |
| Tarteel AI — Senior Full-Stack Engineer | out of reach | 5+ years and a bachelor's degree required; Python required; location field says United States. |
| vidIQ — Senior Frontend Engineer | out of reach | 5+ years required; location list excludes India despite "open to candidates worldwide". |

## 6. Excluded after screening

| Company | Reason (hard filter) |
|---|---|
| Plane | India roles appear on-site in Hyderabad (recruiting partner lists "Onsite - Hyderabad"; careers page "hiring in Hyderabad and San Francisco"); remote never stated. Also seed-stage, 2024 India pay ₹6–11 lakh. |
| Federato | First-party location "Remote - US and Canada". |
| DualEntry | "available across all EU/LATAM countries". |
| refurbed, Slite | Require European timezones (Slite) or location in European timezones (refurbed); Himalayas tagged both "Worldwide". |
| Medallion | Only a US pay band; India eligibility unverified; not pursued. |
| Indian IT-services and staffing firms | Not US/EU product companies; services-market pay. |

## 7. Hiring-process summary and notable differences

| Company | Algorithm emphasis | System design | Work sample | Written emphasis | AI policy in interview |
|---|---|---|---|---|---|
| Hyperproof | low–medium | medium | take-home (Coderbyte) | medium–high (required essay) | unknown |
| HighLevel | low–medium | medium–high (2-hour design round) | timed live API build | medium | allowed (anecdotal) |
| Drivetrain | **high** | medium | none; live coding | low | unknown |
| Gather AI | low–medium | medium | live data-processing problem (anecdotal) | high | unknown |
| Dscout | low | low–medium | possible practical exercise | medium | unknown |
| Infisical | low | medium | take-home + work day (anecdotal) | medium | unknown |
| Metabase | medium | medium–high | take-home (anecdotal) | high | unknown |
| Automattic | low | low | code test or trial up to 20 hours | **high** (Slack interview) | unknown |
| Railway (reach) | low | medium | take-home app + live walkthrough | high | unknown |

Differences that matter for preparation:
- **Practical build rounds dominate.** Six of the nine use a take-home, timed build, trial or practical exercise; only Drivetrain is algorithm-led.
- **Every loop makes you defend your work.** HighLevel's 2-hour design round, Railway's 30-minute code walkthrough, Hyperproof's three 60-minute one-to-ones and Metabase's architecture panel all test the candidate's stated weak area.
- **AI posture splits.** HighLevel, Dscout and vidIQ expect daily AI-agent coding on the job; HighLevel reportedly allows AI in its build round. No company published an official interview AI policy.
- **Domain knowledge gives an edge:** CRM (HighLevel), compliance and risk (Hyperproof), FP&A spreadsheets and charts (Drivetrain), secrets and security (Infisical).

## 8. Evidence quality

- **Strong (first-party):** eligibility and requirements for Hyperproof, HighLevel, Gather AI, Dscout, Drivetrain; published pay for Hyperproof and Automattic; official process for Automattic and Railway.
- **Medium:** HighLevel process (corroborated candidate reports); Drivetrain algorithm focus (corroborated).
- **Weak:** process details for Infisical, Metabase, Gather AI (single or snippet-only reports). Glassdoor, AmbitionBox and several boards blocked direct fetches (HTTP 403); their content was read only through search snippets and labelled so.
- **No official interview AI policy** was found for any shortlisted company.

## 9. Tools used and unavailable

- Used: public ATS JSON endpoints (Greenhouse, Ashby, Lever) via Python scripts; Himalayas, Remotive and Remote OK public APIs; WebSearch and WebFetch; Bash/Python for corpus extraction; general-purpose research agents for market trends and per-company deep dives.
- Not used: Playwright and Claude in Chrome (not needed; ATS APIs worked), context7 (no framework-version question arose), the deep-research skill (a research agent was used instead).
- The final fresh-context source re-check was skipped at the candidate's request to save usage; instead every shortlisted role URL was re-fetched (all live on 2026-10-09).

## 10. Unresolved uncertainty (only the candidate or recruiters can resolve)

- **India eligibility** for Infisical (conflict), Metabase (unverified) and Automattic (likely): ask the recruiter before preparing company-specific material.
- **Employment structure and pay** for Dscout, Gather AI, Drivetrain and HighLevel (HighLevel is direct employment in India; the others are unstated).
- **Education:** the profile records no degree. Tarteel AI requires a bachelor's degree; Hyperproof's AI role requires one.
- **Hyperproof's screening question** (4+ years React and Java Spring Boot) may filter the candidate out regardless of the posting's 3–5 years.
- **Evergreen postings** (Metabase since 2020; Drivetrain since 2024; Railway since 2024) may not reflect an active hiring need this quarter.
