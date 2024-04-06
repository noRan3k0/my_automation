import requests
from bs4 import BeautifulSoup

url = "https://mulka2.com/lapcenter/lapcombat2/split-list.jsp?event=8292&file=1&class=0"
tag = "高橋光"
r = requests.get(url)
#r.encoding = r.apparent_encoding
#soup = BeautifulSoup(r.text, "lxml")
#for i, element in enumerate(soup.findAll(tag)):
#    print(i, element.text)
try:
#    f = open('result.txt', 'x')
#    f.write(r.content)
#    f.close()
    print(r.content)
except:
    print("failed.")