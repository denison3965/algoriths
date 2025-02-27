def binary_search(lst, item, offset=0):
    if len(lst) == 0:
        return None 
    
    middle = len(lst) // 2
    guess = lst[middle]

    if guess == item:
        return middle + offset 
    elif guess > item:
        return binary_search(lst[:middle], item, offset) 
    else:
        return binary_search(lst[middle + 1:], item, offset + middle + 1) 

    
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Saída esperada: 1
print(binary_search(my_list, 1))  # Saída esperada: 0
print(binary_search(my_list, 9))  # Saída esperada: 4
print(binary_search(my_list, -1)) # Saída esperada: None