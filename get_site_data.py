import requests
from bs4 import BeautifulSoup
import re

# 取得対象ページのURL
url = "https://mulka2.com/lapcenter/lapcombat2/split-list.jsp?event=8292&file=1&class=0"

try:
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
except:
    print("Error: get URL")
print(req.status_code)

try:
    for script_tag in enumerate(soup.findAll('script')):
        script_tag_string = str(script_tag)

    # 'runnerData['runnerName'] = '高橋 光';' と 'runnerList.push(runnerData);' の間のテキストを抽出する正規表現パターン
    large_pattern = r"runnerData\['runnerName'\] = '高橋 光';(.*?)runnerList\.push\(runnerData\);"

    matches = re.findall(large_pattern, script_tag_string, re.DOTALL)
except:
    print("Error: check data")

result_pattern = r"runnerData\['result'\] = \'(.*?)\';"
result_matchs = re.findall(result_pattern, str(matches), re.DOTALL)
print(result_matchs)
print(result_matchs[0])
print(type(result_matchs[0]))

#for match in matches:
#    print(match)