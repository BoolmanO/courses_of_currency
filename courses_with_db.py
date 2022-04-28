import sqlite3
import requests
from bs4 import BeautifulSoup





class scrap:

    def __init__(self):
        self.URL = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81&aqs=chrome.0.0i131i433i512l8j0i131i433j0i131i433i512.1587j0j15&sourceid=chrome&ie=UTF-8'


        self.HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
        self.html = requests.get(self.URL, headers = self.HEADERS)
    

    def get_content(self):
        soup = BeautifulSoup(self.html.text, 'html.parser')
    
        items = soup.find_all('div', class_ ='VgAgW PZPZlf')
   
        datas = []

        for item in items:
            datas.append(
                item.find('span',class_ = 'DFlfde SwHCTb').get_text()#old code
        )

        return datas[0]


class scrap20:
    def __init__(self,):
        pass

    def rubl_dollar(self):
        URL = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81&aqs=chrome.0.0i131i433i512l8j0i131i433j0i131i433i512.1587j0j15&sourceid=chrome&ie=UTF-8'
        HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
        html = requests.get(URL, headers = HEADERS)

        soup = BeautifulSoup(html.text, 'html.parser')
    
        items = soup.find_all('div', class_ ='VgAgW PZPZlf')
   
        datas = []

        for item in items:
            datas.append(
                item.find('span',class_ = 'DFlfde SwHCTb').get_text()#old code
        )

        return datas[0]



class sqlite_working(scrap20):

    
    def __init__(self,db_name="sqlite3"):
        self.dbname = db_name
        self.con = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.con.cursor()
        
    def create(self):
        self.cursor.execute("CREATE TABLE rubl_dollar_course (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATETIME DEFAULT CURRENT_TIMESTAMP, course TEXT)")

    def add(self,table,content:str):
        self.cursor.execute(f"INSERT INTO {table} (course) VALUES (?)",[content])


#######
    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()

    def comse(self):
        self.con.commit()
        self.con.close()

    def open(self,db_name="sqlite3"):
        self.con = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.con.cursor()

    def ignore(self):
        self.con.close()
        self.con = sqlite3.connect(f"{self.dbname}.db")
        self.cursor = self.con.cursor()
#######


import time






def main():
    sql = sqlite_working("course")
    scrap = scrap20()

    data = sql.cursor.execute("SELECT * FROM rubl_dollar_course").fetchall()

    if data[len(data)-1][2] == data[len(data)-2][2]:
        return
        
    print(data)

    sql.add(table="rubl_dollar_course",content=scrap.rubl_dollar())

    sql.comse()

    print(sql.cursor.execute("SELECT * FROM rubl_dollar_course").fetchall())

while 1:
    main()
    time.sleep(1)