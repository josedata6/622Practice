def fib (n):
    a, b = 0, 1
    if n < 0:
        print("Incorrect input")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n-2):
            a, b = b, a + b
        return b
    
def main():
    n = int(input("Enter a number: "))
    print(fib(n))

if __name__ == "__main__":
        main()
