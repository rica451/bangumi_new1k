import requests
from bs4 import BeautifulSoup

# 定义要抓取的 URL
url = 'https://www.google-analytics.com/g/collect?v=2&tid=G-1109JLGMHN&gtm=45je4930v9101808400za200&_p=1725454429945&gcd=13l3l3l3l1l1&npa=0&dma=0&tag_exp=0&cid=537831939.1720622414&ul=zh-cn&sr=1707x960&uaa=x86&uab=64&uafvl=Chromium%3B128.0.6613.114%7CNot%253BA%253DBrand%3B24.0.0.0%7CMicrosoft%2520Edge%3B128.0.2739.54&uamb=0&uam=&uap=Windows&uapv=15.0.0&uaw=0&are=1&frm=0&pscdl=noapi&_eu=AEA&_s=5&sid=1725452453&sct=209&seg=1&dl=https%3A%2F%2Fbangumi.tv%2Fanime%2Fbrowser%3Fsort%3Drank&dr=https%3A%2F%2Fbangumi.tv%2Fgroup&dt=%E5%85%A8%E9%83%A8%E5%8A%A8%E7%94%BB%20%7C%20Bangumi%20%E7%95%AA%E7%BB%84%E8%AE%A1%E5%88%92&en=scroll&epn.percent_scrolled=90&_et=5914&tfd=1645875'

# 定���请求头
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

# 发送 POST 请求

response = requests.post(url, headers=headers)
response.raise_for_status()  # 检查请求是否成功
print("请求成功，状态码:", response.status_code)
print("响应内容:", response.text)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所需的元素并获取其内容
element = soup.select_one('')
if element:
    content = element.get_text()
    print("元素内容:", content)
else:
    print("未找到指定的元素")
