# my_list = ["ab", "cd", "ef", "gh"]
# result=[]
# for index,item in enumerate(my_list):
#     if index%2 == 0:
#         result.append(item)
#     else:
#         result.append(item[::-1])
# print(result)
##2##########
# my_list = ["aba", "cad", "aef", "gh", "aaa"]
# result=[]
# for str in (my_list):
#    if str[0] == "a":
#        result.append(str)
# print(result)
##########
my_list = ["ab", "cad", "aef", "gh", "aaa"]
result=[]
for str in (my_list):
   if "a" in str:
       result.append(str)
print(result)
#############
my_list = ["aab", "cad", 222, "gh", "aaa", 555]
result=[]
for index,item in enumerate(my_list):
   if type(item) == str:
       result.append(item)
print(result)
# #5#########
# my_str=("112334556788")
# my_list=[]
# for symbol in my_str:
#     if my_str.count(symbol)==1:
#         my_list.append(symbol)
# print(my_list)
# #6#######
# my_str_1=("123455")
# my_str_2 = ("2344")
# my_list_f=[]
# my_list=list(set(my_str_1))+list(set(my_str_2))
# for symbol in my_list:
#     if my_list.count(symbol)==2:
#         my_list_f.append(symbol)
# print(set(my_list_f))
# #7#########
# my_str_1=("112345")
# my_str_2=("1223445")
# my_list_1=[]
# my_list_2=[]
# for symbol in my_str_1:
#     if my_str_1.count(symbol)==1:
#         my_list_1.append(symbol)
# for symbol in my_str_2:
#     if my_str_2.count(symbol)==1:
#         my_list_2.append(symbol)
# my_list_f=[]
# my_list=list(set(my_list_1))+list(set(my_list_2))
# for symbol in my_list:
#     if my_list.count(symbol)==2:
#         my_list_f.append(symbol)
# print(set(my_list_f))
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
#test