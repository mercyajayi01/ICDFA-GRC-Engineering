# Executive Dashboard: User Guide

## What this is

executive_dashboard.html is a single, self-contained web page summarizing the current security posture of the simulated environment. It can be opened in any browser without an internet connection, since all charts are embedded directly in the file.

## How to open it

Double-click executive_dashboard.html, or open a browser and go to File > Open, then select the file from the security_governance_lab folder.

## Reading the dashboard

Top summary cards: four at-a-glance indicators. Green means the control is in place; red means it is not. These reflect the most recent vulnerability scan and the recorded remediation status.

- Critical / High Findings: the combined count of Critical and High severity items from the latest vulnerability scan. Zero is the goal.
- Patching Status: whether the known Struts vulnerability has been remediated.
- Database Security: whether default database credentials have been changed.
- Network Segmentation: whether the web and database tiers are isolated from each other.

Before vs After Remediation chart: a direct, real-data comparison of patch compliance, remediation time and incident count before and after the controls in Part 3 were implemented.

Current Risk Distribution chart: the risk register's open risks, grouped by severity.

Illustrative Trends: these two charts show a plausible trend shape leading into the current measured value. The earlier points are not actual historical measurements and are labeled as such; only the final point on each line reflects a real recorded value.

Governance Register Summary: a count of policies, controls, risks, incidents, metrics and audits currently tracked.

Remediation Notes: a plain-language summary of what was actually changed to fix each finding.

## Regenerating the dashboard

If the underlying data changes (a new scan, an updated governance record), regenerate the dashboard by running the generate_dashboard.py script from the lab folder. This overwrites executive_dashboard.html with a fresh version reflecting current data.
