def longestSubarray(self, arr, k):
    arr_sum = 0
    max_length = 0
    temp = {}
    
    for i in range(len(arr)):
        arr_sum += arr[i]
        
        if arr_sum == k:
            max_length = i+1
        
        if arr_sum - k in temp:
            max_length = max(max_length,temp[arr_sum-k])
        
        if arr_sum not in temp:
            temp[arr_sum] = i
    
    return max_length
arr= [10, -10, 20, 30]
k = 5
result = longestSubarray(None, arr, k)
print("Longest Subarray Length:", result)
