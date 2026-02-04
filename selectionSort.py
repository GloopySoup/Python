def selection_sort(list):
    index = range(0, len(list)-1)
    for i in index:
        min_value = i

        for j in range(i+1,len(list)):
            if list[j] < list[min_value]:
                min_value = j
        
        if min_value != i:
            list[min_value], list[i] = list[i], list[min_value]
    return list

print(selection_sort([33, 1, 89, 2, 67, 245]))