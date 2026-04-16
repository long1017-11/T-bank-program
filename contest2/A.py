import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    stack = []  
    min_stack = []  
    
    idx = 1
    results = []
    
    for _ in range(n):
        t = int(data[idx])
        idx += 1
        
        if t == 1:  
            x = int(data[idx])
            idx += 1
            stack.append(x)
            if not min_stack or x <= min_stack[-1]:
                min_stack.append(x)
        
        elif t == 2:  
            if stack:
                removed = stack.pop()
                if min_stack and removed == min_stack[-1]:
                    min_stack.pop()
        
        elif t == 3:  
            if min_stack:
                results.append(str(min_stack[-1]))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
