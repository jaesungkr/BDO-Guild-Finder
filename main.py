import pandas as pd
import numpy as np
import requests, re
from bs4 import BeautifulSoup

url = "https://www.kr.playblackdesert.com/Adventure/Guild/GuildProfile?guildName=%EC%9A%B0%EB%A6%AC%EC%99%80%EC%8D%A8%EB%98%90%EC%99%80%EC%8D%A8"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print nicely
# print(soup.prettify())

unordered = soup.find_all("div", {"class": "container guild_profile"})
my_list = soup.find_all("span", {"class": "text"})




print(my_list)

