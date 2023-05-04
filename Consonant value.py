def solve(s):
    vowels = 'aeiou'
    max_consonant_value = 0
    current_consonant_value = 0
    
    for c in s:
        if c in vowels:
            current_consonant_value = 0
        else:
            current_consonant_value += ord(c) - ord('a') + 1
            
            if current_consonant_value > max_consonant_value:
                max_consonant_value = current_consonant_value
    
    return max_consonant_value
