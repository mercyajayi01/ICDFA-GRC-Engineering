# GRC102 Week 4 Practical Lab: Linux Security Monitoring and Auditing

**Course:** GRC102, Information Security Governance
**Institution:** International Cybersecurity and Digital Forensics Academy (ICDFA)
**Student:** Mercy Ajayi
**Registration number:** C11/26/CGRCE/17219
**Lab:** Week 4 Practical Laboratory (Lab 4)
**Date of submission:** 8 October 2026

---

## Overview

This repository holds my report for the Week 4 practical lab. The lab asks me to turn technical evidence from a Linux host into governance assurance. I installed and configured auditd, reviewed the systemd journal, ran a Lynis security assessment, and then mapped what I found to control owners, thresholds, remediation steps and retest steps.

The full write-up, with all screenshots, is in the PDF report. This README is a short guide to what is in it.

## Repository contents

| File | What it is |
|---|---|
| `README.md` | This documentation file |
| `GRC102_W4_LAB_MERCY_AJAYI_C11_26_CGRCE_17219.pdf` | The full lab report with screenshots and saved terminal output |

## Environment and authorisation

- **Platform used:** my own Kali Linux VM (Kali Rolling 2026.2, kernel 6.19.14+kali) running in VirtualBox with NAT networking.
- **Why not the academy Ubuntu Hub:** on the day I started, the ICDFA Ubuntu Practice Hub showed that it was temporarily paused, with browser and SSH access blocked. I asked the class representative and was told I could use my own Kali VM if the academy's Kali and Ubuntu were unavailable, as long as I documented my screenshots and any command issues. Both screenshots (Figure 1 and Figure 2) are in the report.
- **Scope:** everything was done on that one VM. No external systems were targeted, only harmless test events were created, and no logging was disabled or evidence deleted.
- **Time zone:** the VM clock is set to EDT, so all timestamps in the report are EDT.

## What I did

### Module 1: auditd configuration and events

- Checked whether auditd was present. It was not installed on a fresh Kali, so I installed `auditd` and `audispd-plugins`, then started and enabled the service.
- Wrote four rules in `/etc/audit/rules.d/custom.rules`:

```
-w /etc/passwd -p rwxa -k passwd_changes
-w /etc/shadow -p rwxa -k shadow_changes
-a always,exit -F arch=b64 -S execve -k program_execution
-a always,exit -F arch=b32 -S execve -k program_execution
```

- Left out the `auth.log` watch rule because `/var/log/auth.log` does not exist on Kali.
- Loaded the rules with `augenrules --load`, then opened `/etc/passwd` in nano (without saving) to create a test event.
- Queried the events with `ausearch` and summarised them with `aureport`.

Main commands:

```bash
sudo systemctl status auditd --no-pager
sudo apt install auditd audispd-plugins -y
sudo systemctl start auditd && sudo systemctl enable auditd
sudo augenrules --load
sudo auditctl -l
sudo ausearch -k passwd_changes -i -ts 10/07/2026 00:37:29 -te 10/07/2026 00:37:31
sudo ausearch -k program_execution -i | tail -30
sudo aureport
sudo aureport --failed
sudo aureport --login
sudo aureport --anomaly -i
```

**What the evidence showed:** at 00:37:30 the user `kali` opened `/etc/passwd` in nano as root through `sudo`. The audit user ID stayed `kali` all the way through, the file was opened read-only (`O_RDONLY`), and no write access was recorded, so the file was not changed.

### Module 2: log management and analysis

Kali has no `/var/log/auth.log` or `/var/log/syslog`, so I used the systemd journal as the equivalent source.

```bash
sudo journalctl --since "today" --no-pager | tail -40
sudo journalctl -p err --no-pager | tail -30
sudo journalctl -u ssh --no-pager
sudo journalctl -t sudo --no-pager | tail -20
sudo journalctl --no-pager | grep -i "failed password"
sudo journalctl --no-pager | grep -i "pam_unix" | grep -iE "fail|could not"
sudo journalctl --no-pager | grep -i "warning" | tail -20
```

**What the evidence showed:** sudo use is fully attributable (user, terminal, folder, target user, command). I found no failed-password events and no SSH entries. Three authentication errors came from the screen-lock helper, not from a login attempt, and I could not confirm their cause. The journal also showed the `systemd-sslh-generator` crashing twice (SEGV at 00:20:15, ABRT at 00:23:14). The first crash happened before auditd started, so only the journal recorded it. A `daemon-reload` retest did not reproduce the crash.

