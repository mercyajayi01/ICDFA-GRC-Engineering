# Comparison of Simulated Environment to Equifax Data Breach

## Overview

This report compares the security governance failures identified in the simulated environment (see `governance_failure_report_20261009_011821.json`) to those that contributed to the Equifax data breach of 2017.

## Key Governance Failures in the Equifax Breach

1. **Patch Management Failure**: Equifax failed to patch a known vulnerability in Apache Struts (CVE-2017-5638) for over two months after a patch was publicly released.
2. **Security Monitoring Failure**: The breach went undetected for 76 days, reflecting inadequate security monitoring.
3. **Network Segmentation Failure**: Attackers moved laterally within Equifax's network once inside, indicating insufficient segmentation.
4. **Leadership and Accountability Failure**: There was unclear ownership of security responsibilities and limited board oversight.
5. **Policy Implementation Failure**: Security policies existed on paper but were not effectively enforced.

## Comparison with the Simulated Environment

| Governance Failure | Equifax | Simulated Environment | Similarity |
|---|---|---|---|
| Patch Management | Apache Struts vulnerability unpatched for months | Apache Struts S2-045 unpatched, flagged Critical by scanner | High |
| Security Monitoring | Breach undetected for 76 days | No monitoring in place; attack simulation succeeded without detection | High |
| Network Segmentation | Lateral movement enabled by flat network | Web and database containers share one unsegmented network | High |
| Authentication | Weak internal credentials and access controls | Default root/password MySQL credentials | High |
| Policy Implementation | Policies existed but were not enforced | Patch and vulnerability management policies recorded in the tracker, neither enforced | High |
| Metrics and Measurement | Ineffective security metrics | Patch compliance, remediation time and incident metrics all below target (Red) | High |

## Lessons Learned

1. **Patching is only effective if enforced.** Having a Patch Management Policy on paper did not stop the Struts vulnerability from remaining open, the same gap that enabled Equifax's breach.
2. **Detection matters as much as prevention.** The simulated attack succeeded with zero built-in alerting, demonstrating why Equifax's 76-day detection gap mattered.
3. **Flat networks turn single compromises into full breaches.** A segmented network would have limited the web server's reach into the database, just as it would have limited Equifax's attackers.
4. **Metrics without consequences don't drive change.** Three metrics were tracked and all three missed target, mirroring how Equifax's own internal patch tracking failed to translate into action.
5. **Governance failures compound.** No single gap caused the simulated breach; the unpatched flaw, weak credentials, flat network and absent monitoring each removed a layer that could otherwise have stopped or contained it, the same pattern seen at Equifax.

## Conclusion

The simulated environment reproduces the core governance conditions behind the Equifax breach: an unpatched known vulnerability, weak internal authentication, no network segmentation and no effective monitoring, sitting underneath policies that existed but were not enforced. The resulting eight documented failures confirm that technical controls alone are not the issue; the gap is in governance, specifically ensuring policies translate into enforced, monitored, and measured practice.
