def fibonaci(n): 
    if n == 0 or n == 1: 
        return n
    else: 
        return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(6))