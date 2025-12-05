import requests
from bs4 import BeautifulSoup
proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
for start_num in range(0,250,25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}",headers = headers )
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    #将Top250的电影的中文名称储存在title_string中
    all_title = soup.find_all("span",attrs={"class":"title"})
    title_list = []
    print(f"状态码: {response.status_code}")
    print(f"响应头: {response.headers}")
    print(f"响应内容前500字符: {response.text[:500]}")
    for title in all_title:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)

    #         title_list.append(title.string)
    # #将Top250的链接放在link_list中
    # link_list = []
    # all_links_div = soup.find_all("div", attrs={"class":"hd"})
    # for hd in all_links_div:
    #     link = hd.find("a",href=True)
    #     link_list.append(link["href"])
    #     print(link["href"])
    #






