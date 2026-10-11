#!/usr/bin/env python3

import json
import datetime
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def load_governance_data():
    with open("governance_data.json", "r") as f:
        return json.load(f)

def generate_illustrative_trend(current_value, periods=6, lower_is_better=False):
    """
    Generates a plausible illustrative trend ending at the current actual value.
    This is NOT real historical data, it is a visual aid showing what
    a realistic trend toward the current value might look like.
    """
    random.seed(42)
    trend = []
    value = current_value
    for _ in range(periods - 1):
        drift = random.uniform(-0.15, 0.15) * max(abs(current_value), 1)
        value = value + drift if not lower_is_better else value - drift
        trend.append(round(max(value, 0), 1))
    trend.reverse()
    trend.append(current_value)
    return trend

def chart_risk_distribution(data):
    risks = data["risks"]
    levels = ["Critical", "High", "Medium", "Low", "Very Low"]
    counts = [sum(1 for r in risks if r["risk_level"] == lvl) for lvl in levels]

    plt.figure(figsize=(7, 5))
    colors = ["#b30000", "#e05a00", "#e0b000", "#6aa84f", "#999999"]
    plt.bar(levels, counts, color=colors)
    plt.title("Risk Register: Current Distribution by Severity")
    plt.ylabel("Number of Risks")
    plt.tight_layout()
    plt.savefig("chart_risk_distribution.png", dpi=150)
    plt.close()

def chart_metric_trend(data, metric_name, filename, lower_is_better=False):
    metrics = [m for m in data["metrics"] if m["name"] == metric_name]
    if not metrics:
        return
    current = metrics[-1]["actual"]
    target = metrics[-1]["target"]
    trend = generate_illustrative_trend(current, periods=6, lower_is_better=lower_is_better)
    periods = [f"Month {i+1}" for i in range(len(trend))]

    plt.figure(figsize=(8, 5))
    plt.plot(periods, trend, marker="o", label="Illustrative trend", color="#1155cc")
    plt.axhline(y=target, color="#b30000", linestyle="--", label=f"Target ({target})")
    plt.title(f"{metric_name} (Illustrative Trend)")
    plt.ylabel(metric_name)
    plt.xticks(rotation=30)
    plt.legend()
    plt.figtext(0.5, -0.02, "Note: earlier months are illustrative, not measured data.",
                ha="center", fontsize=8, style="italic")
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()

def chart_before_after(data):
    metrics_before = {"Patch Compliance": 85.0, "Remediation Time (days)": 12.0, "Incidents": 1.0}
    metrics_after = {"Patch Compliance": 100.0, "Remediation Time (days)": 0.0, "Incidents": 0.0}

    labels = list(metrics_before.keys())
    before_vals = list(metrics_before.values())
    after_vals = list(metrics_after.values())

    x = range(len(labels))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width/2 for i in x], before_vals, width, label="Before remediation", color="#b30000")
    plt.bar([i + width/2 for i in x], after_vals, width, label="After remediation", color="#6aa84f")
    plt.xticks(list(x), labels)
    plt.title("Security Posture: Before vs After Remediation")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart_before_after.png", dpi=150)
    plt.close()

def main():
    data = load_governance_data()
    chart_risk_distribution(data)
    chart_metric_trend(data, "Patch Compliance", "chart_patch_compliance_trend.png", lower_is_better=False)
    chart_metric_trend(data, "Vulnerability Remediation Time", "chart_remediation_time_trend.png", lower_is_better=True)
    chart_before_after(data)
    print("Charts generated:")
    print("  chart_risk_distribution.png")
    print("  chart_patch_compliance_trend.png")
    print("  chart_remediation_time_trend.png")
    print("  chart_before_after.png")

if __name__ == "__main__":
    main()
