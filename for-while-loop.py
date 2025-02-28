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

number = input("give me a number: ")
number = int(number)
if number <0:
    number = abs(number)
    
i = 2
total =0

while i<= number:
    i+=2
    total += i
    

print(total)