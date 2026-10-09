# Automattic: Experienced Software Engineer

Researched 2026-10-09. **Abbreviated file:** the dedicated research agent was stopped before it finished, at the candidate's request to save usage. Everything below comes from the live first-party posting (S1) and Automattic's "How we hire" page (S2). Candidate reports, the separate developer-hiring guide, AI policy and 2025 layoff details were **not researched**.

## 1. Summary

- **Role:** Experienced Software Engineer, an evergreen worldwide posting, updated 2026-09-21 and live today (S1).
- **Eligibility: likely pass, India not named.** The posting says "We're always looking for talented and experienced engineers worldwide" and mentions a "global workforce in over 70 countries" (S1). The hiring page says "1,410 Automatticians in 83 countries" (S2). No source fetched names India or states employment type (employee, employer-of-record or contractor). Confirm with the recruiter.
- **Pay: published and global.** "$70,000-$170,000 USD. Please note that salary ranges are global, regardless of location, and we pay in local currency" (S1). The bottom of the range ($70,000, about ₹67 lakh a year at ₹96 per US dollar) is far above the ₹1.5–2 lakh per month take-home target.
- **Process (official, generic):** application with heavily weighted written questions, then a skills assessment, then a Slack text interview or a 30–60-minute video interview, then a code test on existing code or a trial of up to 20 hours of real work, then an executive interview and CEO approval (S1, S2).
- **AI policy for candidates: unknown.** Automattic says it "may use automated tools to help evaluate, score, match, or verify candidates" (S2).
- **Fit: stretch (preliminary).** The main gaps are PHP/WordPress, demonstrated "experience working at scale", and written depth in application answers.

## 2. Hard filters

- **Eligibility: likely pass, India not named.** Quotes: "engineers worldwide"; "global workforce in over 70 countries" (S1); "1,410 Automatticians in 83 countries" (S2). The page "To see a full list of benefits by country, consult our Benefits Page" was not fetched, so India-specific employment terms are unverified.
- **Hiring now: pass.** The Greenhouse posting at https://job-boards.greenhouse.io/automatticcareers/jobs/5862239 was live, updated 2026-09-21 (S1).
- **Travel:** "Are open and able to travel 3-4 weeks per year to meet up with your teammates in person" (S1). This is a likely requirement and needs a passport and visas.

## 3. Current role requirements (S1)

| Item | Label |
|---|---|
| Production experience with several programming languages, frameworks and paradigms | required |
| "We mostly use PHP and JavaScript… we expect you to be comfortable with the idea of becoming an expert in these languages, even if being one isn't a requirement to apply" | required (comfort); expertise preferred |
| "Experience working at scale – it can be on the backend and performance side, or via the complexity of interacting with a multi-million diverse userbase" | required |
| Debugging as "a fun challenge"; understanding layers of abstraction above and below your work | required (inferred from posting language) |
| Care for quality and detail; abstraction weighed against its cost | required (inferred from posting language) |
| Willing to travel 3–4 weeks per year | required |
| AI in product and in daily development workflows ("AI is at the heart of many new product developments and powers a lot of our day-to-day development workflows") | inferred from repeated job language |
| Peer code review, continuous integration, deploying many times daily | inferred from repeated job language |
| Years of experience | not stated ("Experienced" in the title) |

Products: WordPress.com, WooCommerce, Gutenberg (block editor, React-based), Tumblr, Jetpack, Beeper, Day One, Pocket Casts.

## 4. Interview stages

| # | Stage | Format | Timebox | AI policy | Competencies | Evidence quality | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Application | Resume, cover letter and application questions; "we are paying extra attention to your answers… They are a significant part of the hiring process" | not stated | unknown | written communication, motivation, relevant experience | official | S1, S2 |
| 2 | Skills assessment | Assessment after the application if you advance; format not described | not stated | unknown | not stated | official (existence only) | S2 |
| 3 | Initial interview | Slack text interview for most roles, or a 30–60-minute video interview | 30–60 min (video) | unknown | communication, experience, fit | official | S2 |
| 4 | Practical test or trial | A shorter code test on existing code (such as a WordPress plugin), or a trial of up to 20 hours on real work; "Most candidates finish within a week or so"; pay not stated on this page | up to 20 hours | unknown | working in an existing codebase, code quality, written communication, debugging | official | S2 |
| 5 | Final review | Many teams hold a final interview with an executive leader; CEO approval can take "a few days to a month" | not stated | unknown | values, impact | official | S2 |
| 6 | Offer | HR discusses compensation and start date | — | — | — | official | S2 |

## 5. Stage-by-stage evaluation targets

- **Application:** concrete written answers showing debugging stories, quality obsession and scale. These are reviewed as a full hiring step.
- **Text interview:** clear, structured written answers in real time on Slack. This suits a candidate who struggles to narrate aloud, but it still requires explaining reasoning, in writing.
- **Code test or trial:** read and change unfamiliar PHP/JavaScript (WordPress plugin code), work through a real task, and communicate progress in writing.

## 6. Competency taxonomy

