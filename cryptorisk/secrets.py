import re

# ----------------------------
# SECRET PATTERNS DATABASE
# ----------------------------
SECRET_PATTERNS = {
    "AWS_ACCESS_KEY": r"AKIA[0-9A-Z]{16}",
    "GITHUB_TOKEN": r"ghp_[A-Za-z0-9]{36}",
    "STRIPE_KEY": r"sk_live_[0-9a-zA-Z]{24,}",
    "PRIVATE_KEY": r"-----BEGIN PRIVATE KEY-----",
    "JWT_TOKEN": r"eyJ[A-Za-z0-9_-]+?\.[A-Za-z0-9_-]+?\.[A-Za-z0-9_-]+"
}


# ----------------------------
# SCAN ONE LINE FOR SECRETS
# ----------------------------
def scan_secrets(line, line_no):
    findings = []

    for name, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, line):
            findings.append(("HIGH", line_no, f"{name} detected"))

    return findings