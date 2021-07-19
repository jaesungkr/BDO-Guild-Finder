import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

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
        crew_list.append(re.compile('">([a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+)').findall(str(x)))
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
    print(len(a[0]))

def send_notification():




guild = '우리와써또와써'
length, my_list = crew_crawling(guild)
saving_list(my_list)
compare_list()