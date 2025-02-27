def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


my_list = [1, 3, 5, 7, 9]
print(count(my_list)) # 5
