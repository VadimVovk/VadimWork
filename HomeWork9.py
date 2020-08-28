import string
import random
def create_string(str_random):
    string_symbol = string.printable
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
    str_random=str("".join(my_list))
    print(str_random)
##################
# string_symbol = string.ascii_lowercase
# key_list=[]
# my_dict={}
# quantity_key=random.randint(5,20)
# for i in range(quantity_key):
#     key_list.append("".join(random.choices(string.ascii_lowercase,k=5)))
# # for num in range(quantity_key):
#     x=random.randint(1,3)
#     if x == 1:
#         data = random.randint(-100,100)
#     elif x == 2:
#         data = random.random()
#     else:
#         y=random.randint(1,2)
#         if y==1:
#             data = True
#         else:
#             data = False
#     my_dict.update({key_list[i]:data})
# print(my_dict)
# ########
# my_list=[]
# my_list_f=[]
# n=random.randint(3,10)
# m=random.randint(3,10)
# for num in range(n):
#     my_list.append(random.choices([0,1],k=m))
# print(my_list)
# print(len(my_list))
# print(len(my_list[1]))
##########
def file_writer(my_path):
    file_resolution = my_path.rsplit(".",1)
    if file_resolution[-1] == "txt":
        with open("my_path", "w") as txtfile:
            txtfile.write(create_string(str))

my_str="F:/Vadim/PycharmProjects/First/first.txt"
file_writer(my_str)