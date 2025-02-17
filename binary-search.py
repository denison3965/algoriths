def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        half = (low + high) // 2 
        guess = lst[half]

        if guess == item:
            return half
        if guess > item:
            high = half - 1  
        else:
            low = half + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Saída esperada: 1
print(binary_search(my_list, 1))  # Saída esperada: 0
print(binary_search(my_list, 9))  # Saída esperada: 4
print(binary_search(my_list, -1)) # Saída esperada: None
