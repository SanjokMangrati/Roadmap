# Study roadmap

**Goal:** be ready by **29 October 2026** for mid-level full-stack interviews at Hyperproof, HighLevel and Drivetrain, plus five stretch companies (Gather AI, Dscout, Infisical, Metabase, Automattic).
**Budget:** about 102 hours of study over 19 days (10–28 October), with the rest of your 7 hours a day kept free for retries and applications.

## How to read this

- Topics are listed **in priority order**. Each one breaks down into subtopics, and those break down further. If something is not in this tree, you don't need it for these interviews.
- Every topic says **how deep to go**, using one of three levels:
  - **Know it:** you can explain what it is and when it matters.
  - **Use it:** you can use it in real code and spot common mistakes.
  - **Interview-ready:** you can solve new problems with it and explain your trade-offs out loud, without notes.
- Every topic ends with **Done when**: a short check you run on yourself. Pass it, then stop and move on. Fail one part, and redo only that part.
- **Skip** lists what to leave out, even if a tutorial or video tries to pull you into it.
- Time and days come from the full day-by-day plan in `study-plan.csv`.

---

## 1. Explaining your thinking out loud
**Level:** interview-ready · **Time:** about 11½ hours · **Days:** 1, 2, 8, 11, 13, 15, 16, 19
**Why first:** every live interview at all eight companies scores this, and you named it as your weakest area.

- **1.1 Coding out loud: one routine, used every time**
  - 1.1.1 Clarify the question: inputs, outputs, size limits, edge cases (empty input, duplicates, negative numbers)
  - 1.1.2 Walk through one or two small examples by hand
  - 1.1.3 Say a brute-force approach first, and its time and space cost
  - 1.1.4 Improve it, and say *why* the new approach is faster
  - 1.1.5 Write the code while saying what each part does
  - 1.1.6 Test it yourself with two edge cases before saying "done"
- **1.2 Your project stories**
  - 1.2.1 CRM system deep dive
    - how it was built (a simple boxes-and-arrows sketch)
    - five decisions you made, and what you chose *not* to do in each
    - one thing that went wrong and how you fixed it
    - real numbers: users, records, response times, team size
  - 1.2.2 SaaS product deep dive (same four parts)
  - 1.2.3 Four short stories in Situation, Task, Action, Result (STAR) form: a disagreement, a failure, going beyond your role, learning something fast
  - 1.2.4 Rehearse all six out loud, recorded, each under 3 minutes
- **1.3 Defending a design when the interviewer pushes back**
  - 1.3.1 Name the trade-off you made and the option you rejected
  - 1.3.2 When challenged, say what would change your mind
- **1.4 Four recorded mock interviews**
  - Mock 1: coding (Decode String, Word Search)
  - Mock 2: system design (URL shortener with analytics, plus three "what if" twists)
  - Mock 3: past projects and behavioral questions
  - Mock 4: final coding (Generate Parentheses, Coin Change)

