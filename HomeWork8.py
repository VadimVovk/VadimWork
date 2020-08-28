import os

def separation_path(my_path):
    my_list= my_path.rsplit("/",1)
    file_name = my_list[1]
    folder_path = my_list[0]
    print(f"Имя файла {file_name}  Путь к папке {folder_path}")
my_str="F:/Vadim/PycharmProjects/First/first.py"
separation_path(my_str)
# #2#######################
def generate_a_list_of_files(folder_path):
    my_folder=os.listdir(folder_path)
    my_folder_f=[]
    for str in my_folder:
        if os.path.isfile(os.path.join(folder_path,str)):
            my_folder_f.append(os.path.join(folder_path,str))
    print(my_folder)
    print(my_folder_f)
my_path = "F:/Vadim/PycharmProjects/First"
generate_a_list_of_files(my_path)


#3#############################
def generate_a_dict_of_files_and_folders(folder_path):
    my_folder=os.listdir(folder_path)
    my_file_f=[]
    my_folder_f=[]
    for str in my_folder:
        if os.path.isfile(os.path.join(folder_path,str)):
            my_file_f.append(os.path.join(folder_path,str))
        else:
            my_folder_f.append(os.path.join(folder_path,str))
    my_dict = {"files": my_file_f,
               "folders":my_folder_f}
    print(my_dict)
my_path="F:\Vadim\PycharmProjects\First"
generate_a_dict_of_files_and_folders(my_path)
#4############## Можно вместо счетчика флаг поставить, но счетчик сразу в голову пришел.
def create_folders(folder_path):
    my_folder=os.listdir(folder_path)
    count=0
    for str in my_folder:
        if os.path.isdir(str):
            os.mkdir(f"{str}_tmp")
            count+=1
    if count == 0:
           os.mkdir("tmp")
my_path="F:/Vadim/PycharmProjects/First"
create_folders(my_path)


