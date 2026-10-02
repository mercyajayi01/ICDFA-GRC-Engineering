# GRC102 Week 4 Practical Lab: Linux Security Monitoring and Auditing

**Student:** Mercy Ajayi
**Registration number:** C11/26/CGRCE/17219
**Course:** GRC102, Information Security Governance (Module 4: Monitoring and Auditing Security Controls)
**Date of lab work:** 2 October 2026
**Environment:** ICDFA Ubuntu Practice Hub, workspace student000272 (Ubuntu 24.04.4 LTS)

## What this folder contains

| File | What it is |
|---|---|
| `GRC102_W4_LAB_MERCY_AJAYI_C11_26_CGRCE_17219.pdf` | The full audit and control assurance report, with the command output and screenshots in the appendix |
| `documentation.md` | This summary |

## What I did

I worked through the lab manual in my assigned workspace and acted as a Security Control Assurance Analyst. For each module I ran the commands, kept the output, and then linked the evidence to a control, an owner and a follow-up action.

- **Module 1 (auditd):** auditd and audispd-plugins were already installed. I tried to start it, created `/etc/audit/rules.d/custom.rules` with four rules, and tried to restart it and load the rules. The service failed to start, `auditctl -l` returned "Operation not permitted", and no audit log was ever created.
- **Module 2 (logs):** `journalctl` returned no entries. `/var/log/auth.log` and `/var/log/syslog` do not exist, and the login record files are empty. I used the apt history log as the equivalent source.
- **Module 3 (Lynis):** I installed Lynis 3.0.9 and ran `sudo lynis audit system`. It gave a hardening index of 62, with 232 tests, 3 warnings and 43 suggestions.
- **Module 4 (SIEM and automation):** done as a table in the report. I did not set up a SIEM because this part of the lab is conceptual.

## Main findings

| ID | Finding | Priority |
|---|---|---|
| W4-F01 | Audit logging is configured but not working | High |
| W4-F02 | System and authentication logs are not being collected | High |
| W4-F03 | Vulnerable packages and 91 pending updates | Moderate |
| W4-F04 | No password ageing or strength rules | Moderate |

The report also has a seven row control-monitoring table, answers to the five governance escalation questions, a SIEM mapping table, and a remediation and retest plan.

## Things to know about this work

- The workspace appears to be a container and not a full virtual machine, because the first process (PID 1) is `sleep` and not systemd. This is the most likely reason auditd and logging do not work, but I could not confirm the cause from inside the workspace.
- I did not run every optional step. The report lists what I left out and why, including the optional hardening and retest in Activity 3.3.
- I tried to reach my instructor about the auditd problem before the deadline but could not, so I recorded the failures as they happened and did not try to force anything.
- All timestamps are in UTC. WAT is UTC plus one hour.
- All commands were run only inside my assigned workspace. The output in the report comes from my own session.

## AI assistance

I used an AI assistant (Claude) during this lab. It explained the commands to me one at a time, helped me understand the results, and helped me structure and word the report. I ran every command myself and the outputs and timestamps come from my own session.
