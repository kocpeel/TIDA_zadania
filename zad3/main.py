def generate_non_decreasing_sequences(n):
    if n <= 0:
        return []
    
    result = []
    
    def backtrack(current, remaining, start):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, remaining + 1):
            current.append(i)
            backtrack(current, remaining - i, i)
            current.pop()
    
    backtrack([], n, 1)
    return result
