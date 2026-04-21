import argparse
from cryptorisk.scanner import run_scan


def cli():
    parser = argparse.ArgumentParser(description="CryptoRisk Scanner")
    parser.add_argument("path", help="Path to scan")

    args = parser.parse_args()

    results = run_scan(args.path)

    print("\nDetailed Results:\n")

    for file in results["files"]:
        print(f"\n{file['file']}")
        for r in file["risks"]:
            print(f"  - {r[0]}: {r[1]}")


if __name__ == "__main__":
    cli()