# GRC103 Practical Laboratory 3A: Phishing Risk Analysis Report

---

## Overview

This folder contains my submission for Lab 3A of GRC103 – Risk Assessment and Management Techniques.  

I act as the lead GRC analyst at GlobalTech Inc. The task is to analyse three phishing simulation campaigns, calculate campaign metrics, build a quantitative annual-loss model, produce a risk assessment matrix, run statistical analysis with confidence intervals, evaluate three security controls (cost-benefit, ROI and break-even), and prepare an executive briefing for the Board, CISO and CFO.

Everything is driven from a single calculation workbook. All figures in the report are produced by visible formulas. Scenario assumptions (breach cost, wave frequency, control effectiveness, etc.) are clearly labelled and never presented as verified industry data.

## Repository contents

| File                              | What it is                                                                 |
| --------------------------------- | -------------------------------------------------------------------------- |
| `README.md`                       | This documentation file                                                    |
| `GRC103_LAB3A_MERCY_AJAYI.xlsx`   | Calculation workbook (all formulas visible)                                |
| `GRC103__LAB3A_MERCY AJAYI.pdf`   | Phishing Risk Analysis Report (executive-ready PDF)                        |

## What is in the workbook

| Sheet              | What it holds                                                                 |
| ------------------ | ----------------------------------------------------------------------------- |
| Cover              | Student details, colour key and sheet index                                   |
| Inputs             | All supplied data + every scenario assumption in one place                    |
| Campaign Metrics   | Phase 1 – open, click-through, credential and conversion rates                |
| Financial          | Phase 2 – compromised accounts, explicit annual-occurrence model, ALE, lab-literal ceiling |
| Controls           | Cost-benefit, ROI, break-even and sensitivity across low/base/high scenarios  |
| Risk Matrix        | Phase 3 – campaign comparison, ratings, priorities and recommended actions    |
| Statistics         | 95 % confidence intervals and sampling limitations                            |
| Corrections        | Arithmetic errors in the lab brief + method changes with reasons              |

**Colour key used throughout the workbook**

- Blue text = supplied data (lab brief or study guide)  
- Yellow fill = scenario assumption (not measured)  
- Black text = formula  
- Green text = formula that links to another sheet  
- Orange fill = corrected figure (differs from the printed lab brief)

## What I did

- Calculated all campaign metrics and conversion rates from the raw simulation counts.
- Replaced the lab’s unjustified “150 independent breaches” approach with an explicit annual-occurrence model: 4 credential-theft waves per year × 25 % chance a wave produces a major breach, scaled by each campaign’s credential rate relative to Campaign B.
- Produced base-case Annual Loss Expectancy (ALE) figures and a side-by-side lab-literal ceiling for transparency.
- Built 95 % confidence intervals for the three credential rates and documented sampling limitations.
- Evaluated MFA, security-awareness training and email filtering on cost, assumed effectiveness, net benefit, ROI and break-even points.
- Ran sensitivity analysis across low / base / high wave frequencies.
- Prepared a full control-portfolio recommendation ($490 k investment, 90 % combined risk reduction) with residual ALE and programme-level break-even.
- Listed every arithmetic error in the lab brief and every method change, with the exact reason for the change.

## Key results (base-case annual-occurrence model)

| Campaign                      | Credential rate | Projected compromised accounts | Breaches / year | ALE (base case) | Rating    | Priority |
| ----------------------------- | --------------- | ------------------------------ | --------------- | --------------- | --------- | -------- |
| B: IT Password Reset          | 30 %            | 600                            | 1.0             | $4,350,000      | CRITICAL  | 1        |
| A: HR Bonus Notification      | 18 %            | 360                            | 0.6             | $2,610,000      | HIGH      | 2        |
| C: CEO Urgent Document        | 15 %            | 300                            | 0.5             | $2,175,000      | HIGH      | 3        |

- Combined credential-submission rate across 430 emails: **24.4 %** (study-guide reference range 3–5 %).
- MFA ($90 k, 99.9 % assumed effectiveness) produces the highest net benefit and pays for itself if it prevents roughly one breach every 48 years.
- Full recommended programme costs **$490,000**, reduces expected annual loss by **$3,915,000** (lab’s 90 % combined figure) and yields **699 %** ROI under the base case.
- Even in the low-frequency scenario (two waves per year) the programme still returns **299 %**.

## Assumptions

- Credential-theft waves per year (base case) = 4 (one per quarter, matching the simulation cadence).  
- Probability that a wave leads to a major breach = 25 % (supplied by the lab; read as per-wave, not per-account).  
- Single Loss Expectancy (SLE) = $4,350,000 (supplied scenario assumption).  
- Breach likelihood scales with each campaign’s credential rate relative to Campaign B.  
- Control effectiveness values (99.9 %, 60 %, 20 %) and the 90 % combined programme reduction are scenario assumptions, not verified benchmarks.  
- CRITICAL / HIGH rating thresholds ($4 M / $2 M) are my own modelling choices.  
- The lab’s original “150 independent breaches → $652.5 M” figure is retained only as a labelled ceiling for comparison; it is not used for ratings or recommendations.
