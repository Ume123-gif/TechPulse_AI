import requests 
from bs4 import BeautifulSoup

class TechScraper:

    def __init__(self,url):
        self.url=url
        self.headers={"User-Agent": "Mozilla/5.0"}

    def fetch_html(self):
        try:
            response=requests.get(self.url,headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None
        
    def extract_headlines(self, html, selector):
        if not html:
            return []
        try:
            soup=BeautifulSoup(html, "html.parser")
            tags=soup.find_all(class_=selector)
            if not tags:
                print(f"Warning: No elements found with class - '{selector}'")
            headlines=[]
            for tag in tags:
                text=tag.get_text().strip()
                if text:
                    headlines.append(text)
            return headlines
        except Exception as e:
            print(f"Error during parsing: {e}")
            return []


if __name__ == "__main__":
    test_url = "https://news.ycombinator.com/"
    scraper = TechScraper(test_url)
    raw_html = scraper.fetch_html()
    results = scraper.extract_headlines(raw_html, "titleline")
    print(f"Found {len(results)} headlines:")
    for r in results[:5]: 
        print(f"- {r}")