def find_kth_element(arr, k):
    # K'th küçük elemanı bulmak için insertion sort mantığı
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr[k-1]

# Test
arr = [12, 3, 5, 7, 19]
k = 4
print(f"{k}. en küçük eleman:", find_kth_element(arr, k))
