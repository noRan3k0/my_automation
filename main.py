import make_data, manage_database, extract_json_data
from time import sleep

data = {
    "RaceDate": {"date": {"start": "2024-05-13", "end": None}},
    "Race": {"title": [{"text": {"content": "testtest"}}]}
}

# データベースにページ作成
manage_database.create_page(data)
sleep(1)
# 作ったページのidを取得
manage_database.get_pages()
page_id = extract_json_data.extract_json()

sleep(1)
test_data = make_data.add_data()    # ブロックのデータを作成, こいつはリストじゃなきゃいけねえ。
manage_database.create_blocks(test_data, page_id)