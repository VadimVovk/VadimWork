import json
import re
def read_json(filename_path):
    with open(filename_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
my_str="F:/Vadim/PycharmProjects/First/data.json"

# def key_sort(maths_dict):
#     name=maths_dict.get("name")
#     name=re.findall(r'\w+$', name)
#     return name
#
# data=read_json(my_str)
# name_sorted=sorted(data,key=key_sort)
# [print(line) for line in name_sorted]

def key_sort_date(maths_dict):
    years = maths_dict.get("years")
    years_str_num = re.findall(r'\d+', years)
    years_num=[int(number) for number in years_str_num]
    d_date= max(years_num) if years.count("BC") < 2 else -1*min(years_num)
    return d_date
data=read_json(my_str)

years_sorted=sorted(data, key=key_sort_date)
[print(line) for line in years_sorted]