### Module 3: Lynis security assessment

```bash
sudo apt install lynis
lynis show version
sudo lynis audit system --quick --no-colors
sudo grep -E "hardening_index|^warning\[\]|^suggestion\[\]" /var/log/lynis-report.dat
```

Lynis 3.1.6 ran 271 tests and returned a **hardening index of 61, with 2 warnings and 49 suggestions**.

### Optional hardening and retest: login banner (BANN-7126)

I added a legal warning banner to `/etc/issue` (backup kept as `/etc/issue.bak`) and ran a targeted retest:

```bash
sudo cp /etc/issue /etc/issue.bak
sudo nano /etc/issue
sudo lynis audit system --tests BANN-7126 --quick --no-colors
```

The check changed from a suggestion to OK. That retest ran only one test, so its score of 100 is not comparable with the full audit result of 61, and I do not claim an overall improvement from it.

## Key results

| Item | Result |
|---|---|
| auditd status | Active (running), enabled, auditd 4.1.2 |
| Audit rules loaded | 4 |
| Audit events in the report window (00:23:14 to 00:45:05) | 6,864 |
| Commands recorded | 108 |
| Logins / failed logins | 0 / 0 |
| Anomaly events | 1 (ANOM_ABEND, sslh generator) |
| Lynis hardening index | 61 |
| Lynis warnings / suggestions | 2 / 49 |
| Packages with pending updates | 1,452 not upgraded (apt output) |

## Main findings

| Finding | Evidence | Priority |
|---|---|---|
| Patch backlog | 1,452 packages not upgraded; Lynis PKGS-7420 | High |
| No host firewall | Lynis FIRE-4590 | High |
| Logs kept only on the host | Lynis LOGG-2154 | Medium |
| No file-integrity or malware tooling | Lynis FINT-4350, HRDN-7230 | Medium |
| Weak password policy settings | Lynis AUTH-9286, AUTH-9262, AUTH-9282 | Medium |
| No legal login banner (remediated for `/etc/issue`) | Lynis BANN-7126 | Low |

I did not check how many of the pending updates are security updates, so the report describes them as pending updates.

## Governance work in the report

- **Control-monitoring table:** seven controls, each with evidence, owner, observed status, KPI or KRI threshold, risk, remediation and retest step.
- **SIEM and continuous monitoring mapping:** how auditd, journal, Lynis and package data could reach a SIEM, and which events stay technical alerts and which become governance issues. No SIEM was deployed in this lab, so this part is conceptual.
- **Escalation questions:** highest priority, owners, escalation triggers, remediation evidence and retest timing.
- **Remediation and retest plan:** actions, owners, priorities and proposed timeframes. The thresholds and timeframes are my own examples.

## Problems I ran into and how I handled them

| Issue | What I did |
|---|---|
| ICDFA Ubuntu Hub unavailable | Used my own Kali VM with approval from the class representative |
| `/var/log/auth.log` missing | Skipped that watch rule and used `journalctl` instead |
| `auditctl -l` showed "No rules" after a restart | Ran `augenrules --load`, and all four rules then appeared. The cause was not confirmed |
| `aureport --login` returned no events | auditd started after my desktop login, so I recorded it as a coverage gap |
| Permission denied on `/var/log/lynis-report.dat` | Reran the command with `sudo` |
| Intermittent sslh generator crash | Retested with `daemon-reload`; it did not reproduce, so the cause stays unconfirmed |
| First VM was too slow and had a password problem | Replaced it with a fresh pre-built Kali image |

## Limitations

- One host and one lab session.
- The Lynis version (3.1.6) reported itself as more than six months old, so newer checks may be missing.
- Kali is a penetration-testing distribution, so some Lynis findings are there by design.
- Some causes (the sslh crashes and the screen-lock errors) were not confirmed.
- No SIEM was available, so the monitoring mapping was not tested.

## Declaration of AI assistance

I carried out all lab activities myself in my own Kali VM, and the commands, output and screenshots in the report come from that work. I used an AI assistant (Claude) to explain commands, help me troubleshoot errors, and help structure and word the report, as the class representative confirmed was allowed provided the errors and fixes were documented. I reviewed the technical claims against my own evidence, and I can explain every command, finding and recommendation.

## Author

Mercy Ajayi, GRC102, ICDFA
