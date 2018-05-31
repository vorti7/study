from bs4 import BeautifulSoup

import requests

s_url = "https://www.melon.com/"

naver = requests.get(s_url)
bs = BeautifulSoup(naver.text,"html.parser")
top_list = bs.select("a.ah_a")
for _ in top_list:
    print(_.text)
