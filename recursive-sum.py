def sum_list(list):
    if list == []:
        return 0
    return list[0] + sum_list(list[1:])


my_list = [1, 3, 5, 7, 9]
print(sum_list(my_list)) # 25