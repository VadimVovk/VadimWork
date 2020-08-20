# my_list = ["ab", "cd", "ef", "gh"]
# result=[]
# for index,item in enumerate(my_list):
#     if index%2 == 0:
#         result.append(item)
#     else:
#         result.append(item[::-1])
# print(result)
# #2##########
# my_list = ["aba", "cad", "aef", "gh", "aaa"]
# result=[]
# for str_a in (my_list):
#    if str_a[0] == "a":
#        result.append(str_a)
# print(result)
# 3#########
# my_list = ["ab", "cad", "aef", "gh", "aaa"]
# result=[]
# for str_1 in (my_list):
#    if "a" in str_1:
#        result.append(str_1)
# print(result)
# #4###########
# my_list = ["aab", "cad", 222, "gh", "aaa", 555]
# result=[]
# for item in (my_list):
#    if type(item) == str:
#        result.append(item)
# print(result)
#5#########
my_str=("112334556788")
my_list=[]
my_str_1=(set(my_str))
for symbol in my_str_1:
    if my_str.count(symbol)==1:
        my_list.append(symbol)
print(my_list)
#6#######
my_str_1=("12345568a")
my_str_2 = ("222344778a")
my_str_3 = my_str_1+my_str_2
my_list_f=[]
my_list=set(my_str_3)
for symbol in my_list:
    if symbol in my_str_1 and symbol in my_str_2:
        my_list_f.append(symbol)
print(my_list_f)
# #7#########
my_str_1=("12345568")
my_str_2 = ("222344778")
my_str_3 = my_str_1+my_str_2
my_list_f=[]
my_list=list(set(my_str_3))
for symbol in my_list:
    if my_str_1.count(symbol)==1 and my_str_2.count(symbol) == 1:
        my_list_f.append(symbol)
print(set(my_list_f))
# #8###########
# person = {"Фамилия" : "Вовк",
#           "Имя": "Вадим",
#           "Возраст": "43",
#           "Адрес": {
#                "Страна": "Украина",
#                "Город": "Днепр",
#                "Улица": "Победы"},
#            "Работа": {
#                "Наличие": "нет",
#                "Должность": ""}
#            }
# print(person ['Адрес'])
# #9############
# cake = {"Коржи":{
#                "Мука": "1000",
#                "Молоко": "500",
#                "Масло": "200",
#                "Яйца": "6"},
#         "Крем": {
#                "Сахар": "300",
#                "Масло": "200",
#                "Ваниль": "10",
#                "Сметана": "300"},
#         "Глазурь":{
#                "Какао": "300",
#                "Сахар": "100",
#                "Масло": "150"}
#         }
# print(cake["Глазурь"])
