# Connectors

MC Capture connects four MCP servers on install. Every skill also works with other connectors you already use in Claude. None of these are required.

## Included with the plugin

| Server | Operator | What the skills use it for | Key |
|---|---|---|---|
| `mc-opportunities` (`api.mergecombinator.com/mcp`) | Merge Combinator | Opportunity search, topic text, alerts, defense intel, Washington briefing, events | None |
| `usaspending` (`usaspending.1102tools.com/mcp`) | [1102tools](https://github.com/1102tools-dev/federal-contracting-mcps), community, MIT | Incumbents, competitors, market size, recompete leads | None |
| `ecfr` (`ecfr.1102tools.com/mcp`) | 1102tools | FAR and DFARS clause text and definitions | None |
| `federal-register` (`federal-register.1102tools.com/mcp`) | 1102tools | Proposed and final FAR and DFARS rules, open comment periods | None |

The 1102tools servers are free and public, and they are not government services. Their hosted versions do not log searches or keep IP addresses ([privacy](https://1102tools.com/privacy)). For your own rate limits, install them locally instead: see their [setup guide](https://github.com/1102tools-dev/federal-contracting-mcps#local-or-hosted).

## Add if you have them

| Category | Connector | What it adds |
|---|---|---|
| Federal data | [SAM.gov by 1102tools](https://claude.ai/directory/sam-gov-by-1102tools) | Entity registrations and exclusions: check a teammate's or competitor's UEI and registration status. The local edition adds reps and certs and SBA certifications with a free SAM.gov key. |
| Federal data | [GSA CALC+](https://claude.ai/directory/gsa-calc-by-1102tools), [BLS OEWS](https://claude.ai/directory/bls-oews-by-1102tools) by 1102tools | Labor rates for a price volume. |
| Market intelligence | [GovTribe](https://govtribe.com) MCP, [HigherGov](https://www.highergov.com) MCP | Paid. Forecasts, contacts, vendor profiles and award history beyond public data. Needs your own API key. |
| Calendar | Google Calendar, Microsoft 365 | `find-opportunities` and `bid-review` can add close dates and TPOC windows as events when you ask. |
| Documents | Google Drive, Notion | Save a bid review or market research report, or read a draft from your drive. |
| CRM | HubSpot, Salesforce | Log a pursuit and its bid call against the company record. |

Claude asks before it writes to a calendar, document or CRM. A skill that finds no connector for a step gives you the text to paste instead.

Data you send through a connector you add is governed by that connector's own terms and privacy policy, not by MC Capture's.
