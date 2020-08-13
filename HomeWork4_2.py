my_list=[25,150,250,15,24,500,100]
for numeric in my_list:
    if numeric > 100:
        print(numeric)
#######
my_list=[25,150,250,15,24,500,100]
my_result=[]
for numeric in my_list:
    if numeric > 100:
        my_result.append(numeric)
print(my_result)
#################
my_list=[100]
if len(my_list) < 2:
    my_list.append(0)
else:
  my_list.append(my_list[-2]+my_list[-1])
print(my_list)
##############
value=input("Введи десятичную дробь:")
try:
    value=float(value)
    res=1/value
    print(res)
except ValueError:
    print("ValueError!, все-таки введи десятичную дробь)))")
except ZeroDivisionError:
    print("ZeroDivisionError!, все-таки введи десятичную дробь, а не ноль))")
print("Попробуй еще раз!")

