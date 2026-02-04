def quick_sort(list):
    if len(list) == 0:
        return []
    else:
        pivot = list.pop()
    
    items_greater = []
    items_lower = []

    for item in list:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([20, 3, 14, 1, 5]))