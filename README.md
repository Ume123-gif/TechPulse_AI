# TechPulse_AI — News Sentiment Aggregator
A modular Python pipeline that scrapes live tech headlines, scores sentiment polarity, and visualizes trends through an interactive dashboard.

# What It Does
Tech news moves fast and reading through dozens of headlines to gauge industry sentiment is inefficient. TechPulse_AI scrapes headlines from Hacker News, classifies them as positive, negative, or neutral using NLP, and lets you filter by keyword to explore sentiment trends across topics like "AI", "crypto", or "Web3".

# Tech Stack
* Python — core pipeline
* BeautifulSoup4 — HTML parsing and headline scraping
* TextBlob — lexicon-based sentiment polarity scoring
* Streamlit — interactive dashboard with real-time keyword filtering
* Pandas — data filtering and metric calculation

# Architecture
The project is split into two reusable OOP classes:
* TechScraper — handles HTTP requests, HTML parsing, and error handling for failed/missing selectors
* TechAnalyser — takes scraped headlines, scores polarity via TextBlob, and applies threshold-based sentiment labels (positive / negative / neutral)
Streamlit Session State is used to persist scraped data across user interactions without re-fetching on every filter change.

# Current Limitations
* Scrapes Hacker News only (single source)
* Sentiment scoring uses TextBlob's lexicon model — no custom-trained classifier yet
* No caching or scheduled refresh; data is fetched on demand when the app is run

# How To Run
```bash
git clone https://github.com/Ume123-gif/TechPulse_AI
cd TechPulse_AI
pip install -r requirements.txt
streamlit run app.py
```
# Planned Improvements
* Add second/third news source (Reddit r/technology, TechCrunch RSS)
* Replace TextBlob with a trained scikit-learn classifier for higher accuracy
* Add 15-minute TTL cache to reduce redundant scraping
