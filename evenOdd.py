'''4)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
program:

# Input: Read the size of the list
size = int(input())

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Input: Read the elements of the list
for _ in range(size):
    number = int(input())
    # Check if the number is even or odd and append to the respective list
    if number % 2 == 0:
        even_numbers.append(number)  # Even numbers
    else:
        odd_numbers.append(number)    # Odd numbers

# Output: Display the even and odd lists
print("The even list", even_numbers)
print("The odd list", odd_numbers)
'''
