# 1. Basic For Loop
def basic_for_loop():
    # Print numbers from 0 to 10
    for i in range(11):
        print(i)


# # 2. Basic While Loop
# def basic_while_loop():
#     # Print numbers from 0 to 9
#     i = 0
#     while i < 10:
#         print(i)
#         i = i + 1


# # 3. Nested For Loops
# def nested_for_loop():
#     # Print coordinates (i,j) for a 5x5 grid
#     for i in range(5):
#         for j in range(5):
#             print(f"({i},{j})")


# # 4. For Loop with If Condition
# def print_even_numbers():
#     # Print even numbers from 1 to 100
#     for i in range(1, 101):
#         if i % 2 == 0:  # If i is divisible by 2 (even)
#             print(i)


# # 5. While Loop with If Condition
# def print_divisible_by_three():
#     # Print numbers divisible by 3 from 1 to 100
#     i = 1
#     while i <= 100:
#         if i % 3 == 0:  # If i is divisible by 3
#             print(i)
#         i = i + 1


# # 6. Bubble Sort
# def bubble_sort(arr):
#     # Sort an array using bubble sort
#     n = len(arr)
    
#     # Go through all array elements
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr


# # 7. Linear Search
# def linear_search(arr, target):
#     # Search for target in array and return its position
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if found
    
#     return -1  # Return -1 if not found


# # 8. Binary Search
# def binary_search(arr, target):
#     # Search for target in a sorted array using binary search
#     left = 0
#     right = len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2  # Find the middle point
        
#         # Check if target is at the middle
#         if arr[mid] == target:
#             return mid
        
#         # If target is greater, ignore left half
#         elif arr[mid] < target:
#             left = mid + 1
        
#         # If target is smaller, ignore right half
#         else:
#             right = mid - 1
    
#     return -1  # Return -1 if not found


# # 9. Fibonacci Sequence
# def fibonacci(n):
#     # Print first n Fibonacci numbers
#     a, b = 0, 1
#     count = 0
    
#     while count < n:
#         print(a)
#         # Update a and b for next Fibonacci number
#         temp = a + b
#         a = b
#         b = temp
#         count = count + 1


# # 10. Fibonacci Sequence (For Loop)
# def fibonacci_for(n):
#     # Print first n Fibonacci numbers using for loop
#     a, b = 0, 1
    
#     for i in range(n):
#         print(a)
#         # Update a and b for next Fibonacci number
#         a, b = b, a + b


# # 11. Factorial Calculation
# def factorial(n):
#     # Calculate factorial of n
#     result = 1
    
#     for i in range(1, n + 1):
#         result = result * i
    
#     return result


# # 12. Sum of Array Elements
# def sum_array(arr):
#     # Calculate sum of all elements in array
#     total = 0
    
#     for num in arr:
#         total = total + num
    
#     return total


# # 13. Maximum Element in Array
# def find_max(arr):
#     # Find the largest element in an array
#     if len(arr) == 0:
#         return None
    
#     max_value = arr[0]  # Start with first element
    
#     for num in arr:
#         if num > max_value:
#             max_value = num
    
#     return max_value


# # 14. For Loop with Break
# def for_loop_break():
#     # Exit loop when number exceeds 10
#     for i in range(100):
#         if i > 10:
#             break  # Exit the loop
#         print(i)


# # 15. While Loop with Continue
# def while_loop_continue():
#     # Skip even numbers and print odd numbers
#     i = 0
#     while i < 20:
#         i = i + 1
#         if i % 2 == 0:
#             continue  # Skip rest of loop if number is even
#         print(i)


# # 16. Prime Number Check
# def is_prime(n):
#     # Check if n is a prime number
    
#     # Numbers less than 2 are not prime
#     if n <= 1:
#         return False
    
#     # Check for factors up to the square root of n
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False  # n is divisible by i
    
#     return True  # n is prime


# # 17. Count Digits in Number
# def count_digits(n):
#     # Count how many digits are in a number
#     count = 0
    
#     # Handle case where n is 0
#     if n == 0:
#         return 1
    
#     # Convert negative to positive for counting
#     n = abs(n)
    
#     while n > 0:
#         n = n // 10  # Integer division to remove last digit
#         count = count + 1
    
#     return count


# # 18. Reverse a String
# def reverse_string(s):
#     # Reverse the characters in a string
#     reversed_str = ""
    
#     for i in range(len(s)-1, -1, -1):
#         reversed_str = reversed_str + s[i]
    
#     return reversed_str


# # 19. Selection Sort
# def selection_sort(arr):
#     # Sort array using selection sort
#     n = len(arr)
    
#     for i in range(n):
#         # Find the minimum element in the unsorted part
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
        
#         # Swap the minimum element with the first element
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
#     return arr


# # 20. Insertion Sort
# def insertion_sort(arr):
#     # Sort array using insertion sort
#     for i in range(1, len(arr)):
#         key = arr[i]  # Current element to be inserted
#         j = i - 1
        
