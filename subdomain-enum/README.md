Subdomain Enumeration (Passive OSINT Automation)
Overview

This utility automates passive subdomain discovery for a given domain and exports the results into a structured JSON file.

It is designed for infrastructure visibility analysis and OSINT-driven reconnaissance workflows. The script functions as a controlled wrapper around Sublist3r in a Kali Linux environment.

No active scanning or intrusive techniques are used.

Objective

Discover publicly visible subdomains

Generate structured output for further analysis

Support domain footprint mapping

Maintain reproducible automation workflow

Environment

Python 3.x

Kali Linux (recommended)

Sublist3r installed

Install Sublist3r if required:

sudo apt install sublist3r
Execution

Run the script:

python3 subdomain_enum.py

Enter the target domain when prompted.

Output Structure

The script generates a JSON file formatted as:

{
  "domain": "example.com",
  "subdomains": [
    "mail.example.com",
    "api.example.com",
    "dev.example.com"
  ],
  "count": 3
}

This structured output allows integration into:

Infrastructure mapping workflows

Threat intelligence enrichment

Exposure monitoring pipelines

Historical comparison analysis

Practical Relevance

Subdomain discovery is foundational in:

Digital footprint assessment

Attack surface mapping

Identifying shadow IT assets

Supporting CTI research

Public subdomains frequently reveal staging environments, legacy services, and externally exposed infrastructure components.

Operational Considerations

Passive enumeration only

Intended for authorized environments

No exploitation or active probing performed

Scope

This utility focuses strictly on structured automation and data formatting. It does not attempt to replace full reconnaissance frameworks.
