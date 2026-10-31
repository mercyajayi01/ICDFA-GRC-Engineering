# GRC103 Week 2 Practical Lab: Advanced Cybersecurity Risk Quantification

---

## Overview

This folder holds my work for Lab 3b of GRC103. In this lab I act as the lead GRC analyst at SecureBank Financial. The CISO gave me penetration test findings for the new SecureMobile banking platform, and I turned them into dollar figures, compared three security controls, and prepared an executive briefing for the CISO and CFO.

Everything is in one Excel workbook, built in Google Sheets with visible formulas. This README is a short guide to what is in it.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `GRC103_LAB03_MERCY_AJAYI.xlsx` | The full workbook: calculations, control analysis, charts, executive briefing and bonus matrix |

## What is in the workbook

| Tab | What it holds |
|---|---|
| Risk Calculations | SLE, ARO, ALE and risk priority for the three findings, as formulas |
| Control Analysis | Residual risk, risk reduction, ROI, payback and a justified recommendation for each control |
| Risk Analysis Data | The working tables behind the charts |
| Documentation | My assumptions and a calculation log |
| Dashboard | The one-page executive dashboard with three charts |
| Executive Briefing | Financial justification and risk treatment plan |
| Treatment Gantt | The 30-day, 90-day and one-year timeline |
| ALE Bar Chart, Risk Pie Chart | Risk exposure charts |
| Cost vs Effectiveness, ROI Comparison, Risk Reduction Timeline | Control evaluation charts |
| Before vs After Risk, Investment Breakdown | Executive dashboard charts |
| Bonus Matrix | Current vs residual risk, cost vs benefit, and the best control selection under a budget |

In the sheets, blue cells are figures supplied by the lab, yellow cells are my assumptions and gray cells are formula results.

## What I did

- Calculated the single loss expectancy (SLE) and annualized loss expectancy (ALE) for each finding using ALE = SLE x ARO.
- Ranked the findings by ALE and rated them High, Medium or Low.
- Matched each control to the finding it protects against, then calculated new ALE, risk reduction, Year 1 ROI and payback period.
- Built the charts, the dashboard, the Gantt chart and the written briefing.
- Completed the bonus challenge, selecting controls under an assumed budget.

## Key results

| Finding | ALE | Priority |
|---|---|---|
| Database Injection | $31,250,000 | High |
| Session Hijacking | $3,000,000 | Medium |
| API Authentication Bypass | $750,000 | Low |

- Total annual exposure before controls: **$35,000,000**.
- Deploying all three controls costs **$805,000** in Year 1 and removes **$26,962,500** of annual risk (77.04%), leaving **$8,037,500**.
- The WAF gives the highest return and should be deployed first. Every control pays back its purchase price in under a year.
- Under an assumed $500,000 budget, the best selection is the WAF and MFA Enhancement ($405,000 in total).

## Assumptions

- The exploit probability is treated as an annual rate (ARO).
- Each control is applied to the finding it is designed to protect against.
- ROI is calculated on a Year 1 basis (initial cost plus one year of maintenance).
- The High, Medium and Low thresholds, the treatment timeline and the $500,000 budget are my own choices, because the lab does not give them.
