🚀 Tech Pulse AI: Sentiment-Driven News Aggregator & Analyser
An intelligent dashboard that scrapes, analyzes, and visualizes the "vibe" of the tech industry in real-time.

💡 The Problem
Tech news moves fast. It’s hard to tell if the industry is feeling optimistic or skeptical about new trends (like AI or Crypto) just by glancing at headlines. Also, it is very cumbersome to skim through the whole lot of news so its better to read only what's important that is the headlines!

🛠️ The Solution
I built a modular Python pipeline that:

Scrapes live headlines from sources like Hacker News using BeautifulSoup4. (Currently optimised for only Hacker News website)

Analyzes sentiment polarity using TextBlob (NLP).

Visualizes data via an interactive Streamlit dashboard with real-time keyword filtering.

🏗️ Architecture
Object-Oriented Design: Separate classes for Scraping and Analysis to ensure reusability.

State Management: Utilized Streamlit Session State for high-performance data persistence.

Data Science Stack: Powered by Pandas for dynamic filtering and metric calculation.

Dynamic Exploration: Implemented a real-time Keyword Filter allowing users to isolate specific tech trends (e.g., "OpenAI", "Web3") across the entire dataset instantly.