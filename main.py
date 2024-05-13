import make_data, manage_database, extract_json_data
from time import sleep
import settings

RACE_DATE = settings.race_date
PAGE_TITLE = settings.page_title

data = {
    "RaceDate": {"date": {"start": RACE_DATE, "end": None}},
    "Race": {"title": [{"text": {"content": PAGE_TITLE}}]}
}

manage_database.create_page(data)
sleep(1)

manage_database.get_pages()
page_id = extract_json_data.extract_json()
sleep(1)

test_data = make_data.add_data()    # ブロックのデータを作成, こいつはリストじゃなきゃいけねえ。
manage_database.create_blocks(test_data, page_id)