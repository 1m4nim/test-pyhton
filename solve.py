# import sys

# try:
#     X,Y=map(int, sys.stdin.read().split())
# except:
#     X,Y=1,1

# def solve():
#     def f(x:int)->int:
#         s_x=str(x)
#         rev_s_x=s_x[::-1]
#         return int(rev_s_x)
    
#     A=[0]*10

#     A[0]=X
#     A[1]=Y

#     for i in range(2,10):
#         next_term=f(A[i-1]+A[i-2])
#         A[i]=next_term


#     print(A[9])

# solve()

# if __name__=="__main__":
#     try:
#         input_data=sys.stdin.read().split()
#         if len(input_data)>=2:
#             X=int(input_data[0])
#             Y=int(input_data[1])

#             A=[0]*10
#             A[0]=x
#             A[1]=Y

#             for i in range(2,10):
#                 A[i]=f(A[i-1]+A[i-2])

#             print(A[9])

#     except EOFError:
#         pass
#     except ValueError:
#         pass


# for i in range(1,101):
#     if(i%3==0)and(i%5==0):
#         print("FizzBuzz", end=" ")
#     elif(i%3==0):
#         print("Fizz", end=" ")
#     elif(i%5==0):
#         print("Buzz", end=" ")
#     else:
#         print(i, end=" ")


input_price=input("insert: ")
product_price=input("product: ")
change=int(input_price)-int(product_price)

coin=[5000,1000,500,100,50,10,5,1]

for i in coin:
    r=change//i
    change=change%i
    print(str(i)+":"+str(r))

    