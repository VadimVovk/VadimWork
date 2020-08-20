import random
1#######################
my_list=[]
my_list_f=[]
for val in range(1,101):
    my_list.append(val)
my_list_f= random.sample(my_list,20)
print(my_list_f)
########################
a=-100
b=100
a_x=random.uniform(a,b)
a_y=random.uniform(a,b)
b_x=random.uniform(a,b)
b_y=random.uniform(a,b)
c_x=random.uniform(a,b)
c_y=random.uniform(a,b)
triangle = {"A" : (a_x,a_y),
            "B" : (b_x,b_y),
            "C" : (c_x,c_y)}
print(triangle)
#####или так, если в целых числах. Прописывать в отдельную функцию не стал, т.к. особой разницы нет, все равно нужно считать каждую координату по отельности, а функция в одно действие.
a = -100
b = 100
a_x = random.randint(a,b)
a_y = random.randint(a,b)
b_x = random.randint(a,b)
b_y = random.randint(a,b)
c_x = random.randint(a,b)
c_y = random.randint(a,b)
triangle = {"A" : (a_x,a_y),
            "B":(b_x,b_y),
            "C":(c_x,c_y)}
print(triangle["A"])

3######
def my_print(my_str_1):
    print(f"***{my_str_1}***")
my_str="vadim"
my_print(my_str)
4#######
def my_print(my_str_1):
    a=("*"*len(my_str_1))
    print(f"{a}\n{my_str_1}\n{a}")
my_str="vadim"
my_print(my_str)
#5###########
def my_print(my_str_1):
    a=("*"*len(my_str_1))
    print(f"{a}\n***{my_str_1}***\n{a}")
my_str="vadim"
my_print(my_str)
## Я категорически не согласен с постановкой задачи(если в 4 задаче(а условие полностью взято из нее) указанно, что количество символов "*"  во верхней
# и нижней строке равно количеству символов во входящей строке, то не понятно, откуда берется увеличение количества символов на 6 в верхней и нижней строке и на каком основании? но сделаю и второй вариант.
def my_print(my_str_1):
    b=len(my_str_1)+6
    a=str("*"*b)
    print(f"{a}\n***{my_str_1}***\n{a}")
my_str="vadim"
my_print(my_str)

