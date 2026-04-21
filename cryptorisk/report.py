import json


# ----------------------------
# SAVE JSON REPORT
# ----------------------------
def save_json(results, summary):
    data = {
        "summary": summary,
        "files": []
    }

    for file, risks in results:
        data["files"].append({
            "file": file,
            "risks": risks
        })

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("\n📁 JSON report saved: report.json")


# ----------------------------
# SAVE HTML REPORT
# ----------------------------
def save_html(results, summary):
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>CryptoRisk Report</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        h1 {{ color: #222; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        .HIGH {{ color: red; font-weight: bold; }}
        .MEDIUM {{ color: orange; }}
        .INFO {{ color: blue; }}
        .ERROR {{ color: gray; }}
    </style>
</head>
<body>

<h1>🔐 CryptoRisk Security Report</h1>

<h2>Summary</h2>
<pre>{summary}</pre>

<h2>Details</h2>
""".format(summary=summary)

    for file, risks in results:
        html += f"<h3>{file}</h3>"
        html += "<table>"
        html += "<tr><th>Level</th><th>Line</th><th>Message</th></tr>"

        for level, line, msg in risks:
            html += f"<tr><td class='{level}'>{level}</td><td>{line}</td><td>{msg}</td></tr>"

        html += "</table>"

    html += """
</body>
</html>
"""

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\n🌐 HTML report saved: report.html")