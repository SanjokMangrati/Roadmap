# Trend evidence: market, AI, interviews, remote-from-India, compensation

Compiled 2026-10-09. All access dates are 2026-10-09 unless noted.

Candidate context: India-based full-stack engineer (React/Next.js, Node/NestJS, PostgreSQL, TypeScript), about 3 years of experience. Targets remote roles at US/EU seed-to-scale-up companies, hired as an employee, through an EOR, or as a contractor. Target take-home is ₹1.5–2 lakh per month.

**Tier key.** M2 means official statistics, job-platform research arms, or large surveys with a stated method. M3 means reputable journalism or analyst reports that cite data. M4 means commentary, used as a lead only.

**Freshness key.** Measured from 2026-10-09:
- current: under 6 months old
- recent: under 12 months old
- old: 12–24 months old, and also any AI-related claim older than 6 months
- stale: over 24 months old

---

## 1. Software-engineering job posting volume, 2025–2026

**1.1 US software development postings index (latest value). Strongest evidence.**
- **Value:** Indeed's US Software Development Job Postings index was **78.33 on 2026-10-02** (1 Feb 2020 = 100, seasonally adjusted).
- **Earlier values from the same series:**
  - 64.30 on 2025-10-02
  - 61.10 on 2025-05-17, the low point of the cycle
  - 67.18 on 2026-01-02
  - 72.49 on 2026-04-03
  - 73.80 on 2026-07-03
- **What I calculated from these values:**
  - Up about 21.8% year over year.
  - Up about 28% from the May 2025 low.
  - Still about 22% below February 2020.
