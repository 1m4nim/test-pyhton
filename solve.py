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


# def uruu(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#         else:
#             return True
#     else:
#         return False


# for i in range(1950, 2051):
#     print(str(i) + " " + str(uruu(i)))


# import sys

# try:
#     H, W = map(int, sys.stdin.readline().split())
# except:
#     exit()

# S = []
# for _ in range(H):
#     S.append(sys.stdin.readline().strip())

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# is_valid = True

# for i in range(H):
#     for j in range(W):

#         if S[i][j] == "#":
#             black_neighor_count = 0

#             for dr, dc in directions:
#                 ni, nj = i + dr, j + dc

#                 if 0 <= ni < H and 0 <= nj < W:
#                     if S[ni][nj] == "#":
#                         black_neighor_count += 1

#             if black_neighor_count != 2 and black_neighor_count != 4:
#                 is_valid = False
#                 break
#     if not is_valid:
#         break

# if is_valid:
#     print("YES")
# else:
#     print("NO")


# import sys

# try:
#     N = int(sys.stdin.readline())
# except:
#     exit()

# try:
#     doors = list(map(int, sys.stdin.readline().split()))
# except:
#     exit()

# for i in range(N):
#     if doors[i] == 1:
#         first_closed = i
#         break

# if first_closed == -1:
#     R = N
# else:
#     R = first_closed

# right_closed = -1

# for i in range(N - 1, -1, -1):
#     if doors[i] == 1:
#         right_closed = i
#         break

# if right_closed == -1:
#     L = 0
# else:
#     L = right_closed + 1

# if R + 1 >= L:
#     print(0)
# else:
#     result = L - R - 1
#     print(result)

import sys


def solve():
    try:
        data = sys.stdin.readline().split()
        if not data:
            return
        N, M, K = map(int, data)
    except:
        return

    perfect_counts = [0] * (N + 1)

    solved_all = set()

    result_order = []

    for _ in range(K):
        try:
            line = sys.stdin.readline().split()
            if not line:
                break
            A, B = map(int, line)
        except:
            break

        person_id = A
        if person_id not in solved_all:
            perfect_counts[person_id] += 1

            if perfect_counts[person_id] == M:
                result_order.append(person_id)
                solved_all.add(person_id)

    print(*(str(p) for p in result_order))


if __name__ == "__main__":
    solve()
