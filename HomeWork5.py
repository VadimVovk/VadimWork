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
my_list_1=[10,20,30,40,51,60,]
my_list_2 = [15,20,35,40,55,65]
my_result =[]
for val in my_list_1:
    if val%2 == 0:
        my_result.append(val)
for value in my_list_2:
    if value%2 !=0:
        my_result.append(value)
print(my_result)
4###############
my_list = [10,20,30,40,50,60]
first_num=my_list.pop(0)
new_list=my_list
new_list.append(first_num)
print(new_list)
5###############
my_list = [10,20,30,40,50,60]
my_list.append(my_list.pop(0))
print(my_list)
# 6##########
my_str="35 меньше чем 45 , но больше чем 25 5"
my_list = my_str.split()
num_list = []
for word in my_list:
    if word.isnumeric():
        num_list.append(int(word))
sum=0
for num in num_list:
    sum=sum+num
print(sum)
7#######
my_str = "abcdefg"
lng=len(my_str)
if lng%2 == 0:
    my_str_1= str(my_str)
else:
    my_str_1=str(my_str+"_")
my_list_f=[]
for num in range(0,lng,2):
    my_str_f = my_str_1[num:num+2]
    my_list_f.append(my_str_f)
print(my_list_f)
#8###########################
my_str ="abcdefgh"
l_limit = "c"
r_limit = "h"
count_l=0
for symbol in my_str:
    if symbol != l_limit:
        count_l+=1
    else:
        break
count_r=0
for symbol in my_str:
    if symbol != r_limit:
        count_r+=1
    else:
        break
sub_str = my_str[(count_l+1):count_r]
print(count_l,count_r)
print(sub_str)
# ############Другое решение, через один цикл с флагами, которое Вы мне показали.
my_str ="abcdefgh"
l_limit = "c"
r_limit = "g"
count_l=0
count_r=0
flag_l = True
flag_r = True
for symbol in my_str:
    if symbol != l_limit and flag_l == True:
        count_l+=1
    else:
        flag_l=False
    if symbol != r_limit and flag_r == True:
        count_r+=1
    else:
        flag_r = False
sub_str = my_str[(count_l+1):count_r]
print(count_l,count_r)
print(sub_str)
#9###########################
my_str ="123426789"
l_limit = "2"
r_limit = "8"
count_l=0
for symbol in my_str:
    if symbol != l_limit:
        count_l+=1
    else:
        break
count_r=0
for symbol in my_str[::-1]:
    if symbol != r_limit:
        count_r+=1
    else:
        break
lrn=len(my_str)-count_r-1
sub_str = my_str[(count_l+1):lrn]
print(sub_str)
#10###################
my_list = [1,1,50,35,40,25,115,20,150,20,200,30]
count = 0
my_list_1=[]
lrn = len(my_list)
my_range = range(1,lrn-1)
for num in my_range:
    if my_list[num] > my_list[num+1]+my_list[num-1]:
        my_list_1.append(my_list[num])
        count +=1
print(f"Таких чисел:{count}. Это числа: {my_list_1}")
# Вывод чисел уже так, себя проверить))))