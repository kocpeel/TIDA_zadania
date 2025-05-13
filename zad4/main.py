def generate_permutations(n):
    if n <= 0 or n > 26:
        return []
    
    letters = [chr(ord('a') + i) for i in range(n)]
    result = []
    
    def permute(current, remaining):
        if not remaining:
            result.append(''.join(current))
            return
        
        for i in range(len(remaining)):
            current.append(remaining[i])
            permute(current, remaining[:i] + remaining[i+1:])
            current.pop()
    
    permute([], letters)
    return sorted(result)
