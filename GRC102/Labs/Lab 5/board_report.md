# Board Report: Security Governance Simulation

## Prepared for: Board Risk Committee
## Subject: Equifax-Style Breach Simulation, Remediation, and Governance Findings

## Executive Summary

This report summarizes a controlled simulation that recreated the core technical and governance conditions behind the 2017 Equifax data breach, then measured the effectiveness of a structured remediation program against it. The exercise confirms that the three primary failure conditions, an unpatched critical vulnerability, weak database authentication, and absent network segmentation, were all successfully remediated, and that governance oversight failures dropped from 8 identified issues to 0 once remediation status was properly tracked.

## What Was Tested

A private, isolated simulation environment was built containing a deliberately vulnerable web application (reproducing CVE-2017-5638, the same Apache Struts vulnerability exploited in the Equifax breach), a database seeded with synthetic customer records, and no monitoring. A simulated attack was run against this baseline environment before any remediation took place.

## Baseline Findings

The baseline scan identified three severity-rated findings: one Critical (the unpatched web vulnerability), one High (default database credentials), and one Medium (lack of network segmentation). The simulated attack succeeded without detection, consistent with the 76-day detection gap documented in the real Equifax breach.

A deeper governance analysis identified 8 distinct failures spanning patch management, incident detection, policy implementation, vulnerability management, metrics and measurement, security architecture, and authentication and access control.

## Remediation Actions

Four technical controls were implemented and independently verified:

1. The vulnerable application was replaced with a patched baseline.
2. Database credentials were rotated from defaults to strong, unique values.
3. The database was moved to an isolated network segment, removing its direct reachability from the web tier.
4. A monitoring capability was built to detect failed authentication attempts and known attack patterns in real time.

## Results

Following remediation, the vulnerability scan returned zero Critical, High, or Medium findings, down from one of each. The same attack that previously succeeded now fails. The governance failure analysis, re-run against the documented remediation status, returned zero outstanding failures, down from 8. A deliberately triggered failed login was detected by the new monitoring capability within seconds.

## Governance Observations

Two findings are worth board-level attention beyond the technical fixes:

First, having a documented policy is not the same as having an effective one. The simulation's own Patch Management Policy existed in the governance register before the breach simulation, yet did nothing to prevent it, mirroring Equifax's own experience. Governance effectiveness should be measured by enforcement and outcome, not by policy existence alone.

Second, metrics only add value when their direction of improvement is correctly understood. An error was identified and corrected during this exercise in which a metrics dashboard incorrectly marked a worsening trend as positive, because it assumed every metric was "higher is better." This kind of silent measurement error is itself a governance risk, since leadership relying on an inaccurate dashboard could reasonably believe a problem is improving when it is not.

## Recommendation

The remediation pattern demonstrated in this simulation, patch, secure credentials, segment, monitor, and formally record completion, is directly transferable to production environments. The committee should consider whether current patch and credential management practices are verified through independent testing (as performed here) rather than relying on self-reported compliance alone.
