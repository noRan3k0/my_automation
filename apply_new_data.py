import settings, get_site_data, make_data, manage_database


# データベースにページ作成
# 作ったページのidを取得

test_data = make_data.add_data()    # ブロックのデータを作成, こいつはリストじゃなきゃいけねえ。
manage_database.create_blocks(test_data)