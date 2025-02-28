number = input("give me a number: ")
number = int(number)
if number <0:
    number = abs(number)

total = 0
i = 1

while i < number:
    total+=i
    i+=1

print(total)