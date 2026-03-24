# AI Financial Analyst

## Description

AI Financial Analyst is an exploratory Python project that combines multi-agent pipelines, news sentiment, and stock market data to generate automated trading intelligence and visualizations. The app uses Streamlit for UI, yfinance for historical data, and RSS sentiment analysis to deliver a quick stock snapshot.

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

## What I Used / Tech Stack

- Language: Python 3.10+ (or compatible)
- UI: Streamlit (`app.py` for interactive dashboard)
- Orchestration: Custom agent workflow in `orchestrator/crew.py`
- Data sources:
  - `yfinance` for historical stock data
  - Google News RSS (`feedparser`) for news
- NLP/Sentiment: `TextBlob` for polarity scoring
- Visualization: `matplotlib` for generating stock charts
- Logging: custom `AgentLogger` in `utils/logger.py`
- Storage: local filesystem (`output/log.txt`, `output/charts/*.png`)

## Dependencies

- Python packages: `streamlit`, `yfinance`, `feedparser`, `textblob`, `matplotlib`, `Pillow`.
- `requirements.txt` should include these (verify installed environment).

## How to Run

1. Clone the repository:
   - `git clone <repo-url>`
   - `cd financial-agent-crew`

2. Create and activate a Python virtual environment:
   - `python -m venv venv`
   - Windows: `venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   - `pip install -r requirements.txt`

4. Run CLI version:
   - `python main.py`

5. Run Streamlit UI:
   - `streamlit run app.py`

6. Open browser for Streamlit at provided local URL (typically `http://localhost:8501`).

7. Check outputs:
   - `output/log.txt` for agent logs.
   - `output/charts/{ticker}.png` for generated chart.

## Real-world Problem Solved

This project addresses the challenge of quickly synthesizing market news sentiment and historical price trends into a single, readable report for decision support. It helps retail traders, financial analysts, and small advisory teams perform initial stock screening and sentiment-informed risk checks without manual data stitching.

## How to Scale

1. Parallelized agent pipeline
   - Convert sequential `research_task` + `analysis_task` to asynchronous or multiprocessing to handle many tickers per run.
   - Use a task queue (Celery/RQ) for distributed worker execution.

2. Production maturity
   - Add robust error handling, retries, and circuit-breakers for API failures.
   - Store results in a database (PostgreSQL, MongoDB) instead of local filesystem.

3. Data scaling
   - Replace `yfinance` with a dedicated market data provider (e.g., Alpha Vantage, IEX, or paid API) for higher quota and historical depth.
   - Cache news/sentiment results in Redis to avoid repeated RSS pulls.

4. Model improvements
   - Improve sentiment with transformer models (e.g., HuggingFace `distilbert-base-uncased-finetuned-sst-2`) and fine-tune on finance text.
   - Add risk/volatility signals, event detection, and cross-asset correlation analysis.

5. Deployment
   - Containerize with Docker + Kubernetes for reliability.
   - Add CI/CD and monitoring (Prometheus/Grafana, Sentry).

## Notes

- This repo is architecture-friendly for extension with more agents (e.g., risk model, macro analysis).
- Error handling is minimal; production hardening should add input validation and API failure resilience.
