# PubMed Research Agent

A CLI-based agentic AI that autonomously searches PubMed for any user-provided topic, retrieves publication counts by year, and summarizes key findings using Google Gemini.

## What it does
- Searches PubMed using the NCBI Entrez API
- Retrieves and parses article abstracts
- Shows publication trends by year
- Summarizes findings using Google Gemini AI
- Accepts optional user-defined focus for the summary

## Architecture
User Input → PubMed Search → Fetch Abstracts → Count by Year → Gemini Summary

## Tech Stack
- Python 3.12
- Biopython (NCBI Entrez API)
- Google Gemini AI (google-genai)
- python-dotenv

## Setup

1. Clone the repository
git clone https://github.com/geet1210/ai-task-agent.git
cd ai-task-agent

2. Install dependencies
pip install biopython google-genai python-dotenv

3. Create a .env file
GEMINI_API_KEY=your_gemini_api_key_here

4. Run
python agent.py

## Example Output
Enter a medical topic to research: PDE6
Searching PubMed for: PDE6
Found 10 articles

Publications by year:
2023: 3 articles
2024: 4 articles
2025: 3 articles

Any specific aspect you want to focus on?: structure
Summary of findings: ...

## Concepts Demonstrated
- Agentic AI design pattern
- ReAct loop (Reason + Act + Observe)
- Tool use with external APIs
- LLM-powered summarization