#         # Move elements greater than key to one position ahead
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j = j - 1
        
#         # Insert key at correct position
#         arr[j + 1] = key
    
#     return arr


# # 21. Count Occurrences in Array
# def count_occurrences(arr, element):
#     # Count how many times element appears in array
#     count = 0
    
#     for item in arr:
#         if item == element:
#             count = count + 1
    
#     return count


# # 22. Matrix Addition
# def add_matrices(A, B):
#     # Add two matrices together
#     # Assuming both matrices have the same dimensions
    
#     # Create a result matrix filled with zeros
#     rows = len(A)
#     cols = len(A[0])
#     result = []
    
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(A[i][j] + B[i][j])
#         result.append(row)
    
#     return result


# # 23. Print Triangle Pattern
# def print_triangle(n):
#     # Print a triangle pattern of stars
#     for i in range(1, n + 1):
#         # Print i stars on each line
#         for j in range(i):
#             print("*", end="")
#         print()  # Move to next line


# # 24. Check if String is Palindrome
# def is_palindrome(s):
#     # Check if string reads the same forward and backward
    
#     # Convert to lowercase and remove non-alphanumeric characters
#     cleaned = ""
#     for char in s.lower():
#         if char.isalnum():
#             cleaned = cleaned + char
    
#     # Compare original with reversed
#     return cleaned == cleaned[::-1]


# # 25. Greatest Common Divisor (GCD)
# def gcd(a, b):
#     # Find GCD of two numbers using Euclidean algorithm
#     while b:
#         a, b = b, a % b
#     return a


# # 26. Print Odd Numbers Only
# def print_odd_numbers():
#     # Print odd numbers from 1 to 100
#     for i in range(1, 101):
#         if i % 2 != 0:  # If i is not divisible by 2 (odd)
#             print(i)


# # 27. Merge Two Sorted Lists
# def merge_sorted_lists(list1, list2):
#     # Merge two sorted lists into one sorted list
#     merged = []
#     i = 0  # Index for list1
#     j = 0  # Index for list2
    
#     # Compare elements from both lists and add smaller one to result
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
    
#     # Add remaining elements from list1 if any
#     while i < len(list1):
#         merged.append(list1[i])
#         i += 1
    
#     # Add remaining elements from list2 if any
#     while j < len(list2):
#         merged.append(list2[j])
#         j += 1
    
#     return merged


# # 28. Sum of Digits
# def sum_of_digits(n):
#     # Calculate sum of all digits in a number
#     total = 0
    
#     # Convert negative to positive for summing
#     n = abs(n)
    
#     while n > 0:
#         digit = n % 10  # Get the last digit
#         total = total + digit
#         n = n // 10  # Remove the last digit
    
#     return total


# # 29. Power Function
# def power(base, exponent):
#     # Calculate base raised to the power of exponent
#     result = 1
    
#     for i in range(exponent):
#         result = result * base
    
#     return result


# # 30. Binary to Decimal Conversion
# def binary_to_decimal(binary):
#     # Convert binary number to decimal
#     decimal = 0
#     power = 0
    
#     # Convert to integer in case it's a string
#     if isinstance(binary, str):
#         binary = int(binary)
    
#     while binary > 0:
#         last_digit = binary % 10
#         decimal = decimal + last_digit * (2 ** power)
#         power = power + 1
#         binary = binary // 10
    
#     return decimal


# # 31. Find Duplicate Elements in Array
# def find_duplicates(arr):
#     # Find elements that appear more than once in array
#     duplicates = []
#     seen = []
    
#     for item in arr:
#         if item in seen and item not in duplicates:
#             duplicates.append(item)
#         else:
#             seen.append(item)
    
#     return duplicates


# # 32. Armstrong Number Check
# def is_armstrong(n):
#     # Check if n is an Armstrong number
#     # (sum of each digit raised to power of number of digits equals n)
    
#     # Convert to string to count digits
#     num_str = str(n)
#     num_digits = len(num_str)
    
#     total = 0
#     temp = n
    
#     while temp > 0:
#         digit = temp % 10
#         total = total + digit ** num_digits
#         temp = temp // 10
    
#     return total == n


# # 33. Print First N Prime Numbers
# def print_first_n_primes(n):
#     # Print the first n prime numbers
#     count = 0
#     num = 2
    
#     while count < n:
#         if is_prime(num):
#             print(num)
#             count = count + 1
#         num = num + 1


# # 34. Check if Array is Sorted
# def is_sorted(arr):
#     # Check if array is sorted in ascending order
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
    
#     return True


# # 35. Calculate Average of Array
# def average(arr):
#     # Calculate the average value of array elements
#     if len(arr) == 0:
#         return 0
    
#     total = sum(arr)
#     avg = total / len(arr)
    
#     return avg


# # 36. Reverse Digits of Number
# def reverse_number(n):
#     # Reverse the digits of a number
#     reversed_num = 0
    
#     while n > 0:
#         last_digit = n % 10
#         reversed_num = reversed_num * 10 + last_digit
#         n = n // 10
    
