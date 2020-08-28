import string
import random
def create_string(str_random):
    string_symbol = string.printable
    my_list = []
    my_list_num = []
    lrn = random.randint(100,1000)
    for num in range(lrn):
        my_list.append(random.choice(string_symbol))
        my_list_num.append(num)
    my_list_num_f = my_list_num[1:lrn - 1]
    random.shuffle(my_list_num_f)
    list_9 = my_list_num_f[0:9]
    for symbol in list_9:
        my_list[symbol] = "\n"
    str_random=str("".join(my_list))
    print(str_random)

# file_writer(my_path):
my_str = "F:/Vadim/PycharmProjects/First/first.txt"
file_resolution = my_str.rsplit(".",1)
if file_resolution[-1] == "txt":
    create_string(str_1)
    with open("my_path", "w") as file:
    file.write("str_1")
    print(str_f)
