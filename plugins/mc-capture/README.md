# MC Capture

A Claude plugin for defense founders and small businesses. It finds funding opportunities that fit your technology, sends you new ones every week, and argues both sides of a pursuit before you spend weeks writing.

## Skills

| Skill | What it does |
|---|---|
| `find-opportunities` | Searches open and upcoming DoD SBIR/STTR, DARPA, DIU, GoColosseum, Ratio Exchange and SAM.gov opportunities and ranks them against your company. Looks up a SAM.gov notice by ID. |
| `opportunity-alerts` | Sets up a weekly email of new matches. You confirm by email before anything is sent. |
| `market-research` | Finds the incumbent, sizes up competitors and teammates, shows what an agency spends on a technology area, and lists contracts ending soon, from USAspending award data. |
| `bid-review` | Steel-mans and red-teams a pursuit, idea or draft against the evaluation criteria, the incumbent and the clauses that apply, and gives a bid, shape-first or no-bid call with next actions. |
| `write-in-voice` | Drafts proposal sections, abstracts and emails in your own voice, and builds your voice profile from samples of your writing. |

## MCP servers

| Server | Tools the skills use |
|---|---|
| `mc-opportunities` (`api.mergecombinator.com/mcp`), run by Merge Combinator | `search_opportunities`, `get_opportunity`, `defense_intel_feed`, `washington_briefing`, `events_outlook`, `create_alert` |
| `usaspending` (`usaspending.1102tools.com/mcp`) | `search_awards`, `spending_by_category`, `lookup_piid`, `get_award_detail`, `get_idv_activity`, `search_recipients`, `search_subawards` |
| `ecfr` (`ecfr.1102tools.com/mcp`) | `lookup_far_clause`, `find_far_definition` |
| `federal-register` (`federal-register.1102tools.com/mcp`) | `open_comment_periods`, `far_case_history`, `search_documents` |

The `usaspending`, `ecfr` and `federal-register` servers are free, keyless, open-source servers from [1102tools](https://github.com/1102tools-dev/federal-contracting-mcps). Merge Combinator does not run them. [CONNECTORS.md](CONNECTORS.md) lists them and the other connectors that work with these skills: SAM.gov entity lookup, GovTribe, HigherGov, Google Calendar, Drive, Notion and HubSpot.

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

The skills send data to the MCP servers above and to the services below. Each one receives a public notice number, contract number, company name or search term, never your documents or personal data:

| Service | When | What it receives |
|---|---|---|
| 1102tools servers (`usaspending`, `ecfr`, `federal-register`) | `market-research`, `bid-review` | Agency, keyword, NAICS, PSC, contract number, company name or clause number |
| `api.mergecombinator.com/api/opportunities` (REST) | `find-opportunities`, only if the connector is unavailable | Search terms and filters |
| sam.gov | `find-opportunities`, looking up a specific notice, if Claude has web access | The notice number |
| govtribe.com, highergov.com, fpds.gov | Same, when SAM.gov has too little detail | The notice number or title |
| Web search | Same | The notice number and title words |

Listings come from public sources and can be out of date. Confirm deadlines and eligibility on the notice before you commit. This is decision support, not legal or contracting advice.
