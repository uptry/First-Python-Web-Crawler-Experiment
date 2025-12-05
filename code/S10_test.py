import requests
from bs4 import BeautifulSoup
import time

# 1. 设置代理（必须！）
proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

# 2. 爬取一页试试
url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
print(f"状态码: {response.status_code}")

# 3. 解析数据
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all('div', class_='item')

for movie in movies[:5]:  # 只看前5部
    title = movie.find('span', class_='title').text
    rating = movie.find('span', class_='rating_num').text
    print(f"{title} - {rating}分")

# 等3秒再继续
time.sleep(3)