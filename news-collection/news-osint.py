import feedparser
import csv

# -----------------------------
# KEYWORD INPUT
# -----------------------------

keyword = input("Enter keyword to search: ").lower()

# -----------------------------
# NEWS SOURCES (GLOBAL + INDIA)
# -----------------------------

news_feeds = {

    # Global
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "Reuters": "http://feeds.reuters.com/reuters/topNews",
    "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "The Guardian": "https://www.theguardian.com/world/rss",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "Washington Post": "http://feeds.washingtonpost.com/rss/world",
    "Fox News": "http://feeds.foxnews.com/foxnews/latest",
    "Bloomberg": "https://www.bloomberg.com/feed/podcast/etf-report.xml",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",

    # India
    "Times of India": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "Hindustan Times": "https://www.hindustantimes.com/feeds/rss/topnews/rssfeed.xml",
    "Indian Express": "https://indianexpress.com/section/india/feed/",
    "The Hindu": "https://www.thehindu.com/news/national/feeder/default.rss",
    "NDTV": "https://feeds.feedburner.com/ndtvnews-top-stories",
    "News18": "https://www.news18.com/rss/india.xml",
    "Zee News": "https://zeenews.india.com/rss/india-national-news.xml",
    "India Today": "https://www.indiatoday.in/rss/home",
    "Economic Times": "https://economictimes.indiatimes.com/rssfeedstopstories.cms",
    "Firstpost": "https://www.firstpost.com/rss",
    "Scroll": "https://scroll.in/feeds/home.rss",
    "Deccan Herald": "https://www.deccanherald.com/rss/topstories.xml"
}

results = []

print("\nCollecting articles...\n")

# -----------------------------
# FETCH ARTICLES
# -----------------------------

for source, url in news_feeds.items():

    try:
        feed = feedparser.parse(url)

        for entry in feed.entries:

            title = entry.title.lower()
            summary = ""

            if "summary" in entry:
                summary = entry.summary.lower()

            if keyword in title or keyword in summary:

                results.append({
                    "source": source,
                    "title": entry.title,
                    "url": entry.link
                })

    except Exception as e:
        print(f"Error with {source}")

# -----------------------------
# SAVE RESULTS
# -----------------------------

filename = f"osint_news_{keyword}.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(file, fieldnames=["source", "title", "url"])
    writer.writeheader()
    writer.writerows(results)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("\nCollected Articles:\n")

for r in results:
    print(f"[{r['source']}] {r['title']}")
    print(r['url'])
    print("-"*60)

print(f"\nTotal articles found: {len(results)}")
print(f"Saved to {filename}")
