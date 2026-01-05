def sumlist(list):
    if not list:
        return 0
    else:
        return list[0]+sumlist(list[1:])
print(sumlist([1,2,3,4,5]))    