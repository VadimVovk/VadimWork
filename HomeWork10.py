import json
import re
def read_json(filename_path):
    with open(filename_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
my_str="F:/Vadim/PycharmProjects/First/data.json"
# # print(read_json(my_str))

# def key_sort(maths_dict):
#     name=maths_dict.get("name")
#     name=re.findall(r'\w+$', name)
#     return name
#
data_dict=read_json(my_str)
# name_sorted=sorted(data,key=key_sort)
# [print(line) for line in name_sorted]

def key_sort_date(maths_dict):
    years=maths_dict.get("years")
    years=re.findall(r'\d+$', years )
    return years
years_sorted=sorted(data_dict,key=key_sort_date)
[print(line) for line in years_sorted]

