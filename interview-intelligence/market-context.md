# Market context: remote full-stack roles open to India-based engineers

Snapshot date: 2026-10-09. Full source details (URLs, tiers, freshness) for every secondary claim are in `raw/trend-evidence.md`; the primary posting corpus and scripts are in `raw/`.

## 1. Segment, corpus and limits

**Segment.** Mid-level (about 2–5 years) full-stack software engineering, fully remote, at US/EU (or globally distributed) companies from seed stage to late-stage private, where the role can be done from India as an employee, through an employer-of-record (EOR), or as a contractor.

**Primary corpus (M1), fetched 2026-10-09.**

| Corpus | What it contains | N |
|---|---|---|
| ATS boards | Public Greenhouse, Ashby and Lever boards for 148 companies chosen as likely remote-friendly startups and scale-ups (list in `raw/postings/_probe-*.json`). Engineering individual-contributor postings after title filtering. | 2,072 postings; 1,547 below staff level |
| Himalayas | Himalayas public search API, `country=India` (returns India-listed and worldwide-friendly jobs), 10 full-stack/TypeScript queries × Mid-level/Senior, first page each (20 results per page). Source: Himalayas (himalayas.app), credited per its API terms. | 405 unique jobs; 281 engineering |
| **Segment A** (`A_india_remote`) | Remote, non-staff engineering postings open to India-based candidates: ATS postings listing India, worldwide, global or APAC (excluding office or hybrid roles), plus Himalayas engineering postings. Indian IT-services and staffing firms removed (they pay India-services rates; list in `raw/extract_skills.py`). Deduplicated by company + title. | **264 postings, 145 companies** |
| **Segment B** (`B_fullstack_all`) | Full-stack, product-engineer and frontend non-staff postings on the ATS boards, any location. Shows what full-stack roles at these companies ask for, whether or not India-based candidates can apply. | **151 postings** |

**Corpus limits.**
- The ATS board list was hand-built from remote-friendly, mostly venture-backed software companies. It over-represents developer-tools, infrastructure and AI companies and under-represents agencies, enterprises and non-tech employers.
- Himalayas results are keyword-driven (full-stack and TypeScript queries), so Segment A over-represents JavaScript/TypeScript roles relative to all India-eligible remote engineering work. Only the first page of each query was fetched, which caps Himalayas at about 20 results per query and seniority combination; deeper pages exist (for example, 299 Senior results for "full stack engineer").
- Himalayas location tags are not reliable for India eligibility. Spot checks found several "Worldwide" postings that the first-party text restricts to the EU, Latin America or European timezones (DualEntry, refurbed, Slite). Segment A therefore overstates true India eligibility somewhat. Shortlisted companies were verified individually against first-party postings.
- Skill counts come from regular-expression matching (`raw/extract_skills.py`). Broad patterns ("performance", "API", "ownership", "communication") overcount; specific technologies (React, PostgreSQL, NestJS) are reliable. "Required" means the mention appears outside a section headed nice-to-have, bonus or preferred; it is an approximation.
- One snapshot only. No trend can be read from this corpus until it is re-run.

## 2. Demand summary

**India access is the binding constraint, not skills.** On the 148 ATS boards, 22 of 197 non-staff full-stack/frontend postings (11%) were not locked to a named region outside India. Across all non-staff engineering postings, the figure was 215 of 1,547 (14%). Most open-to-India roles at well-known companies were infrastructure, kernel, data or staff-level positions, not full-stack product roles. (M1, fetched 2026-10-09.)

**Top skills in Segment A (N = 264).** Full table in `skill-demand.csv`.

| Skill | Mentioned | Required (approx.) |
|---|---|---|
| Performance / scalability (broad match) | 77% | 75% |
| Product sense / ownership (broad match) | 73% | 72% |
| Written communication (broad match) | 72% | 66% |
| REST / API work (broad match) | 66% | 60% |
| System design / architecture | 61% | 58% |
| Testing (any) | 56% | 52% |
| JavaScript | 50% | 44% |
| Security (incl. authentication/authorization) | 45% | 43% |
| TypeScript | 41% | 37% |
| Observability / monitoring | 41% | 38% |
| Debugging | 36% | 34% |
| React | 36% | 31% |
| Python | 34% | 31% |
| PostgreSQL | 31% | 27% |
| Docker / AWS (each) | 30% | 21–23% |
| Node.js | 28% | 25% |
| LLM API integration | 26% | 23% |
| Code review | 26% | 26% |
| AI-assisted development tools | 22% | 20% |
| AI agents / tool calling | 22% | 20% |
| Next.js | 11% | 9% |
| NestJS | 7% | 5% |

