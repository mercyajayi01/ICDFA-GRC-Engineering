# GRC103 Practical Lab: Ransomware Risk Treatment Decision Case

---

## Overview

This folder holds my work for Module 3, Lab 2 of GRC103. In this lab I acted as a GRC risk advisor to Northbridge Community Health, a fictional three-clinic provider with a $100,000 first-year budget, and had to decide how to spend it against the threat of ransomware.

The case is built on the 2021 ransomware attack on Ireland's Health Service Executive (HSE). I used two facts from the official HSE account as my evidence, and kept them clearly separate from the Northbridge conditions the lab gives me, which are fictional. This is a desk-based exercise: no live systems, virtual machines or real organisations were involved.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `Northbridge Community Health Ransomware Risk Treatment Report.pdf` | The report: evidence, risk register, treatment decisions, insurance calculations, change response, 30-day plan and board memo |
| `Northbridge_Risk_Treatment_Workbook.xlsx` | The editable spreadsheet: initial register, revised register, budget (initial and revised) and insurance calculations, with live formulas |

## What is in the report

| Section | What it holds |
|---|---|
| 1. Scenario, Method and Evidence | The scoring scale, the two real HSE facts with their source, and the Northbridge assumptions kept separate |
| 2. Initial Risk Register | Four risks, each with asset, threat, weakness, owner, likelihood, impact, score and the reason for the rating |
| 3. Treatment Selection and Budget | The options chosen and rejected, with the initial and revised decisions side by side, plus the initial decision record and a time-limited acceptance |
| 4. Insurance Calculations | The payment formula applied to a $180,000 and a $400,000 loss, with each step shown, and what happens if a claim is excluded |
| 5. Change Event, Revised Decision and Residual Risk | The failed restoration test and price change, the revised decision record, and each risk's score now and as a proposed residual |
| 6. 30-Day Treatment Plan | Dated actions with an owner, a cost where there is one, and a test for whether each action worked |
| 7. Board Memo | The decision I am asking the board to make, the budget, continuity priorities and the risks that remain |
| 8. Limitations | Why the scores and costs should be read as classroom judgement, not measurement |

## What I did

- Read the lab brief and sorted what I was allowed to claim into two groups: real HSE facts, and fictional Northbridge conditions.
- Scored four risks (service disruption, sensitive-data loss, supplier exposure and delayed detection) on likelihood and impact, gave each one an owner, and wrote the reason behind every rating.
- Chose a set of treatments within the $100,000 budget, said why I rejected the others, and recorded one time-limited risk acceptance.
- Worked through the insurance payment formula by hand for two loss amounts, then built the same calculations as live formulas in the spreadsheet.
- Applied the change event (a failed restoration test, paper bookings that last only four hours, and one option rising in price), revised my decision, and recorded what changed and what I deferred.
- Wrote a 30-day plan and a short board memo.

## Key results

| Risk | Initial score | After the change event | Proposed residual |
|---|---|---|---|
| Service disruption | 20 (Critical) | 20 (Critical) | 10 (High) |
| Sensitive-data loss | 20 (Critical) | 20 (Critical) | 15 (High) |
| Supplier exposure | 16 (High) | 16 (High) | 4 (Low) |
| Delayed detection | 20 (Critical) | 20 (Critical) | 12 (High) |

| Decision | Spent | Held back |
|---|---|---|
| Initial | $90,000 | $10,000 contingency |
| Revised | $80,000 | $20,000 reserve for fixing and re-testing recovery |

| Insurance case | Insurer pays | Northbridge pays | Total first-year outlay |
|---|---|---|---|
| $180,000 loss | $155,000 | $25,000 | $45,000 |
| $400,000 loss | $250,000 | $150,000 | $170,000 |

- No score has dropped yet after the change event. The restoration test failed, and I did not count any control as working until it passes its own test.
- In the revised decision I deferred cyber insurance. It pays money after the damage is done, but it cannot bring the clinics back up, and recovery was the urgent gap.
- If an insurance claim is excluded, Northbridge carries the whole loss plus the premium it already paid.

## Assumptions and limitations

- Northbridge, its prices, its budget and the insurance terms are all fictional. The scores and costs are my judgement for the exercise and are not measurements of any real organisation.
- Only two facts from the official HSE account were used as evidence. It is not a full forensic report.
- The residual scores are proposals. Each one depends on a control passing its test, and none has been tested.
- Costs are first-year figures only, so running costs after year one are not included.
- Real insurance policies have exclusions, conditions and waiting periods that could change who bears a loss.

## Source

Health Service Executive, *Cyber-attack and HSE response*, accessed 18 October 2026: https://www2.hse.ie/services/cyber-attack/what-happened/
