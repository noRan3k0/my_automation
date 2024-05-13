import json


def extract_json():
    path = 'db.json'

    with open(path, encoding='utf-8') as f:  # ファイルをutf-8で開く
        # JSONデータを読み込んで変数に代入する
        json_data = json.load(f)

    # resultsリスト内の各要素の"last_edited_time"をチェックし、最新のものを取得する
    latest_id = None
    latest_time = None

    for result in json_data['results']:
        edited_time = result['last_edited_time']
        if latest_time is None or edited_time > latest_time:
            latest_time = edited_time
            latest_id = result['id']

    print("最後に更新されたページのID:", latest_id)
    return latest_id