**Segment B (full-stack/product at the 148 companies, any location, N = 151)** is more TypeScript- and AI-product-heavy than Segment A: TypeScript 71%, React 70%, product sense/ownership 88%, AI agents/tool calling 42%, LLM API integration 38%, AI-assisted development 25%, PostgreSQL 17%, Node.js 27%.

**Seniority.** In Segment A, 83 of 264 titles (31%) say "Senior"; 14 (5%) explicitly say mid or "II"; 4 (2%) say junior or associate; the rest are unlabelled. Of 143 Segment A postings that state a minimum years figure, 115 (80%) ask for 2–5 years; 3 years is the most common single value (37 postings).

**Employment type.** Himalayas labels 20 of 147 Segment A postings it supplied (14%) as contractor roles; ATS postings rarely state employment type.

## 3. Trend findings (secondary evidence)

- **US software postings are recovering; Europe is not.** Indeed's US software-development postings index was 78.33 on 2026-10-02 (February 2020 = 100): +21.8% year over year, still about 22% below pre-pandemic. Germany 48.29 (−16.5% year over year), France 52.85 (−7.9%), UK 61.26 (+2.2%). FRED/Indeed Hiring Lab, M2, current.
- **The rebound is senior- and AI-led.** 71% of the May 2025–May 2026 increase in US software postings came from senior roles, and 37% from roles with "AI" in the title (overlapping). Indeed Hiring Lab, 2026-07-08, M2, current. Senior roles were 69.3% of US software postings in Q1 2026; entry-level 4.5%. Indeed Hiring Lab, 2026-07-23, M2, current.
- **Remote is shrinking.** Remote-or-hybrid share of software postings on Indeed: US 30.8% (2026-08-31) versus 33.7% a year earlier and 42.0% in February 2022; UK 45.9% (from 49.0%); Germany 44.5% (from 46.6%); France 38.8% (from 42.1%). Indeed Hiring Lab remote tracker data, M2, current. This counts hybrid too, so fully remote, India-eligible roles are a much smaller subset (inference).
- **Competition per opening is high.** Ashby reports over 300 applications per hire across 100 million applications, about triple 2021 (2026-05-07, M2, current). Greenhouse's CEO cites about 254 applicants per job advertisement (Fortune, 2026-07-27, M3, current). Neither figure is specific to remote engineering.
- **Cross-border hiring into India skews to smaller companies.** Deel's Global Hiring Report 2026 says software developers are the top cross-border EOR role, and that SMBs are more likely than top-funded startups ($100M+ raised) to recruit in India; top-funded startups' cross-border hires went mainly to the UK, Canada, Germany and Australia. Deel, about March 2026, M2 vendor data, recent.
- **TypeScript is the most-used language on GitHub by contributors** (since August 2025), and India added over 5 million developers in the year to August 2025, so India-based competition is growing. GitHub Octoverse 2025, M2, recent for these counts.
- **Pay benchmarks.** Levels.fyi India software-engineer median total compensation is about ₹30 lakh (23,718 submissions, updated 2026-10-08; 25th percentile ₹17.5 lakh, 75th ₹49.3 lakh), M2, current; includes Big Tech and onsite roles, no experience split. No M2 source for remote India pay from US/EU employers was found; contractor-rate figures ($25–60 per hour mid-level) are vendor claims, unverified.

## 4. AI shift: the role

