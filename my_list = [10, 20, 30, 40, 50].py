def bunary_search(lst, item_search):
    low = 0 
    high = len(lst)
    search_res = False
    while low <= high and not search_res:
        middle = (low + high)//2 
        guess = lst[middle]
        if guess == item_search:
            search_res = True
            return search_res
        if guess > item_search:
            high = middle - 1
        else:
            low = middle + 1
    return search_res
 
lst = [3, 24, 35, 67, 78, 81, 93, 94]
value = 90
print(bunary_search(lst, value))