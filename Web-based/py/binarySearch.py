def binarySearch(arr, key):
    sorted_search = sorted(arr)
    maxx = len(sorted_search)
    fl = 0
    ll = maxx - 1

    while fl <= ll:
        mp = (fl + ll) // 2  
        if key == sorted_search[mp]:
            print("Search successful:", sorted_search[mp])
            return mp  
        elif key < sorted_search[mp]:
            ll = mp - 1  
        else:
            fl = mp + 1
    print("Search unsuccessful")
    return -1  

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"]

print(binarySearch(names, "Jack"))