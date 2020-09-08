import os
def separation_path(my_path):
    my_list= my_path.rsplit("/",1)
    file_name = my_list[1]
    folder_path = my_list[0]
    return file_name, folder_path

my_str="F:/Vadim/PycharmProjects/First/Second.py"
print(separation_path(my_str))
########################список из путей элементов папки
def listdir_folder(folder_path):
    list_from_folder=[]
    my_folder=os.listdir(folder_path)
    for str_1 in my_folder:
        list_from_folder.append(os.path.join(folder_path,str_1))
    return list_from_folder
######## список путей подпапок из папки
def generate_a_list_of_folders(list_path):
    list_folders=[]
    for str_1 in list_path:
        if os.path.isdir(str_1):
            list_folders.append(str_1)
    return list_folders
########### список путей файлов из папки.
def generate_a_list_of_files(list_path):
    list_files=[]
    for str_1 in list_path:
        if os.path.isfile(str_1):
            list_files.append(str_1)
    return list_files


my_path = "F:/Vadim/PycharmProjects/First"
print(f"список файлов {generate_a_list_of_files(listdir_folder(my_path))}")
print(f"список папок {generate_a_list_of_folders(listdir_folder(my_path))}")
# #3################### Словарь из путей элементов папки
def generate_a_dict_of_files_and_folders(folder_path):
    list_folder=listdir_folder(my_path)
    my_file_f= generate_a_list_of_files(list_folder)
    my_folder_f=generate_a_list_of_folders(list_folder)
    my_dict = {"FILES": my_file_f,
               "FOLDERS": my_folder_f}
    return my_dict
my_path = "F:\Vadim\PycharmProjects\First"
print(generate_a_dict_of_files_and_folders(my_path))
##3#############################Предыдущее решение. По честному, потратил на него значительно меньше времени.
def generate_a_dict_of_files_and_folders(folder_path):
    my_folder=os.listdir(folder_path)
    my_file_f=[]
    my_folder_f=[]
    for str_1 in my_folder:
        if os.path.isfile(os.path.join(folder_path,str_1)):
            my_file_f.append(os.path.join(folder_path,str_1))
        else:
            my_folder_f.append(os.path.join(folder_path,str_1))
    my_dict = {"files": my_file_f,
               "folders":my_folder_f}
    return my_dict
my_path="F:\Vadim\PycharmProjects\First"
print(generate_a_dict_of_files_and_folders(my_path))
#4############## Можно вместо счетчика флаг поставить, но счетчик сразу в голову пришел.
def create_folders(folder_path):
    my_folder=os.listdir(folder_path)
    count=0
    for str_1 in my_folder:
        if os.path.isdir(os.path.join(folder_path,str_1)):
            os.mkdir(f"{str_1}_tmp")
            count+=1
    if count == 0:
           os.mkdir("tmp")
my_path="F:/Vadim/PycharmProjects"
create_folders(my_path)


