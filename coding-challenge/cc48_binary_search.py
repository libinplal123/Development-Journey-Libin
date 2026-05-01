def search_binary(lst, num):
    lst = sorted(lst)
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return 'number not found'

list1 = [12, 34, 56, 78, 98, 22, 45, 13] 

print(search_binary(list1, 22))