- **Languages:** PHP (WordPress plugin and hook model), JavaScript/TypeScript, React (Gutenberg).
- **Working in existing code:** reading unfamiliar code, debugging, layers of abstraction.
- **Scale and performance:** backend performance or large user bases.
- **Engineering practice:** peer code review, continuous integration, frequent deploys.
- **Written, async communication:** application answers, the Slack interview, trial updates.

## 7. Process changes and history

Not researched. The "How we hire" page shows no last-updated date (S2).

## 8. Candidate-report findings

Not researched (agent stopped).

## 9. Fit check

**Verdict: stretch (preliminary).**
- **Gap: PHP/WordPress.** It is the main backend language; the candidate reports none (S1).
- **Gap: "experience working at scale".** Not evidenced in the candidate profile (scale of the candidate's CRM and SaaS work is unspecified).
- **Gap: written depth.** Application answers are weighted like an interview step (S1).
- **Strength:** the text-based interview and asynchronous trial reduce the weight of explaining aloud, which is the candidate's stated weak area (S2).
- **Strength:** the global pay range far exceeds the target (S1).
- **Not checked:** layoffs or hiring trajectory in 2025–2026, and how crowded the applicant pool is (a well-known brand suggests a crowded pool; inference).

## 10. Exclusions and unknowns

- Whether India hires are employees, employer-of-record hires or contractors.
- Whether the trial is paid, and at what rate (not on the page fetched).
- AI policy for candidates in the code test or trial.
- Candidate reports, the separate "How we hire Developers" guide, and 2025–2026 layoffs: not researched.

## 11. Source ledger

```yaml
company: "Automattic"
anchor: false
match:
  hard_filters:
    eligibility: "likely pass; 'engineers worldwide', 83 countries; India not named"
    hiring_now: "pass; https://job-boards.greenhouse.io/automatticcareers/jobs/5862239"
  soft_dimensions:
    - dimension: "work mode: fully remote, async, text-based interview"
      evidence: [S1, S2]
    - dimension: "pay: global range $70k-170k paid in local currency"
      evidence: [S1]
    - dimension: "interview style: trial on real work instead of algorithm rounds"
      evidence: [S2]
fit:
  verdict: "stretch"
  preliminary: true
  gaps:
    - gap: "PHP/WordPress"
      evidence: [S1]
    - gap: "experience working at scale"
      evidence: [S1]
    - gap: "written application depth"
      evidence: [S1]
role:
  title: "Experienced Software Engineer"
  url: "https://job-boards.greenhouse.io/automatticcareers/jobs/5862239"
  seniority: "experienced (years not stated)"
  compensation: "$70,000-$170,000 USD, global, paid in local currency"
  verified_date: "2026-10-09"
process:
  url: "https://automattic.com/how-we-hire/"
  verified_date: "2026-10-09"
  stages:
    - {id: "1", name: "Application", format: "resume, cover letter, weighted questions", timebox: "", ai_policy: "unknown", competencies: ["written communication"], evidence_quality: "official", sources: [S1, S2]}
    - {id: "2", name: "Skills assessment", format: "not described", timebox: "", ai_policy: "unknown", competencies: [], evidence_quality: "official", sources: [S2]}
    - {id: "3", name: "Initial interview", format: "Slack text interview or 30-60 min video", timebox: "30-60 min", ai_policy: "unknown", competencies: ["communication", "experience"], evidence_quality: "official", sources: [S2]}
    - {id: "4", name: "Code test or trial", format: "code test on existing code or up to 20-hour trial", timebox: "up to 20 hours", ai_policy: "unknown", competencies: ["existing codebase", "debugging", "written communication"], evidence_quality: "official", sources: [S2]}
    - {id: "5", name: "Final review", format: "executive interview; CEO approval", timebox: "", ai_policy: "unknown", competencies: ["values"], evidence_quality: "official", sources: [S2]}
  changes: []
requirements:
  explicit_required: ["several languages/frameworks in production", "comfort becoming expert in PHP and JavaScript", "experience at scale", "travel 3-4 weeks per year"]
  explicit_preferred: []
  inferred_repeated: ["debugging", "quality and detail", "peer code review", "continuous integration"]
  ai_expectations: ["AI powers day-to-day development workflows (posting language)"]
uncertainty:
  - {claim: "India-based work is allowed", reason: "India not named; 83 countries stated", confidence: "medium"}
  - {claim: "trial is paid", reason: "not stated on fetched page", confidence: "low"}
sources:
  - {id: "S1", url: "https://job-boards.greenhouse.io/automatticcareers/jobs/5862239", title: "Experienced Software Engineer (Greenhouse posting)", tier: 1, published_or_updated: "2026-09-21", accessed: "2026-10-09", freshness: "current", supports: ["eligibility", "pay", "requirements", "travel"]}
  - {id: "S2", url: "https://automattic.com/how-we-hire/", title: "How we hire", tier: 1, published_or_updated: "unknown", accessed: "2026-10-09", freshness: "unknown", supports: ["process stages", "automated screening tools", "83 countries"]}
```
