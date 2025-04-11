

# def fib (n):
#     a, b = 0, 1
#     if n < 0:
#         print("Incorrect input")
#         return
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for i in range(n-2):
#             a, b = b, a + b
#         return b
    
# def main():
#     n = int(input("Enter a number: "))
#     print(fib(n))

# if __name__ == "__main__":
#         main()

#############################

# def fibRec(n):
#      if n == 0:
#          return 0
#      if n==1:
#          return 1
#      return fibRec(n-1) + fibRec(n-2)

# def main():
#     n = int(input("Enter a number: "))
#     print(fibRec(n))

# if __name__ == "__main__":
#         main()

########################## factorial ###################

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
    
# n = int(input("Enter a number: "))
# print(f"The factorial of {n} is {factorial(n)}")

def factRec(n):
    if n == 0:
        return 1
    else:
        return n * factRec(n-1)
n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factRec(n)}")