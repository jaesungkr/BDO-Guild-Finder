import pandas as pd
import numpy as np
import requests, re
from bs4 import BeautifulSoup

url = "https://www.kr.playblackdesert.com/Adventure/Guild/GuildProfile?guildName=%EC%9A%B0%EB%A6%AC%EC%99%80%EC%8D%A8%EB%98%90%EC%99%80%EC%8D%A8"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print nicely
# print(soup.prettify())
my_list = []
unordered = soup.find_all("div", {"class": "container guild_profile"})
unordered_list = soup.find_all("span", {"class": "text"})
unordered_list.pop(0)
people_list = unordered_list
#print(people_list[0])
for x in people_list:
    my_list.append(str(x))

# 아이디 추출
a = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+').findall(my_list[0])
print(a)

#print(re.findall('">[\', people_list[0]))


#print(unordered)
#print(len(my_list))