- **Comparison:** Indeed's all-sector US postings index (IHLIDXUS) was 103.84 on 2026-10-02, against 101.28 a year earlier, which is +2.5%. Software is recovering faster than the overall market, but from a much lower base.
- **Source:** "Software Development Job Postings on Indeed in the United States (IHLIDXUSTPSOFTDEVE)", FRED / Federal Reserve Bank of St. Louis, with data from Indeed Hiring Lab. https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE (CSV: https://fred.stlouisfed.org/graph/fredgraph.csv?id=IHLIDXUSTPSOFTDEVE).
- **Publication date:** Daily series, last observation 2026-10-02.
- **Tier and freshness:** M2, current.
- **Note:** Secondary write-ups quote slightly different points: 76.1 on 2026-09-04, and 74.4 in an August 2026 snapshot (BlueLine Research, https://bluelinesearch.ai/insights/software-dev-postings-26-below-prepandemic-indeed-august-2026, published 2026-08-26, M4). This is the same series read on different dates. FRED is the authoritative read.

**1.2 Europe and Canada software development postings (same Indeed method, via FRED).** Values below are for 2026-10-02 against 2025-10-02. The year-over-year changes are my calculations.

| Country | 2026-10-02 | 2025-10-02 | Change | Note |
|---|---|---|---|---|
| Germany | 48.29 | 57.81 | −16.5% | Feb 2020 = 100; the weakest market |
| France | 52.85 | 57.39 | −7.9% | |
| UK | 61.26 | 59.93 | +2.2% | Flat at a low level |
| Canada | 77.81 | 78.85 | −1.3% | |

- **Series IDs:** IHLIDXDETPSOFTDEVE, IHLIDXFRTPSOFTDEVE, IHLIDXGBTPSOFTDEVE, IHLIDXCATPSOFTDEVE. Search page: https://fred.stlouisfed.org/searchresults/?st=software%20development%20job%20postings%20on%20indeed
- **Publisher and dates:** FRED / Indeed Hiring Lab, daily data to 2026-10-02.
- **Tier and freshness:** M2, current.
- **Reading:** The rebound is a US story. EU software posting volume, especially in Germany and France, is still falling. Hiring Lab says the same thing (see 1.3).

**1.3 Hiring Lab: the US rebound is driven by senior roles and AI-titled roles.**
- **Rebound size:** US software development postings "have grown by almost 15%" since Claude Code launched on 24 February 2025. Total postings fell 7% over the same period.
- **Gap to pre-pandemic:** Software development postings "remain about 27.5% below their pre-pandemic level" (data through June 2026).
- **Senior roles:** "71% of the increase in software development job postings between May 2025 and May 2026 is from senior roles."
- **AI-titled roles:** "37% is due to jobs that mention AI in their title." The two shares overlap, so they should not be added.
- **Other countries:** Outside Germany and France, the software development share of postings is rising in most large developed economies.
- **Author's caveat:** "correlation does not imply causation."
- **Source:** "AI and Job Postings: From Destruction to Creation?", Guillermo Gallacher, Indeed Hiring Lab. https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/
- **Publication date:** 2026-07-08.
- **Tier and freshness:** M2, current.

**1.4 Entry vs mid vs senior share.**
- **Software development, Q1 2026:** Senior-level positions were **69.3%** of US software development postings. Entry-level was **4.5%**, the lowest entry-level share of any sector.
- **Tech, 2019 to 2025:** Entry-level share fell by just over 1 percentage point, mid-level fell 7.7 points, and senior rose 9 points.
- **All US postings, January 2025 to May 2026:** Senior +13.5%, mid-level −6.7%, entry-level −6.2/−6.3% (the article gives both figures).
- **Source:** "The Labor Market Is Tilting Toward Seniority", Felix Aidala and Sneha Puri, Indeed Hiring Lab. https://hiringlab.indeed.com/2026/07/23/the-labor-market-is-tilting-toward-seniority/
- **Publication date:** 2026-07-23.
- **Tier and freshness:** M2, current.
- **Caveat:** Hiring Lab gives no separate mid-level share for software development, so the mid share is roughly 26% (100 − 69.3 − 4.5). That is my inference.
- **Implication for this candidate:** At about 3 years of experience, the candidate sits at the mid/senior boundary that most postings target. Positioning as "mid-to-senior" rather than "junior" matters.

**1.5 Remote or global volume.** I found no single index of remote-only or global software postings. The proxy is the remote/hybrid share in 6.1.

---

## 2. AI/LLM skills inside software-engineering postings; AI-engineer and product-engineer demand

**2.1 AI mentions in US postings.**
- **AI Tracker high:** Indeed's AI Tracker hit 4.2% of all US postings at the end of 2025.
- **Growth:** Postings mentioning AI were 134% above February 2020 levels.
- **Tech postings:** Tech postings mentioning AI were about 45% higher than in February 2020, while total tech postings were 34% below.
- **Software development:** Software development, IT systems & solutions, and scientific R&D each mentioned AI in "20% or more" of postings. The article gives no exact software-only share.
- **Source:** "January 2026 US Labor Market Update: Jobs Mentioning AI Are Growing Amid Broader Hiring Weakness", Cory Stahle, Indeed Hiring Lab. https://hiringlab.indeed.com/2026/01/22/january-labor-market-update-jobs-mentioning-ai-are-growing-amid-broader-hiring-weakness/
- **Publication date:** 2026-01-22.
- **Tier and freshness:** M2, old (AI-related and more than 6 months old).

**2.2 AI mentions in UK postings.**
- **Overall:** 9.4% of UK postings mentioned AI as of end-June 2026, a record.
- **Software development:** One of the highest shares "by some margin," but no figure is given.
- **Data & analytics:** 48.8%.
- **Source:** "Indeed's 2026 Mid-Year UK Jobs & Hiring Trends Report", Jack Kennedy, Indeed Hiring Lab UK. https://hiringlab.indeed.com/uk/blog/2026/08/03/mid-year-uk-jobs-hiring-trends-report/
- **Publication date:** 2026-08-03.
- **Tier and freshness:** M2, current.

**2.3 AI-titled roles drive the US software rebound.** 37% of the May 2025 to May 2026 increase in software postings came from roles with AI in the title (Hiring Lab, 2026-07-08, M2, current; see 1.3).

**2.4 "AI engineer" is the fastest-growing US job title (LinkedIn Jobs on the Rise 2026).**
- **Rank:** AI engineer is #1. AI consultants/strategists are #2 and AI/ML researchers are #5.
- **Top skills for AI engineer:** LangChain, RAG, PyTorch.
- **Flexibility:** 26.2% remote and 27.1% hybrid.
- **Method:** Based on job starts by LinkedIn members from 2023-01-01 to 2025-07-31. Remote data comes from postings dated November 2024 to November 2025.
- **Source:** "LinkedIn Jobs on the Rise 2026: The 25 fastest-growing roles in the U.S.", LinkedIn News / Economic Graph. https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c/
- **Publication date:** 2026-01-07.
- **Tier and freshness:** M2, old (AI-related, 9 months).
- **Unverified growth figure:** A secondary claim of "+143% YoY" postings for AI engineer did not appear on the LinkedIn page.
- **India edition (M3, unverified):** News coverage says LinkedIn India's 2026 list ranked Prompt Engineer, AI Engineer and Software Engineer as the top three. I could not fetch the LinkedIn India page.

**2.5 "Product engineer" title demand: weak evidence only.**
- **England:** ITJobsWatch shows permanent England postings for "Product Engineer" rose to 72 in the six months to early January 2026, from 20 a year earlier. The share is still tiny (0.14%). https://www.itjobswatch.co.uk/jobs/england/product%20engineer.do (M3, recent).
- **Startup listings:** Startup.jobs listed about 1,263 "Product Engineer" openings in July 2026 (M4, no trend data).
- **Reading:** I found no M2 source measuring growth in product-engineer postings. Treat the title as a positioning choice, not a proven demand trend.

**2.6 Skills to show in a full-stack application (inference from 2.1–2.4, not a measured statistic).** "AI-adjacent" now means building LLM features (RAG, agents, evaluations) into products. The senior and AI tilt in 1.3 suggests a full-stack TypeScript engineer gains most by shipping LLM-integrated product features.

---

## 3. Developer AI-tool adoption, and trust in and verification of AI code

**3.1 Stack Overflow Developer Survey 2026 (results published 2026-10-06).**
- **Sample:** More than 30,000 respondents over a 7-week field period.
- **Usage:**
  - Coding assistants and agents are the top AI use case at 66%, ahead of chatbots at 63%.
  - 73% of coding assistant/agent users use them daily.
  - Of daily users, 31% use AI for 4 or more hours a day.
- **Leading agents:** Claude Code (66%) and GitHub Copilot (59%).
- **Sentiment:** 62% view AI at least somewhat positively, rising to 71% among daily users.
- **Production use:** Only 20% use AI to deploy, operate or troubleshoot production systems.
- **Trust:**
  - 48% trust AI when they can easily validate its answers.
  - 16% trust it for most tasks that are not important decisions.
  - 93% say source attribution is needed to trust AI output.
- **Work pattern:** Only 18% go into an office every day.
- **Sources:**
  - "The results of the 2026 Developer Survey are here!", Ryan Donovan, Stack Overflow Blog. https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
  - The AI section of the survey site. https://survey.stackoverflow.co/2026/ai
- **Publication date:** 2026-10-06.
- **Tier and freshness:** M2, current.
- **Conflict:** Secondary outlets (comparethecloud.net, byteiota.com) quote "83% use AI" and "6.6% trust AI for important decisions." I did not see either figure on the official AI page I fetched, so both are **unverified**. Byteiota's "84%" is the 2025 figure.

**3.2 Stack Overflow Developer Survey 2025 (baseline).**
- **Adoption:** 84% were using or planning to use AI tools (76% in 2024), and 50.6% of professional developers used AI daily.
- **Trust:** 46% distrust the accuracy of AI output; 33% trust it, and 3.1% "highly trust" it.
- **Frustrations:** 66% cite "AI solutions that are almost right, but not quite" as their top frustration. 45.2% say debugging AI-generated code takes more time.
- **Vibe coding:** 72% say they are not vibe coding.
- **Source:** "AI | 2025 Stack Overflow Developer Survey", Stack Overflow. https://survey.stackoverflow.co/2025/ai
- **Publication date:** July 2025 (exact day unverified).
- **Tier and freshness:** M2, old.

**3.3 GitHub Octoverse 2025.**
- **Scale:** More than 180M developers on GitHub, with over 36M joining in the year.
- **India:** Added more than 5M developers, over 14% of new accounts. Projected to reach 57.5M developers by 2030, passing the US. India also overtook the US in open-source contributor count.
- **TypeScript:** Became the #1 language by contributors in August 2025. GitHub attributes part of this to typed languages making agent-assisted coding more reliable.
- **Copilot adoption:** Nearly 80% of new developers use Copilot in their first week.
- **LLM SDKs:** 1.1M+ public repos use an LLM SDK, +178% YoY.
- **Copilot code review:** 72.6% of users say it improved their effectiveness.
- **Copilot coding agent:** Opened 1M+ pull requests between May and September 2025.
- **Data period:** 2024-09-01 to 2025-08-31.
- **Source:** "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", GitHub Blog. https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- **Publication date:** 2025-10-28, updated 2026-02-28.
- **Tier and freshness:** M2, old for the AI claims; recent for the India and TypeScript counts.
- **Relevance:** TypeScript's #1 position directly favours this candidate's stack. India's developer growth also means more India-based competition.

**3.4 DORA 2025 (Google).**
- **Adoption:** 90% AI adoption among software professionals (+14 from last year), with a median of about 2 hours a day.
- **Trust:** 24% trust AI "a great deal" or "a lot"; 30% trust it "a little" or "not at all".
- **Self-reported impact:** More than 80% say it raised their productivity; 59% say it improved code quality.
- **Sample:** About 5,000 respondents.
- **Source:** "How are developers using AI? Inside our 2025 DORA report", Google blog. https://blog.google/technology/developers/dora-report-2025/ Report: https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
- **Publication date:** September 2025 (exact day unverified).
- **Tier and freshness:** M2, old. These figures came via search summaries; I did not fetch the full report.

**3.5 Sonar State of Code 2026, the verification gap.**
- **Sample:** More than 1,100 developers.
- **Trust:** 96% do not fully trust that AI code is functionally correct.
- **Checking:** Only 48% always verify AI-assisted code before committing.
- **Share of code:** Respondents estimate AI produces 42% of committed code, and expect 65% by 2027.
- **Review effort:** 38% say reviewing AI code takes more effort than reviewing human code.
- **Most important AI-era skill:** "Reviewing and validating AI-generated code" (47%), ahead of prompting (42%).
- **Sources:**
  - Sonar press release. https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/
  - The Register, "Most devs don't trust AI-generated code, but fail to check it anyway". https://www.theregister.com/2026/01/09/devs_ai_code/
- **Publication dates:** Sonar 2026-01-08; The Register 2026-01-09.
- **Tier and freshness:** M3, since it is vendor-run and Sonar sells verification tools. Old (AI, 9 months). The figures came via search summaries.

**3.6 Reading.** Adoption is near-universal and has levelled off. Trust is conditional on verification. That is why employers and interviewers now test review, validation and debugging of AI output (sections 4 and 5).

---

## 4. What employers say they now weight more (first-party statements)

**4.1 Canva: AI use is expected in interviews.**
- **The change:** Canva now expects Backend, Frontend and ML candidates to use Copilot, Cursor or Claude. A new "AI-Assisted Coding" competency "replaces our traditional Computer Science Fundamentals screening".
- **What interviewers assess:**
  - "Do they understand when and how to leverage AI effectively?"
  - "How well do they break down complex, ambiguous requirements?"
  - "Can they identify and fix issues in AI-generated code?"
  - Whether candidates make solutions meet production standards.
- **Fundamentals:** Canva says it is "still assessing computer science fundamentals through the new process."
- **Source:** "Yes, You Can Use AI in Our Interviews", Simon Newton, Canva Engineering Blog. https://canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews
- **Publication date:** 2025-06-11.
- **Tier and freshness:** M2 (first-party), old.
- **Follow-up post:** "AI Interview Success: An Interviewer's Inside Guide", Karl Hörnlund, 2025-10-20. https://www.canva.dev/blog/engineering/ai-interview-success/ (M2, old). It says "We're assessing your engineering capabilities enhanced by AI collaboration, not your AI skills in isolation." Candidates must explain design choices, spot issues before reviewers do, and keep control of technical decisions.

**4.2 Anthropic: assume AI will solve any take-home.**
- **The problem:** The performance-engineering take-home had to be redesigned repeatedly. Claude Opus 4 beat most applicants within the time limit, and Opus 4.5 matched the top candidates: "we no longer had a way to distinguish between the output of our top candidates and our most capable model."
- **Advice:** Assume any take-home or interview will eventually be solved by AI. Realism and resistance to AI trade off against each other. Test how candidates use tools and make decisions, not only their output.
- **AI on the redesigned test:** AI use is allowed "as they would on the job."
- **Source:** "Designing AI-resistant technical evaluations", Tristan Hume, Anthropic Engineering. https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
- **Publication date:** 2026-01-21.
- **Tier and freshness:** M2 (first-party), old (AI, 8.5 months).

**4.3 Coinbase: the loop rebuilt for the AI era.**
- **What the listing says:** AI-generated code, with human review, now accounts for "roughly 100%" of merged code. The interview loop was rebuilt to test how candidates "direct AI, evaluate its output, and apply judgment where models fall short", starting with a pilot gated on exit criteria.
- **Source:** "Interviewing Engineers in the AI Era: Lessons from a Year of Rebuilding", Coinbase Blog. https://www.coinbase.com/blog/interviewing-engineers-in-the-ai-era-lessons-from-a-year-of-rebuilding
- **Publication date:** 2026-07-13, per the blog listing.
- **Tier and freshness:** M2, current. **The direct fetch failed (HTTP 403)**, so these details come from the blog listing and search metadata.
- **Unverified:** "Repo-based coding/debugging as a live signal; system design with AI in early testing." This comes from an aggregator summary (zeli.app), which also gives a conflicting "50%" AI-code share.

**4.4 GitHub: three skills to strengthen.**
- **The three skills:** "Learn to direct AI, not just use it"; "Don't trust AI's first answer"; and use the time saved on implementation for customer needs, tradeoffs and system design.
- **Source:** "AI is changing developer work. Here are three skills to strengthen.", Gwen Davis, GitHub Blog. https://github.blog/ai-and-ml/ai-is-rewriting-the-developer-career-ladder-heres-how-to-stand-out/
- **Publication date:** 2026-10-02.
- **Tier and freshness:** M3 (vendor commentary, cites no hiring data), current.

**4.5 Shopify: AI use is a baseline expectation.**
- **The memo:** CEO Tobi Lütke's memo made "reflexive AI usage" a "baseline expectation". Teams must show AI cannot do a job before requesting headcount, and AI use enters performance reviews.
- **Source:** Fortune. https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/
- **Publication date:** 2025-04-08.
- **Tier and freshness:** M3, old.
- **Interview format (third-party only):** Hello Interview (Evan King) reports two AI-enabled coding rounds where candidates bring their own IDE and AI. The task is an open-ended problem in an empty repo that grows with follow-up requirements. Graders look at design, testing, readability and how candidates handle bad AI output. https://www.hellointerview.com/blog/shopify-ai-enabled-coding (M4, date **unverified**, page shows © 2026).

**4.6 Pattern across sources.** Employers converge on the same small set of skills:
- Decomposing ambiguous requirements
- Directing AI while keeping architectural control
- Spotting and fixing defects in AI output
- Testing strategy
- Explaining and defending tradeoffs, including system design

Pure syntax and algorithm recall are explicitly de-emphasised at Canva and Shopify. At large companies they are not removed (see 5.6).

---

## 5. AI in interviews: policies, format changes, cheating tools

**5.1 Meta: AI-enabled coding round.**
- **Reporting:** 404 Media and Business Insider reported internal Meta communications: "Meta is developing a new type of coding interview in which candidates have access to an AI assistant," which "makes LLM-based cheating less effective." Meta confirmed this to Business Insider.
- **Source:** "Meta Is Going to Let Job Candidates Use AI During Coding Tests", Jason Koebler, 404 Media (paywalled). https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/
- **Publication date:** late July 2025.
- **Tier and freshness:** M3, old.
- **Format details (third-party prep guides only):** The round has run since about October 2025. It is 60 minutes in CoderPad with a selectable model, and replaces one of two onsite coding rounds. interviewing.io, IGotAnOffer and Prepfully report it, but they disagree on the scope by level (E6 and below vs E7+) and on the model list. https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples (M4).

**5.2 Google.**
- **(a) Return to in-person rounds:** Google reintroduced at least one in-person round for some roles to counter AI cheating. VP of Recruiting Brian Ong said virtual interviews sped hiring by nearly two weeks but "we definitely have more work to do to integrate how AI is now more prevalent in the interview process." Sundar Pichai's comments were reported from a town hall and the Lex Fridman podcast, and reports disagree on his exact wording. The original was a CNBC report; I fetched none of these primary sources.
  - Storyboard18. https://www.storyboard18.com/brand-makers/google-to-reintroduce-in-person-interviews-amid-rising-ai-cheating-concerns-79624.htm
  - Publication date: about August 2025.
  - Tier and freshness: M3, old.
- **(b) Pilot of a Gemini-assisted interview:** Google is piloting a "code comprehension" round where candidates use Gemini on an existing multi-file codebase to read, debug, extend and optimise it. Interviewers score prompting, validation of AI output, and debugging. The pilot covers junior and mid-level roles on select US teams (Cloud, Platforms & Devices) in H2 2026, and is described as "human-led, AI-assisted."
  - Source: "Google to allow AI use in engineering interviews, signalling hiring shift", Storyboard18, citing Business Insider. https://www.storyboard18.com/amp/digital/google-to-allow-ai-use-in-engineering-interviews-signalling-hiring-shift-ws-l-97700.htm
  - Publication date: 2026-05-10.
  - Tier and freshness: M3, current.
  - **Not fetched:** the original Business Insider article and Google's on-record confirmation. Start dates conflict across secondary sources (May 2026 vs H2 2026).

**5.3 Amazon: AI banned in interviews.**
- **Policy:** Internal guidance reported by Business Insider bans generative AI during interviews "unless explicitly permitted". Violations "may result in disqualification." Interviewers were told to watch for typing while being asked questions, reading answers, and wandering eyes. A spokesperson said candidates must acknowledge they "won't use unauthorized tools."
- **Sources:**
  - ITPro. https://itpro.com/business/careers-and-training/amazon-bans-ai-tools-during-job-interviews
  - NBC News. https://www.nbcnews.com/tech/tech-news/columbia-university-student-trolls-big-tech-ai-tool-job-applications-rcna198454
- **Publication date:** about February to March 2025 (the NBC piece is 2025-03-27).
- **Tier and freshness:** M3, old.

**5.4 Anthropic: candidate AI guidance.**
- **Applications:** "Please create your first draft yourself, then use Claude to refine it."
- **Take-homes:** "Complete these without Claude unless we indicate otherwise."
- **Live interviews:** "This is all you–no AI assistance unless we indicate otherwise."
- **Source:** "Guidance on Candidates' AI Usage", Anthropic. https://www.anthropic.com/candidate-ai-guidance
- **Last updated:** 2025-07-10.
- **Tier and freshness:** M2 (first-party), old.
- **Note:** The engineering post in 4.2 shows Anthropic does allow AI on specific take-homes.

**5.5 Cheating tools and the employer response.**
- **Interview Coder (Roy Lee):** NBC reports the tool screenshots problems and generates hidden real-time solutions. Lee says it reached $170k in monthly subscriptions, that he got offers from Amazon, Meta, TikTok and Capital One, and that Columbia suspended him. "I think no form of online assessment is safe."
  - Source: "Kicked out of Columbia, this student doesn't plan to stop trolling big tech with AI", Angela Yang, NBC News. https://www.nbcnews.com/tech/tech-news/columbia-university-student-trolls-big-tech-ai-tool-job-applications-rcna198454
  - Publication date: 2025-03-27.
  - Tier and freshness: M3, old.
  - **Unverified:** The successor company Cluely raised about $20M+ (a16z) and reported 70k+ paying subscribers; this comes from secondary sources only.
- **Gartner forecast and survey:** By 2028, 1 in 4 candidate profiles worldwide could be fake (a forecast). In a Q2 2025 survey of 3,000 candidates, 6% admitted interview fraud; 62% say in-person interviews make them more likely to apply.
  - Source: Gartner press release via HR Dive. https://www.hrdive.com/news/fake-job-candidates-ai/757126/ and https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them
  - Publication date: 2025-07-31.
  - Tier and freshness: M3, old.
- **Greenhouse 2026 Candidate AI Interview Report (about employer-run AI interviewers, not cheating):** 2,950 job seekers in the US, UK, IE, DE and AU. 63% of US job seekers have had an AI interview, and 38% withdrew from a process because of one.
  - Source: https://www.greenhouse.com/blog/2026-candidate-ai-interview-report
  - Publication date: 2026-04-29 or 2026-05-06 (the page shows both).
  - Tier and freshness: M2, current.
- **Pragmatic Engineer, from interviews with 50+ hiring managers and engineers:** reports candidates using LLMs live, proxy interviewees, and suspected North Korean applicants at remote-hiring US/UK/EU companies. The free section says remote roles are "going extinct" in the UK and EU (details are paywalled).
  - Source: "Tech jobs market in 2026, part 3: hiring managers & job seekers", Gergely Orosz. https://newsletter.pragmaticengineer.com/p/tech-jobs-market-in-2026-part-3-hiring
  - Publication date: 2026-07-07.
  - Tier and freshness: M3, current.
  - **Relevance:** Fraud concern is highest exactly in the segment this candidate targets (remote, cross-border). Expect identity checks, camera-on rounds, and live follow-up questions on any take-home.

**5.6 Is LeetCode-style interviewing expanding or contracting? Evidence is mixed, and the best data is weak.**
- **interviewing.io survey (67 interviewers, 52 at FAANG):**
  - 0 of 52 FAANG respondents said their company had moved away from algorithmic questions.
  - 58% changed the kinds of questions they ask, and 21% asked harder ones.
  - About a third had caught a cheater, and 81% suspected AI cheating.
  - 67% of startup respondents said AI had meaningfully changed their process, against 0% at FAANG.
  - Over half expect algorithmic interviews to be less prominent in 2–5 years.
  - Source: "How is AI changing interview processes? Not much and a whole lot", Aline Lerner, interviewing.io. https://interviewing.io/blog/how-is-ai-changing-interview-processes-not-much-and-a-whole-lot
  - Publication date: no date on the page; it references an edit from about October 2025.
  - Tier and freshness: M3 (small, self-selected sample), old.
- **Karat survey (400 engineering leaders in the US, India and China):**
  - 71% say AI makes technical skills harder to assess.
  - 62% of organisations still prohibit AI in technical interviews.
  - US vs China: live technical interviews 79% vs 87%; AI allowed 38% vs 68%; automated code tests 63% vs 49%; take-home projects 45% vs 20%.
  - Source: "Engineering interview trends 2026", Karat. https://karat.com/engineering-interview-trends-2026
  - Publication date: 2026-01-07.
  - Tier and freshness: M3 (vendor), old (AI). The 71% may repeat Karat's 2025 report.
- **Take-homes:** Anthropic (4.2) shows take-homes are being rescoped or made AI-permitted rather than dropped. I found **no M2 dataset** showing startups systematically replacing take-homes with paid work trials. A practitioner list found 17 of 51 companies (33%) use take-homes and 5 use paid work trials. https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/06-home-assignments.md (M4, date unverified).
- **Reading:**
  - Large companies are hardening algorithmic rounds (proctoring, in-person rounds, modified questions) and adding one AI-enabled round alongside them, not instead of them (Meta, Google).
  - Startups and scale-ups are moving faster toward practical, repo-based, AI-allowed rounds (Canva, Shopify, Coinbase, interviewing.io's 67%).
  - No dataset shows algorithmic rounds disappearing.
  - For seed-to-scale-up targets, expect practical build or debug rounds, sometimes with AI allowed, plus light data-structures-and-algorithms screens. Preparation should cover both.

---

## 6. Remote hiring of India-based engineers: volume, EOR/contractor trends, competition

**6.1 Remote/hybrid share of software postings is falling in every major market. Strong primary data.**
- **Software postings, remote/hybrid share** (Indeed category "techsoftware", 7-day average). Values are for 2026-08-31 against 2025-08-31.

| Country | 2026-08-31 | 2025-08-31 | Earlier reference |
|---|---|---|---|
| US | 30.8% | 33.7% | 42.0% in Feb 2022 |
| UK | 45.9% | 49.0% | |
| Germany | 44.5% | 46.6% | |
| France | 38.8% | 42.1% | |
| Ireland | 37.9% | 45.1% | |
| Canada | 42.6% | 42.1% | Flat |

- **All US postings:** 8.4% remote/hybrid on 2026-08-31.
- **Source:** Indeed Hiring Lab Remote Tracker data repository (remote_postings_sector.csv and remote_postings.csv), CC-BY-4.0. https://github.com/hiring-lab/remote-tracker
- **Publication date:** data to 2026-08-31, refreshed monthly.
- **Tier and freshness:** M2, current.
- **Caveat:** The measure counts remote **or hybrid** keywords, so the share of postings that are **fully remote and open to someone in India** is far smaller (that is an inference; no source measures it).

**6.2 Ireland cross-check.** Software development had the highest remote/hybrid share of Irish occupations, at 47% of postings (data from late December 2025).
- **Source:** "Indeed's 2026 Ireland Jobs & Hiring Trends Report", Indeed Hiring Lab. https://hiringlab.indeed.com/uk/blog/2026/01/27/indeed-2026-ireland-jobs-hiring-trends-report/
- **Publication date:** 2026-01-27.
- **Tier and freshness:** M2, recent.

**6.3 Deel Global Hiring Report 2026 (2025 data).**
- **Sample:** More than 1M contracts at 37,000+ companies in 150+ countries.
- **Software developers:** The **#1 cross-border EOR role**; 28% of cross-border hires at top-funded startups are software developers.
- **India:** Ranked #2 for AI-trainer hiring. Deel's sponsored Raconteur piece puts India at 7.2% of specialist AI trainers.
- **Who hires in India:** SMBs are more likely than top-funded startups ($100M+ raised) to recruit in India. The top-funded startups' cross-border hires went mainly to the UK (12.2%), Canada (11.9%), Germany (8.8%) and Australia (5.8%).
- **Sources:**
  - "Global Hiring Report 2026", Deel. https://www.deel.com/global-hiring-report-2026/
  - "What Deel's data reveals about the future of global hiring in 2026", Raconteur (Deel-sponsored). https://www.raconteur.net/global-business/what-deels-data-reveals-about-the-future-of-global-hiring-in-2026
- **Publication date:** about March 2026 (no date on the page).
- **Tier and freshness:** M2 for the Deel data and M3 for Raconteur; recent.
- **Not published:** Deel gives no India-specific contractor or EOR software-engineer counts or pay.
- **Implication (inference):** Well-funded startups hire cross-border mainly into time-zone- or culture-adjacent markets. India-based hires skew toward SMBs and earlier-stage companies.

**6.4 Oyster.** India was 7% of new global hires through Oyster, behind the Philippines (9%) and the US (8%), according to Oyster's Global Hiring Trends and Impact Report, which is based on 2024 hires. 57% of companies plan to hire globally.
- **Source:** "Global Hiring: What today's global hiring data reveals…", Marine Pescher, Oyster. https://www.oysterhr.com/library/global-hiring-in-2026
- **Publication date:** 2026-01-16.
- **Tier and freshness:** M2 vendor data. The page is recent, but the data is old (2024).

**6.5 Applicant volume and competition.**
- **Ashby:**
  - More than 100M applications across 200k jobs.
  - **Over 300 applications per hire** on average, about triple 2021.
  - Candidates are about 50% less likely to get an interview than five years ago.
  - Technical roles take about 10 weeks to first fill and need nearly twice the interview time of business roles.
  - Source: Ashby press release, PR Newswire. https://www.prnewswire.com/news-releases/new-data-from-ashby-reveals-surge-in-applications-rising-selectivity-and-shifting-recruiter-workloads-302765846.html
  - Publication date: 2026-05-07.
  - Tier and freshness: M2, current.
  - Caveat: all roles, not engineering-only or remote-only.
- **Greenhouse:**
  - About **254 applicants per job ad**, with about 175k live jobs.
  - Applications per recruiter up 412%.
  - Auto-apply tools cost about "$20."
  - Source: "CEO of the top-rated hiring platform says the job market is so bad…", Orianna Rosa Royle, Fortune. https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/
  - Publication date: 2026-07-27.
  - Tier and freshness: M3, current.
- **Pragmatic Engineer anecdotes:** 800 résumés over three months for one Seattle SWE role; 1,000+ applicants per posting with about 98% unqualified (secondhand). (M3, current; see 5.5.)
- **LinkedIn remote share of applications:** Fully remote roles are a small share of postings (about 9–14%) but draw a large share of applications (about 40–52%). **Unverified:** I could not reach a primary 2026 LinkedIn source, and secondary figures conflict.
- **Reading:** Remote postings open to India are scarce and heavily applied to. Inbound applications to public remote postings have low conversion, so referrals, direct outreach and niche boards matter more (inference).

---

## 7. Compensation, FX and Indian tax, with take-home arithmetic

### 7.1 Exchange rate

**USD/INR rate.**
- **Fed H.10 (FRED DEXINUS):** **96.31 on 2026-10-02**, against 88.74 on 2025-10-02, so the rupee is about 8.5% weaker year over year.
  - Source: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXINUS
  - Tier and freshness: M2, current.
- **Trading Economics:** **96.94–96.95 on 2026-10-09**; the rupee is down 1.3% over the month and 9.2% over the year. https://tradingeconomics.com/india/currency (M3, current).
- **Cross-checks:** MTFX shows 96.73 and Investing.com 96.98 on 2026-10-09 (M3/M4).
- **Planning rate used below:** **₹96 per USD**.
- **Implication:** INR weakness raises the rupee value of USD contracts. That helps contractors, and helps employees only if the salary is indexed to USD.

### 7.2 Pay benchmarks

**India pay benchmarks (not remote-specific).**
- **Levels.fyi, Software Engineer, India, all levels:**
  - Median total comp **₹30.0–30.4 lakh**: ₹30,02,164 on 23,718 submissions (updated 2026-10-08), and ₹30,44,063 on 21,924 on the HTML page (updated 2026-10-09).
  - Percentiles: 25th ₹17.5L, 75th ₹49.3L, 90th ₹69.8L.
  - Source: https://www.levels.fyi/t/software-engineer/locations/india
  - Tier and freshness: M2, current.
  - Caveat: includes Big Tech and on-site roles, has no years-of-experience split in what I fetched, and is self-reported.
- **Levels.fyi, Bengaluru:** median ₹36.8L on 12,886 submissions, updated 2026-10-03. https://www.levels.fyi/t/software-engineer/locations/greater-bengaluru (M2, current).
- **Wellfound, India startup full-stack engineers:**
  - Average $43,042 a year; range $19k–175k; "average" tier $19k–60k; average experience about 3 years.
  - Source: https://wellfound.com/hiring-data/r/full-stack-developer-1/l/india
  - Tier and freshness: M3 (data updated weekly; period **unverified**).
  - Caveats: the currency labelling is ambiguous and the page contains an evident error in its experience data.
- **Wellfound, remote full-stack at US startups:** average $124k (range $38k–210k). Not India-specific. https://wellfound.com/hiring-data/r/full-stack-developer-1/l/remote-friendly (M3).
- **Contractor rates:** Vendor blogs (Second Talent, Omnivoo, F5 Hiring, and others) put **mid-level India contractor rates at about $25–60 per hour**. Marketplaces (Turing, Toptal, Andela) bill clients $40–150 an hour, and engineers receive less after the 30–50% platform margin.
  - Tier and freshness: M4. **Unverified**, since the vendors have a commercial interest.
  - I found no M2 dataset of remote India pay from US/EU employers.
- **EOR platform fees:** About $599–699 per employee per month for Remote and Oyster. This is the employer's cost and does not come out of the candidate's CTC. (M4 comparison sites, for example https://remote.com/blog/eor-peo/oyster-vs-remote.)

### 7.3 Income tax rules (FY 2026-27, tax year 2026-27)

**Legal framework.**
- **The Act:** The Income-tax Act, 2025 came into effect on **1 April 2026**.
  - Source: Budget 2026-27 Speech, para 99, Ministry of Finance, Government of India. https://www.indiabudget.gov.in/doc/budget_speech.pdf
  - Publication date: 2026-02-01.
  - Tier and freshness: M2, recent.
- **Slabs unchanged in Budget 2026:** Personal income-tax rates and slabs were left unchanged.
  - Source: Moneylife. https://www.moneylife.in/article/budget-202627-no-change-in-incometax-slabs-fm-offers-compliance-relief-for-individuals/79540.html
  - Publication date: 2026-02-01.
  - Tier and freshness: M3, recent.
  - Note: I searched the speech text and found no slab change.

**New-regime slabs.**
- **Rates (official page, AY 2026-27):**
  - Nil up to ₹4L
  - 5% from ₹4–8L
  - 10% from ₹8–12L
  - 15% from ₹12–16L
  - 20% from ₹16–20L
  - 25% from ₹20–24L
  - 30% above ₹24L
- **Rebate:** up to ₹60,000 where taxable income is at most ₹12L.
- **Cess:** 4% health and education cess.
- **Surcharge:** nil up to ₹50L.
- **Source:** Income Tax Department e-filing portal, "Individual – business/profession" help page. https://www.incometax.gov.in/iec/foportal/help/individual-business-profession
- **Tier and freshness:** M2, current.
- **For FY 2026-27:** The same rates carry into the new Act as section 202 (M3 sources: Bajaj Housing Finance, BankBazaar).
- **Unverified:** The rebate's section number under the 2025 Act (156 or 202).

**Standard deduction for salaried employees.** ₹75,000 under the new regime. Sources: ClearTax and Outlook Money (M3). **Not confirmed on an incometax.gov.in page.** The Taxation Laws (Amendment) Act 2025 reportedly fixed a drafting gap.

**Presumptive taxation for professionals (old section 44ADA, now section 58 of the 2025 Act).**
- **Rule:** Deemed profit is **50% of gross receipts**. The receipts limit is **₹50 lakh, or ₹75 lakh if cash receipts are no more than 5%** of total receipts.
  - Official source for the ₹75L limit: Budget 2023-24 Speech, para 134, and the Annex: "for specified professions from ₹50 lakh to ₹75 lakh… only in case… received during the year, in cash, does not exceed five per cent." https://www.indiabudget.gov.in/budget2023-24/doc/Budget_Speech.pdf
  - Publication date: 2023-02-01.
  - Tier and freshness: M2. Stale as a document, but the rule is still in force per the sources below.
- **Carry-over into section 58 of the 2025 Act:** 50% deemed profit and the ₹50L/₹75L limits carried over.
  - Source: TaxGuru, "Section 58 Presumptive Taxation Under Income Tax Act 2025", Shubham Goyal CA. https://taxguru.in/income-tax/section-58-presumptive-taxation-income-tax-act-2025.html
  - Publication date: 2026-05-28.
  - Tier and freshness: M3, current.
  - **Unverified against the Act text.** Commentary disagrees on how losses and deductions are treated under section 58.
- **Eligibility of software development (unverified):** Practitioners commonly treat it as a "specified profession" (engineering or technical consultancy). This should be confirmed with a CA.

### 7.4 GST on exporting services

- **Zero-rating:** Export of services is a zero-rated supply under **IGST Act s.16**.
- **Export conditions (IGST Act s.2(6)):** All five must hold together:
  1. The supplier is in India.
  2. The recipient is outside India.
  3. The place of supply is outside India.
  4. Payment is received in convertible foreign exchange, or in INR where RBI permits.
  5. The two parties are not establishments of the same person.
- **LUT:** A **registered** supplier can export under an LUT without paying IGST (Notification 37/2017-CT extended the LUT to all exporters).
- **Registration threshold:** Notification 10/2017-Integrated Tax (13 October 2017) exempts suppliers of inter-state services with aggregate turnover **up to ₹20 lakh** from registering. Aggregate turnover **includes exports**.
- **Sources:**
  - The provisions as reproduced in a Goa Commercial Tax circular: https://statetax.goa.gov.in/PDF/state_notif/Circulars/161_17_2021_GST_14_2021-22_GST_2021_circular.pdf
  - ICMAI course slides: https://icmai.in/upload/Taxation/Courses/CCIT_9_PPT_1512_2025_1.pdf
  - The CBIC aggregate-turnover flyer: https://cbic-gst.gov.in/hindi/pdf/e-version-gst-fliers/aggregate-turnover-in-GST_04aug2017.pdf
- **Tier and status:** M2 or M3. I **could not extract text from the CBIC PDF** (it is binary), so the CBIC wording is **unverified by direct read**.
- **Practical result:**
  - Below ₹20L of receipts, a pure exporter of services generally need not register. Practitioners disagree on this point and no official source settles it, so treat it as **unverified**.
  - Above ₹20L, register and file an LUT. GST payable is then nil.

### 7.5 Labour Codes (affects EOR/employee CTC structure)

- **The rule:** The four Labour Codes took effect on **2025-11-21**. Basic pay plus DA must be **at least 50% of remuneration**, which raises gratuity and possibly PF and lowers monthly in-hand pay by about 3–5% for many people.
- **Sources:** India Briefing (https://india-briefing.com/news/salary-structure-india-labor-code-compliance-guide-44332.html) and others. M3, recent.
- **Unverified:** Sources conflict on whether EPF is computed on the wider wage definition yet.

### 7.6 Take-home arithmetic (my calculation; assumptions stated)

**Targets.**
- ₹1.5L/month = **₹18.0L a year** net.
- ₹2.0L/month = **₹24.0L a year** net.

**Shared assumptions.**
- FY 2026-27 new regime, resident individual, under 60.
- Slabs as in 7.3, with the 12L rebate, marginal relief, and 4% cess.
- No surcharge, since income is below ₹50L.
- FX rate ₹96/USD.

**A. Contractor (sole proprietor, presumptive 50%).**
- **Assumptions:**
  - Gross receipts G are in USD, converted at a 1% FX and platform cost.
  - ₹1.5L a year of real costs: CA and GST compliance, laptop amortisation, internet, and self-paid health insurance.
  - Taxable income = 0.5 × G.
  - No PF, gratuity or paid leave.
- **Formula:** Net = 0.99G − 1.5L − tax(0.5G).
- **For ₹18L net:**
  - **G ≈ ₹19.7L.** Taxable income is ₹9.85L, under ₹12L, so **tax is ₹0** after the rebate.
  - That is **about $20,500 a year**, roughly $1,710 a month, or about $11.4 an hour at 1,800 hours a year.
  - With no costs assumed: about $18,900.
- **For ₹24L net:**
  - **G ≈ ₹26.6L.** Taxable income is ₹13.3L. Tax = ₹60,000 + 15% × ₹1.3L = ₹79,500, plus cess = ₹82,700.
  - That is **about $27,700 a year**, roughly $2,310 a month, or about $15.4 an hour.
  - G is above ₹20L, so GST registration and an LUT are needed; GST payable is still nil.
- **Pricing guidance:** Because a contractor has no paid leave, PF, gratuity or employer health cover, quote about 20–30% above these break-evens: **about $25k–27k for the ₹1.5L target and about $33k–36k for ₹2L**.
- **Market comparison:** These remain well under the vendor-reported mid-level contractor band of $25–60 an hour (M4, unverified).

**B. Employee via EOR or direct (salaried).**
- **Assumptions:**
  - Basic = 50% of CTC (Labour Codes).
  - Gratuity provision 4.81% of basic is inside the CTC and not paid monthly.
  - Standard deduction ₹75,000.
  - Professional tax ₹2,500 a year.
  - Employee PF is shown as a deduction from in-hand pay, although it is the employee's own savings.
- **B1, PF on the ₹15,000 wage ceiling** (₹21,600 a year each for employer and employee):
  - **₹18L net needs a CTC of about ₹20.9L.** Taxable income is about ₹19.4L, tax about ₹1.96L. At ₹96 this is about $21,800.
  - **₹24L net needs a CTC of about ₹29.5L.** Tax is about ₹4.29L. This is about $30,700.
- **B2, PF at 12% on full basic:**
  - **₹18L net needs a CTC of about ₹23.8L**, about $24,800. In-hand pay is lower because about ₹1.43L a year goes to the employee's own PF.
  - **₹24L net needs a CTC of about ₹34.1L**, about $35,500.
- **Market comparison:**
  - ₹21–24L CTC sits slightly above the Levels.fyi India 25th percentile and below the median (₹30L).
  - ₹29.5–34L sits at about the India median, or above it.
  - For about 3 years of experience, the ₹1.5L target is realistic. The ₹2L target needs median-or-better India pay, or a USD-indexed remote offer. This is an inference from 7.2.

**C. Contract vs employee at the same rupee net (inference from the arithmetic above).**
- The presumptive scheme makes the contractor route roughly 6–10% cheaper in gross terms at ₹18L, and about 10–23% cheaper at ₹24L, depending on PF treatment.
- The gap reflects tax only. It ignores the benefits the contractor gives up and the client's misclassification risk.
- Many US/EU startups prefer contractor agreements for India because they avoid EOR fees of about $7–8.4k a year.

**Arithmetic caveats.**
- Section 58 details are unverified against the Act text.
- Software development's eligibility as a "specified profession" is practice, not a confirmed rule.
- The GST position below ₹20L is unsettled.
- FX moves ±1% shift the USD figures by about ±$200–280.
- Calculation script: scratchpad/calc.py, which is not saved in the project.

---

## Weak or contradicting evidence (summary)

- **US software index level:** Values differ (73, 74.4, 76.1, 78.3) because they were read on different dates. FRED's 78.33 on 2026-10-02 is the latest.
- **Stack Overflow 2026 secondary figures:** "83% use AI" and "6.6% trust for important decisions" were not seen on the official page; marked unverified.
- **Meta AI round:** Level scope and model list conflict across prep sites, and there is no official Meta documentation.
- **Google Gemini pilot:** The start date conflicts (May 2026 vs H2 2026). I did not fetch the primary Business Insider article.
- **Coinbase:** The AI-code share conflicts (about 100% in the blog listing vs 50% in an aggregator).
- **LeetCode trend:** The only quantitative sources are small surveys from 2025 and early 2026. No source shows algorithmic rounds being removed at large companies.
- **Take-home to paid-trial shift:** There is no M2 evidence that it is happening at scale.
- **LinkedIn remote share of applications:** Secondary figures conflict (9–14% of postings vs 40–52% of applications); unverified.
- **India-specific remote pay:** No M2 source. The Wellfound India page has data-quality problems, and the contractor-rate sources are vendors.
- **Section 58 vs 44ADA:** Treatment of losses and deductions, and the audit trigger, are unverified.
- **GST registration below ₹20L for pure exporters:** Not settled.
- **Pragmatic Engineer's "remote going extinct in UK/EU":** The supporting details are paywalled. The Indeed tracker does show the remote/hybrid share in software falling 2–7 points year over year in the UK, DE, FR and IE, which supports the direction but not the strength of the claim.

## Sources that failed or blocked fetches

| Source | URL | What happened |
|---|---|---|
| Coinbase blog | https://www.coinbase.com/blog/interviewing-engineers-in-the-ai-era-lessons-from-a-year-of-rebuilding | HTTP 403. Only the listing and search metadata were used. |
| Computerworld, "To counter AI cheating, companies bring back in-person job interviews" | https://www.computerworld.com/article/4046269/... | HTTP 404 at the guessed URL. Not used directly. |
| CBIC aggregate-turnover flyer PDF | https://cbic-gst.gov.in/hindi/pdf/e-version-gst-fliers/aggregate-turnover-in-GST_04aug2017.pdf | Fetched, but no text could be extracted (binary). |
| 404 Media Meta article | https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/ | Paywalled. Only the opening was visible, via secondary summaries. |
| Pragmatic Engineer, part 3 | https://newsletter.pragmaticengineer.com/p/tech-jobs-market-in-2026-part-3-hiring | Paywalled after section 3. Remote-role and compensation sections not read. |
| Business Insider (Google Gemini pilot, Amazon AI ban, Meta confirmation) | none found | Primary articles not retrieved. Relied on Storyboard18, ITPro and NBC. |
| LinkedIn Jobs on the Rise 2026, India edition | none found | Not retrieved. Only news coverage. |
| LinkedIn Economic Graph remote share of applications, 2026 | none found | No primary source found. |
| Levels.fyi by-experience breakdown for India | https://www.levels.fyi/t/software-engineer/locations/india | Filter not available via fetch. Only all-levels figures. |
| Hiring Lab US remote share for software in a written report | none found | None located. Used the raw tracker CSV instead, which worked. |
| incometax.gov.in pages for the ₹75,000 standard deduction and for section 44ADA/58 | incometax.gov.in | Not found on the pages fetched. Relied on the Budget speeches and M3 tax sites. |
