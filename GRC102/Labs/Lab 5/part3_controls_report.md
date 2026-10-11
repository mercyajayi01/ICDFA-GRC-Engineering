# Part 3: Controls Implementation Report

## Overview

This report documents the technical controls implemented to remediate the five governance failures identified in Part 2, and the evidence confirming each control is genuinely effective rather than merely flagged as complete.

## 1. Patch Management

**Finding:** Apache Struts2 running a known Critical RCE vulnerability (CVE-2017-5638), unpatched.

**Control implemented:** The vulnerable web container image was replaced with a current, non-vulnerable Tomcat baseline (tomcat:9-jre11), removing the exploitable Struts Showcase application entirely. No Struts-based patched image exists for the demo application used, so a clean image swap was used as the functional equivalent of upgrading to a patched version.

**Verification:** Re-running the vulnerability scanner after the change showed the Struts finding drop from Critical to not applicable. The attack simulation, which previously succeeded, subsequently failed against the same target.

## 2. Database Security

**Finding:** MySQL accessible using default root/password credentials.

**Control implemented:** Root and application credentials were rotated to randomly generated 24-character passwords.

**Verification:** A login attempt using the new password succeeded; a login attempt using the old default password was rejected with Access denied. Customer data was confirmed intact after the credential change.

## 3. Network Segmentation

**Finding:** Web and database containers shared a single flat network, permitting direct access between them.

**Control implemented:** The database was moved to a dedicated, isolated Docker network. The web container's access to this network was removed entirely.

**Verification:** A direct hostname lookup for the database from the web container returned no result, and a direct connection attempt failed with a DNS resolution error, confirming the web tier can no longer reach the database tier.

## 4. Monitoring

**Finding:** No monitoring or alerting capability existed; the simulated attack succeeded without detection.

**Control implemented:** A monitoring script was built to check container health, scan web server logs for known Struts exploitation markers, and scan database logs for failed authentication attempts.

**Verification:** A deliberately failed database login was correctly detected and logged by the monitoring script within seconds.

## 5. Governance Oversight

**Finding:** Policies existed in the governance tracker but were not reflected as enforced; the automated failure analysis flagged 8 governance failures.

**Control implemented:** The remediation status of each technical control above was formally recorded, making the state of patching, database security and network segmentation visible to governance tooling rather than only existing as undocumented infrastructure changes.

**Verification:** Re-running the governance failure analysis after recording the remediation status returned 0 failures, down from 8.

## Summary

All five identified governance failures have corresponding technical controls, each independently verified through re-scanning, re-testing, and re-running the failure analysis, rather than relying on a single pass/fail flag. The before-and-after comparison (Critical/High/Medium findings reduced from 1/1/1 to 0/0/0, and governance failures reduced from 8 to 0) demonstrates measurable improvement in the environment's security posture.
