import os

def separation_path(my_path):
    my_list= my_path.rsplit("/",1)
    file_name = my_list[1]
    folder_path = my_list[0]
    return file_name, folder_path

my_str="F:/Vadim/PycharmProjects/First/first.py"
print(separation_path(my_str))
# # #2#######################
def generate_a_list_of_files(folder_path):
    my_folder=os.listdir(folder_path)
    list_files=[]
    for str_1 in my_folder:
        if os.path.isfile(os.path.join(folder_path,str_1)):
            list_files.append(os.path.join(folder_path,str_1))
    return list_files
my_path = "F:/Vadim/PycharmProjects/First"
print(generate_a_list_of_files(my_path))
############
def generate_a_list_of_folders(folder_path):# в отдельную ф-ю не стал выновить считывание содержимого папки, т.к, по моему мнению, теряется автономность функции. В том плане, функция формирования списка файлов становится неразрывно связана с ф-ей считывания содержимого папки. Если нужно, могу переделать, дело 5-ти минут.
    my_folder=os.listdir(folder_path)
    list_folders=[]
    for str_1 in my_folder:
        if os.path.isdir(os.path.join(folder_path,str_1)):
            list_folders.append(os.path.join(folder_path,str_1))
    return list_folders
my_path = "F:/Vadim/PycharmProjects/First"
print(generate_a_list_of_folders(my_path))
#3###################
def generate_a_dict_of_files_and_folders(folder_path):
    my_file_f= generate_a_list_of_files(folder_path)
    my_folder_f=generate_a_list_of_folders(folder_path)
    my_dict = {"files": my_file_f,
               "folders": my_folder_f}
    return my_dict
my_path = "F:\Vadim\PycharmProjects\First"
print(generate_a_dict_of_files_and_folders(my_path))
###3#############################Предыдущее решение.
# def generate_a_dict_of_files_and_folders(folder_path):
#     my_folder=os.listdir(folder_path)
#     my_file_f=[]
#     my_folder_f=[]
#     for str_1 in my_folder:
#         if os.path.isfile(os.path.join(folder_path,str_1)):
#             my_file_f.append(os.path.join(folder_path,str_1))
#         else:
#             my_folder_f.append(os.path.join(folder_path,str_1))
#     my_dict = {"files": my_file_f,
#                "folders":my_folder_f}
#     return my_dict
# my_path="F:\Vadim\PycharmProjects\First"
# print(generate_a_dict_of_files_and_folders(my_path))
#4############## Можно вместо счетчика флаг поставить, но счетчик сразу в голову пришел.
def create_folders(folder_path):
    my_folder=os.listdir(folder_path)
    count=0
    for str_1 in my_folder:
        if os.path.isdir(str_1):
            os.mkdir(f"{str_1}_tmp")
            count+=1
    if count == 0:
           os.mkdir("tmp")
my_path="F:/Vadim/PycharmProjects/First"
create_folders(my_path)
#

