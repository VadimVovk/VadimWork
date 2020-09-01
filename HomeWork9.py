import string
import random
import json
import csv
def create_string_txt():
#    string_symbol = string.printable при смпользовании данной команды происходят дополнительные переходы на новую строку.
    string_symbol=(string.ascii_letters+string.digits+string.punctuation+" ")
    my_list = []
    my_list_num = []
    lrn = random.randint(100,1000)
    for num in range(lrn):
        my_list.append(random.choice(string_symbol))
        my_list_num.append(num)
    my_list_num_f = my_list_num[1:lrn - 1]
    random.shuffle(my_list_num_f)
    list_9 = my_list_num_f[0:9]
    for symbol in list_9:
        my_list[symbol] = "\n"
    data=str("".join(my_list))
    return data
##################
def create_dict_json():
    key_list=[]
    my_dict={}
    quantity_key=random.randint(5,20)
    for i in range(quantity_key):
        key_list.append("".join(random.choices(string.ascii_lowercase,k=5)))
        x=random.randint(1,3)
        if x == 1:
            dat = random.randint(-100,100)
        elif x == 2:
            dat = random.uniform(0,1)# не знаю, как лучше, или random.random
        else:
            dat=random.choices([True, False])#ну или как ниже, по простому
            # y=random.randint(1,2)
            # if y==1:
            #     dat = True
            # else:
            #     dat = False
        my_dict.update({key_list[i]:dat})
    data=my_dict
    return data
# # ########
def create_csv():
    my_list=[]
    n=random.randint(3,10)
    m=random.randint(3,10)
    for num in range(n):
        my_list.append(random.choices([0,1],k=m))
    data=my_list
    return data
##########
def file_writer(my_path):
    file_resolution = my_path.rsplit(".",1)[-1]
    if file_resolution == "txt":
        data=create_string_txt()
        with open(my_path, "w") as txtfile:
            txtfile.write(data)

    elif file_resolution == "json":
        # data=create_dict_json()
        data_1 = json.dumps(create_dict_json())
        with open(my_path, "w") as jsonfile:
            jsonfile.write(data_1)

    elif file_resolution == "csv":
        data=create_csv()
        with open(my_path, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
my_str="F:/Vadim/PycharmProjects/First/11.txt"
file_writer(my_str)