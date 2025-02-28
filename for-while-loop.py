# number = input("give me a number: ")
# number = int(number)
# if number <0:
#     number = abs(number)

# total = 0
# i = 1

# while i < number:
#     total+=i
#     i+=1

# print(total-i+1)

####################################################

# number = input("give me a number: ")
# number = int(number)
# if number <0:
#     number = abs(number)

# total = 0
# i = 1

# while i < number:
#     i+=1
#     total+=i
#     if i == number:
#         total = total - number
  
# print(total)

#################################################

### only adding the even numbers

# number = input("give me a number: ")
# number = int(number)
# if number <0:
#     number = abs(number)

#     total =0

# for i in range(2, number+1,2):
#     total = total +i
#     print(total)

#############
###### using while only adding even numbers

# number = input("give me a number: ")
# number = int(number)
# if number <0:
#     number = abs(number)
    
# i = 2
# total =0

# while i<= number:
#     i+=2
#     total += i

# print(total)

###########################################
### rewrite the while with for loop
# count = 0
# total = 0

# while True:
#     user_input= input("entera numer or type end to finish: ")
#     if user_input.lower()=="end": #making sure the input is lowercase
#         print("Thanks for your input")
#         break
#     elif user_input.isnumeric():
#         count+=1
#         total = total + float(user_input)
#     else: ### adding a check if inout is something else than end
#         print("your input is not valid")
#         pass

#     print(count, " ", total)

###################
######## calculates the factorial of n

product = 1
count = 2
countNon = 0

while True:
    n = input("provide an input: ")

    if n.lower()=="end":
        print("Thanks for the input")
        break

    elif n.isnumeric():        
        while count< int(n):
            product = product * count 
            count +=1
        print("the count is:", product)
        print("the count is ", count)
        break

    else:
        print("your input is not a number")
        pass
    print(countNon)


    #####

    n = int(input())
    product = 1
    i=1

    while i<=n
        product *=i
        i+=1

    print(product)