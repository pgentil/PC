def fib(n: int):
    if n < 2:
        return 1
    if n == 2:
        return 2
    return fib(n-1) + fib(n-2)

memo = {0: 1, 1: 1}

def fib2(n):
    global memo
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]

if __name__ == "__main__":
    print(fib2(6))