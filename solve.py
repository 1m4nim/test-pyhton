# def fibonacci(n):
#     if (n == 1) or (n == 2):
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)


# print(fibonacci(6))

# # メモ化
# memo = {1: 1, 2: 1}


# def fibonacci(n):
#     if n in memo:
#         return memo[n]

#     memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
#     return memo[n]


# print(fibonacci(6))


# # ループ
# def fibonacci(n):
#     fib = [1, 1]
#     for i in range(2, n):
#         fib.append(fib[i - 2] + fib[i - 1])
#     return fib[n - 1]


# print(fibonacci(6))


def uruu(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


for i in range(1950, 2051):
    print(str(i) + " " + str(uruu(i)))
