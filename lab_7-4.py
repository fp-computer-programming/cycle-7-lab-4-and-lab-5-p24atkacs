"""
Create a Python file named lab_7-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-2 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately




________________________________________________________________________________

Create a Python file named lab_7-5.py


Copy the code from your labs 6-5 through 6-8
Turn each of the programs into a function
Add 4 test cases to the functions
Ensure your code runs accurately


"""
# lab_7-4.py

# Author: Andrew Tkacs

def find_sum(num1, num2):
    """
    This function takes two numbers as parameters, adds them, and returns the sum.
    """
    # Add the arguments passed to num1 and num2
    num_sum = num1 + num2
    
    # Return the sum
    return num_sum

# Call the find_sum function with arguments 111 and 222
my_sum = find_sum(111, 222)

# Print the result
print(my_sum)

# Printed the sum of 111 + 222, which printed 333.  This is because I printed the function that added the two numbers.  

# Test Case 1

# Call the find_sum function with arguments 5 and 10

result1 = find_sum(5, 10)
print(result1) 

# Test Case 2

# Call the find_sum function with arguments -3 and 7

result2 = find_sum(-3, 7)
print(result2)  

# Test Case 3

# Call the find_sum function with arguments 0 and 0

result3 = find_sum(0, 0)
print(result3)  

# Test Case 4

# Call the find_sum function with large numbers

result4 = find_sum(1000, 2000)
print(result4)  
