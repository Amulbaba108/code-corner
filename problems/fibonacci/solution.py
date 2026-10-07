def fibonacci(n):
    if n <= 1:
        return n

    back2 = 0
    back1 = 1

    for i in range(2, n + 1):
        current = back1 + back2
        back2 = back1
        back1 = current

    return current


n = int(input())
print(fibonacci(n))
