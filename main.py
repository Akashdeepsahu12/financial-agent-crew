
from orchestrator.crew import run_crew

if __name__ == "__main__":
    company = "Tesla"
    ticker = "TSLA"

    report, logs = run_crew(company, ticker)

    print("\n=== FINAL REPORT ===\n")
    print(report)

    print("\n=== AGENT LOGS ===\n")
    print(logs)
