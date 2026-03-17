def research_task(company, tools, logger):
    logger.log("Researcher", f"Fetching news for {company}")

    news = tools["news"](company)

    if not news:
        return "No recent news found."

    summary = "\n".join([
        f"• {n['title']} (Sentiment: {n['sentiment']:.2f})"
        for n in news
    ])

    return summary