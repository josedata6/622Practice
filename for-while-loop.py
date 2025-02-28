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

count = 0
total = 0

while True:
    user_input= input("entera numer or type end to finish: ")
    if user_input.lower()=="end": #making sure the input is lowercase
        print("Thanks for your input")
        break
    elif user_input.isnumeric():
        count+=1
        total = total + float(user_input)
    else: ### adding a check if inout is something else than end
        print("your input is not valid")
        pass

    print(count, " ", total)