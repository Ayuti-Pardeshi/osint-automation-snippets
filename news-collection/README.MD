OSINT News Intelligence Collector

A Python-based Open Source Intelligence (OSINT) tool that automatically collects news article URLs from multiple international and Indian news outlets based on user-defined keyword queries.

The script aggregates publicly available information from RSS feeds of major news organizations and extracts relevant articles containing the specified keyword. The collected data can assist in monitoring events, cyber incidents, geopolitical developments, and emerging threats.

Overview

Open Source Intelligence (OSINT) involves collecting and analyzing information from publicly available sources. News platforms are one of the most important OSINT sources for understanding global events, cyber incidents, and geopolitical developments.

This tool automates the process of monitoring multiple news outlets and collecting relevant articles for a given topic or keyword.

Features

Collects news articles from 20+ global and Indian news sources

Keyword-based intelligence gathering

Extracts article title, source, and URL

Supports multiple international news outlets

Exports results to CSV format

Useful for OSINT investigations, cyber threat intelligence, and research

Supported News Sources
Global News Sources

BBC

Reuters

New York Times

The Guardian

Al Jazeera

CNN

Washington Post

Fox News

Bloomberg

CNBC

Indian News Sources

Times of India

Hindustan Times

Indian Express

The Hindu

NDTV

News18

Zee News

India Today

Economic Times

Firstpost

Scroll

Deccan Herald

Installation

Clone the repository

git clone https://github.com/yourusername/osint-news-collector.git
cd osint-news-collector

Install required dependency

pip install feedparser
Usage

Run the script

python3 news_osint.py

Enter the keyword when prompted

Enter keyword to search: ransomware

Example output

[Reuters] Global ransomware attacks increase
https://www.reuters.com/article/...

[BBC] Cyber attack affects telecom infrastructure
https://www.bbc.com/news/...

Results will also be saved in a CSV file

osint_news_ransomware.csv
Output Format

The script generates a CSV file containing:

Source	Title	URL
Reuters	Global ransomware attacks increase	https://...
BBC	Cyber attack affects telecom infrastructure	https://...
Use Cases

This tool can be useful for:

Cyber Threat Intelligence monitoring

Tracking cyber attacks and data breaches

Geopolitical event monitoring

News intelligence gathering

Security research and analysis

Academic research projects

Ethical Use

This project collects data only from publicly available RSS feeds of news organizations.
It is intended strictly for research, educational, and OSINT purposes.

Future Improvements

Possible enhancements include:

Adding more global news sources

Exporting results to JSON format

Removing duplicate articles

Building a timeline of collected news

Integrating with Google News search

Adding automated alerts for new articles

License

This project is open-source and available under the MIT License.
