# Security Metrics Framework

## Purpose

This framework defines how security posture is measured, tracked, and reported within the simulated governance program, and explains how each metric drives action rather than sitting unused.

## Metrics Tracked

| Metric | Definition | Target | Direction |
|---|---|---|---|
| Patch Compliance | Percentage of systems with all critical patches applied | 95% | Higher is better |
| Vulnerability Remediation Time | Average days to remediate a critical vulnerability | 7 days | Lower is better |
| Security Incidents | Number of security incidents per reporting period | 0 | Lower is better |

## How Status Is Determined

Each metric is scored Green or Red by comparing its actual value against its target, accounting for whether the metric is "higher is better" (like Patch Compliance) or "lower is better" (like Remediation Time and Incidents). This distinction matters: an earlier version of the tracking tool used in this lab treated every metric as "higher is better," which meant a rising incident count was incorrectly shown as Green. That bug was identified and corrected before the post-remediation metrics were recorded, so the directionality shown in this report is accurate.

## Reporting Cadence

In a production environment, these metrics would be reviewed monthly by the security team and quarterly by governance leadership, with Red status on any metric triggering a documented remediation plan and an update at the following review. In this simulation, metrics are captured at two points: before remediation (reflecting the Equifax-style baseline) and after remediation (reflecting the controls implemented in Part 3).

## Ownership

Each metric has a nominal owner recorded in the governance tracker: patch compliance and remediation time are owned by the Security Engineer role, and the incident count by the Security Director role, consistent with the governance structure recorded in the risk and control register.

## Limitation

The trend charts accompanying this framework use illustrative historical data points to visualize what a realistic trend toward the current measured value might look like. Only the final data point in each trend, and the full before/after comparison chart, reflect actual measurements taken during this exercise.
