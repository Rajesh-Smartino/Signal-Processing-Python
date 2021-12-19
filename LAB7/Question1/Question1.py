def is_balanced(inp):
    stack = []
    
    for idx, char in enumerate(inp):
        if char in closing_opening_map.values():
            stack.insert(0, (idx, char))

        elif char in closing_opening_map:
            if stack:
                top = stack.pop(0)
                if top[1] != closing_opening_map[char]:
                    print(top[0])
                    return False
            else:
                print(idx)
                return False
            
    if stack:
        print(stack[-1][0])
    return not stack
        
        
closing_opening_map = {
    ')': '(' ,
    '}': '{',
    ']': '['
}

inp = "{a*b(c-d)+a})"

print(is_balanced(inp))