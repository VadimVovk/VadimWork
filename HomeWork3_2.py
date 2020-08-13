#1############################################################
value=150
new_value = (value / 2) if value < 100 else (value *(-1))
print(new_value)
#2#############################################################
value=100
new_value = (1) if value < 100 else (0)
print(new_value)
3#############################################################
value=21
new_value = True if value < 100 else False
print(new_value)
#4#############################################################
my_str="abfAT123"
my_str=my_str.upper()
print(my_str)
#5#############################################################
my_str = "abfAT123"
my_str = my_str.lower()
print(my_str)
#6#############################################################
my_str = "abf1"
my_str_2=(my_str*2) if len(my_str) < 5 else my_str
print(my_str_2)
#7#############################################################
my_str = "abf1"
my_str=(my_str + my_str[::-1]) if len(my_str) < 5 else my_str
print(my_str)
# #8#############################################################
my_str = "abf1AADD25#&&&??"
for symbol in my_str:
    if symbol.isdigit() or symbol.isalpha():
        print(symbol)
# #9############################################################
my_str = "abf1AADD2  5#&&  &??"
for symbol in my_str:
    if not symbol.isdigit() and not symbol.isalpha():
        print(symbol)
10###############################################################
my_str = "abf 1AADD 25#&       &&??"
for symbol in my_str:
    if not symbol in("012345678 9") and not symbol.isalpha():
        print(symbol)
#
