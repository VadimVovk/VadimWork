a = input("Введите месяц: ")
if a == "январь" or a == "март" or a == "май" or a == "июль" or a == "август" or a =="октябрь" or a == "декабрь" or a == "1" or a == "3" or a == "5" or a == "7" or a == "8" or a == "10" or a == "12":
    print("31")
elif a =="апрель" or a == "июнь" or a == "сентябрь" or a == "ноябрь" or a == 4 or a == "6" or a == "9" or a == "11":
    print("30")
elif a == "февраль" or a == "2":
    print("28")
else:
    print("Вы ввели неверное значение")