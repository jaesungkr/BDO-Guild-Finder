import requests, re
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import openpyxl

# scraping the bdo guild page
def crew_scraping(guild_name):
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

# This function is to find specific user from a guild.
def find_user(username, guild_lists):
    for i in range(len(guild_lists)):
        tmp, guild = crew_scraping(guild_lists[i])
        if username in guild:
            return guild_lists[i], tmp

def saving_list(crew_list, guild_name):
    df = pd.DataFrame(crew_list)
    try:
        os.mkdir(f'{guild_name}')
        print('created')
    except FileExistsError:
        print(f'{guild_name} file already exists')

    writer = pd.ExcelWriter(f'{guild_name}\{guild_name}_{datetime.today().strftime("%Y-%m-%d")}.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name='guild', index = False)
    writer.save()

# This function meant to run once a day everyday to update all lists of crew members (in progress)
def saving_everyday(guild_list):
    for i in range(len(guild_list)):
        saving_list(crew_scraping(guild_list[i])[1], guild_list[i])

# argument past_list, current_list
def compare_list():
    past_list = pd.read_excel('guild_info.xlsx', engine = 'openpyxl')[0].values.tolist()
    current_list = crew_scraping('우리와써또와써')[1]

    past_list.sort()
    current_list.sort()
    if(past_list == current_list):
        print("it's same")
    print(past_list)
    print(current_list)

    left_users = []
    for i in past_list:
        if i not in current_list:
            left_users.append(i)
    print(left_users)

    new_users = []
    for i in current_list:
        if i not in past_list:
            new_users.append(i)
    print(new_users)

def send_notification():
    pass

list_g = ['우리와써또와써', 'Destroyer', '그리폰', '레드카드', '땡깡', '지나갑니다', 'ASH', '사도', '말랑말랑칸디둠해적단', 'Sin', '아기상어', '돔황챠', 'KiLL', '우릴만나다니', '베르세르크', '시바', '몰랑몰랑']
'''
user = str(input("What's the username ? "))
store = find_user(user, list_g)
print()
print(store[0])
print("길드 인원 수 :", store[1])
'''
#compare_list()
#saving_list(my_list)
#compare_list()
saving_everyday(list_g)