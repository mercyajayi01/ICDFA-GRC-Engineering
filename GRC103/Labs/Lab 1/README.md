# GRC103 Week 1 Practical Lab: Vulnerability Assessment

---

## Overview

This folder holds my report for the Week 1 practical lab of GRC103 (Risk Assessment and Management Techniques). In this lab I act as an internal GRC auditor and assess an authorised Metasploitable 2 test server in a development environment. I discovered the server, listed its ports and services, ran Nmap, Nikto and Nuclei, and then turned the technical results into a risk assessment and a short summary for management.

The full write-up, with all figures, is in the PDF report. This README is a short guide to what is in the folder.

## Repository contents

| File or folder | What it is |
|---|---|
| `README.md` | This documentation file |
| `GRC103_W1_LAB_MERCY_AJAYI_C11_26_CGRCE_17219.pdf` | The full lab report: introduction, executive summary, method, scan results, 21-row risk assessment table and limitations |
| `Scan_Outputs/` | The original scan files, unedited: `ping_result.txt`, `initial_scan.nmap`, `initial_scan.gnmap`, `initial_scan.xml`, `initial_scan_report.html`, `nikto_scan.txt`, `nuclei_web_scan.txt`, `nuclei_full_scan.txt` |
| `Screenshots/` | 25 screenshots: lab setup, ping, Nmap, the Nmap HTML report, Nikto, both Nuclei scans and the manual checks |
| `Command_Log/commands_run.txt` | The commands I ran, in order |

## Environment and authorisation

- **Platform:** Oracle VirtualBox on my own laptop. Kali Linux 2026.2 is the assessor machine (192.168.56.102). Metasploitable 2 is the target (192.168.56.101).
- **Network:** both machines are on an isolated host-only network. Kali has a second NAT adapter that I used only for tool updates. Metasploitable was never connected to the internet.
- **Scope:** only the Metasploitable VM was scanned. No public, institutional or other third-party system was touched.
- **Date of assessment:** 20 October 2026.
- **Tools:** Nmap 7.99, xsltproc, Nikto 2.6.0, Nuclei 3.8.0 (templates v10.5.0), and the ping, ftp and telnet clients.

## What I did

### Phase 1: Discovery and enumeration

- Confirmed the target was alive with `ping`. Four packets sent, four received.
- Ran a full Nmap scan of all 65,535 TCP ports with version detection, default scripts and OS detection, saving all three output formats, then built an HTML report from the XML.

```bash
ping -c 4 192.168.56.101 | tee ping_result.txt
sudo nmap -sV -sC -O -p- -oA initial_scan 192.168.56.101
xsltproc -o initial_scan_report.html /usr/share/nmap/nmap.xsl initial_scan.xml
```

**Result:** 30 open ports. The services include vsftpd 2.3.4, Telnet, Apache 2.2.8 with PHP 5.2.4, Samba 3.0.20, MySQL 5.0.51a, PostgreSQL 8.3, VNC and a service on port 1524 that Nmap labels "Metasploitable root shell".

### Phase 2: Vulnerability identification

```bash
nikto -h http://192.168.56.101 -o nikto_scan.txt
nuclei -u http://192.168.56.101 -o nuclei_web_scan.txt
nuclei -target 192.168.56.101 -o nuclei_full_scan.txt
```

- **Nikto:** 8,242 requests, 30 items reported, 16 errors.
- **Nuclei:** 71 matches in the web scan and 65 in the full scan.
- **Manual checks:** I confirmed a handful of results myself without logging in to anything. I did not try any password and did not run any exploit.

### Phase 3: Analysis and reporting

I rated each finding as likelihood (1 to 3) multiplied by impact (1 to 3), giving High (6 to 9), Medium (3 to 4) or Low (1 to 2). Controls are mapped to **CIS Controls v8** and **NIST CSF 1.1**. A control gap is only stated where the evidence supports it.

## Key results

- **21 findings: 12 High, 7 Medium, 2 Low.**
- **Confirmed by hand (6 findings):** anonymous FTP login; Telnet reachable; default credentials shown in the Telnet login banner; `phpinfo.php` exposed; phpMyAdmin login page reachable; directory listing on `/test/`.
- **Observed directly by Nmap (6):** outdated software, the port 1524 shell service, r-services, SMB signing disabled, SSLv2 with expired certificates, NFS and RPC.
- **Unverified scanner results (9):** for example the vsFTPd backdoor, distccd, PostgreSQL and VNC default passwords, PHP-CGI and the Samba CVE-2026-4480. These are reported as potential risks only.
- Some Nuclei "critical" ratings looked doubtful, such as the AJP result on Tomcat 5.5 and the FTP "weak credentials" results, so I rated them lower and explained why in the report.

## Limitations

- Nuclei reported runtime errors in 10 templates in both scans, reported itself as outdated, and skipped ports 9780, 4040 and 5814 as unresponsive.
- Nikto's update check failed (403) and it logged 16 errors.
- Results are a single snapshot against one virtual machine, and unverified findings were not tested by hand.
