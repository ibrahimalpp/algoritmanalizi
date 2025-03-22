
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Örnek bir dizi
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sıralama yapılmadan önceki dizi:", arr)

# Bubble Sort'u çalıştır
sorted_arr = bubble_sort(arr)

print("Sıralama yapıldıktan sonra dizi:", sorted_arr)
