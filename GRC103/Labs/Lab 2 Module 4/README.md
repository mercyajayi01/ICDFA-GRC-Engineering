# GRC103 Practical Lab: Risk Monitoring Dashboard and Management Reporting

---

## Overview

This folder holds my work for Module 4, Lab 2 of GRC103. In this lab I acted as a GRC analyst at Northbridge Services, a fictional organisation. I took three months of control-monitoring data (January to March) and turned it into a working dashboard, an interpretation of the March position, an updated risk register, an action and assurance plan, and a one-page briefing for the Head of Operations.

The lab is a desk-based analysis exercise. It uses only the fictional dataset supplied in the lab brief. No live systems, real organisations or real personal data were involved at any point.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `MERCY AJAYI MODULE 4 LAB 2 DASHBOARD.xlsx`| The editable workbook: source data, live formulas, Green/Amber/Red classifications and charts |
| `GRC 103 Module 4 Lab 2 REPORT.pdf`| The three-page report: risk register, action and assurance plan, and the one-page management report |

## What is in the workbook

| Sheet | What it holds |
|---|---|
| Dashboard | The source data (entered as inputs), the five calculated indicators, a Green/Amber/Red status for each month, gap and backlog counts, a line chart for the three percentage indicators and a separate bar chart for unauthorised changes |
| Thresholds | The Green, Amber and Red limits from the lab brief. The status formulas read from this sheet, so a threshold can be changed in one place |
| Interpretation | My working notes on the March results: three priority concerns, the effect of the rise in eligible endpoints, and the March coverage gap |

## What is in the report

| Section | What it holds |
|---|---|
| 1. Risk Register Update | Four register entries (monitoring blind spots, delayed alert review, failed restoration, overdue treatment actions), each with evidence, existing control, likelihood, impact, score, owner, action and review date, plus a justification for every rating |
| 2. Action and Assurance Plan | One short-term containment step and one longer-term improvement for each risk, with an owner, a target date, an outcome test and the evidence needed to close it |
| 3. Executive Summary and Recommendations | The one-page management report: March status, key findings, business implications, decisions requested, owners and the next review date |

## What I did

- Entered the monthly source data in the workbook and calculated five indicators by formula: monitoring coverage, timely critical-alert review, restore-test success, overdue high-risk action rate, and confirmed unauthorised changes (kept as a plain count).
- Classified each result as Green, Amber or Red using the unrounded values, and set any indicator with a zero denominator to show N/A instead of a misleading 0% or 100%.
- Built a labelled trend chart for the three percentage indicators, and kept the unauthorised-changes count on its own chart so counts and percentages never share an axis.
- Worked out the March coverage gap in endpoints, and explained why the rise in eligible endpoints (100 to 120) makes the raw monitored count look better than the real position.
- Picked three priority concerns for March and, for each one, kept what the data shows separate from what might have caused it.
- Wrote the four risk register entries and scored them myself, explaining why a Red indicator does not automatically mean a high risk score.
- Wrote an action and assurance plan with outcome tests, so that an action only counts as closed once there is evidence that the control works.
- Wrote the management report for the Head of Operations, with the decisions and resources I would ask for.

## Key results

| Indicator | January | February | March | March status |
|---|---|---|---|---|
| Monitoring coverage | 98.0% | 95.0% | 90.0% | Red |
| Timely critical-alert review | 95.0% | 80.0% | 70.0% | Red |
| Restore-test success | 100.0% | 90.0% | 80.0% | Red |
| Overdue high-risk action rate | 10.0% | 25.0% | 40.0% | Red |
| Confirmed unauthorised changes | 1 | 3 | 5 | Red |

- All five indicators are Red in March, and every one has moved in the wrong direction since January.
- The March coverage gap is 12 endpoints (120 eligible, 108 monitored). Reaching the 98% Green threshold would need at least 118 monitored, which is 10 more than today.
- All four risks rate High: R1 monitoring blind spots 16, R2 delayed alert review 16, R3 failed restoration 15, R4 overdue treatment actions 12.
- The three priority concerns are monitoring coverage (with the rise in unauthorised changes), late review of critical alerts, and failed restore tests.

## Assumptions and limitations

- The data is fictional and covers only three months, so it shows direction. It cannot support a reliable long-term forecast.
- The Green, Amber and Red limits are classroom thresholds from the lab brief, not ICDFA policy or an industry standard.
- The rise in unauthorised changes happened while coverage fell, but the data cannot show that one caused the other. The possible causes in my write-up are hypotheses that would need checking against real records.
- Only 10 restore tests are run each month, so a single failure moves the success rate by 10 percentage points.
- The likelihood and impact scores are my own judgement and could reasonably be set differently with more information.
- Every action in the plan is proposed. None was implemented, so their expected effect has not been measured.
