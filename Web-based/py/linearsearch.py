
linSearch = [12, 33, 43, 45, 6, 4, 24, 6, 7, 8, 9]
k = 24
max = len(linSearch)
i = 0
    
while i < max and k != linSearch[i]:
    i += 1
    
    if i == max:
        print("This is the end of the search")
    elif k == linSearch[i]:
        print("Element found at index:", i)
    else:
        print("Element not found")

