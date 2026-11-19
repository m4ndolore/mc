---
name: price-to-win
description: Estimate what a defense bid should cost and what the government has paid for comparable work, then give a price range to win. Builds a bottom-up estimate from labor rates, hours, travel and other costs, and checks it against comparable awards and the solicitation's ceiling. Use for "what should we price this at", "price to win", a cost volume or rough order of magnitude, labor rates for a proposal, whether a price is reasonable, travel costs, or fitting work inside an SBIR/STTR phase limit.
---

# Price to win

A price that is too high loses on cost. A price that is too low tells the evaluator the team does not understand the work, or leaves the company unable to deliver it. This skill builds the estimate from the work, checks it against what the government has paid for similar work, and gives a range with the reasons for each end.

## Tools

The plugin connects these servers from 1102tools (free, no key, community-maintained, not government services):

| Server | Tools | Use it for |
|---|---|---|
| `gsa-calc` | `igce_benchmark`, `price_reasonableness_check`, `keyword_search`, `vendor_rate_card` | Fully burdened hourly ceiling rates that vendors charge on GSA schedules, by labor category and experience. |
| `bls-oews` | `igce_wage_benchmark`, `get_wage_data`, `compare_metros`, `list_common_soc_codes` | What the labor market pays an occupation, nationally or in a metro area, with a burden range. |
| `gsa-perdiem` | `estimate_travel_cost`, `lookup_city_perdiem` | Lodging and meals for each trip in the work plan. |
| `usaspending` | `search_awards`, `get_award_detail`, `spending_by_category` | What comparable awards cost: the market check. |

If a server is not available, say which number you could not check and give the public source: buy.gsa.gov/pricing (CALC+), bls.gov/oes (OEWS), gsa.gov/perdiem, usaspending.gov. Never fill a rate or award value from memory.

## Inputs

Ask for what is missing:

- **The requirement:** the notice or topic, its period of performance, and any ceiling or phase limit. For SBIR/STTR, the solicitation sets the maximum for each phase and component; read it from the topic (`get_opportunity`) or the solicitation instructions, never from a general rule.
- **The work plan:** tasks, deliverables and milestones. If there is none, draft one from the topic objectives and confirm it with the user before pricing.
- **The team:** roles, the people in them, where they sit (metro area), and subcontractors or a research institution partner (an STTR requirement).
- **The company's own rates,** if it has them: salaries or direct rates, fringe, overhead, G&A, and fee. Their real rates beat any benchmark.

## Workflow

1. **Labor mix.** Turn the work plan into roles and hours per task. Use [references/pricing-method.md](references/pricing-method.md#labor-mix) for typical splits. A Phase I that is 90% principal investigator hours, or a prototype with no test engineer, is a finding.
2. **Rates.** For each role, in this order:
   - the company's actual direct rate, burdened with its actual indirect rates;
   - otherwise `bls-oews` `igce_wage_benchmark` for the occupation and metro, with the burden range it returns;
   - `gsa-calc` `igce_benchmark` for the same role and experience, as the market ceiling. A rate above the CALC 75th percentile needs a reason the evaluator will accept.
3. **Other costs.** Travel from `gsa-perdiem` `estimate_travel_cost` for each trip in the plan (test events, customer reviews, kickoff). Add materials, equipment, cloud or test range time, and subcontracts at the quotes the user has. List anything unknown as an assumption.
4. **Build the estimate:** direct labor, indirect costs, other direct costs, subcontracts, then fee. Show the arithmetic in a table so the user can change one number.
5. **Market check.** Find 3–8 comparable awards with `usaspending` `search_awards`: same agency or component, similar scope words, similar period of performance, last 5 fiscal years. For SBIR/STTR, the solicitation's phase maximum and prior awards on similar topics. Use `get_award_detail` for the value and period of each. Report obligated amounts and say which are ceilings.
6. **Price to win.** Give a range, not a point:
   - **Floor:** the lowest price that still delivers the work plan at the company's real costs. Below this, the company loses money or cuts scope.
   - **Target:** where the estimate and the comparable awards agree, adjusted for the evaluation basis (see [references/pricing-method.md](references/pricing-method.md#evaluation-basis)).
   - **Ceiling:** the solicitation limit, or the top of the comparable range.
7. **Report** in the format below. Offer the next step: `proposal-templates` for the cost volume structure, or `bid-review` if the price does not fit and the pursuit needs a fresh call.

## Report format

```
## The work being priced
<one paragraph: scope, period of performance, ceiling or phase limit and its source>

## Estimate
| Role | Hours | Rate | Source | Cost |
| ... |
| Indirects / ODCs / travel / subcontracts / fee | | | | |
| **Total** | | | | |

## What comparable work cost
| Award (PIID) | Recipient | Agency | Obligated | Period | Why comparable |

## Price to win
Floor $X · Target $Y · Ceiling $Z
<why each, and what would move the target>

## Assumptions and gaps
<every number the user should confirm>
```

## Rules

- Every rate, wage, per diem and award value comes from a tool result or from the user. Cite the source in the table. Write "not found" rather than estimate.
- Label every benchmark for what it is. CALC rates are fully burdened GSA schedule ceiling prices. OEWS figures are wages before fringe, overhead and fee. They are not comparable until the burden is applied.
- Never price above the solicitation's limit, and never quietly cut scope to fit it. If the work does not fit, say so.
- This is an estimate for planning. It is not a cost volume, an audit-ready rate build, or accounting advice. Indirect rates for a cost-type contract need the company's accounting system; point to DCAA guidance or an APEX Accelerator when that comes up.
- Rates and fees are the company's competitive information. Do not send them to any server; the tools above receive only occupations, locations, labor categories and search terms.
