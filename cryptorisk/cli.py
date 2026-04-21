import argparse
from cryptorisk.scanner import scan_folder
from cryptorisk.report import save_json, save_html


def cli():
    parser = argparse.ArgumentParser(description="CryptoRisk Scanner")
    parser.add_argument("command", help="scan")
    parser.add_argument("path", help="Path to scan")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--html", action="store_true")

    args = parser.parse_args()

    if args.command != "scan":
        print("Only 'scan' command supported")
        return

    print("\n🔐 CryptoRisk PRO Scanner (FINAL ENGINE)\n")

    results, summary = scan_folder(args.path)

    # ---------------- PRINT RESULTS ----------------
    for file, risks in results:
        print(f"\n📄 FILE: {file}")
        for level, line, msg in risks:
            print(f"  → {level} (line {line}): {msg}")

    print("\n====================")
    print("📊 SUMMARY REPORT")
    print("====================")
    print(summary)

    # ---------------- OPTIONAL REPORTS ----------------
    if args.json:
        save_json(results, summary)

    if args.html:
        save_html(results, summary)


if __name__ == "__main__":
    cli()