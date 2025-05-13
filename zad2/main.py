def find_longest_max_sum_subsequence(numbers):
    
    if not numbers:
        return []
    
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    current_start = 0
    max_length = 0
    
    for i, num in enumerate(numbers):
        current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            max_length = i - current_start + 1
        elif current_sum == max_sum and (i - current_start + 1) > max_length:
            start = current_start
            max_length = i - current_start + 1
        
        if current_sum < 0:
            current_sum = 0
            current_start = i + 1
    
    return numbers[start:start + max_length]