**Done when:** in two mocks in a row, you ask clarifying questions before starting, never go silent for more than a minute, and state complexity or trade-offs without being asked. Each story fits in 3 minutes, and your CRM story survives five "why?" questions in a row.
**Skip:** public-speaking courses, accent coaching, more than four full mocks.
**Resource:** [Tech Interview Handbook: coding interview techniques](https://www.techinterviewhandbook.org/coding-interview-techniques/) and [behavioral interviews](https://www.techinterviewhandbook.org/behavioral-interview/)

---

## 2. JavaScript and TypeScript
**Level:** interview-ready · **Time:** about 5 hours · **Days:** 1–3
**Start with a 20-minute self-test on Day 1. If you pass it, skip this whole topic.**

- **2.1 How async JavaScript really runs**
  - 2.1.1 The event loop: call stack, microtasks (promises) vs macrotasks (timers)
  - 2.1.2 Predicting the output order of mixed `setTimeout` and promise code
  - 2.1.3 `Promise.all`, `allSettled`, `race`, `any`: what each does when one promise fails
  - 2.1.4 Error handling with `async`/`await` (try/catch, unhandled rejections)
- **2.2 Build these from scratch, with tests**
  - debounce · throttle · deepEqual · flattenObject · promiseAll · retryWithBackoff
- **2.3 TypeScript you'll actually use**
  - 2.3.1 Narrowing: `typeof`, `in`, `instanceof`
  - 2.3.2 Discriminated unions, plus the `never` check that catches a missed case
  - 2.3.3 Generics: generic functions and constraints (`<T extends …>`)
  - 2.3.4 Utility types: `Partial`, `Pick`, `Omit`, `Record`, `ReturnType`
- **2.4 Classic bugs to spot instantly**
  - losing `this` · a closure capturing a loop variable · a promise nobody awaits · `==` type coercion

**Done when:** you predict all five output-order puzzles correctly, write `promiseAll` in 15 minutes with tests, type an API response with no `any`, and find three of four planted bugs.
**Skip:** advanced type tricks (conditional and mapped types), decorators, engine internals, bundler configuration.
**Resource:** [javascript.info: async](https://javascript.info/async) and [event loop](https://javascript.info/event-loop); [TypeScript Handbook: narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

---

## 3. Data structures and algorithms (easy to medium only)
**Level:** interview-ready · **Time:** about 17 hours · **Days:** 2–6, 8, 10, 15
**Why:** Drivetrain's first round is live algorithm coding, and you're out if you fail it. Hyperproof and Metabase also include some.

Do one pattern per day: 20 minutes learning the pattern, then three problems out loud, without AI, at about 25 minutes each.

- **3.1 Arrays and hash maps:** Two Sum (1), Group Anagrams (49), Top K Frequent Elements (347)
- **3.2 Two pointers and sliding window:** 3Sum (15), Longest Substring Without Repeating Characters (3), Container With Most Water (11)
- **3.3 Stacks, including monotonic stacks:** Min Stack (155), Asteroid Collision (735), Daily Temperatures (739). *Drivetrain has asked the first two.*
- **3.4 Binary search:** Search a 2D Matrix (74), Find Minimum in Rotated Sorted Array (153), Koko Eating Bananas (875)
- **3.5 Recursion and backtracking:** Subsets (78), Permutations (46), Combination Sum (39)
- **3.6 Grids and trees (BFS and DFS):** Number of Islands (200), Binary Tree Level Order Traversal (102), Rotting Oranges (994)
- **3.7 Dynamic programming, simple and knapsack:** Climbing Stairs (70), House Robber (198), Partition Equal Subset Sum (416). *Drivetrain has asked knapsack.*
- **3.8 Intervals, heaps and nested objects:** Merge Intervals (56), Kth Largest Element (215), and comparing two nested JSON objects (a Gather AI-style task)

**Done when:** you solve each pattern's last problem alone in 25 minutes, and in Mock 4 you solve two new medium problems in 45 minutes while narrating.
**Skip:** Hard problems, advanced graphs (Dijkstra, union-find, topological sort), tries, segment trees, bit tricks, daily streaks beyond these 24 problems.
**Resource:** [NeetCode roadmap](https://neetcode.io/roadmap) (watch a video only after failing a problem for 25 minutes); problems on LeetCode (all free)

---

## 4. Building APIs with Node.js
**Level:** interview-ready · **Time:** 6 hours · **Days:** 2, 4, 12, 14
**Why:** HighLevel's deciding round is "build a working API in about an hour", reportedly with AI tools allowed.

- **4.1 REST basics**
  - 4.1.1 Naming resources (`/contacts/:id/tags`)
  - 4.1.2 The status codes that matter: 200, 201, 204, 400, 401, 403, 404, 409, 422, 500
  - 4.1.3 One consistent error format for every endpoint
  - 4.1.4 Validating input (for example with zod)
- **4.2 Pagination:** offset vs cursor, and why a cursor is safer for large or changing lists
- **4.3 Idempotency keys:** making a retried POST create only one record
- **4.4 Laying out a one-hour build:** routes → services → database layer; what to skip under time pressure
- **4.5 Four timed builds (60 minutes plus a 20-minute review)**
  - contacts with tags · social feed with cursor pagination · seat booking with holds that expire · one unseen spec (your final check)

**Done when:** in the final build, every endpoint works, bad input returns 400, the list endpoint pages with a cursor, a retried POST doesn't duplicate, at least five tests pass, and you can explain your schema in 5 minutes.
**Skip:** GraphQL servers, gRPC, API gateways, NestJS internals beyond modules.
**Resource:** [Zalando REST guidelines](https://opensource.zalando.com/restful-api-guidelines/) (naming, status codes, errors, pagination sections only); [Stripe on idempotency](https://stripe.com/blog/idempotency)

---

## 5. PostgreSQL and data modelling
**Level:** interview-ready · **Time:** about 6 hours · **Days:** 1, 6, 7, 8
**Start with a 20-minute self-test on Day 1. If you pass it, skip to 5.5 practice only.**

- **5.1 Designing tables**
  - 5.1.1 Primary keys, foreign keys, unique and not-null constraints
  - 5.1.2 Many-to-many with a join table (contacts ↔ tags)
  - 5.1.3 When to normalise and when duplication is fine
- **5.2 Indexes**
  - 5.2.1 What a B-tree index is, in one paragraph
  - 5.2.2 Composite indexes, and why column order matters
  - 5.2.3 Partial indexes and index-only scans
- **5.3 Reading a query plan**
  - 5.3.1 `EXPLAIN` vs `EXPLAIN ANALYZE`
  - 5.3.2 Sequential scan vs index scan, and estimated vs actual rows
  - 5.3.3 Lab: a 1-million-row table, before and after adding an index
- **5.4 Transactions and concurrency**
  - 5.4.1 Isolation levels: read committed (the default), repeatable read, serializable, and what each allows
  - 5.4.2 MVCC in plain words: readers don't block writers
  - 5.4.3 Preventing double booking with `SELECT … FOR UPDATE` or a unique constraint
- **5.5 SQL practice:** joins, `GROUP BY`/`HAVING`, window functions (timed, on pgexercises.com)

**Done when:** in 20 minutes you design a contacts–tags–notes schema, fix a slow query with the right index and explain why, write a join and a window query that work first time, and explain how you'd stop a double booking.
**Skip:** database internals (WAL, vacuum), replication setup, building sharding, stored procedures.
**Resource:** [Use The Index, Luke](https://use-the-index-luke.com/) (chapters 1–2 and 5); [PostgreSQL docs: EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html); [pgexercises](https://pgexercises.com/)

---

## 6. System design (mid-level product scale)
**Level:** interview-ready · **Time:** about 11½ hours · **Days:** 9, 10, 12, 13, 14
**Why:** HighLevel has a 2-hour design round; Drivetrain, Metabase and Hyperproof include design. You named it as a weak area.

- **6.1 The routine for every design question**
  - 6.1.1 Requirements: what it must do, plus numbers (users, requests per second, data size)
  - 6.1.2 Core entities (the main tables or objects)
  - 6.1.3 The API: the 4–6 main endpoints
  - 6.1.4 A high-level sketch: client, servers, database, cache, queue
  - 6.1.5 Deep dives: the two hardest parts
- **6.2 Back-of-envelope maths:** requests per second, storage per year, read vs write ratio
- **6.3 The building blocks you need**
  - 6.3.1 Choosing a database: relational vs document, and picking a partition key
  - 6.3.2 Cache: what to cache and how it goes stale (links to topic 14)
  - 6.3.3 Queue for background work (links to topic 7)
  - 6.3.4 Search index: one sentence on what it's for
- **6.4 Concurrency:** seat holds and preventing double booking
- **6.5 Handling the "what if" questions:** 10× more traffic · a service you depend on goes down · a requirement changes
- **6.6 Practice designs, out loud, each compared afterwards with a written answer**
  - HighLevel-style contacts service (millions of contacts, tags, segment search, bulk import)
  - Drivetrain-style booking app (seat holds, no double booking)
  - Hyperproof-style risk register (scheduled control tests, audit trail, roles and permissions)
  - Infisical-style one-time secret sharing (encryption, expiry, access log)
  - News feed / notifications
  - Rate limiter for a public API
- **6.7 Class-level design (2 × 45 minutes):** booking system classes; Snake and Ladders (asked at HighLevel)

**Done when:** in Mock 2, on a new prompt, you state requirements with numbers in the first 8 minutes, justify your database choice, go deep on two bottlenecks, answer all three "what ifs" with a concrete change, and name two trade-offs.
**Skip:** global multi-region systems, consensus algorithms (Raft, Paxos), "design YouTube"-scale problems.
**Resource:** [Hello Interview: delivery framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery), plus its free [Ticketmaster](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster), [News Feed](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed) and [Rate Limiter](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter) breakdowns

---

## 7. Background jobs and reliability
**Level:** interview-ready, for these subtopics only · **Time:** 4 hours · **Day:** 7
**Why:** HighLevel's job posts name retries, idempotency and queues outright; Gather AI and Infisical use queues too.

- **7.1 Delivery guarantees:** "at least once" means duplicates will happen, so you design for them
- **7.2 Idempotent workers:** store a processed-job key, so a duplicate does nothing
- **7.3 Retries:** exponential backoff, and why you add random jitter
- **7.4 Dead-letter queue:** where jobs go after failing too many times, and how to replay them
- **7.5 Transactional outbox:** saving to the database and sending a message without losing either
- **7.6 Build it:** a BullMQ worker on Redis (in Docker) with retries, an idempotency table and a dead-letter path, plus a test that sends the same job twice

**Done when:** you explain 7.1–7.5 aloud in 10 minutes without notes, your duplicate-job test shows exactly one effect, and you can talk through "the worker crashed halfway" and "the webhook arrived twice".
**Skip:** Kafka internals (partitions, offsets), RabbitMQ routing, stream processing, Temporal.
**Resource:** [AWS: timeouts, retries and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter); [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html); [BullMQ docs](https://docs.bullmq.io/)

---

## 8. Testing
**Level:** interview-ready · **Time:** 4½ hours · **Days:** 5, 13
**Why:** Hyperproof asks for a testing essay and gives a take-home; take-homes at Infisical and Metabase are graded on tests.

- **8.1 The three layers**
  - unit (one function) · integration (your API plus a real database) · end-to-end (a real browser)
- **8.2 Writing good tests**
  - 8.2.1 Name a test by the behaviour it checks
  - 8.2.2 Arrange, act, assert
  - 8.2.3 What to mock (outside services) and what to run for real (your database)
- **8.3 Tools:** Vitest; Supertest for API tests against PostgreSQL in Docker; one Playwright browser test

**Done when:** in 30 minutes you test a small module you haven't seen and one endpoint, and your tests catch all three bugs someone plants in the code.
**Skip:** test-driven development as a method, mutation-testing tools, load testing, visual regression.
**Resource:** [Vitest guide](https://vitest.dev/guide/); [The Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications); [Playwright docs](https://playwright.dev/docs/intro)

---

## 9. Working with AI coding tools
**Level:** interview-ready · **Time:** about 2½ hours (plus practice inside every API build) · **Days:** 4, 9
**Why:** HighLevel wants an "AI-native builder" and reportedly allows AI in its build round; Dscout requires daily AI tool use.

- **9.1 Directing an agent:** plan first, keep the change small, use tests to check its work
- **9.2 An instructions file (AGENTS.md or CLAUDE.md):** your stack, the commands to run, conventions, and "tests must pass"
- **9.3 Reviewing AI code like a pull request:** find three hidden bugs in each of three AI-written changes
- **9.4 Saying out loud** which code the AI wrote and how you checked it

**Done when:** you find all three hidden bugs in a fresh AI-written change within 20 minutes, and in your final API build you can name how you checked every piece of AI code you kept.
**Skip:** building your own agent, comparing AI tools, prompt-engineering courses.
**Resource:** [Claude Code best practices](https://code.claude.com/docs/en/best-practices); [AGENTS.md](https://agents.md/)

---

## 10. Debugging code you didn't write
**Level:** interview-ready · **Time:** about 4 hours · **Days:** 9, 10, 13
**Why:** Automattic's code test and Infisical's work day both drop you into an unfamiliar codebase.

- **10.1 Finding your way into a new repository:** entry points, the tests, recent commits
- **10.2 Reproduce first:** write a failing test before you change anything
- **10.3 Tools:** Node debugger breakpoints; the Chrome DevTools Performance panel
- **10.4 Three timed bug fixes (60 minutes each)** in open-source TypeScript projects, each with a pull-request description

**Done when:** you fix a bug in an unfamiliar repository within 60 minutes, talking throughout: a failing test first, the cause found with the debugger or logs rather than guessing, and a clear pull-request description.
**Skip:** setting up monitoring tools, memory-leak profiling, network-level debugging.
**Resource:** [Node.js debugging](https://nodejs.org/learn/getting-started/debugging); [Chrome DevTools: performance](https://developer.chrome.com/docs/devtools/performance)

---

## 11. React
**Level:** interview-ready · **Time:** about 7 hours · **Days:** 1, 11, 15
**Start with a 20-minute self-test on Day 1. If you pass it, do only 11.3.**

- **11.1 Common mistakes**
  - 11.1.1 Using an effect for something you can calculate during render
  - 11.1.2 Keys: why the array index breaks list state
  - 11.1.3 When `memo`, `useMemo` and `useCallback` actually help, and when they don't
- **11.2 Big lists:** a 10,000-row spreadsheet-style grid with virtual scrolling, sort, filter and inline editing; check its re-renders in the profiler (*Drivetrain builds exactly this kind of UI*)
- **11.3 Three timed builds (45 minutes each, no AI):** search box with debounce · filterable list that keeps its filters in the URL · accessible modal dialog

**Done when:** you fix a broken list component and explain all three problems in 20 minutes, and you build the debounced search box with loading, error, empty and keyboard states in 45 minutes.
**Skip:** Server Components and Next.js internals, chart libraries, CSS architecture, React Native, animation.
**Resource:** [react.dev: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect); [TanStack Virtual](https://tanstack.com/virtual/latest/docs/introduction)

---

## 12. Writing
**Level:** interview-ready · **Time:** 3 hours · **Days:** 1, 11, 13
**Why:** Hyperproof's application includes a written essay, and Automattic scores written answers as a hiring step.

- **12.1 Hyperproof's two essays** (testing and reliability; async communication). Write them and submit the real application on Day 1.
- **12.2 Pull-request descriptions:** what changed, why, one trade-off, how you checked it, all under 200 words
- **12.3 A 1–2 page design document:** background, goals, non-goals, the design, options you rejected, risks

**Done when:** the essays are submitted, each pull-request description stays under 200 words with all four parts, and the design document names two rejected options and three risks.
**Skip:** blogging, documentation sites.
**Resource:** [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)

---

## 13. Adding an AI (LLM) feature to an app
**Level:** use it · **Time:** 4½ hours · **Day:** 16
**Why:** Dscout requires that you've built one; HighLevel has AI teams; demand is growing.

- **13.1 Streaming a model's answer** into a React page
- **13.2 Tool calling:** the model calls one of your own API endpoints
- **13.3 Structured output:** check the model's JSON with zod, and show a fallback when it's wrong or the call fails
- **13.4 A half-page note:** which parts should use the AI and which should be plain code, and how you'd measure quality

**Done when:** the feature streams, makes the tool call, validates its output and handles failure, and your note decides AI vs plain code for two parts.
**Skip:** vector databases and retrieval, fine-tuning, LangChain-style frameworks, hosting models.
**Resource:** [AI SDK docs](https://ai-sdk.dev/docs/introduction), with the [Gemini free tier](https://ai.google.dev/gemini-api/docs/pricing) or [Ollama](https://ollama.com/)

---

## 14. Caching and NoSQL
**Level:** use it · **Time:** about 2 hours · **Day:** 18

- **14.1 Redis cache-aside:** reading through the cache, expiry times (TTL), clearing the cache when data changes
- **14.2 Cache stampede:** many requests rebuilding the same cache entry at once, and one way to prevent it
- **14.3 MongoDB modelling:** when to embed a document inside another and when to reference it
- **14.4 Build it:** add caching to your booking API and measure the hit rate

**Done when:** you explain read and write paths and two ways to clear stale data, choose embed vs reference for two cases, and your API shows a measured hit rate with no stale reads after an update.
**Skip:** Redis Cluster, Firestore specifics, DynamoDB design, Elasticsearch internals.
**Resource:** [Redis: cache-aside](https://redis.io/tutorials/howtos/solutions/microservices/caching/); [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)

---

## 15. Quick refreshers (you're probably already at the level needed)
**Time:** 2½ hours · **Days:** 17, 19. Take each check cold, and only study what you miss.

- **15.1 Docker and Kubernetes:** a multi-stage Dockerfile; Pod, Deployment, Service, ConfigMap and Secret in one sentence each; a CI pipeline (lint, test, build, deploy)
- **15.2 Security:** the OWASP Top 10 categories relevant to APIs; spotting a missing permission check; password hashing vs encryption
- **15.3 Product thinking:** scope a vague feature in 10 minutes: who it's for, the problem, the smallest useful version, two things you leave out, one success measure

**Skip:** Terraform, Helm charts, cloud certifications, penetration testing.
**Resource:** [Docker: get started](https://docs.docker.com/get-started/); [Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/); [OWASP Top 10](https://top10.owasp.org/)

---

## 16. Company-specific extras
**Time:** about 10½ hours in total. The last three need a written "yes, India is OK" from the recruiter first; email them on Day 1. If no yes arrives in time, skip that item.

- **16.1 Hyperproof (1 hour, Day 1):** risk register; inherent vs residual risk; control testing; SOC 2 vs ISO 27001 in one sentence each ([guide](https://hyperproof.io/resource/risk-register-key-benefits/))
- **16.2 Drivetrain (30 minutes, Day 1):** planning vocabulary (plan vs actuals, variance, driver-based models, scenarios) and one paragraph on "why Drivetrain"
- **16.3 HighLevel (3½ hours, Day 17):** Vue 3 basics (`ref`, `reactive`, `computed`, `watch`) and Pinia stores; rebuild your search box in Vue
- **16.4 Dscout (2 hours, Day 18):** add retry, edit and confidence cues to your AI feature, plus a 10-case quality check
- **16.5 Infisical (1 hour, Day 18, needs India confirmation):** secret rotation, envelope encryption, what PKI and KMS do
- **16.6 Metabase (1 hour, Day 17, needs India confirmation):** Redux Toolkit slices and selectors on your grid
- **16.7 Automattic (1½ hours, Day 12, needs India confirmation):** written application answers; how WordPress plugins hook in (actions vs filters)

Per-company interview stages are in `company-branches.md`.

---

## Not on this roadmap

If a resource leads you here, stop and note it; you don't need it for these interviews. Each item's reason, and what would bring it back, is in `rabbit-hole-parking-lot.md`.

- **Languages:** Python, Java/Spring Boot, C#, Go, Elixir, PHP beyond plugin basics
- **Frameworks:** Next.js internals, GraphQL servers, micro-frontends
- **Infrastructure:** Kafka internals, Kubernetes operators, Terraform, monitoring stacks
- **Theory:** consensus algorithms, database internals, planet-scale system design
- **Algorithms:** Hard problems, advanced graphs, tries, segment trees
- **AI:** vector databases, fine-tuning, agent frameworks, building your own agent
- **Frontend:** chart libraries, CSS architecture (Metabase only, if eligible)

---

## Day by day

| Day | Date | What you do |
|---|---|---|
| 1 | Oct 10 | Narration routine and a recorded first try · self-tests: JS/TS, PostgreSQL, React · Hyperproof essays (submit) · Hyperproof and Drivetrain domain basics · **email Infisical, Metabase, Automattic about India** |
| 2 | Oct 11 | Algorithms 3.1 · CRM and SaaS project stories · async JavaScript · first timed API build (doubles as a self-test) |
| 3 | Oct 12 | Algorithms 3.2 · build the six JS utilities · TypeScript types |
| 4 | Oct 13 | Algorithms 3.3 · REST basics · AI-tool workflow and instructions file · timed API build 2 |
| 5 | Oct 14 | Algorithms 3.4 · testing layers · write tests for build 2 |
| 6 | Oct 15 | Algorithms 3.5 · indexes · query plans and transactions · 1-million-row lab |
| 7 | Oct 16 | Background jobs: learn, build the worker, explain it · SQL practice part 1 |
| 8 | Oct 17 | Algorithms 3.6 · four more behavioral stories · SQL practice part 2 |
| 9 | Oct 18 | Design routine · Design 1 (contacts service) · review AI-written code · debugger tools |
| 10 | Oct 19 | Algorithms 3.7 · bug fixes 1 and 2 · Design 2 (booking app) |
| 11 | Oct 20 | React mistakes · 10,000-row grid · pull-request descriptions · rehearse stories |
| 12 | Oct 21 | Design 3 (risk register) · timed API build 3 · Automattic answers (if confirmed) |
| 13 | Oct 22 | **Mock 1 (coding)** · Design 4 (secret sharing) · design document · browser test · testing check · bug-fix check |
| 14 | Oct 23 | Design 5 (news feed) · Design 6 (rate limiter) · class-level design · **final API build check** |
| 15 | Oct 24 | Three React timed builds · Algorithms 3.8 · **Mock 2 (design)** |
| 16 | Oct 25 | **Mock 3 (projects and behavioral)** · AI feature: learn, build, write the note |
| 17 | Oct 26 | Vue 3 for HighLevel · Redux for Metabase (if confirmed) · Docker/Kubernetes refresher |
| 18 | Oct 27 | Caching and MongoDB · Dscout AI extras · Infisical secrets (if confirmed) |
| 19 | Oct 28 | **Mock 4 (final coding)** · security refresher · product-thinking drill |
| 20 | Oct 29 | Nothing scheduled: redo anything you failed, and send applications |

**After Day 3:** compare how long Days 1–3 actually took with the plan (about 17 hours). If you're more than 15% slower, drop items from the bottom of this roadmap first (topic 14, then the stretch-company extras in 16.4–16.6), not from the top.
