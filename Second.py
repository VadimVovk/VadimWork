import os
def listdir_folder(folder_path):
    list_from_folder=[]
    my_folder=os.listdir(folder_path)
    for str_1 in my_folder:
        list_from_folder.append(os.path.join(folder_path,str_1))
    return list_from_folder
def generate_a_list_of_folders(list_path):
    list_folders=[]
    for str_1 in list_path:
        if os.path.isdir(str_1):
            list_folders.append(str_1)
    return list_folders

def generate_a_list_of_files(list_path):
    list_files=[]
    for str_1 in list_path:
        if os.path.isfile(str_1):
            list_files.append(str_1)
    return list_files
my_path = "F:/Vadim/PycharmProjects/First"

print(generate_a_list_of_files(listdir_folder(my_path)))
print(generate_a_list_of_folders(listdir_folder(my_path)))



