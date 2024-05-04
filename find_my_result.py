import re

# テキストファイルを開いて読み込む
with open('output.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 'runnerData['runnerName'] = '高橋 光';' と 'runnerList.push(runnerData);' の間のテキストを抽出する正規表現パターン
pattern = r"runnerData\['runnerName'\] = '高橋 光';(.*?)runnerList\.push\(runnerData\);"

# パターンにマッチする全てのテキストを検索する
matches = re.findall(pattern, text, re.DOTALL)

# 結果を表示する
for match in matches:
    print(match)