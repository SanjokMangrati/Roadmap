# Resource selection rules

## Verify before recommending

A resource recalled from memory is a candidate, not a recommendation. Before it enters the curriculum:

1. **Live:** fetch the exact URL (WebFetch, or a browser tool for JS-rendered pages) and confirm it resolves to the named material. Record the verification date.
2. **Current:** for fast-moving topics (frameworks, cloud services, AI tooling, AI-assisted workflows), confirm the material matches the current major version. Use context7 for library and framework docs; check publish/update dates otherwise. Material older than the current major version, or older than 12 months for AI tooling, needs a stated reason to stay.
3. **Accessible:** matches the candidate's free/paid constraint and learning format.

Unverifiable resources are dropped, or listed as `unverified` with the reason.

## Rank candidates

Rank internally on:

1. Coverage precision: does it cover the exact subskills?
2. Depth match: does it teach the required D0–D3 level?
3. Practice quality: does it let the learner perform the target behavior in the format the target companies use?
4. Time efficiency: does it fit the budget?
5. Currentness: per the verification above.
6. Accessibility: free/paid, format.
7. Signal quality: official docs, recognized authors, or demonstrably high quality. Popularity is not evidence of fit.

Choose per topic rather than forcing one resource across everything.

For each recommended resource state exactly which curriculum nodes it covers and, for partially relevant resources, which sections to skip.
