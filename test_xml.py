import requests
from bs4 import BeautifulSoup
import re

url = "https://mulka2.com/lapcenter/lapcombat2/split-list.jsp?event=8292&file=1&class=0"
tag = "高橋光"

req = requests.get(url)
req.encoding = req.apparent_encoding
soup = BeautifulSoup(req.text, "html.parser")

result = re.findall('', soup, re.S)

"""
with open('output.txt', 'w', encoding='utf-8') as file:
    for script_tag in enumerate(soup.findAll('script')):
        script_tag_string = str(script_tag)
        file.write(str(script_tag))
"""

print(req.status_code)