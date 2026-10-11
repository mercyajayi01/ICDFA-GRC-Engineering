# GRC102 Week 5 Practical Lab: Equifax-Style Breach Simulation, Remediation, and Executive Reporting

---

## Overview

This repository holds my report for the Week 5 practical lab. The lab asks me to recreate the core technical and governance conditions behind the 2017 Equifax data breach in an isolated environment, identify the resulting governance failures, implement and independently verify real security controls, and then produce metrics-based executive reporting on the results.

The full write-up, with all screenshots, is in the PDF report. This README is a short guide to what is in it.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `GRC102_W5_LAB_MERCY_AJAYI_C11_26_CGRCE_17219.pdf` | The full lab report with screenshots and saved terminal output |
| `docker-compose.yml`, `database_init/init.sql` | The simulated environment (web, database, monitoring containers) |
| `vulnerability_scanner.py` | Scans for the three intended weaknesses |
| `governance_tracker.py`, `initialize_governance.py` | The governance register (policies, controls, risks, incidents, metrics, audits) |
| `simulate_attack.py` | Safely demonstrates exploitation (proof-of-vulnerability header only, no real code execution) |
| `analyze_governance_failures.py` | Cross-references scan, attack, and governance data to identify failures |
| `monitor_containers.py` | Real-time detection of failed logins and attack patterns |
| `generate_charts.py`, `generate_dashboard.py` | Builds the charts and the executive dashboard |
| `executive_dashboard.html` | Self-contained dashboard (open directly in a browser) |
| `equifax_comparison.md`, `part2_lessons_learned.md`, `part3_controls_report.md` | Write-ups for Parts 2 and 3 |
| `metrics_framework.md`, `dashboard_user_guide.md`, `board_report.md` | Write-ups for Part 4 |
| `patch_status.json`, `governance_data.json`, `attack_log.json`, `monitoring_alerts.log` | Evidence/state files the scripts read and write |
| `vulnerability_report_20261010_050227.json`, `governance_failure_report_20261010_050526.json` | Final ("after") scan and failure analysis results |

**Note:** the baseline ("before") `vulnerability_report_*.json` and `governance_failure_report_*.json` files were overwritten during the lab session and are not included here. The baseline results (Critical/High/Medium findings, 8 governance failures) are fully documented with screenshots in the PDF report.

## Environment and authorisation

- **Platform used:** my own Kali Linux VM (Kali Rolling 2026.2) running in VirtualBox.
- **Why not the academy hub:** the ICDFA shared Kali/Ubuntu practice hub was unavailable at the time. I asked the class representative and was told I could use my own Kali VM if the academy's Kali and Ubuntu were unavailable, as long as I documented why and included screenshots.
- **Scope:** everything was done inside a private, isolated Docker environment on that one VM. The vulnerable web service was bound only to 127.0.0.1 and never exposed beyond the lab's own isolated Docker networks. No external system was scanned, targeted, or accessed. All customer data used is synthetic, standard, publicly known test data, not real personal information.
- **AI-assisted troubleshooting:** I used Claude to help troubleshoot errors in the lab's provided scripts. Every instance is documented inline in the report.

## What I did

### Part 1: Building the simulated environment

- Built a three-container Docker environment: a vulnerable Apache Struts web server (CVE-2017-5638 / S2-045), a MySQL database seeded with synthetic customer records and default credentials, and a monitoring container.
- The lab's own vulnerable image tag (`vulhub/struts2:s2-045`) did not exist on Docker Hub, so I substituted `piesecurity/apache-struts2-cve-2017-5638`, which targets the same CVE.
- Ran a baseline vulnerability scan confirming all three intended weaknesses: Critical (unpatched Struts), High (default MySQL credentials), Medium (no network segmentation).
- Built a governance tracker and populated it with sample policies, controls, risks, incidents, and metrics. Found and fixed a bug in its own dashboard logic, which assumed every metric was "higher is better" and so marked a worsening metric as Green.

### Part 2: Simulating the attack and analyzing governance failures

- Ran a simulated attack against the unpatched environment; it succeeded and went undetected, reflecting the 76-day detection gap in the real Equifax breach.
- Ran a governance failure analysis script cross-referencing the scan, the attack log, and the governance register, identifying 8 distinct failures across patch management, incident detection, policy implementation, vulnerability management, metrics and measurement, security architecture, and authentication and access control.

### Part 3: Implementing and verifying controls

- Replaced the vulnerable web container with a patched Tomcat baseline.
- Rotated MySQL's default credentials to randomly generated 24-character passwords.
- Moved the database to a dedicated, isolated Docker network, removing its direct reachability from the web tier.
- Built a monitoring script to detect failed authentication attempts and known attack-pattern markers in real time.
- Found and fixed several bugs in the lab's own provided scripts along the way: a scanner probe targeting the wrong URL, a shell redirection error that always forced a successful exit code regardless of the real result, and a missing `patch_status.json` file that caused the governance analysis to assume nothing had been fixed.
- After remediation: vulnerability scan returned zero Critical, High, or Medium findings (down from one of each); the attack simulation failed where it had previously succeeded; governance failures dropped to zero (down from 8).

### Part 4: Metrics, dashboard, and executive reporting

- Recorded post-remediation metrics alongside the baseline figures: Patch Compliance rose from 85% to 100%, Vulnerability Remediation Time fell from 12 days to effectively 0, Security Incidents fell from 1 to 0.
- Generated charts (before/after comparison, risk distribution, and two illustrative trend charts, clearly labeled as such since they are not real historical measurements).
- Built a self-contained HTML executive dashboard, a metrics framework document, a dashboard user guide, and a board report for a risk-committee audience.

## Key results

| Item | Before remediation | After remediation |
|---|---|---|
| Critical findings | 1 | 0 |
| High findings | 1 | 0 |
| Medium findings | 1 | 0 |
| Attack simulation | Succeeded, undetected | Failed |
| Governance failures identified | 8 | 0 |
| Patch Compliance | 85% | 100% |
| Vulnerability Remediation Time | 12 days | ~0 days |
| Security Incidents | 1 | 0 |

## Problems I ran into and how I handled them

| Issue | What I did |
|---|---|
| ICDFA practice hub unavailable | Used my own Kali VM with approval from the class representative |
| Lab's `vulhub/struts2:s2-045` image does not exist on Docker Hub | Substituted `piesecurity/apache-struts2-cve-2017-5638` (same CVE) |
| Vulnerability scanner reported a false negative on Struts | Probe was hitting the server root instead of the actual Struts action URL; corrected the target URL |
| Network segmentation check always reported "vulnerable" | A stray `\|\| true` in the scanner's shell command always forced a successful exit code; removed it and corrected the pass/fail logic |
| Governance failure analysis still showed 8 failures after remediation | The lab's own `patch_status.json` file, which the script reads to know what's fixed, was never created; created it honestly reflecting the real changes made |
| Governance dashboard showed a worsening metric as Green | Dashboard logic assumed every metric was "higher is better"; added a `lower_is_better` flag and corrected the status calculation |

## Limitations

- One VM, one lab session.
- The trend charts in Part 4 use illustrative historical data points leading into the real measured value; only the final point on each line and the before/after comparison chart reflect real measurements.
- The database credentials shown during the lab session were rotated before this repository was published; the compose file in the report reflects the commands run, not live credentials.

## Author

Mercy Ajayi, GRC102, ICDFA
