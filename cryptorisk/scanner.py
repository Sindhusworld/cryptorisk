import os
from cryptorisk.secrets import scan_secrets


# ----------------------------
# SCAN SINGLE FILE
# ----------------------------
def scan_file(file_path):
    results = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, start=1):

            # --- MD5 check ---
            if "md5" in line.lower():
                results.append(("HIGH", i, "MD5 usage detected"))

            # --- SHA1 check ---
            if "sha1" in line.lower():
                results.append(("MEDIUM", i, "SHA1 usage detected"))

            # --- SECRET SCANNER (NEW) ---
            results.extend(scan_secrets(line, i))

    except Exception as e:
        results.append(("ERROR", 0, str(e)))

    return results


# ----------------------------
# SCAN FOLDER
# ----------------------------
def scan_folder(path):
    results = []
    summary = {"HIGH": 0, "MEDIUM": 0, "INFO": 0, "ERROR": 0}

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_results = scan_file(file_path)

                results.append((file_path, file_results))

                for level, _, _ in file_results:
                    if level in summary:
                        summary[level] += 1

    return results, summary