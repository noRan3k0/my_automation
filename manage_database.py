import requests
import json
from datetime import datetime, timezone

import settings

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



name = "name"
title = "Test"
race_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "Race": {"title": [{"text": {"content": name}}]},
    "RaceDate": {"date": {"start": race_date, "end": None}}
}
child_data = {
    "heading_1": {"rich_text": [{"text": {"content": "この言葉は見えているか！"}}]}
}
create_page(data)
#get_pages()