def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        minors = []
        for i in lst[1:]:
            if i <= pivot:
                minors.append(i)

        majors = []
        for i in lst[1:]:
            if i > pivot:
                majors.append(i)
        return quicksort(minors) + [pivot] + quicksort(majors)
    
print(quicksort([10, 5, 2, 3]))