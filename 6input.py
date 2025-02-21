####### flowchart ########
# Inputting six numbers.
# Initializing third and fourth placeholders.
# Using nested loops to count smaller and equal values.
# Identifying the third and fourth smallest numbers.
# Calculating the median.


number1 = float(input("Enter number 1st numnber: "))
number2 = float(input("Enter number 2st numnber: "))
number3 = float(input("Enter 3rd numnber: "))
number4 = float(input("Enter 4th numnber: "))
number5 = float(input("Enter number 5st numnber: "))
number6 = float(input("Enter number 6st numnber: "))


nums = [number1, number2, number3, number4, number5, number6]
    
# Initialize placeholders for the third and fourth smallest numbers
third = None
fourth = None
    
for i in range(6):
        count_smaller = 0  # Count of numbers smaller than nums[i]
        count_equal = 0  # Count of numbers equal to nums[i]
        
        for j in range(6):
            if nums[j] < nums[i]:
                count_smaller += 1
            elif nums[j] == nums[i]:
                count_equal += 1
        
        # The third smallest number is the one where count_smaller is exactly 2 or (2 and equal count includes it)
        if count_smaller == 2 or (count_smaller < 2 and count_smaller + count_equal > 2):
            third = nums[i]
        
        # The fourth smallest number is the one where count_smaller is exactly 3 or (3 and equal count includes it)
        if count_smaller == 3 or (count_smaller < 3 and count_smaller + count_equal > 3):
            fourth = nums[i]
    
# Compute median
median = (third + fourth) / 2
print("The Median is!:", median)

## no loop being used

# Taking inputs manually
number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))
number3 = float(input("Enter 3rd number: "))
number4 = float(input("Enter 4th number: "))
number5 = float(input("Enter 5th number: "))
number6 = float(input("Enter 6th number: "))

# Creating the list of numbers
nums = [number1, number2, number3, number4, number5, number6]

# Manual sorting (since we can't use loops)
if nums[0] > nums[1]: nums[0], nums[1] = nums[1], nums[0]
if nums[2] > nums[3]: nums[2], nums[3] = nums[3], nums[2]
if nums[4] > nums[5]: nums[4], nums[5] = nums[5], nums[4]

if nums[0] > nums[2]: nums[0], nums[2] = nums[2], nums[0]
if nums[1] > nums[3]: nums[1], nums[3] = nums[3], nums[1]
if nums[4] > nums[2]: nums[4], nums[2] = nums[2], nums[4]
if nums[5] > nums[3]: nums[5], nums[3] = nums[3], nums[5]

if nums[1] > nums[4]: nums[1], nums[4] = nums[4], nums[1]
if nums[0] > nums[1]: nums[0], nums[1] = nums[1], nums[0]
if nums[2] > nums[3]: nums[2], nums[3] = nums[3], nums[2]
if nums[4] > nums[5]: nums[4], nums[5] = nums[5], nums[4]

# The third and fourth smallest elements
third = nums[2]
fourth = nums[3]

# Compute median
median = (third + fourth) / 2
print("The Median is:", median)
