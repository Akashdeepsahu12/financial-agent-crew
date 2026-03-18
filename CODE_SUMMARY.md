# AI Financial Analyst Crew - Code Summary

## Code Summary

AI Financial Analyst Crew is a modular Python project that uses a multi-agent workflow to combine market news sentiment and historical stock price data into an automated report. It is structured as:

- `app.py`: Streamlit dashboard for interactive stock analysis.
- `main.py`: CLI script for offline execution.
- `orchestrator/crew.py`: Orchestration of researcher, analyst, writer tasks and tool integrations.
- `agents/researcher.py`: News fetching and sentiment summary.
- `agents/analyst.py`: Stock data analysis and chart generation.
- `agents/writer.py`: Report generation.
- `tools/market_data.py`: `yfinance` data retrieval.
- `tools/sentiment.py`: RSS scraping plus `TextBlob` sentiment.
- `tools/charting.py`: Matplotlib chart output.
- `utils/logger.py`: Timestamps and logging to `output/log.txt`.

## How to Run

1. Clone repository and change directory:
   - `git clone <repo-url>`
   - `cd financial-agent-crew`

2. Create and activate virtual environment:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   - `pip install -r requirements.txt`

4. Run CLI example:
   - `python main.py`

5. Run Streamlit web UI:
   - `streamlit run app.py`

6. Inspect results:
   - `output/log.txt` for logs
   - `output/charts/{ticker}.png` for generated chart

## Dependencies

- Python packages: `streamlit`, `yfinance`, `feedparser`, `textblob`, `matplotlib`, `Pillow`.
