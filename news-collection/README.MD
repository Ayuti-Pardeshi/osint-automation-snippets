🛰️ OSINT News Intelligence Collector

A Python-based Open Source Intelligence (OSINT) tool that collects news article URLs from 20+ international and Indian news outlets based on a user-defined keyword.

The script automatically aggregates publicly available information from RSS feeds of major news organizations and extracts articles relevant to the keyword.

This project demonstrates automated intelligence gathering from open sources, commonly used in Cyber Threat Intelligence (CTI), security research, and geopolitical monitoring.

📌 Overview

Open Source Intelligence (OSINT) involves collecting and analyzing information from publicly accessible sources.

News platforms are among the most valuable OSINT sources for tracking:

cyber incidents

geopolitical developments

misinformation campaigns

emerging global events

This tool helps automate the process of monitoring multiple news sources simultaneously.

⚙️ Features

✅ Collects articles from 20+ global and Indian news outlets
✅ Keyword-based intelligence gathering
✅ Extracts title, source, and article URL
✅ Saves results in CSV format
✅ Uses public RSS feeds (OSINT-friendly)
✅ Lightweight and easy to run

🌍 Supported News Sources
📰 Global Sources

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

🇮🇳 Indian Sources

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

📦 Installation

Clone the repository

git clone https://github.com/yourusername/osint-news-collector.git
cd osint-news-collector

Install dependency

pip install feedparser
🚀 Usage

Run the script

python3 news_osint.py

Enter the keyword when prompted:

Enter keyword to search: ransomware

Example output:

[Reuters] Global ransomware attacks increase
https://www.reuters.com/article/...

[BBC] Cyber attack affects telecom infrastructure
https://www.bbc.com/news/...
📊 Output

The script generates a CSV file containing collected intelligence data.

Example:

osint_news_ransomware.csv

CSV format:

Source	Title	URL
Reuters	Global ransomware attacks increase	https://...
BBC	Cyber attack affects telecom infrastructure	https://...
🧠 OSINT Use Cases

This tool can assist in:

🔎 Cyber Threat Intelligence (CTI)
🌐 Geopolitical monitoring
📡 Security research
📰 News intelligence gathering
📊 Academic research projects
🛡️ Tracking cyber attacks and data breaches

🔒 Ethical Use

This project collects data only from publicly available RSS feeds of news organizations.

It is intended strictly for:

OSINT research

educational purposes

security analysis

Please use responsibly and respect the terms of service of the respective news platforms.

🔮 Future Improvements

Possible enhancements:

Add more global news sources

Export results to JSON

Remove duplicate URLs

Generate timeline-based intelligence reports

Integrate Google News search

Build a dashboard for visualization

📁 Project Structure
osint-news-collector
│
├── news_osint.py
├── README.md
└── sample_output.csv
📜 License

This project is released under the MIT License.
