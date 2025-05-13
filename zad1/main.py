def find_longest_increasing_subsequence(numbers):
   
    if not numbers:
        return []
    
    dp = [1] * len(numbers)
    prev = [-1] * len(numbers)
    
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] > numbers[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    result = []
    while max_index != -1:
        result.append(numbers[max_index])
        max_index = prev[max_index]
    
    return list(reversed(result))
