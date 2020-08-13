my_val = int(10506075000)
my_val= str(my_val)
my_num=my_val.count("0")
print(my_num)
2##############
my_val = 101010101000
my_val= str(my_val)
my_val=my_val[::-1]
my_num=0
for symbol in my_val:
    if symbol == "0":
        my_num += 1
    else:
        break
print(my_num)
3##############
my_list_1=[10,20,30,40,50,60,"AA"]
my_list_2 = [15,25,35,45,55,65]
my_result =[]
my_result.extend(my_list_1[::2]+my_list_2[1::2])
print(my_result)
4###############
my_list = [10,20,30,40,50,60]
first_num=my_list.pop(0)
new_list=my_list
new_list.append(first_num)
print(new_list)
5###############
my_list = [10,20,30,40,50,60]
first_num=my_list.pop(0)
my_list.append(first_num)
print(my_list)
