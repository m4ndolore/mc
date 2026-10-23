# MC Capture

A Claude plugin for defense founders and small businesses. It finds funding opportunities that fit your technology, sends you new ones every week, and argues both sides of a pursuit before you spend weeks writing.

## Skills

| Skill | What it does |
|---|---|
| `find-opportunities` | Searches open and upcoming DoD SBIR/STTR, DARPA, DIU, GoColosseum, Ratio Exchange and SAM.gov opportunities and ranks them against your company. Looks up a SAM.gov notice by ID. |
| `opportunity-alerts` | Sets up a weekly email of new matches. You confirm by email before anything is sent. |
| `bid-review` | Steel-mans and red-teams a pursuit, idea or draft against the evaluation criteria and gives a bid, shape-first or no-bid call with next actions. |
| `write-in-voice` | Drafts proposal sections, abstracts and emails in your own voice, and builds your voice profile from samples of your writing. |

The plugin connects Claude to the `mc-opportunities` MCP server at `https://api.mergecombinator.com/mcp`. Its tools: `search_opportunities`, `get_opportunity`, `defense_intel_feed`, `washington_briefing`, `events_outlook`, `create_alert`.

## Install

**Claude Code:**

```
/plugin marketplace add m4ndolore/mc
/plugin install mc-capture@mc
```

**Connector only:** in claude.ai, add a custom connector with the URL `https://api.mergecombinator.com/mcp` to use the tools without the skills.

## Data handling

- Searches and topic lookups go to Merge Combinator's opportunities service. They are not stored against you.
- An alert stores your email address and keywords until you unsubscribe. Nothing is emailed until you click the confirmation link.
- Documents you share for a bid review or a draft stay in your conversation. The plugin does not send them anywhere.

Read the full [Privacy Policy](PRIVACY.md) and [Terms of Service](TERMS.md).

## Other services the skills use

The skills send data only to the `mc-opportunities` connector, with these exceptions. Each one receives a public notice number or search term, never your documents or personal data:

| Service | When | What it receives |
|---|---|---|
| `api.mergecombinator.com/api/opportunities` (REST) | `find-opportunities`, only if the connector is unavailable | Search terms and filters |
| sam.gov | `find-opportunities`, looking up a specific notice, if Claude has web access | The notice number |
| govtribe.com, highergov.com, fpds.gov | Same, when SAM.gov has too little detail | The notice number or title |
| Web search | Same | The notice number and title words |

Listings come from public sources and can be out of date. Confirm deadlines and eligibility on the notice before you commit. This is decision support, not legal or contracting advice.
