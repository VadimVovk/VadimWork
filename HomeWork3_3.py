my_str= 'barbarbarianbar'
my_symbol ="bar"
t = (my_str.count(my_symbol))
if t>0:
    count=1
    while count<=t:
        print(my_symbol)
        count+=1
else:
    print("совпадений нет")
#### ну или так#####
my_str= 'barbarbarianbar'
my_symbol ="ar"
t = (my_str.count(my_symbol))
print(my_symbol*4)
################
my_str= 'barbarbarianbar'
my_symbol ="ar"
t = (my_str.count(my_symbol))
print(t)
################
my_str= 'abababAAAAAAHhababde3'
my_str=my_str.lower()
my_set=set(my_str)
m = len(my_set)
print(m)