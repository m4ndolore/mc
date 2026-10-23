# Looking up a SAM.gov notice

## Notice IDs

SAM.gov notice and solicitation numbers encode the buying office and fiscal year:

- `W91…` Army, `N00…` Navy, `FA…` Air Force, `47QF…` GSA Federal Acquisition Service
- Two year digits, e.g. `25` = FY2025
- A type letter near the end: `Z` sources sought, `R` RFP, `Q` RFQ

SAM.gov page URLs use an internal UUID, not the notice number. `sam.gov/opp/<NOTICE_ID>/view` does not work. Search first to get the UUID.

## Procedure

1. Call `search_opportunities` with the notice number as `keyword` and `sources: ["sam"]`. The MC server only indexes DoD special notices, solicitations and sources sought from the last six months, so a miss here does not mean the notice does not exist.
2. If it is not found, search `https://sam.gov/search/?index=opp&keywords=<NOTICE_ID>` in a browser if one is available. SAM.gov is a single-page app that takes 5–8 seconds to render. Check both Active and Inactive: notices stay visible about 15 days after the response deadline.
3. Open the public page `sam.gov/opp/<UUID>/view`. Search results link to `/workspace/contract/opp/…`, which needs a login: strip `workspace/contract/` to get the public page.
4. Record: title, notice ID, type, status, published date, response deadline, NAICS, set-aside, place of performance, description, attachments, points of contact, and amendment history.

## Controlled attachments

When the Attachments/Links section is empty, the attachments are usually controlled (CUI or sensitive but unclassified). Only a signed-in SAM.gov user with the right role can download them. Aggregators such as GovTribe and HigherGov cannot see them, and the public API does not return them. There is no workaround. Tell the user to:

1. Sign in to SAM.gov (free, through login.gov) and request access on the notice.
2. Email the contracting officer listed on the notice. They usually answer, especially for sources sought and RFIs.
3. Ask an APEX Accelerator (apexaccelerators.us) for free help if the process is new to them.

## Other places to look

- The `usaspending` tools: who won the predecessor contract. Use `lookup_piid` if the notice names one, or the `market-research` skill.
- GovTribe and HigherGov: forecasts, history and contacts, if the user has an account.
- A web search for the exact notice number plus title words.
