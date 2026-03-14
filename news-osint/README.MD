# News Intelligence Snippets

This repository contains small JavaScript utilities used for building a news intelligence aggregation tool.

The snippets demonstrate techniques used for:

* Fetching news articles from public APIs
* Normalizing article data structures
* Removing duplicate news stories
* Generating AI summaries from multiple articles

These utilities were originally built as part of the **NewsHarvest** project — a tool that collects news articles across sources and produces an AI-generated briefing.

---

## Included Snippets

### 1. News API Search

Fetch news articles dynamically based on a keyword.

### 2. Article Deduplication

Removes duplicate stories using URL matching and title similarity.

### 3. AI News Summary

Uses Gemini API to generate a summarized briefing from multiple articles.

### 4. Article Normalization

Standardizes responses from multiple news APIs into a single structure.

---

## Example Use Case

```
keyword → fetch articles → deduplicate → summarize
```

Useful for:

* news monitoring
* OSINT research
* media analysis
