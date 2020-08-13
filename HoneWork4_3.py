my_indexes=[0,1,2,3,4]
my_list=[10,20,30,40,50]
for index in my_indexes:
    print(my_list[index])
#########################
my_indexes=[0,1,2,3,4]
my_list1=[10,20,30,40,50]
my_list2=[15,25,35,45,55]
for index in my_indexes:
    print(f"{my_list1[index],my_list2[index]}")
#########################
my_string="0123456789"
my_list=[]
for symb_1 in my_string:
    for symb_2 in my_string:
        value = int(symb_1+symb_2)
        my_list.append(value)
print(my_list)
