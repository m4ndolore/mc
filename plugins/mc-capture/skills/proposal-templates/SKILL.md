---
name: proposal-templates
description: Lay out a compliant defense proposal or response before anyone writes it. Produces the outline, required sections, page budget and compliance checklist for DoD SBIR/STTR Phase I and II proposals, DIU CSO solution briefs, DARPA and other BAA abstracts and white papers, innovation-unit pitch submissions, sources sought and RFI responses, and capability statements. Use for "how do I structure this proposal", "what volumes does DSIP need", "outline a solution brief", a compliance matrix, a capability statement, or answering an RFI.
---

# Proposal templates

Evaluators score what the solicitation asked for, in the order it asked. Most small-business proposals lose points on structure before anyone reads the technology: a missing section, a page over the limit, an answer filed under the wrong heading. This skill builds the skeleton first, from the solicitation itself, and leaves the writing to `write-in-voice`.

## Workflow

1. **Identify the instrument.** Read the notice or topic (`get_opportunity` for an SBIR/STTR topic; the notice the user shares otherwise) and decide which template applies:

   | The notice is | Template |
   |---|---|
   | DoD SBIR or STTR topic | [references/sbir-sttr.md](references/sbir-sttr.md) |
   | DIU Commercial Solutions Opening, or another CSO or OT call | [references/other-transactions.md](references/other-transactions.md#diu-commercial-solutions-opening) |
   | DARPA or other broad agency announcement | [references/other-transactions.md](references/other-transactions.md#broad-agency-announcements) |
   | AFWERX, SOFWERX, xTech, Ratio Exchange or other innovation-unit challenge | [references/other-transactions.md](references/other-transactions.md#innovation-unit-challenges) |
   | Sources sought, RFI, request for white papers, or "tell us about your company" | [references/rfi-response.md](references/rfi-response.md) |

2. **Read the governing instructions.** The solicitation and the component's instructions override every template here. Extract page and slide limits, font and margin rules, required volumes or sections, the evaluation criteria and their order, the submission portal, the deadline with its time zone, and anything that is grounds for rejection. Quote each rule with its section number.
3. **Build the outline.** Use the template's structure, renamed and reordered to mirror the evaluation criteria. Under each heading, write one line saying what goes there and which criterion it answers.
4. **Budget the pages.** Split the page or slide limit across sections in proportion to evaluation weight. The technical approach and the evidence behind it get the most space; boilerplate gets the least.
5. **Compliance matrix.** One row per "shall" or required item: requirement, source section, where the proposal answers it, status. See the format below.
6. **Hand off.** Offer `write-in-voice` to draft sections into the outline, `price-to-win` for the cost volume, and `bid-review` (red team) once a full draft exists.

## Output

```
## <Instrument> response: <topic or notice number>
Deadline: <date, time, time zone> · Portal: <where it is submitted> · Limit: <pages or slides, and what counts>

## Outline
1. <Section> (<pages>) — answers <criterion>. <what goes here>
...

## Compliance matrix
| # | Requirement (quoted) | Source | Answered in | Status |

## Rejection risks
<every rule that gets a proposal thrown out unread>

## Still needed from the team
<documents, letters, registrations, data>
```

## Rules

- The solicitation wins. When it conflicts with a template, follow the solicitation and say so. Templates here describe typical structures as of 2026 and can be out of date.
- Never invent a page limit, deadline, volume name or criterion. If the notice does not state it, write "not stated" and tell the user where to find it (the component instructions, the BAA, or the contracting officer).
- Registrations take time and block submission: SAM.gov (UEI) for every federal award, plus the SBA company registry and a DSIP account for DoD SBIR/STTR. Flag any the user lacks, with the lead time, in "Still needed".
- Keep CUI, export-controlled and proprietary markings exactly as the solicitation and the company require. Mark proprietary pages with the restrictive legend the solicitation specifies.
- Do not draft section text here beyond one-line placeholders. Drafting is `write-in-voice`, so the user's own voice and evidence fill the outline.
