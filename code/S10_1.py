import pandas as pd
import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
movies_list = []
for start_num in range(0,250,25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}",headers = headers )
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    #将Top250的电影的中文名称储存在title_string中
    all_items = soup.find_all("div", class_="item")
    for item in all_items:
        movie_info = {}
        title = item.find("span", class_="title")
        #寻找电影的中文名字
        movie_info["中文名称"] = title.text if title and "/" not in title.text else ""
        #找电影的链接
        link = item.find("div", class_="hd").find("a", href=True)
        movie_info["链接"] = link["href"] if link else ""
        #找电影的评分
        rating = item.find("span", class_="rating_num")
        movie_info["评分"] = rating.text if rating else ""
        #找电影的评语
        comment = item.find("p", class_="quote")
        movie_info["评语"] = comment.find("span").text if comment else ""
        movies_list.append(movie_info)
df = pd.DataFrame(movies_list)
df.to_csv('film.csv', index=False, encoding='utf-8-sig')
print("电影信息已保存到 film.csv 文件中。")