- **AI coding tools are near-universal; trust depends on verification.** Stack Overflow Developer Survey 2026 (over 30,000 respondents, published 2026-10-06, M2, current): coding assistants and agents are the top AI use (66%); 73% of their users use them daily; Claude Code (66%) and GitHub Copilot (59%) lead among agents; 48% trust AI only when they can easily validate its answers; only 20% use AI to deploy, operate or troubleshoot production systems.
- **Postings now name AI tools and AI product work.** In Segment A, 22% of postings mention AI-assisted development tools, 26% LLM API integration, 22% AI agents or tool calling, 11% retrieval/vector search, 5% evaluations (M1). In full-stack/product postings at the 148 companies, agents/tool calling reaches 42% and LLM integration 38% (M1).
- **AI-titled roles drive growth.** "AI engineer" is LinkedIn's fastest-growing US title (Jobs on the Rise 2026, 2026-01-07, M2, old for AI claims); 37% of the US software-posting rebound came from AI-titled roles (Hiring Lab, M2, current); public repositories using an LLM SDK grew 178% year over year (Octoverse 2025, M2, old for AI claims).
- **What employers say they weight more.** Canva expects candidates to use AI tools and evaluates whether they "identify and fix issues in AI-generated code" and break down ambiguous requirements (Canva engineering blog, 2025-06-11 and 2025-10-20, first-party, old). Coinbase says it rebuilt its loop to test how candidates "direct AI, evaluate its output, and apply judgment where models fall short" (blog listing 2026-07-13; the article itself returned HTTP 403, so details are from the listing only). GitHub names directing AI, not trusting its first answer, and spending saved time on trade-offs and system design (GitHub blog, 2026-10-02, M3, current).

## 5. AI shift: the interview

- **Startups and scale-ups are moving toward practical, repository-based rounds, sometimes AI-allowed.** Canva replaced its computer-science-fundamentals screen with an AI-assisted coding round (2025-06-11, first-party). In an interviewing.io survey, 67% of startup interviewers said AI had meaningfully changed their process, versus 0 of 52 at FAANG (undated, about October 2025, M3, small self-selected sample).
- **Large companies are hardening, not removing, algorithm rounds.** Google reintroduced in-person rounds for some roles (reported about August 2025, M3) and is piloting a Gemini-assisted code-comprehension round (reported 2026-05-10, M3; primary not fetched). Meta added one AI-enabled coding round (reported July 2025, M3). Amazon bans generative AI in interviews unless permitted (reported February–March 2025, M3).
- **Most organisations still ban AI in interviews.** Karat's survey of 400 engineering leaders: 62% still prohibit AI in technical interviews; in the US, 79% use live technical interviews and 45% take-home projects (2026-01-07, M3 vendor, old).
- **Take-homes are being rescoped, not clearly replaced.** Anthropic says to assume any take-home will eventually be solved by AI and redesigned its own to allow AI "as they would on the job" (2026-01-21, first-party, old). No dataset shows a broad shift from take-homes to paid work trials.
- **Fraud controls are rising in exactly this segment.** The Pragmatic Engineer reports proxy interviewees and live LLM use at remote-hiring US/UK/EU companies (2026-07-07, M3, current, partly paywalled); Gartner reports 6% of surveyed candidates admitted interview fraud (2025-07-31, M3, old). Expect camera-on rounds, identity checks and live follow-up questions on any submitted work (inference).

## 6. Trajectory verdicts

Only one corpus snapshot exists, so a verdict needs two independent M2/M1 sources or a named successor. Most technology families therefore read `insufficient-data`; their current share is still reported.

