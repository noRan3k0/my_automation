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
def create_blocks(data: dict):
    block_url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"

    payload = {"children": data}

    res = requests.patch(block_url, headers=headers, json=payload)
    print(res.status_code)
    return res

name = "name"
title = "Test"
race_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "Race": {"title": [{"text": {"content": name}}]},
    "RaceDate": {"date": {"start": race_date, "end": None}}
}

# こいつはリストじゃなきゃいけねえ。
test_data = [
    # head contents
    {
        "table_of_contents": {
            "color": "default"
        }
    },
    {
        "heading_1": {
	        "rich_text": [{"text": {"content": "Race Data"} }]
	    }   
    },
    {
        "table": {
            "table_width": 2,
            "has_column_header": False,
            "has_row_header": True,
            "children": [
                   {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "column1 content",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "column2 content",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "テレイン",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "where",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "距離",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "6km",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "アップ",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "300m",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "タイム",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "いくらか",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "巡航",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "いくらか",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "ミス率",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "めっちゃ%",
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "table_row": {
                            "cells": [
                                [
                                    {
                                        "text": {
                                            "content": "ミスタイム",
                                        }
                                    }
                                ],
                                [
                                    {
                                        "text": {
                                            "content": "+18915730",
                                        }
                                    }
                                ]
                            ]
                        }
                    }
            ]
        }
    },
    {
	    "heading_2": {
	        "rich_text": [{"text": {"content": "MAP"}}],
	    }
	},
    {
	    "heading_2": {
	        "rich_text": [{"text": {"content": "LOG"}}],
	    }
	},
	{
	    "heading_1": {
	        "rich_text": [{"text": {"content": "Leg Assessment"} }]
	    }
	},
	{
	    "heading_2": {
	        "rich_text": [{"text": {"content": "○->1"}}],
	        "is_toggleable": True
	    }
	},
    {
        "heading_2": {
	        "rich_text": [{"text": {"content": "1->2"}}],
	        "is_toggleable": True
	    }
    },
    { 
        "heading_2": {
	        "rich_text": [{"text": {"content": "2->3"}}],
	        "is_toggleable": True
	    }
    },
    { 
        "heading_2": {
	        "rich_text": [{"text": {"content": "3->4"}}],
	        "is_toggleable": True
	    }
    },
    { 
        "heading_2": {
	        "rich_text": [{"text": {"content": "4->5"}}],
	        "is_toggleable": True
	    }
    },
    { 
        "heading_2": {
	        "rich_text": [{"text": {"content": "5->6"}}],
	        "is_toggleable": True
	    }
    },
    { 
        "heading_2": {
	        "rich_text": [{"text": {"content": "6->◎"}}],
	        "is_toggleable": True
	    }
    }
]

create_blocks(test_data)
#get_pages_data()