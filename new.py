import re
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry  # 使用urllib3库中的Retry


def get_bgm_url(page_num):
    url_list = []
    vote_num = []
    base_url = "https://bangumi.tv/anime/browser?sort=rank&page="
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

    for i in range(1, page_num + 1):
        url = base_url + str(i)
        response = session.get(url, headers=headers)
        response.raise_for_status()  # 检查响应状态码
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取动画链接
        anime_links = soup.find_all('a', class_='l')
        for link in anime_links:
            href = link.get('href')
            if '/subject' in href:
                url_list.append(href)

        # 提取评分人数
        rating_spans = soup.find_all('span', class_='tip_j')
        for span in rating_spans:
            number = re.findall(r'\d+', span.text)
            if number:
                vote_num.append(number[0])

    return url_list, vote_num


def get_need_points(vote_num):
    # 每种类别需要的数量
    pass


def data_deal(stars, need_num):
    # 数据处理
    stars = [int(num) for num in stars]
    ahead_10_result = sum(stars)
    return ahead_10_result / sum(need_num)



def get_points(url_list, vote_num):
    result = []
    page_num = 1
    kind = ['/collections?page=', '/doings?page=', '/on_hold?=?', '/dropped?page=']
    stars = []
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

    for i, url in enumerate(url_list):
        base_url = "https://bangumi.tv" + url + '/collections'
        response = session.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        num_temp = soup.find_all('small')
        need_num = []
        stars = []
        for n in num_temp:
            number = re.findall(r'\d+', n.text)
            if number:
                need_num.append(number[0])
        need_num = need_num[1:5]
        need_num = [int(num) for num in need_num]
        total_need_num = sum(need_num)
        for j in range(4):
            need_num[j] = int(need_num[j]) * int(vote_num[i]) / (10 * total_need_num)
            need_num[j] = int(need_num[j])
        print(need_num)

        for k, kind_content in enumerate(kind):
            success_num = 0
            while True:
                base_url = "https://bangumi.tv" + url + kind_content + str(page_num)
                response = session.get(base_url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                stars_recent = soup.find_all('span', class_=re.compile(r'\bstarlight\b'))
                for s in stars_recent:
                    class_list = s.get('class')
                    for cls in class_list:
                        number = re.findall(r'\d+', cls)
                        if number:
                            stars.append(number[0])
                            success_num += 1
                page_num += 1
                print(f"page{page_num - 1} success_num:{success_num}")
                if success_num > need_num[k]:
                    need_num[k] = success_num
                    page_num = 1
                    print("success")
                    break
        result.append(data_deal(stars, need_num))
        print(result)
    with open('result.txt', 'w') as file:
        for item in result:
            file.write(f"{item}\n")



if __name__ == '__main__':
    url_list, vote_num = get_bgm_url(20)
    print(url_list)
    print(vote_num)
    # 爬取前480的动画链接和评分人数
    get_points(url_list, vote_num)
