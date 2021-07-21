import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

def find_user(username, guild_lists):
    for i in range(len(guild_lists)):
        tmp, guild = crew_crawling(guild_lists[i])
        # print(guild)
        if username in guild:
            return guild_lists[i], tmp


def crew_crawling(guild_name):
    url = f"https://www.kr.playblackdesert.com/Adventure/Guild/GuildProfile?guildName={guild_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Guild members extracting
    crew_list = []
    unordered_list = soup.find_all("span", {"class": "text"})
    unordered_list.pop(0)
    people_list = unordered_list

    for x in people_list:
        crew_list.append(re.compile('">([0-9|a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+)').findall(str(x))[0])
    # number of crew members
    n_crew = len(crew_list)
    return n_crew, crew_list

def saving_list(crew_list):
    df = pd.DataFrame(crew_list)
    writer = pd.ExcelWriter('guild_info.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name='guild', index = False)
    writer.save()

def compare_list():
    a = pd.read_excel('guild_info.xlsx', engine = 'openpyxl')
    print(a[0])

def send_notification():
    pass
'''
list_g = ['우리와써또와써', 'Destroyer', '그리폰', '레드카드', '땡깡', '지나갑니다', 'ASH', '사도', '말랑말랑칸디둠해적단', 'Sin', '아기상어', '돔황챠', 'KiLL', '우릴만나다니', '베르세르크', '시바', '몰랑몰랑']
user = str(input("What's the username ? "))
store = find_user(user, list_g)
print()
print(store[0])
print("길드 인원 수 :", store[1])
'''
compare_list()
#saving_list(my_list)
#compare_list()