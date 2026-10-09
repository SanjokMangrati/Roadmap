"""Fetch public ATS job boards for a list of candidate company tokens.

Usage: python -I fetch_boards.py <out_dir> <date> [token_file]
Tries each token against Greenhouse, Ashby and Lever public endpoints and
saves every board that responds as <out_dir>/<slug>-<date>.json, plus
<out_dir>/_probe-<date>.json recording which endpoint worked for each token.
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

TOKENS = """
gitlab supabase posthog deel remotecom canonical sourcegraph airbyte n8n hasura appsmith
directus strapi doist buffer hotjar toggl automattic wikimedia mattermost grafanalabs elastic
kong docker vercel netlify clerk neon neondatabase planetscale railway render flyio tailscale
sentry linear replit codesandbox ghost plausible chatwoot twenty appwrite hoppscotch novu
triggerdev inngest dub documenso formbricks medusajs medusa payload payloadcms rocketchat nhost
zed zeddev cal calcom calendso tiptap liveblocks prisma convex convexdev temporal temporaltechnologies
dagster airplane retool tooljet budibase nocodb baserow outline metabase cypress playwright
browserstack postman hashicorp pulumi spacelift env0 coder gitpod daytona warp raycast
superhuman loom miro figma notion clickup airtable coda zapier make pipedream
hubspot attio folk close closeio pipedrive copper freshworks
fullstory amplitude mixpanel heap june june-so segment rudderstack jitsu
stripe paddle lemonsqueezy chargebee recurly maxio orb lago
wise revolut monzo n26 bitpanda
ably pusher stream getstream sendbird knock courier resend loops customerio
algolia meilisearch typesense weaviate qdrant pinecone chroma zilliz
huggingface langchain llamaindex anyscale modal baseten replicate together fireworksai
vapi elevenlabs deepgram assemblyai livekit daily dailyco
voiceflow intercom front helpscout gorgias crisp
tines torq drata vanta secureframe sprinto
kaizen trunk graphite codecov sonarsource snyk socket
oyster omnipresent multiplier rippling gusto justworks
toptal turing andela proxify arc lemonio
crossover x-team gunio
mozilla duckduckgo protonmail proton brave
clevertap browserstack chargebee freshworks postman hasura
fyle rocketlane atlan hevo hevodata setu
smallpdf typeform hotjar personio pitch
spotify-remote kraken bitcoin coinbase consensys chainlink alchemy
""".split()

HEADERS = {"User-Agent": "Mozilla/5.0 (research script; contact via candidate)"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def probe(token):
    tries = [
        ("greenhouse", f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true",
         lambda d: d.get("jobs", [])),
        ("ashby", f"https://api.ashbyhq.com/posting-api/job-board/{token}?includeCompensation=true",
         lambda d: d.get("jobs", [])),
        ("lever", f"https://api.lever.co/v0/postings/{token}?mode=json",
         lambda d: d if isinstance(d, list) else []),
    ]
    for ats, url, jobs_of in tries:
        try:
            data = get(url)
            jobs = jobs_of(data)
            if jobs:
                return token, ats, url, data, len(jobs)
        except Exception:
            continue
    return token, None, None, None, 0


def main():
    out_dir, date = sys.argv[1], sys.argv[2]
    toks = open(sys.argv[3], encoding="utf-8").read().split() if len(sys.argv) > 3 else TOKENS
    tokens = list(dict.fromkeys(toks))
    probe_log = {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        for token, ats, url, data, n in ex.map(probe, tokens):
            probe_log[token] = {"ats": ats, "url": url, "jobs": n}
            if data is not None:
                with open(f"{out_dir}/{token}-{date}.json", "w", encoding="utf-8") as f:
                    json.dump({"company": token, "ats": ats, "url": url,
                               "fetched": date, "data": data}, f)
    tag = os.path.splitext(os.path.basename(sys.argv[3]))[0] if len(sys.argv) > 3 else "default"
    with open(f"{out_dir}/_probe-{tag}-{date}.json", "w", encoding="utf-8") as f:
        json.dump(probe_log, f, indent=1)
    ok = {k: v for k, v in probe_log.items() if v["ats"]}
    print(f"{len(ok)} of {len(tokens)} tokens responded")
    for k, v in sorted(ok.items()):
        print(f"{k:22} {v['ats']:10} {v['jobs']}")


if __name__ == "__main__":
    main()
