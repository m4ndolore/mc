---
name: market-research
description: Research who already wins defense work in a space before a company pursues it. Finds the incumbent on a requirement, sizes up competitors and likely teammates, shows what an agency has spent on a technology area, and surfaces contracts ending soon as recompete leads. Use for "who is the incumbent", "who else wins this work", "how big is this market", "who should we team with", "what contracts are expiring", prior SBIR winners on a topic, or market research for a sources sought or RFI response.
---

# Market research: incumbents, competitors, money

Before a founder writes, they should know who the government already pays for this work and how much. This skill answers that from USAspending award data, then hands the result to `bid-review` or `find-opportunities`.

## Tools

The plugin connects the `usaspending` MCP server from 1102tools (`https://usaspending.1102tools.com/mcp`, free, no key, community-maintained, not a government service). The tools used most:

| Tool | Use it for |
|---|---|
| `search_awards` | Awards matching keywords, agency, NAICS, PSC, recipient and date filters. The main search. |
| `spending_by_category` | Top recipients, agencies, NAICS or PSC for a filter set. Market size and share. |
| `lookup_piid` | One contract or IDV by its PIID, from a notice that names the predecessor contract. |
| `get_award_detail`, `get_transactions` | Period of performance, ceiling, modifications and options on one award. |
| `get_idv_activity` | Task orders under a vehicle, to see who actually gets work on a multiple-award IDV. |
| `search_recipients`, `get_recipient_profile` | A company's federal award history, by name or UEI. |
| `search_subawards` | Who primes subcontract to. Teaming leads. |
| `autocomplete_naics`, `autocomplete_psc`, `autocomplete_awarding_agency` | Exact codes and agency names for filters. |

For ready-made research questions on these tools, see the 1102tools prompt library: https://github.com/1102tools-dev/federal-contracting-prompts (sections "Research competitors" and "Track potential recompetes").

If the `usaspending` tools are not available, say so and offer the same searches at https://www.usaspending.gov/search. Do not estimate award data from memory.

## Workflow

1. **Frame the question.** One of: the incumbent on a specific requirement; the competitive field for a technology or mission area; a single competitor or teammate; recompete leads for an agency or NAICS. Get the agency, the technology in the government's words, and any NAICS, PSC or predecessor contract number the notice gives.
2. **Resolve codes first.** Use the autocomplete tools for NAICS, PSC and agency names. Filters with the wrong agency name return nothing, and an empty result is not evidence that no one does this work.
3. **Search.** Run 2–4 `search_awards` queries with different keywords and the same agency, over the last 5 fiscal years. Then run `spending_by_category` by recipient to rank the field.
4. **Read the top awards.** For the 3–5 awards that matter, use `get_award_detail` for period of performance, ceiling and description. On an IDV, check `get_idv_activity`: a vehicle with a large ceiling and few orders is a hunting license, not revenue.
5. **SBIR history.** For an SBIR/STTR topic, search the topic's key terms with the sponsoring component. SBIR awards appear as ordinary contracts in USAspending, usually with "SBIR" or "STTR" and the phase in the description. Coverage is partial: say so, and point to https://www.sbir.gov/awards for the authoritative list of prior winners.
6. **Report** in the format below, then offer the next step: `bid-review` with the incumbent findings, or `find-opportunities` for the recompete leads.

## Report format

```
## Question
<one sentence>

## Who gets this money
| Recipient | Awards | Obligated (FY range) | Agency / office | Notes |

## The awards that matter
<3–5 bullets: PIID, recipient, value, period of performance end, one line on scope>

## What this means for <company>
<incumbent strength, open lanes, teaming candidates, timing>

## Limits
<data date from awards_last_updated, filters used, what the search could not see>
```

## Rules

- Every dollar figure, date and PIID comes from a tool result. Cite the PIID or award ID with it. Write "not found" rather than estimate.
- Obligated is money committed so far. A ceiling or potential value is not revenue. Label which one you report.
- A period of performance ending is a research lead, not a confirmed recompete. The agency may extend, exercise options, bridge, or move the work to another vehicle.
- USAspending lags and misses some data: classified work, some OTAs and consortium awards, and small purchases. DIU and many prototype awards run through OT consortia and may show the consortium manager, not the performer. Say what the search could not see.
- Call `awards_last_updated` once and report the data date in the Limits section.
- Competitor research uses public award data only. Do not speculate about a named company's finances, staff or intent beyond what the records show.
