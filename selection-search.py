def searchMinor(list):
    minor = list[0]
    minor_index = 0
    for i in range(1, len(list)):
        if list[i] < minor:
            minor = list[i]
            minor_index = i
    return minor_index

def selectionSearch(list):
    newList = []
    for i in range(len(list)):
        minor = searchMinor(list)
        newList.append(list.pop(minor))
    return newList

print(selectionSearch([5, 3, 6, 2, 10]))