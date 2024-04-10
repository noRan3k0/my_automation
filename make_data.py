made_data = [
    # head contents
    {"table_of_contents": {"color": "default"}},
    {"heading_1": {"rich_text": [{"text": {"content": "Race Data"}}]}},
    # table
    {
        "table": {
            "table_width": 2,
            "has_column_header": False,
            "has_row_header": True,
            "children": [
                {"table_row": {"cells": [[{"text": {"content": "テレイン"}}], [{"text": {"content": "where"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "距離"}}], [{"text": {"content": "6km"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "アップ"}}], [{"text": {"content": "300m"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "タイム"}}], [{"text": {"content": "いくらか"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "巡航"}}], [{"text": {"content": "いくらか"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "ミス率"}}], [{"text": {"content": "めっちゃ%"}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "ミスタイム"}}], [{"text": {"content": "+18915730"}}]]}}
            ]
        }
    },
    {"heading_2": {"rich_text": [{"text": {"content": "MAP"}}]}},
    {"heading_2": {"rich_text": [{"text": {"content": "LOG"}}]}},
	{"heading_1": {"rich_text": [{"text": {"content": "Leg Assessment"}}]}}
]

def main():
    pass

def add_data():
    # make toggle
    for i in range(10):
        if i == 0:
            text = "○->1"
        elif i == 9:
            text = "9->◎"
        else:
            text = str(i) + "->" + str(i+1)
        add_data = {"heading_2": {"rich_text": [{"text": {"content": text}}], "is_toggleable": True}}
        made_data.append(add_data)
    
    return made_data

if __name__ == "__main__":
    main()