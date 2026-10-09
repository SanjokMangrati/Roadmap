# Market research

Goal: know which roles and skills the market currently pays for, and how AI has changed the target role and its interviews, so the curriculum spends hours only on what still lands offers.

The segment is defined by the candidate profile: role families × level × eligible locations × work mode.

## 1. Demand snapshot (primary data you collect)

1. **Build a posting corpus** of current postings in the segment. Sources: public ATS endpoints (see SKILL.md) for companies in the segment, including but not limited to shortlist candidates; first-party careers pages; job boards only where their terms permit. Target N ≥ 50 when the segment allows; report the actual N whatever it is.
2. **Save raw postings** to `interview-intelligence/raw/postings/` with fetch date. Deduplicate by URL, then by company + title.
3. **Extract skill mentions with a script** (saved next to its output), using a normalization dictionary (`Postgres|PostgreSQL → postgresql`, `k8s|Kubernetes → kubernetes`). Split required vs preferred when the posting marks the sections. Count each skill once per posting.
4. **Write `skill-demand.csv`** with columns:
   `skill, skill_family, postings_mentioning, share, required_mentions, required_share, n_postings, corpus_date, segment`
5. **State corpus limits** in `market-context.md`: which companies and boards, ATS-hosted companies skewing toward startups/scale-ups, geography, and anything else that biases the sample. Claims stay within the corpus; never extrapolate it to "the market".

On a re-run, compare against the previous `skill-demand.csv`; your own dated snapshots are the strongest trend evidence available.

## 2. Trend evidence (secondary)

Search for dated, attributed data on:
- posting volume for the target role and level over time (e.g. Indeed Hiring Lab, LinkedIn Economic Graph, national labor statistics)
- entry-level versus senior hiring share
- AI/LLM skill share inside software-engineering postings
- layoffs and hiring freezes in the segment
- developer AI-tool adoption (e.g. Stack Overflow Developer Survey, GitHub Octoverse)
- compensation movement (e.g. levels.fyi), when comp matters to the candidate

Use `extended` WebSearch or the deep-research skill. Each claim records: metric, value, geography, period, source, publication date.

### Market source tiers

- **M1**: primary posting data you collected (the corpus above)
- **M2**: official statistics and platform datasets (labor bureaus, job-platform research arms, large developer surveys) with published methodology
- **M3**: reputable journalism or analyst reports citing data
- **M4**: commentary, opinion, social posts (leads only)

A trajectory verdict needs M1 or M2 support. M3 corroborates; M4 never decides.

## 3. AI shift: the role

For each target role family, establish with evidence:
- which tasks employers now expect to be AI-assisted, per postings and first-party engineering writing
- which new competencies appear in postings (AI coding tools, reviewing/verifying generated code, LLM API integration, retrieval, evals, agents, AI security), with share from the corpus
- which role families are growing or shrinking (e.g. AI engineer, product engineer, entry-level SWE), from M1/M2 data
- what employers say they now weight more heavily (review, debugging, system reasoning, product judgment), quoted and sourced

## 4. AI shift: the interview

- Company policies on AI tools in interviews: allowed, banned, proctored, or a dedicated AI-assisted round. First-party sources first.
- Format changes: take-homes replaced or rescoped, live and onsite rounds added, work trials, anti-cheating measures. Date each change.
- Whether algorithm-style rounds are expanding or contracting in the segment, from dated evidence only.

## 5. Trajectory verdicts

Assign one verdict per skill family:

| Verdict | Criteria |
|---|---|
| `rising` | Share grew against a dated baseline in your corpus, or ≥2 independent M1/M2 sources show growth within 12 months |
| `stable` | Present at a similar share; no credible decline evidence |
| `shifting` | Still demanded or tested, but its form changed (e.g. coding rounds now permit AI; emphasis moved from writing code to reviewing it) |
| `declining` | Falling share across ≥2 independent M1/M2 sources, or displaced by a named successor (cited) |
| `insufficient-data` | Anything that meets none of the above. This is the default when evidence is thin. |

**Interview reality beats market trend.** A skill that a target company's current process still tests stays required for that company, whatever its market trajectory. Record both facts.

## `market-context.md` structure

1. Snapshot date; segment definition; corpus N and composition; corpus limits.
2. Demand summary: top skills by share, required vs preferred.
3. Trend findings, each sourced and dated.
4. AI shift: the role.
5. AI shift: the interview.
6. Trajectory verdict table with evidence per row.
7. Implications for this candidate, stated as data (e.g. `entry-level postings: 6 of 112 (5%)`; `TypeScript in 71% of postings; candidate has 0.5 yrs`).
8. Open questions and evidence gaps.
