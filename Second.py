###########
# s = "43 больше 38, но меньше 56 "
# l = len(s)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integ.append(int(s_int))
# print(integ)
#########
# str = "012345678"
# len_s = len(str)
# if len_s % 2 == 0:
#     my_list = list(str)
# else:
#     my_list= list(str)
#     # my_list.appehd(" ")
# # my_list =([str[i:i + 2] for i in range(0, len_s, 2)])
# # my_list.append(" ")
# print(my_list)
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[::2]
print(b)