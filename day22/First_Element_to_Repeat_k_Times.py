def first_element_to_repeat_k_times(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == k:
            return num
    return -1

arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(first_element_to_repeat_k_times(arr, k)) 