#     return reversed_num


# # 37. Find Elements Common to Two Arrays
# def find_common_elements(arr1, arr2):
#     # Find elements that appear in both arrays
#     common = []
    
#     for item in arr1:
#         if item in arr2 and item not in common:
#             common.append(item)
    
#     return common


# # 38. Print Multiplication Table
# def multiplication_table(n):
#     # Print multiplication table for number n
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")


# # 39. Simple Linear Search with Break
# def linear_search_with_break(arr, target):
#     # Search for target in array, exit as soon as found
#     found = False
#     position = -1
    
#     for i in range(len(arr)):
#         if arr[i] == target:
#             found = True
#             position = i
#             break  # Exit loop as soon as found
    
#     if found:
#         return position
#     else:
#         return -1


# # 40. Simple Depth-First Search (DFS)
# def dfs(graph, start, visited=None):
#     # Perform depth-first search on a graph
#     if visited is None:
#         visited = []
    
#     # Mark current node as visited
#     visited.append(start)
#     print(start)
    
#     # Visit all neighbors
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)
    
#     return visited


# # 41. Simple Breadth-First Search (BFS)
# def bfs(graph, start):
#     # Perform breadth-first search on a graph
#     visited = []  # List to keep track of visited nodes
#     queue = [start]  # Queue for BFS
    
#     while queue:
#         # Remove and get first vertex from queue
#         vertex = queue.pop(0)
        
#         # If not already visited, mark as visited
#         if vertex not in visited:
#             visited.append(vertex)
#             print(vertex)
            
#             # Add all unvisited neighbors to queue
#             for neighbor in graph[vertex]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
    
#     return visited


# # 42. Check Leap Year
# def is_leap_year(year):
#     # Check if a year is a leap year
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False


# # 43. Remove Duplicates from Array
# def remove_duplicates(arr):
#     # Remove duplicate elements from array
#     result = []
    
#     for item in arr:
#         if item not in result:
#             result.append(item)
    
#     return result


# # 44. Find Second Largest Element
# def second_largest(arr):
#     # Find the second largest element in array
#     if len(arr) < 2:
#         return None
    
#     # Find largest element
#     largest = max(arr)
    
#     # Remove all occurrences of largest element
#     while largest in arr:
#         arr.remove(largest)
    
#     # Find largest in remaining elements (second largest overall)
#     if len(arr) == 0:
#         return None
    
#     return max(arr)


# # 45. Simple Maximum Subarray Sum
# def max_subarray_sum(arr):
#     # Find maximum sum of contiguous subarray
#     max_so_far = arr[0]
#     current_max = arr[0]
    
#     for i in range(1, len(arr)):
#         # Current maximum is either current element or
#         # current element plus previous maximum
#         current_max = max(arr[i], current_max + arr[i])
        
#         # Update overall maximum if current maximum is larger
#         max_so_far = max(max_so_far, current_max)
    
#     return max_so_far


# # 46. Print Numbers in Range with Step
# def print_range(start, end, step):
#     # Print numbers from start to end with given step
#     i = start
#     while i <= end:
#         print(i)
#         i = i + step


# # 47. Simple Pascal's Triangle
# def pascals_triangle(rows):
#     # Print Pascal's triangle with given number of rows
#     for i in range(rows):
#         # Start with 1
#         num = 1
        
#         # Print spaces for formatting
#         for j in range(rows - i - 1):
#             print(" ", end="")
        
#         # Calculate and print values
#         for j in range(i + 1):
#             print(num, end=" ")
#             # Calculate next value
#             num = num * (i - j) // (j + 1)
        
#         print()  # Move to next line


# # 48. Simple Sieve of Eratosthenes
# def sieve_of_eratosthenes(n):
#     # Find all prime numbers up to n
    
#     # Create a boolean array "is_prime[0..n]"
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
    
#     # Check each number up to square root of n
#     for i in range(2, int(n**0.5) + 1):
#         # If i is prime, mark all its multiples as non-prime
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False
    
#     # Print all prime numbers
#     for i in range(2, n+1):
#         if is_prime[i]:
#             print(i)


# # 49. Simple Binary Exponentiation
# def binary_exponentiation(base, exponent):
#     # Calculate base^exponent more efficiently
    
#     # Base case
#     if exponent == 0:
#         return 1
    
#     # Recursive case for even exponent
#     if exponent % 2 == 0:
#         half_pow = binary_exponentiation(base, exponent // 2)
#         return half_pow * half_pow
    
#     # Recursive case for odd exponent
#     else:
#         half_pow = binary_exponentiation(base, (exponent - 1) // 2)
#         return base * half_pow * half_pow


# # 50. Print Pyramid Pattern
# def print_pyramid(n):
#     # Print a pyramid pattern of stars
#     for i in range(1, n + 1):
#         # Print spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print stars
#         for j in range(2 * i - 1):
#             print("*", end="")
        
#         print()  # Move to next line