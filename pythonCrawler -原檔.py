# !/usr/bin/python
# coding:utf-8

# import requests as rq
# from bs4 import BeautifulSoup
# import re

# addressURL = input("輸入網址：")
# inp = input("輸入關鍵字：")
# # url = "https://www.marry.com.tw/studio-7531" # PTT NBA 板
# response = rq.get(addressURL) # 用 requests 的 get 方法把網頁抓下來
# html_doc = response.text # text 屬性就是 html 檔案
# soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

# # 檔案自動生成
# fp = open("marryData.txt", "w",encoding="utf-8")
# for i in soup.find_all('device',''text=re.compile(inp)):  
#     fp.write('\n'+i + '\n'+'-----------------------------------------------------------------')

# fp.close()


import requests as rq
from bs4 import BeautifulSoup
import re
import io
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# addressURL = "https://www.marry.com.tw/studio-9210"
# inp = "meta"
# response = rq.get(addressURL) # 用 requests 的 get 方法把網頁抓下來
# html_doc = response.text # text 屬性就是 html 檔案
# soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
# fp = io.open("marryData.txt", "ab+")
# pid = soup.findAll('li', {'class': 'icon-check'})
# company = soup.select('h1')[0].text.strip()
# Con = ",".join([p.text for p in pid])
# if company != '' :
#     fp.write(company.encode('utf-8') + ':'.encode('utf-8'))  
#     # for i in range(len(Con)):
#     fp.write( Con.encode('utf-8')+ '。'.encode('utf-8') + '\n'.encode('utf-8')) 

tStart = time.time()#計時開始
fp = io.open("marryData.txt", "ab+")
for i in range(9210,9235):
    addressURL = "https://www.marry.com.tw/studio-"+str(i)
    print(addressURL)
    response = rq.get(addressURL) # 用 requests 的 get 方法把網頁抓下來
    html_doc = response.text # text 屬性就是 html 檔案
    soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
    sysMsg = soup.findAll('p', {'class': 'admonition'})
    # 表示工作室營運中
    if sysMsg == []:
        print('正常營運中')
        company = soup.select('h1')[0].text.strip()  
        # 判斷是否有H1
        if company != '' :
            print('名稱:',company)
            # 取得所有a
            for menu_studio_works in soup.find_all('a'):
                # 取得name 等於 menu_studio_works 的元件
                if menu_studio_works.get('name') == 'menu_studio_works':
                    # 判斷 name 等於 廳房才執行(表示是婚宴場地)
                    if menu_studio_works.text.strip().find('廳房')>=0:
                        pid = soup.findAll('li', {'class': 'icon-check'})
                        Con = ",".join([p.text for p in pid])
                        print('寫入資料:',Con)
                        fp.write(company.encode('utf-8') + '='.encode('utf-8'))  
                        fp.write(Con.encode('utf-8')+ '\n'.encode('utf-8')) 

        else:
            print('沒有名稱')
    else:
        print('關閉中')
# csvfile.close()     
tEnd = time.time()#計時結束
fp.close()
print ("It cost %f sec" % (tEnd - tStart))#會自動做近位



# fp.write( Con.encode() )

# for i in pid:
    # print(i) 
     # 对每项s使用get函数取得tag属性值
# for i in soup.find_all(text = re.compile(inp)):
#     print(i)
    # fp.write('\n'+ str(i) + '\n'+'-----------------------------------------------------------------')
    # fp.write(str(i))
