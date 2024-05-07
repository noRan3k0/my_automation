import settings, get_site_data, make_data, manage_database


test_data = make_data.add_data()    # ブロックのデータを作成, こいつはリストじゃなきゃいけねえ。
manage_database.create_blocks(test_data)