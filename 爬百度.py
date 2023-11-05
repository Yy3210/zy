
import requests
from bs4 import BeautifulSoup
import sqlite3

#库
conn = sqlite3.connect('history_today.db')
c = conn.cursor()

#表
c.execute('''CREATE TABLE IF NOT EXISTS history_today
             (year TEXT, event_type TEXT, title TEXT, content TEXT)''')





url = 'https://baike.baidu.com/calendar'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

events = soup.find_all('ul', {'class': 'history-list'})
for event in events:
    year = event.find_previous_sibling('h3').text.strip()
    event_type = event.find_previous_sibling('div', {'class': 'title'}).text.strip()
    items = event.find_all('li')

    for item in items:
        title = item.find('a').text.strip()
        content = item.find('p').text.strip()

        #
        title = title.replace('\n', '').replace('（', '').replace('）', '')
        content = content.replace('\n', '').replace('（', '').replace('）', '')


        c.execute("INSERT INTO history_today VALUES (?, ?, ?, ?)", (year, event_type, title, content))














conn.commit()
conn.close()



