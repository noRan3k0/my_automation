data = []
tableOfBlock = {
    "table_of_contents": {
        "color": "default"
    }
}

{
    "heading_1": {
        "rich_text": [{"text": {"content": "Leg_assessment"} }]
    }
},
{
    "heading_2": {
        "rich_text": [{"text": {"content": "leg_1"}}],
        "is_toggleable": True
    }
}

# data作成
data.append(tableOfBlock)

num = 1
leg_num = str(num)

add_data = {
    "heading_3": {
        "rich_text": [{"text": {"content": leg_num}}],
        "is_toggleable": True
    }
}
data.append(add_data)

print(data)