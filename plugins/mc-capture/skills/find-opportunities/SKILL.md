---
name: find-opportunities
description: Find open and upcoming defense funding opportunities (DoD SBIR/STTR, DARPA, DIU, GoColosseum, Ratio Exchange, SAM.gov) that fit a company's technology, and look up a specific notice or topic. Use when someone asks what they could bid on, what is open for a technology or mission area, about a SAM.gov notice ID or SBIR topic code, or for defense intel and events that bear on a pursuit.
---

# Find defense opportunities

Turn "what could we bid on?" into a short, ranked list the user can act on this week. Every record comes from a public listing and can be stale, so each answer ends with the links to check.

## Tools

The plugin connects the `mc-opportunities` MCP server (`https://api.mergecombinator.com/mcp`):

| Tool | Use it for |
|---|---|
| `search_opportunities` | Keyword search across all six sources. `status` defaults to active (open, closing soon, pre-release). |
| `get_opportunity` | Full text of one SBIR/STTR topic by `topicId`. Other sources: open the record's `url`. |
| `defense_intel_feed` | Recent defense news, for context on a program or agency. |
| `washington_briefing` | Today's policy briefing. |
| `events_outlook` | Industry days and events this month. |

If the tools are not available (the connector is off, or the client does not load plugin MCP servers), fetch the same data from `https://api.mergecombinator.com/api/opportunities?keyword=<term>&status=active` and say that you used the public API.

## Workflow

1. **Profile the company.** Ask only for what you do not already have: the technology in one sentence, the mission problem it solves, its maturity (lab, prototype, fielded), company size and ownership (SBIR/STTR is for US small businesses), and any clearance or facility limits. Two or three sentences from the user is enough to start.
2. **Search wide, then narrow.** Run 3–6 searches with different terms: the technology ("edge inference"), the mission ("counter-UAS"), the user's words, and the government's words for the same thing ("autonomy", "C-sUAS", "sensor fusion"). Agencies rarely use the founder's vocabulary.
3. **Read before ranking.** For each plausible SBIR topic, call `get_opportunity` and read the objective and phase descriptions. For other sources, open the notice. Drop anything the description rules out.
4. **Rank by fit and time.** Put first the records where the company's technology answers the stated need and the close date leaves time to write. A Phase I proposal usually needs 3–6 weeks. Flag anything closing in under 14 days.
5. **Report.** Use the format below. Offer the next step: `bid-review` on the best one, or an alert with `opportunity-alerts` so new matches arrive weekly.

## Report format

A table, best fit first, at most 8 rows:

| Opportunity | Source / agency | Closes | Why it fits | Watch out |
|---|---|---|---|---|

Under the table:

- **Pre-release topics:** DoD SBIR/STTR topics in pre-release allow direct questions to the Technical Point of Contact (TPOC). Once a topic opens, questions go only through the DSIP Topic Q&A. If a strong fit is in pre-release, say so first: that window is the highest-value action available.
- **Links:** one per row, and the line "Confirm the deadline, eligibility and current version on the linked notice before you commit."

## Rules

- Never invent a topic number, notice ID, deadline or dollar figure. If a field is missing, write "not listed".
- `estimatedValue` on SBIR records is an estimate from the phase, not the award amount. Label it as an estimate.
- Status and deadlines come from each source and can lag. If a listing looks expired or contradictory, say so.
- SBIR/STTR authorization and component rules change. When eligibility or funding levels matter to the decision, tell the user to check the current solicitation instructions on dodsbirsttr.mil and sbir.gov.
- Keep the list short. Ten weak matches hide the two that matter.

## Looking up a specific SAM.gov notice

For a notice ID, solicitation number or "controlled attachments" question, read [references/sam-gov.md](references/sam-gov.md).
