import requests
from bs4 import BeautifulSoup
import re
import settings

# 取得対象ページのURL
URL = settings.requests_url

def get_results():
    # GET request
    try:
        req = requests.get(URL)
        req.encoding = req.apparent_encoding
        soup = BeautifulSoup(req.text, "html.parser")
    except:
        print("Error: get URL. STATUS is "+ str(req.status_code))

    # data成型
    try:
        for script_tag in enumerate(soup.findAll('script')):
            script_tag_string = str(script_tag)

        # 'runnerData['runnerName'] = '高橋 光';' と 'runnerList.push(runnerData);' の間のテキストを抽出する正規表現パターン
        large_pattern = r"runnerData\['runnerName'\] = '高橋 光';(.*?)runnerList\.push\(runnerData\);"

        matches = re.findall(large_pattern, script_tag_string, re.DOTALL)
    except:
        print("Error: check data.")

    # variables
    result_pattern = r"runnerData\['result'\] = \'(.*?)\';"
    result_matchs = re.findall(result_pattern, str(matches), re.DOTALL)
    result_text = result_matchs[0]

    rank_pattern = r"runnerData\['rank'\] = \'(.*?)\';"
    rank_matchs = re.findall(rank_pattern, str(matches), re.DOTALL)
    rank_text = rank_matchs[0]

    speed_pattern = r"runnerData\['speed'\] = \'(.*?)\';"
    speed_matchs = re.findall(speed_pattern, str(matches), re.DOTALL)
    speed_text = speed_matchs[0]

    lossRate_pattern = r"runnerData\['lossRate'\] = \'(.*?)\';"
    lossRate_matchs = re.findall(lossRate_pattern, str(matches), re.DOTALL)
    lossRate_text = lossRate_matchs[0]

    totalRelative_pattern = r"runnerData\['totalRelative'\] = \'(.*?)\';"
    totalRelative_matchs = re.findall(totalRelative_pattern, str(matches), re.DOTALL)
    totalRelative_text = totalRelative_matchs[0]

    totalLossTime_pattern = r"runnerData\['totalLossTime'\] = \'(.*?)\';"
    totalLossTime_matchs = re.findall(totalLossTime_pattern, str(matches), re.DOTALL)
    totalLossTime_text = totalLossTime_matchs[0]

    idealTime_pattern = r"runnerData\['idealTime'\] = \'(.*?)\';"
    idealTime_matchs = re.findall(idealTime_pattern, str(matches), re.DOTALL)
    idealTime_text = idealTime_matchs[0]

    # list
    lapTime_pattern = r"runnerData\['lapTime'\] = \[(.*?)\];"
    lapTime_matchs = re.findall(lapTime_pattern, str(matches), re.DOTALL)
    lapTime_list = list(lapTime_matchs[0].split(","))

    lapRank_pattern = r"runnerData\['lapRank'\] = \[(.*?)\];"
    lapRank_matchs = re.findall(lapRank_pattern, str(matches), re.DOTALL)
    lapRank_list = list(lapRank_matchs[0].split(","))

    elapsedTime_pattern = r"runnerData\['elapsedTime'\] = \[(.*?)\];"
    elapsedTime_matchs = re.findall(elapsedTime_pattern, str(matches), re.DOTALL)
    elapsedTime_list = list(elapsedTime_matchs[0].split(","))

    elapsedRank_pattern = r"runnerData\['elapsedRank'\] = \[(.*?)\];"
    elapsedRank_matchs = re.findall(elapsedRank_pattern, str(matches), re.DOTALL)
    elapsedRank_list = list(elapsedRank_matchs[0].split(","))

    legLossTime_pattern = r"runnerData\['legLossTime'\] = \[(.*?)\];"
    legLossTime_matchs = re.findall(legLossTime_pattern, str(matches), re.DOTALL)
    legLossTime_list = list(legLossTime_matchs[0].split(","))

    legSpeed_pattern = r"runnerData\['legSpeed'\] = \[(.*?)\];"
    legSpeed_matchs = re.findall(legSpeed_pattern, str(matches), re.DOTALL)
    legSpeed_list = list(legSpeed_matchs[0].split(","))

    return result_text, speed_text, lossRate_text, totalLossTime_text, lapTime_list, legLossTime_list