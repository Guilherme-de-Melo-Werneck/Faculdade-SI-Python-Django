def rec(n):
    if n > 0:
        print(n)

        rec(n - 1)
        
        print(n)

rec(4)