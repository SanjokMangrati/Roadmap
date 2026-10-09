# Intake

Goal: a candidate profile precise enough to filter companies, judge fit, and size a curriculum. Every later phase reads this profile; nothing in it is filled by assumption.

## Step 1 — Harvest before asking

Look in the working directory for material that already answers questions:
- resume/CV (`.pdf`, `.docx`, `.md`, `.txt`): read with the pdf/docx skills
- LinkedIn export, portfolio, GitHub profile links
- an existing `interview-intelligence/candidate-profile.md` from an earlier run

Pre-fill what these answer. Ask only for fields that are missing, ambiguous, or likely outdated (a resume can be a year old: ask whether it is current).

## Step 2 — Ask

Use the AskUserQuestion tool when available: at most 4 questions per call, 2–4 options each; the candidate can always type a custom answer. Without the tool, send the same questions as one numbered plain-text list. Skip any question Step 1 already answered.

**Round 1 — target**

| Question | Options | Notes |
|---|---|---|
| Which role families are you targeting? | Backend · Frontend · Full-stack · Other (AI/ML eng, mobile, DevOps/SRE, data) | multiSelect. "Not sure" → Phase 1 compares 2–3 adjacent families and the fit check recommends one with evidence; the candidate decides. |
| What level are you aiming for? | Entry / new grad · Mid (≈2–5 yrs) · Senior (≈5+ yrs) · Staff+ | |
| Where can you work, and on what authorization? | Remote, any country · Remote, my country/region only · Hybrid/onsite in a specific city · I need visa sponsorship | Follow up for country, city, timezone limits. |
| What kind of company? | Early startup (seed–B) · Scale-up (C+) · Big tech / public · No preference | multiSelect |

**Round 2 — goals and constraints**

| Question | Options | Notes |
|---|---|---|
| What is the main goal? | First software job · Same level, better company · Level up · Pivot into a new role family | |
| When must you be interview-ready? | Under 4 weeks · 1–3 months · 3–6 months · Flexible | Ask for an exact date if one exists. |
| Hours per week for preparation? | Under 10 · 10–20 · 20–40 · 40+ | |
| Do you have specific target companies? | Yes, I'll list them · No, find matches for me | Named companies become anchors. |

**Round 3 — free text** (one plain message, since these need prose answers):

1. Current stack, with years of real use for each item.
2. Top 3 achievements: what you built, its scale, a measurable outcome, and your exact role.
3. Interview history in the last 12 months: companies, formats faced, where you passed or failed.
4. Weak areas and interview formats you struggle with.
5. What counts as a win: e.g. offer at a given company type, comp floor, role title, date.
6. Constraints: free-only resources, preferred learning format, domains or company types to avoid, comp floor, anything non-negotiable.

Probe vague answers once before moving on: "built APIs" → which APIs, what scale, what you owned; "good at React" → what you built, which hooks/patterns, what broke. Record answers as claims. Skill depth is measured later by the assessment interview in `finite-interview-curriculum`; this intake does not test.

## Step 3 — Write and confirm

Write `interview-intelligence/candidate-profile.md` using the schema below, then show the candidate a summary of at most 10 lines and ask them to confirm or correct it.

**Done when:** the candidate confirms, or their corrections are applied and re-confirmed.

## Schema

```yaml
generated: ""            # YYYY-MM-DD
sources: []              # resume path, answers, links
target:
  role_families: []
  level: ""
  goal: ""               # first-job | same-level | level-up | pivot
  named_companies: []    # anchors; may be empty
  company_types: []
  win_condition: ""      # the candidate's own words
eligibility:
  locations: []
  work_authorization: ""
  needs_sponsorship: null
  timezone_limits: ""
  work_mode: []          # remote | hybrid | onsite
experience:
  years_professional: null
  stack:
    - skill: ""
      years: null
      depth_self_rating: ""   # none | used | comfortable | strong (a claim; measured later)
  achievements:
    - what: ""
      scale: ""
      outcome: ""
      role: ""
  interview_history:
    - company: ""
      date: ""
      formats: []
      result: ""
      notes: ""
  weak_areas: []
constraints:
  deadline: ""           # exact date, or range
  hours_per_week: null
  resources: ""          # free-only | paid ok
  learning_format: []
  avoid: []
  comp_floor: ""
unspecified: []          # fields the candidate declined or could not answer
```
