import requests
from bs4 import BeautifulSoup

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self,url):
        self.url = url
        self.title = ""
        self.text = ""
        self.fetch()

    def fetch(self):
        try:
            response = requests.get(self.url,headers=Headers)
            soup = BeautifulSoup(response.content,'html.parser')

            self.title = soup.title.string.strip() if soup.title else "No title found"

            for tag in soup(["script", "style", "img", "input"]):
                tag.decompose()

            self.text = soup.get_text(separator="\n", strip=True)
        except Exception as e:
            raise RuntimeError(f"Error fetching or parsing website: {e}")