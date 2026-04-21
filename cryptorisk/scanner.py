import os
import re
import json
from datetime import datetime

RULES = [
    (r"(?i)md5\s*\(", "HIGH", "MD5 usage detected"),
    (r"(?i)sha1\s*\(", "MEDIUM", "SHA1 usage detected"),
    (r"(?i)password\s*=", "HIGH", "Hardcoded password detected"),
    (r"(?i)api[_-]?key\s*=", "HIGH", "Hardcoded API key detected"),
]


def scan_file(path):
    risks = []

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

            for pattern, level, message in RULES:
                if re.search(pattern, content):
                    risks.append([level, message])

    except Exception as e:
        risks.append(["ERROR", str(e)])

    return risks


def scan_directory(base_path):
    results = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)

                results.append({
                    "file": full_path,
                    "risks": scan_file(full_path)
                })

    return results


def generate_report(results):
    summary = {"HIGH": 0, "MEDIUM": 0, "INFO": 0, "ERROR": 0}

    for f in results:
        for r in f["risks"]:
            if r[0] in summary:
                summary[r[0]] += 1

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "summary": summary,
        "files": results
    }


def run_scan(path):
    results = scan_directory(path)
    report = generate_report(results)

    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("Scan complete")
    print(json.dumps(report["summary"], indent=2))

    # CI FAIL RULE
    if report["summary"]["HIGH"] > 0:
        print("❌ HIGH risk detected")
        exit(1)

    return report