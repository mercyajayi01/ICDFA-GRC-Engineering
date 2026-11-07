# GRC103 Practical Lab: Social Engineering & Phishing Campaign Simulation

---

## Overview

This folder holds my work for Lab 3C of GRC103. In this lab I acted as a GRC analyst running an authorised, self-contained phishing simulation to measure how far a credential-harvesting attack can travel through a single target before any control or human judgement stops it. I built and launched the campaign myself using GoPhish, captured the results, and wrote them up as campaign evidence, a risk assessment table, and an executive briefing.

The simulation ran entirely inside my own lab environment — a Kali Linux VM, with GoPhish as the phishing framework and Mailtrap as a sandboxed SMTP relay. No real individuals, production systems, or external domains were involved at any point.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `The Report`| This includes lab setup, campaign evidence, risk assessment table, executive summary and limitations |

## What is in the report

| Section | What it holds |
|---|---|
| 1. Laboratory Setup and Method | The local environment (Kali VM, GoPhish v0.12.1, Mailtrap sandbox) and the four campaign components (sending profile, landing page, email template, target group) |
| 2. Campaign Evidence | Seven screenshots covering the sending profile configuration, the delivered email, and the campaign's funnel results, with SMTP credentials concealed |
| 3. Phishing Risk Assessment Table | Event counts, denominators, calculated rates, risk interpretation and recommended controls for each stage of the funnel (sent, opened, clicked, submitted) |
| 4. Executive Summary and Recommendations | Scope and method, key findings, business implications, and five prioritised recommended actions |
| 5. Limitations | Why a single-subject result cannot be read as an organisation-wide susceptibility rate |

## What I did

- Installed and configured GoPhish v0.12.1 on a Kali Linux VM, with its admin interface and phishing server running locally.
- Set up a Mailtrap sandbox as the SMTP relay, so no email left the controlled lab environment.
- Built a generic mock VPN login page as the landing page (not a clone of any real organisation), configured to capture submitted credentials and redirect to a training page.
- Wrote an urgency-themed phishing lure ("Your VPN Password Expires in 24 Hours") using GoPhish's personalisation variables.
- Launched the campaign against a single authorised target (myself), and acted as the "victim" — opening the email, clicking the link, and submitting mock credentials — to generate real funnel data end to end.
- Turned the raw campaign data into a risk assessment table and an executive-style briefing.

## Key results

| Metric | Result | Rate |
|---|---|---|
| Emails Sent | 1 of 1 | 100% |
| Emails Opened | 1 of 1 | 100% |
| Links Clicked | 1 of 1 | 100% |
| Credentials Submitted | 1 of 1 | 100% |

- Every stage of the simulated attack chain succeeded — no technical control or user judgement interrupted it at any point.
- The highest-priority recommendation is enforcing MFA on VPN and remote-access systems, since it is the one control that would still have stopped this specific attack even after credentials were phished.

## Assumptions and limitations

- The sample size is 1 (myself as the sole authorised target), so every rate above is either 0% or 100%. These are reported honestly at that scale and are not treated as an organisation-wide susceptibility rate.
- No control group or repeated trials were run, so the result cannot separate a general human tendency to fall for this lure from behaviour specific to this one test.
- The landing page was a generic mock-up, not a clone of a real organisation's portal — a brand-matched clone could plausibly produce a different real-world result.
- MFA and email filtering were recommended based on their expected effect; they were not deployed or tested directly, since this lab's scope was the attack simulation itself.
