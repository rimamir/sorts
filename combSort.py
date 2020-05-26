def comb_sort(arr):
    alen = len(arr)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:  ## variant "comb-11"
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if arr[i + gap] < arr[i]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return arr
