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

# import sys


# def solve():
#     try:
#         data = sys.stdin.readline().split()
#         if not data:
#             return
#         N, M, K = map(int, data)
#     except:
#         return

#     perfect_counts = [0] * (N + 1)

#     solved_all = set()

#     result_order = []

#     for _ in range(K):
#         try:
#             line = sys.stdin.readline().split()
#             if not line:
#                 break
#             A, B = map(int, line)
#         except:
#             break

#         person_id = A
#         if person_id not in solved_all:
#             perfect_counts[person_id] += 1

#             if perfect_counts[person_id] == M:
#                 result_order.append(person_id)
#                 solved_all.add(person_id)

#     print(*(str(p) for p in result_order))


# if __name__ == "__main__":
#     solve()


# import sys


# def solve():

#     try:
#         N_line = sys.stdin.readline()
#         if not N_line:
#             return
#         N = int(N_line)
#     except:
#         return

#     try:
#         A = list(map(int, sys.stdin.readline().split()))
#     except:
#         return

#     P = [0] * N
#     used_elements = set()

#     for i in range(N):
#         val = A[i]

#         if val != -1:

#             if val in used_elements:
#                 print("No")
#                 return

#             P[i] = val
#             used_elements.add(val)

#     all_elements = set(range(1, N + 1))

#     unused_elements = list(all_elements - used_elements)

#     unused_elements.sort()
#     unused_index = 0

#     for i in range(N):
#         if P[i] == 0:

#             if unused_index < len(unused_elements):
#                 P[i] = unused_elements[unused_index]
#                 unused_index += 1
#             else:
#                 print("No")
#                 return

#     print("Yes")
#     print(*(str(p) for p in P))


# if __name__ == "__main__":
#     solve()

# import sys


# def solve():
#     try:
#         S = sys.stdin.readline().strip()
#     except:
#         return

#     counts = {}
#     for char in S:
#         counts[char] = counts.get(char, 0) + 1

#     for char, count in counts.items():
#         if count == 1:
#             print(char)
#             return


# if __name__ == "__main__":
#     solve()

# import sys

# def f(x):
#     return sum(int(digit) for digit in str(x))

# def solve():
#     try:
#         N = int(sys.stdin.readline())
#     except:
#         return

#     A = [0] * (N + 1)
#     A[0] = 1

#     if N == 1:
#         print(f(A[0]))
#         return

#     A[1] = f(A[0])

#     for i in range(2, N + 1):
#         f_val_prev = f(A[i-1])
#         A[i] = A[i-1] + f_val_prev

#     print(A[N])

# if __name__ == "__main__":
#     solve()

# import sys


# def solve():
#     try:
#         N = int(sys.stdin.readline())
#         M = int(sys.stdin.readline())
#         # print("N:{N},M:{M}")
#     except:
#         return

#     if N == 1:
#         X = M + 1

#     LIMIT = 10**9


#     for i in range(M + 1):
#         term = N**1

#         if term > LIMIT:
#             X = LIMIT + 1
#             break

#         if X > LIMIT - term:
#             X = LIMIT + 1
#             break

#         X += term

#     if X <= LIMIT:
#         print(X)
#     else:
#         print("inf")


# if __name__ == "__main__":
#     solve()


# import sys


# def solve():
#     try:
#         N = int(sys.stdin.readline())
#         M = int(sys.stdin.readline())
#     except:
#         return

#     LIMIT = 10**9

#     if N == 1:
#         X = M + 1
#     else:
#         X = 0

#         for i in range(M + 1):
#             term = N**i

#             if term > LIMIT:
#                 X = LIMIT + 1
#                 break

#             if X > LIMIT - term:
#                 X = LIMIT + 1
#                 break

#             X += term

#     if X <= LIMIT:
#         print(X)
#     else:
#         print("inf")


# if __name__ == "__main__":
#     solve()


# import sys


# def solve():
#     try:
#         N = int(sys.stdin.readline())
#     except:
#         return

#     logged_in = False
#     error_count = 0

#     for _ in range(N):
#         try:
#             S = sys.stdin.readline().strip()
#         except:
#             break

#         if not S:
#             continue

#         if S == "login":
#             logged_in = True
#         elif S == "logout":
#             logged_in = False
#         elif S == "public":
#             pass
#         elif S == "private":
#             if logged_in == False:
#                 error_count += 1

#     print(error_count)


# if __name__ == "__main__":
#     solve()

# 421
import sys


def solve():
    try:
        N_str = sys.stdin.readline().strip()
        M_str = sys.stdin.readline().strip()
        
        if not N_str or not M_str:
            return

        N = int(N_str)
        M = int(M_str)
    except:
        return

    S = []
    for _ in range(N):
        try:
            S.append(sys.stdin.readline().strip())
        except:
            break

    scores = [0] * (N + 1)

    for j in range(M):
        count_0 = 0
        count_1 = 0

        vote_0 = []
        vote_1 = []

        for i in range(1, N + 1):
            if i - 1 >= len(S) or j >= len(S[i - 1]):
                continue
                
            vote = S[i - 1][j]

            if vote == "0":
                count_0 += 1
                vote_0.append(i)
            else:
                count_1 += 1
                vote_1.append(i)

        if count_0 == 0 or count_1 == 0:
            for i in range(1, N + 1):
                scores[i] += 1

        elif count_0 < count_1:
            for person_id in vote_0:
                scores[person_id] += 1

        else:
            for person_id in vote_1:
                scores[person_id] += 1
    
    max_score = 0
    if N > 0:
        max_score = max(scores[1:])

    winners = []
    for i in range(1, N + 1):
        if scores[i] == max_score:
            winners.append(str(i))
            
    print(" ".join(winners))


if __name__ == "__main__":
    solve()