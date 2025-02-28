## class loop practice

stopValue = int(input("Provide the stop value: "))
startValue = int(input("Provide the start value: "))
stepValue = int(input("Provide the step value: "))

## startNum = int(input("Provide the starting number: "))


if startValue < 0:
    startValue = abs(starttNum)

if stopValue  < 0:
    iterationNum = abs(stopValue)

product = 1
iterator = 1

for iterator in range(startValue, stopValue, stepValue):
    product = product * startValue * (iterator +1)
    print(product)