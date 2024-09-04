import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry  # 使用urllib3库中的Retry


def

url = "https://bangumi.tv/anime/browser?sort=rank"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
session = requests.Session()
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

try:
    response = session.get(url, headers=headers)
    response.raise_for_status()  # 检查响应状态码

    soup = BeautifulSoup(response.content, 'html.parser')

    anime_links = soup.find_all('a', class_='l')
    print(anime_links)

    for link in anime_links:
        href = link.get('href')
        print(href)
except requests.exceptions.RequestException as e:
    print(f"发生错误: {e}")