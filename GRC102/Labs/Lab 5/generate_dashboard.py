#!/usr/bin/env python3

import json
import base64
import datetime

def load_json(path, default=None):
    import os
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def main():
    governance = load_json("governance_data.json", {"policies": [], "controls": [], "risks": [], "incidents": [], "metrics": [], "audits": []})
    patch_status = load_json("patch_status.json", {})

    import glob
    vuln_reports = sorted(glob.glob("vulnerability_report_*.json"))
    latest_vuln = load_json(vuln_reports[-1]) if vuln_reports else None

    charts = {}
    for name in ["chart_before_after.png", "chart_risk_distribution.png",
                 "chart_patch_compliance_trend.png", "chart_remediation_time_trend.png"]:
        try:
            charts[name] = img_to_base64(name)
        except FileNotFoundError:
            charts[name] = None

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Security Governance Executive Dashboard</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; color: #222; }}
  h1 {{ color: #1a1a1a; }}
  .summary-cards {{ display: flex; gap: 20px; margin: 20px 0; flex-wrap: wrap; }}
  .card {{ background: white; border-radius: 8px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); flex: 1; min-width: 180px; }}
  .card h3 {{ margin: 0 0 8px 0; font-size: 14px; color: #666; text-transform: uppercase; }}
  .card .value {{ font-size: 32px; font-weight: bold; }}
  .green {{ color: #2e7d32; }}
  .red {{ color: #c62828; }}
  .section {{ background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.15); }}
  img {{ max-width: 100%; height: auto; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
  .note {{ font-size: 12px; color: #888; font-style: italic; }}
</style>
</head>
<body>

<h1>Security Governance Executive Dashboard</h1>
<p class="note">Generated {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} &mdash; Simulated environment, GRC102 Practical Lab 8</p>

<div class="summary-cards">
  <div class="card">
    <h3>Critical / High Findings</h3>
    <div class="value {'green' if latest_vuln and latest_vuln['summary']['critical'] == 0 and latest_vuln['summary']['high'] == 0 else 'red'}">
      {latest_vuln['summary']['critical'] + latest_vuln['summary']['high'] if latest_vuln else 'N/A'}
    </div>
  </div>
  <div class="card">
    <h3>Patching Status</h3>
    <div class="value {'green' if patch_status.get('struts_patched') else 'red'}">
      {'Patched' if patch_status.get('struts_patched') else 'Open'}
    </div>
  </div>
  <div class="card">
    <h3>Database Security</h3>
    <div class="value {'green' if patch_status.get('mysql_secured') else 'red'}">
      {'Secured' if patch_status.get('mysql_secured') else 'At Risk'}
    </div>
  </div>
  <div class="card">
    <h3>Network Segmentation</h3>
    <div class="value {'green' if patch_status.get('network_segmented') else 'red'}">
      {'Segmented' if patch_status.get('network_segmented') else 'Flat'}
    </div>
  </div>
</div>

<div class="section">
  <h2>Before vs After Remediation</h2>
  <img src="data:image/png;base64,{charts['chart_before_after.png']}">
</div>

<div class="section">
  <h2>Current Risk Distribution</h2>
  <img src="data:image/png;base64,{charts['chart_risk_distribution.png']}">
</div>

<div class="section">
  <h2>Illustrative Trends</h2>
  <p class="note">The charts below use illustrative historical points leading up to the current, actually-measured value. Earlier points are not real measurements.</p>
  <img src="data:image/png;base64,{charts['chart_patch_compliance_trend.png']}">
  <img src="data:image/png;base64,{charts['chart_remediation_time_trend.png']}">
</div>

<div class="section">
  <h2>Governance Register Summary</h2>
  <table>
    <tr><th>Category</th><th>Count</th></tr>
    <tr><td>Policies</td><td>{len(governance['policies'])}</td></tr>
    <tr><td>Controls</td><td>{len(governance['controls'])}</td></tr>
    <tr><td>Risks</td><td>{len(governance['risks'])}</td></tr>
    <tr><td>Incidents</td><td>{len(governance['incidents'])}</td></tr>
    <tr><td>Metrics Tracked</td><td>{len(governance['metrics'])}</td></tr>
    <tr><td>Audits</td><td>{len(governance['audits'])}</td></tr>
  </table>
</div>

<div class="section">
  <h2>Remediation Notes</h2>
  <p>{patch_status.get('notes', 'No remediation notes recorded.')}</p>
</div>

</body>
</html>
"""

    with open("executive_dashboard.html", "w") as f:
        f.write(html)

    print("Dashboard generated: executive_dashboard.html")

if __name__ == "__main__":
    main()