| Skill family | Verdict | Evidence |
|---|---|---|
| AI product work (LLM integration, agents, retrieval) | `rising` | Hiring Lab: 37% of the US software-posting rebound from AI-titled roles (2026-07-08, M2); LinkedIn Jobs on the Rise 2026: AI engineer #1 (M2); Octoverse: LLM-SDK repositories +178% (M2). Segment A share: LLM integration 26%, agents 22%. |
| AI-assisted engineering (using and verifying AI coding tools) | `rising` | Stack Overflow 2026: coding agents top AI use at 66%, daily use 73% of users (M2); DORA 2025: 90% adoption (M2, old). Segment A share 22%. |
| Code review and verification of generated code | `shifting` | Form changed: interviews now test fixing AI output (Canva, first-party 2025); Stack Overflow 2026: trust conditional on validation (M2). Segment A code-review mention 26%. |
| Data structures and algorithms (interview) | `shifting` | Canva replaced its fundamentals screen with an AI-assisted round (first-party); large companies keep and harden algorithm rounds (interviewing.io, Karat, M3). Still tested; form varies by company. |
| System design / architecture | `insufficient-data` | No dated trend source. Current Segment A share 61% (broad match). GitHub commentary says weight is increasing (M3 only). |
| TypeScript / JavaScript | `insufficient-data` (posting trend) | Octoverse: TypeScript #1 by contributors (M2, usage, not hiring demand). Segment A: TypeScript 41%, JavaScript 50%; Segment B: TypeScript 71%. |
| React / Next.js | `insufficient-data` | Segment A React 36%, Next.js 11%; Segment B React 70%. |
| Node.js / NestJS | `insufficient-data` | Segment A Node.js 28%, NestJS 7%. |
| PostgreSQL / SQL | `insufficient-data` | Segment A PostgreSQL 31%. |
| Cloud (AWS / GCP), containers | `insufficient-data` | Segment A AWS 30%, GCP 17%, Docker 30%, Kubernetes 27%. |
| Testing, observability, debugging | `insufficient-data` | Segment A testing 56%, observability 41%, debugging 36%. |
| Remote work availability (market condition, not a skill) | `declining` | Indeed remote tracker: software remote/hybrid share down in US, UK, Germany, France, Ireland year over year (M2); Pragmatic Engineer reports remote roles shrinking in UK/EU (M3). |
| Entry-level hiring (market condition) | `declining` | Hiring Lab: entry-level 4.5% of US software postings in Q1 2026; senior share up 9 points 2019–2025 (M2). |

## 7. Implications for this candidate (stated as data)

- **Eligibility, not skill fit, limits the pool.** 11% of non-staff full-stack/frontend postings on 148 startup/scale-up boards were open beyond named non-India regions (22 of 197, M1). The shortlist was built from the India-explicit subset and verified per role.
- **Experience band matches.** 80% of Segment A postings stating years ask for 2–5; 3 years is the modal requirement (M1). But 31% of Segment A titles and 69.3% of US software postings (M2) are senior, so many roles labelled "Senior" will be reachable only by presenting at the mid-to-senior boundary.
- **Stack overlap is strong on the core, thin on the edges.** TypeScript 41% / React 36% / PostgreSQL 31% / Node.js 28% of Segment A. NestJS (7%) and Next.js (11%) are niche; framework names matter less than TypeScript, React, Node and SQL depth.
- **AI product exposure is now a differentiator.** LLM integration (26%) and agents/tool calling (22%) in Segment A; 38% and 42% in full-stack roles at the 148 companies. The candidate's profile lists AI-assisted coding (1.5 years, self-reported) but no shipped LLM feature.
- **The stated weak areas are tested directly.** System design/architecture appears in 61% of Segment A postings (broad match) and written communication in 72%; AI-era interviews explicitly score explaining and defending decisions (Canva, Coinbase).
- **Pay target is within reach of ordinary remote offers.** At ₹96 per US dollar (FRED/Fed H.10 96.31 on 2026-10-02; Trading Economics about 96.9 on 2026-10-09), ₹1.5 lakh per month take-home needs about $20,500 per year gross as a contractor using presumptive taxation, or about ₹20.9–23.8 lakh CTC as an employee; ₹2 lakh needs about $27,700 (contractor) or ₹29.5–34.1 lakh CTC (employee). Pricing a contract 20–30% higher covers missing leave and benefits: about $25,000–27,000 and $33,000–36,000. Full assumptions in `raw/trend-evidence.md` section 7.6; section 58 (formerly 44ADA) details and software's status as a "specified profession" should be confirmed with a chartered accountant.
- **Competition.** Over 300 applications per hire overall (Ashby, M2) and heavy application volume on remote roles mean public applications convert poorly; less-known companies with India-explicit postings are the better-odds subset (inference; no source measures applicants per India-eligible posting).

## 8. Open questions and evidence gaps

- No source measures applicants per India-eligible remote posting, so "less saturated" is judged by proxies (brand prominence, India-explicit postings at smaller companies).
- No M2 source for remote pay to India-based engineers from US/EU employers.
- The skill-trend verdicts need a second corpus snapshot; re-run `raw/fetch_boards.py`, `raw/fetch_himalayas.py`, `raw/normalize.py` and `raw/extract_skills.py` in 4–8 weeks and compare `skill-demand.csv`.
- Primary sources for the Coinbase, Google and Meta interview changes were not fully read (blocked or paywalled).
