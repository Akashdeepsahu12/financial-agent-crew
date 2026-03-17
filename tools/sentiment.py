import feedparser
from textblob import TextBlob

def get_news(company):
    # Google News RSS URL
    url = f"https://news.google.com/rss/search?q={company}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)

    results = []

    for entry in feed.entries[:5]:
        title = entry.get("title", "").strip()

        # 🔥 Clean filter
        if not title or title.lower() == "none":
            continue

        sentiment = TextBlob(title).sentiment.polarity

        results.append({
            "title": title,
            "sentiment": sentiment
        })

    return results