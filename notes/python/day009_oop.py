def slidingWindow(arr, k):
    window_sum = sum(arr[:k])
    min_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        min_sum = min(min_sum, window_sum)
        
    return min_sum

print(slidingWindow([1, 2, 3, 4, 5], 2))  # 3 (1+2)
print(slidingWindow([1, 2, 3, 4, 5], 3))  # 6 (1+2+3)