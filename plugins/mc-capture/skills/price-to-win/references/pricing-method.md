# Pricing method

## Labor mix

Start from tasks, not from a budget. These splits are sanity checks for a small company's work plan, not targets:

| Work type | Typical shape |
|---|---|
| SBIR/STTR Phase I (feasibility) | PI 20–40% of hours; 1–3 engineers or scientists doing most of the work; little management. STTR: the research institution does at least 30% of the work and the small business at least 40%. |
| SBIR Phase II or prototype | Engineering most of the hours; a test or integration role; a program manager at 5–15%; documentation and security time if the work touches government systems. |
| Software prototype under an OT | Product, engineering, design and DevSecOps; ATO or authorization support if the software runs on a government network. |
| Services or support | Labor categories named in the solicitation; match its categories exactly. |

Missing roles are as telling as extra ones: a hardware prototype with no test engineer, or an ATO-bound system with no security time.

## Rates

| Source | What the number is | How to use it |
|---|---|---|
| Company actuals | Real salary or direct rate, plus the company's fringe, overhead and G&A | Always first. |
| BLS OEWS wage | Market wage for an occupation and area, before fringe, overhead and fee | Multiply by a burden. The `igce_wage_benchmark` tool returns a range, typically about 1.8–2.2× for a small business. Use the low end for a lean company, and say which you chose. |
| GSA CALC+ rate | Fully burdened ceiling price that schedule vendors charge per hour, including profit | The market ceiling. Compare the company's burdened rate to the CALC median and 75th percentile with `price_reasonableness_check`. |

Annual wage to hourly: divide by 2,080. Productive hours per year are fewer, about 1,800–1,900 after leave and holidays; use the company's figure if it has one.

## Building the price

```
Direct labor        = Σ hours × direct rate
Fringe              = direct labor × fringe rate
Overhead            = (direct labor + fringe) × overhead rate
Other direct costs  = travel + materials + equipment + subcontracts
G&A                 = (labor + fringe + overhead + ODCs) × G&A rate
Total cost          = sum of the above
Fee or profit       = total cost × fee rate
Price               = total cost + fee
```

Companies define their indirect pools differently. Follow the company's structure when it has one. For a company without established rates, say the estimate uses a single wrap rate and name it.

For fee, DoD SBIR/STTR awards commonly allow a fee or profit on top of cost. The solicitation states whether and how much. Do not assume a percentage the solicitation does not allow.

## Evaluation basis

| Basis | What it means for price |
|---|---|
| SBIR/STTR, BAA, CSO | Technical merit drives selection. Price must be reasonable and inside the limit; a lower price rarely wins on its own. Price the work properly. |
| Best value tradeoff | Technical can outweigh price, but the gap has to be worth paying for. Target near the comparable median unless the technical advantage is clear. |
| Lowest price technically acceptable (LPTA) | The lowest acceptable price wins. Target the floor, and only bid if the floor still makes money. |
| Fixed price | The company carries cost overruns. Price the risk into the estimate and say how much. |
| Cost-reimbursement | Needs an adequate accounting system. Flag it for a small company without one. |

## Comparable awards

A comparable award has the same customer or a close one, similar scope words, similar period of performance, and the same kind of instrument. Report obligated amounts, label ceilings separately, and note when an award is a contract vehicle with many orders rather than one job. DIU and many prototype awards run through other transaction consortia and may show the consortium manager as the recipient, so their values may be missing or bundled.
