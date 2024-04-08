import requests
from datetime import datetime, timezone

import settings

NOTION_API_TOKEN = settings.api_key
DATABASE_ID = settings.db_id

headers = {
    "Authorization": "Bearer " + NOTION_API_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    import json
    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results

def create_page(data:dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res

def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, headers=headers, json=payload)
    print(res.status_code)
    return res

def delete_page(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, headers=headers, json=payload)
    print(res.status_code)
    return res

def create_blocks(page_id: str, data: dict):
    create_url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    payload = {"children": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res    

def get_blocks(page_id: str):
    url = f"https://api.notion.com/v1/databases/{page_id}"

    #payload = {"page_size": 100}
    response = requests.post(url,headers=headers)

    data = response.json()
    print(response.status_code)

    import json
    with open('blocks.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results



name = "name"
title = "Test"
race_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "Race": {"title": [{"text": {"content": name}}]},
    "RaceDate": {"date": {"start": race_date, "end": None}}
}

child_data = {
    #"heading_1": {"rich_text": [{"text": {"content": "Can you see that！"}}]}
}
page_id = "7e9ccfba-5a53-4d76-832e-6085783e93f0"
#create_page(data)
#get_pages()
#create_blocks(page_id, child_data)
get_blocks(page_id) 