import string
import random
import json
import csv
# create_dict_json():
key_list=[]
my_dict={}
quantity_key=random.randint(5,20)
for i in range(quantity_key):
    key_list.append("".join(random.choices(string.ascii_lowercase,k=5)))
# for num in range(quantity_key):
    x=random.randint(1,3)
    if x == 1:
        dat = random.randint(-100,100)
    elif x == 2:
        dat = random.random()
    else:
        y=random.randint(1,2)
        if y==1:
            dat = True
        else:
            dat = False
    my_dict.update({key_list[i]:dat})
print(my_dict)