#!/usr/bin/env python3

import subprocess
import json
import datetime
import time

ALERT_LOG = "monitoring_alerts.log"

def log_alert(message):
    timestamp = datetime.datetime.now().isoformat()
    line = f"[{timestamp}] {message}"
    print(line)
    with open(ALERT_LOG, "a") as f:
        f.write(line + "\n")

def check_container_health():
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}\t{{.Status}}"],
        capture_output=True, text=True
    )
    running = {}
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        name, status = line.split("\t", 1)
        running[name] = status
        if not status.startswith("Up"):
            log_alert(f"ALERT: {name} is not healthy (status: {status})")
    for expected in ["web_server", "database_server", "monitoring_server"]:
        if expected not in running:
            log_alert(f"ALERT: {expected} is not running")
    return running

def check_web_logs_for_attack_patterns():
    result = subprocess.run(
        ["docker", "logs", "--since", "60s", "web_server"],
        capture_output=True, text=True
    )
    combined = (result.stdout or "") + (result.stderr or "")
    suspicious_markers = ["com.opensymphony.xwork2", "multipart/form-data", "ClassLoader"]
    for marker in suspicious_markers:
        if marker in combined:
            log_alert(f"ALERT: potential Struts exploitation pattern detected in web_server logs ('{marker}')")

def check_database_auth_failures():
    result = subprocess.run(
        ["docker", "logs", "--since", "60s", "database_server"],
        capture_output=True, text=True
    )
    combined = (result.stdout or "") + (result.stderr or "")
    if "Access denied" in combined:
        count = combined.count("Access denied")
        log_alert(f"ALERT: {count} failed database authentication attempt(s) in the last 60 seconds")

def run_once():
    log_alert("--- Monitoring sweep started ---")
    check_container_health()
    check_web_logs_for_attack_patterns()
    check_database_auth_failures()
    log_alert("--- Monitoring sweep complete ---")

if __name__ == "__main__":
    run_once()
