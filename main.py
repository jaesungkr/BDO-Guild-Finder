import pandas as pd
import numpy as np
import requests, re
from bs4 import BeautifulSoup
guild_name = '우리와써또와써'
url = f"https://www.kr.playblackdesert.com/Adventure/Guild/GuildProfile?guildName={guild_name}"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Guild members extracting
crew_list = []
unordered = soup.find_all("div", {"class": "container guild_profile"})
unordered_list = soup.find_all("span", {"class": "text"})
unordered_list.pop(0)
people_list = unordered_list
#print(people_list[0])
for x in people_list:
   #soup_set.append(str(x))
    crew_list.append(re.compile('">([a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+)').findall(str(x)))

# 길드원 수
n_crew = len(crew_list)
print(crew_list)
print(n_crew)


