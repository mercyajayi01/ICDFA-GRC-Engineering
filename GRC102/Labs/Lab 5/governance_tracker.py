#!/usr/bin/env python3

import os
import sys
import json
import datetime
import argparse

class GovernanceTracker:
    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {
                "policies": [],
                "controls": [],
                "risks": [],
                "incidents": [],
                "metrics": [],
                "audits": []
            }

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_policy(self, name, description, owner, approval_date, review_date):
        policy = {
            "id": f"POL-{len(self.data['policies']) + 1:03d}",
            "name": name,
            "description": description,
            "owner": owner,
            "approval_date": approval_date,
            "review_date": review_date,
            "status": "Active"
        }
        self.data["policies"].append(policy)
        self.save_data()
        return policy["id"]

    def add_control(self, name, description, policy_id, owner, implementation_date):
        control = {
            "id": f"CTL-{len(self.data['controls']) + 1:03d}",
            "name": name,
            "description": description,
            "policy_id": policy_id,
            "owner": owner,
            "implementation_date": implementation_date,
            "status": "Implemented"
        }
        self.data["controls"].append(control)
        self.save_data()
        return control["id"]

    def add_risk(self, name, description, likelihood, impact, owner, mitigation_plan):
        risk_level = self.calculate_risk_level(likelihood, impact)
        risk = {
            "id": f"RISK-{len(self.data['risks']) + 1:03d}",
            "name": name,
            "description": description,
            "likelihood": likelihood,
            "impact": impact,
            "risk_level": risk_level,
            "owner": owner,
            "mitigation_plan": mitigation_plan,
            "status": "Open"
        }
        self.data["risks"].append(risk)
        self.save_data()
        return risk["id"]

    def add_incident(self, name, description, date, severity, affected_systems, root_cause, resolution):
        incident = {
            "id": f"INC-{len(self.data['incidents']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "severity": severity,
            "affected_systems": affected_systems,
            "root_cause": root_cause,
            "resolution": resolution,
            "status": "Closed"
        }
        self.data["incidents"].append(incident)
        self.save_data()
        return incident["id"]

    def add_metric(self, name, description, target, actual, period, trend, lower_is_better=False):
        metric = {
            "id": f"MET-{len(self.data['metrics']) + 1:03d}",
            "name": name,
            "description": description,
            "target": target,
            "actual": actual,
            "period": period,
            "trend": trend,
            "lower_is_better": lower_is_better,
            "status": "Active"
        }
        self.data["metrics"].append(metric)
        self.save_data()
        return metric["id"]

    def add_audit(self, name, description, date, auditor, findings, recommendations):
        audit = {
            "id": f"AUD-{len(self.data['audits']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "auditor": auditor,
            "findings": findings,
            "recommendations": recommendations,
            "status": "Completed"
        }
        self.data["audits"].append(audit)
        self.save_data()
        return audit["id"]

    def calculate_risk_level(self, likelihood, impact):
        risk_matrix = {
            "High": {"High": "Critical", "Medium": "High", "Low": "Medium"},
            "Medium": {"High": "High", "Medium": "Medium", "Low": "Low"},
            "Low": {"High": "Medium", "Medium": "Low", "Low": "Very Low"}
        }
        return risk_matrix.get(likelihood, {}).get(impact, "Unknown")

    def list_policies(self):
        return self.data["policies"]

    def list_controls(self):
        return self.data["controls"]

    def list_risks(self):
        return self.data["risks"]

    def list_incidents(self):
        return self.data["incidents"]

    def list_metrics(self):
        return self.data["metrics"]

    def list_audits(self):
        return self.data["audits"]

    def generate_dashboard(self):
        dashboard = {
            "generated_date": datetime.datetime.now().isoformat(),
            "summary": {
                "policies": len(self.data["policies"]),
                "controls": len(self.data["controls"]),
                "risks": len(self.data["risks"]),
                "incidents": len(self.data["incidents"]),
                "metrics": len(self.data["metrics"]),
                "audits": len(self.data["audits"])
            },
            "risk_summary": {
                "critical": sum(1 for r in self.data["risks"] if r["risk_level"] == "Critical"),
                "high": sum(1 for r in self.data["risks"] if r["risk_level"] == "High"),
                "medium": sum(1 for r in self.data["risks"] if r["risk_level"] == "Medium"),
                "low": sum(1 for r in self.data["risks"] if r["risk_level"] == "Low"),
                "very_low": sum(1 for r in self.data["risks"] if r["risk_level"] == "Very Low")
            },
            "incident_summary": {
                "critical": sum(1 for i in self.data["incidents"] if i["severity"] == "Critical"),
                "high": sum(1 for i in self.data["incidents"] if i["severity"] == "High"),
                "medium": sum(1 for i in self.data["incidents"] if i["severity"] == "Medium"),
                "low": sum(1 for i in self.data["incidents"] if i["severity"] == "Low")
            },
            "metrics_summary": [
                {
                    "name": m["name"],
                    "target": m["target"],
                    "actual": m["actual"],
                    "status": "Green" if (m["actual"] <= m["target"] if m.get("lower_is_better") else m["actual"] >= m["target"]) else "Red"
                }
                for m in self.data["metrics"]
            ]
        }
        return dashboard

def main():
    parser = argparse.ArgumentParser(description="Security Governance Tracker")
    parser.add_argument("--add-policy", action="store_true")
    parser.add_argument("--add-control", action="store_true")
    parser.add_argument("--add-risk", action="store_true")
    parser.add_argument("--add-incident", action="store_true")
    parser.add_argument("--add-metric", action="store_true")
    parser.add_argument("--add-audit", action="store_true")
    parser.add_argument("--list-policies", action="store_true")
    parser.add_argument("--list-controls", action="store_true")
    parser.add_argument("--list-risks", action="store_true")
    parser.add_argument("--list-incidents", action="store_true")
    parser.add_argument("--list-metrics", action="store_true")
    parser.add_argument("--list-audits", action="store_true")
    parser.add_argument("--dashboard", action="store_true")

    args = parser.parse_args()
    tracker = GovernanceTracker()

    if args.list_policies:
        print(json.dumps(tracker.list_policies(), indent=2))
    elif args.list_controls:
        print(json.dumps(tracker.list_controls(), indent=2))
    elif args.list_risks:
        print(json.dumps(tracker.list_risks(), indent=2))
    elif args.list_incidents:
        print(json.dumps(tracker.list_incidents(), indent=2))
    elif args.list_metrics:
        print(json.dumps(tracker.list_metrics(), indent=2))
    elif args.list_audits:
        print(json.dumps(tracker.list_audits(), indent=2))
    elif args.dashboard:
        print(json.dumps(tracker.generate_dashboard(), indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
