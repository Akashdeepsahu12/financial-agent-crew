# AI Financial Analyst Crew - Code Summary

## Overview

This repository implements a lightweight multi-agent financial analysis tool for US equities using Python.

- `app.py`: Streamlit UI frontend (company/ticker controls, analysis trigger, results display).
- `main.py`: CLI entrypoint for running `run_crew` and printing report/logs.
- `orchestrator/crew.py`: Core workflow orchestration (fetch news, compute analysis, generate report, log events).

### Agents

- `agents/researcher.py`: Calls news sentiment tool, formats top results.
- `agents/analyst.py`: Calls stock data tool, computes average and latest closing price, generates chart image.
- `agents/writer.py`: Compiles final report text from research + analysis.

### Tools

- `tools/market_data.py`: Uses `yfinance` to retrieve 6-month stock history.
- `tools/sentiment.py`: Scrapes Google News RSS for company, scores titles with `TextBlob` sentiment polarity.
- `tools/charting.py`: Plots close price history with Matplotlib and saves `output/charts/{ticker}.png`.

### Utilities

- `utils/logger.py`: Simple timestamped logger for agent events; writes `output/log.txt`.

## Execution Flow

1. `run_crew(company, ticker)` initializes `AgentLogger` and tool mapping.
2. `research_task` fetches and summarizes news items.
3. `analysis_task` fetches stock history, calculates averages/latest price, and generates chart file.
4. `write_report` creates markdown-like report plus recommendation text.
5. `run_crew` logs process, writes log file, returns report and log text.

## Output

- `output/log.txt`: All agent/action logs.
- `output/charts/{ticker}.png`: Stock price chart.

## Dependencies

- Python packages: `streamlit`, `yfinance`, `feedparser`, `textblob`, `matplotlib`, `Pillow`.
- `requirements.txt` should include these (verify installed environment).

## Notes

- This repo is architecture-friendly for extension with more agents (e.g., risk model, macro analysis).
- Error handling is minimal; production hardening should add input validation and API failure resilience.
