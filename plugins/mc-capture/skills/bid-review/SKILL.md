---
name: bid-review
description: Steel-man and red-team a defense pursuit, an idea, or a draft proposal, then give a bid / no-bid / shape-first call with the actions that would change it. Use for "should we bid on this", "poke holes in this", "red team my proposal", "steel man this idea", a murder board, a pink or red team review, or before committing writing time to an SBIR/STTR topic, BAA, CSO or solicitation.
---

# Bid review: steel man, red team, decide

A founder's scarcest resource is writing time. This skill decides whether a pursuit deserves it, and if so, what would lose it. It argues both sides at full strength and then makes a call. It never stops at "it depends".

## Inputs

Collect before reviewing. Ask for what is missing, and read every document you are given:

- **The opportunity:** the notice or topic text. Use `get_opportunity` for an SBIR/STTR topic ID, or the notice the user shares. The evaluation criteria section matters most: Section M in a FAR-based solicitation; for DoD SBIR/STTR, technical merit, team qualifications and commercialization potential, in the order and weights the solicitation gives.
- **The company:** technology, maturity (TRL if they know it), team, past performance, customers or operators already engaged, size and ownership.
- **The thing under review:** a pursuit decision, an idea, or a draft. For a draft, review the draft against the criteria, not the idea in the abstract.
- **The field:** who already does this work for this customer. If the notice names a predecessor contract, call `lookup_piid`. Otherwise run a short `market-research` pass with the `usaspending` tools: the top recipients for the agency and technology over the last five years. Skip this for an idea with no customer named yet.
- **The clauses that bite:** when the notice cites FAR or DFARS clauses that could disqualify or cost the company, read the current text with `lookup_far_clause` from the `ecfr` server. Check DFARS 252.204-7012 and 252.204-7021 (CMMC), 252.227-7013/7018 (data rights), and 252.225-7048 (export control) when they appear.

If the user asks you to review an idea with no opportunity attached, run the same steps with "the customer who would fund this" in place of the evaluator, and name who that customer is.

## Workflow

1. **Restate the bet** in two sentences: what the government says it needs, and what the company claims it will deliver. If you cannot write this, the review stops here and that is the finding.
2. **Steel man.** Build the strongest honest case for pursuing it. See [references/review-frames.md](references/review-frames.md#steel-man). Use only facts the user gave you or the notice states.
3. **Red team.** Score it as the evaluator would, criterion by criterion, then attack it. See [references/review-frames.md](references/review-frames.md#red-team). Each weakness names the evidence that would fix it. A strong incumbent the company cannot displace or team with is a red-team finding. So is a clause the company cannot meet by award, such as a CMMC level it does not hold.
4. **Decide.** One of:
   - **Bid:** the steel man holds against the red team, and the fixes fit before the deadline.
   - **Shape first:** the fit is real but the proof is not. Talk to the TPOC or program office, get an operator letter, or answer an RFI before writing a full proposal.
   - **No-bid:** a disqualifier stands, or the fixes cannot land in time. Name the next opportunity type that would fit better.
5. **Actions.** At most five, in order, each with an owner role and a date relative to the deadline. Signal first, then action: what we learned, then what to do about it.

## Output

```
## The bet
<two sentences>

## Steel man
<the strongest case, 4–8 bullets, each tied to a fact>

## Red team
| Criterion | Evaluator score (1–5) | Weakness | Evidence that fixes it |
|---|---|---|---|
<then the kill shots: anything that would lose the bid outright>

## Call: Bid | Shape first | No-bid
<one paragraph: why, and what would change the call>

## Next actions
1. ...
```

## Rules

- Argue each side as its best advocate would. A weak steel man or a soft red team wastes the user's time.
- No flattery. Do not soften a no-bid. Say what it would cost to pursue: weeks of writing, a key person's time, a better opportunity missed.
- Every claim points at the notice, the draft, or something the user said. Mark anything you inferred as an assumption.
- Check eligibility first. A failed eligibility rule is a kill shot that ends the review: SBIR/STTR small business size and ownership, STTR research-institution partner, set-asides, clearances, facility or ITAR limits.
- Do not draft the proposal here. Offer `write-in-voice` for the sections the review says to strengthen.
- This is decision support, not legal or contracting advice. For questions about eligibility or data rights, point to the solicitation instructions, the contracting officer, or an APEX Accelerator.
