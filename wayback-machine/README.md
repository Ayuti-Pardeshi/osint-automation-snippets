# Wayback Machine Automation Script

## Purpose
This script queries the Wayback Machine (via the CDX API) to extract archived URLs for a given domain. The URLs are grouped by year and exported into a structured JSON file.

## Usage


python wayback_scraper.py

Enter a domain like:

example.com
Output

Creates a JSON file like:

example_com_wayback_data.json

Structure:

{
  "example.com": {
    "2003": ["/index.html", "/about.html"],
    "2004": ["/products/item1", "/contact"]
  }
}
Notes

Uses only passive data (no scanning)

Ideal for OSINT and timeline analysis


---

## Ethical Reminder

This script only uses **public archived data** from a well-known public API. It respects platform boundaries and performs **read-only querying**.

---

## Optional Enhancements (Future Ideas)

- Add filtering by filetype or URL patterns  
- Limit by start/end year  
- Include status codes or snapshot counts  
- Export CSV version too  

---

If you want, I can:

- Add this script to your GitHub repo structure as markdown  
- Help you make a CLI version with flags (like `--domain`, `--out`)  
- Combine this with other OSINT automation scripts into a single toolkit

Let me know what you'd like next.
