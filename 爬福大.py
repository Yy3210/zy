
import requests
from bs4 import BeautifulSoup
import re
import sqlite3



conn = sqlite3.connect('fuda_notice.db')      #通知库
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS fuda_notice                                  
             (source TEXT, title TEXT, date TEXT, detail_link TEXT)''')           #通知表


url = 'https://jwch.fzu.edu.cn/jxtz.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')



total_count = int(soup.find('span', class_='count').text.strip())
total_pages = total_count // 10 + 1

#爬取
for page in range(1, total_pages + 1):
    url = f'https://jwch.fzu.edu.cn/jxtz.htm?&curr_page={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    notices = soup.find_all('div', class_='article-item')
    for notice in notices:
        source = notice.find('p', class_='source').text.strip()
        title = notice.find('a', class_='title').text.strip()
        date = notice.find('span', class_='date').text.strip()
        detail_link = notice.find('a', class_='title')['href']


        source = source.replace('\n', '').replace('（', '').replace('）', '')
        title = title.replace('\n', '').replace('（', '').replace('）', '')
        date = date.replace('\n', '').replace('（', '').replace('）', '')

        #插入
        c.execute("INSERT INTO fuda_notice VALUES (?, ?, ?, ?)", (source, title, date, detail_link))

#换
conn.commit()
conn.close()



conn = sqlite3.connect('fuda_notice.db')       #附件库
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS fuda_attachment
             (notice_id INTEGER, attachment_name TEXT, download_count INTEGER, attachment_link TEXT)''')     #表


c.execute("SELECT rowid, detail_link FROM fuda_notice")
notice_rows = c.fetchall()

for notice_row in notice_rows:
    notice_id = notice_row[0]
    detail_link = notice_row[1]

    response = requests.get(detail_link)
    soup = BeautifulSoup(response.content, 'html.parser')

    attachments = soup.find_all('div', class_='file-item')
    for attachment in attachments:
        attachment_name = attachment.find('a').text.strip()
        download_count = int(re.search(r'\d+', attachment.find('em').text.strip()).group())
        attachment_link = attachment.find('a')['href']

        #
        attachment_name = attachment_name.replace('\n', '').replace('（', '').replace('）', '')

        # 插入
        c.execute("INSERT INTO fuda_attachment VALUES (?, ?, ?, ?)",
                  (notice_id, attachment_name, download_count, attachment_link))


conn.commit()
conn.close()







# if __name__=="__main__":
#     #main()