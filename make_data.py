import get_site_data as gst

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
                {"table_row": {"cells": [[{"text": {"content": "タイム"}}], [{"text": {"content": gst.result_text}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "巡航"}}], [{"text": {"content": gst.speed_text}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "ミス率"}}], [{"text": {"content": gst.lossRate_text}}]]}},
                {"table_row": {"cells": [[{"text": {"content": "ミスタイム"}}], [{"text": {"content": gst.totalLossTime_text}}]]}}
            ]
        }
    },
    {"heading_2": {"rich_text": [{"text": {"content": "MAP"}}]}},
    {"heading_2": {"rich_text": [{"text": {"content": "LOG"}}]}},
	{"heading_1": {"rich_text": [{"text": {"content": "Leg Assessment"}}]}}
]

leg_num = len(gst.lapTime_list)

def main():
    pass

def add_data():
    # make toggle
    for i in range(leg_num):
        if i == 0:
            text = "○->1"
        elif i == leg_num-1:
            text = str(leg_num-1) + "->◎"
        else:
            text = str(i) + "->" + str(i+1)
        add_header_data = {"heading_2": {"rich_text": [{"text": {"content": text}}], "is_toggleable": True}}
        made_data.append(add_header_data)
        add_legTime_data = {"paragraph": {"rich_text": [{"text": {"content": "ラップタイム: " + gst.lapTime_list[i]}}]}}
        made_data.append(add_legTime_data)
        add_legLossTime_data = {"paragraph": {"rich_text": [{"text": {"content": "ミスタイム　: " + gst.legLossTime_list[i]}}]}}
        made_data.append(add_legLossTime_data)
    return made_data

if __name__ == "__main__":
    print("This is make_data.")