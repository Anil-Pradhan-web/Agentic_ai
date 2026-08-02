import os
import re
from datetime import datetime

SKILLS_FOLDER = "skills"
REPORT_FILE = "vulnerability_report.md"

danger_patterns = [
    "subprocess",
    "os.system",
    "eval(",
    "exec(",
    "password",
    "private_key",
    "secret",
    "token",
    "api_key"
]


def scan_file(file_path):
    issues = []

    try:
        with open(file_path, "r", errors="ignore") as file:
            content = file.read()

            for pattern in danger_patterns:
                if pattern.lower() in content.lower():
                    issues.append(
                        f"Possible risky pattern found: `{pattern}`"
                    )

    except Exception as e:
        issues.append(f"Could not read file: {e}")

    return issues


def scan_skills():
    results = []

    for root, _, files in os.walk(SKILLS_FOLDER):
        for file in files:
            path = os.path.join(root, file)

            issues = scan_file(path)

            if issues:
                results.append({
                    "file": path,
                    "issues": issues
                })

    return results


def generate_report(results):

    with open(REPORT_FILE, "w") as report:
        report.write("# Skill Spector Vulnerability Report\n\n")
        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        if not results:
            report.write(
                "No suspicious patterns detected.\n"
            )
        else:
            for item in results:
                report.write(
                    f"## {item['file']}\n"
                )

                for issue in item["issues"]:
                    report.write(
                        f"- {issue}\n"
                    )

                report.write("\n")


if __name__ == "__main__":

    findings = scan_skills()

    generate_report(findings)

    print("Scan completed.")
    print("Report saved:", REPORT_FILE)