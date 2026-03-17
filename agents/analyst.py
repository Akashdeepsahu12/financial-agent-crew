
def analysis_task(ticker, tools, logger):
    logger.log("Analyst", f"Fetching stock data for {ticker}")

    data = tools["market"](ticker)
    hist = data["history"]

    if hist.empty:
        logger.log("Analyst", "No stock data found")
        return {"summary": "No data available", "chart": None}

    avg_price = hist["Close"].mean()
    latest_price = hist["Close"].iloc[-1]

    chart = tools["chart"](hist, ticker)

    logger.log("Analyst", "Analysis complete")

    return {
        "summary": f"Avg Price: {avg_price:.2f}, Latest Price: {latest_price:.2f}",
        "chart": chart
    }
