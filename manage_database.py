import requests
import json
from datetime import datetime, timezone

import settings
import make_data

NOTION_API_TOKEN = settings.api_key
DATABASE_ID = settings.db_id
PAGE_ID = settings.page_id

headers = {
    "Authorization": "Bearer " + NOTION_API_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# データベースからページの情報取得
def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results

# データベースに新しいページを作成
def create_page(data:dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res

# データベース上のページを更新
def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, headers=headers, json=payload)
    print(res.status_code)
    return res

# データベース上のページを削除
def delete_page(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, headers=headers, json=payload)
    print(res.status_code)
    return res

# ページから情報を取得
def get_pages_data():
    page_url = f"https://api.notion.com/v1/pages/{PAGE_ID}"
    block_url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"

    page_response = requests.get(page_url, headers=headers)
    page_result = page_response.json()

    with open('page_result.json', 'w', encoding='utf-8') as f:
        json.dump(page_result, f, ensure_ascii=False, indent=4)
    print("page_result: " + str(page_response.status_code))

    block_response = requests.get(block_url, headers=headers)
    block_result = block_response.json()
    with open('blocks_result.json', 'w', encoding='utf-8') as f:
        json.dump(block_result, f, ensure_ascii=False, indent=4)
    print("page_result: " + str(block_response.status_code))

    #print(block_result.keys())
    results = block_result["results"]
    return results

# ページにブロックを追加する。
def create_blocks(data: dict, page_id: str):
    block_url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    payload = {"children": data}

    res = requests.patch(block_url, headers=headers, json=payload)
    print(res.status_code)
    return res

if __name__ == "__main__":
    name = "name"
    title = "Test"
    race_date = datetime.now().astimezone(timezone.utc).isoformat()
    page_data = {
        "Race": {"title": [{"text": {"content": name}}]},
        "RaceDate": {"date": {"start": race_date, "end": None}}
    }
    to_id = input("url :")
    to_id = to_id.replace("https://www.notion.so/", "")
    if ("test-url-" in to_id):
        to_id = to_id.replace("test-url-", "")
    to_id = to_id.replace("?pvs=4", "")
    print(to_id)
    # ブロック作成部分
    test_data = make_data.add_data()    # こいつはリストじゃなきゃいけねえ。
    create_blocks(test_data, to_id)
    #https://www.notion.so/test-url-7e9ccfba5a534d76832e6085783e93f0?pvs=4
    
    