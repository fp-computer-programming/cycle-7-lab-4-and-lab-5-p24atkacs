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
 # Author: Andrew Tkacs

 #Lab_7-5 (6-5 to 6-8)


#Lab_6-5

def find_high_low(input_list):
    """
    This function finds the highest and lowest values in a list.
    """
    # Check if the list has at least two unique numbers
    unique_numbers = set(input_list)

    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    # Find the highest and lowest values in the list
    highest_value = max(input_list)
    lowest_value = min(input_list)

    return highest_value, lowest_value

# Test cases
test_list_1 = [4, 7, 2, 9, 1]
result_1 = find_high_low(test_list_1)
print("Test 1 Result:", result_1)

test_list_2 = [3, 3, 3, 3]
result_2 = find_high_low(test_list_2)
print("Test 2 Result:", result_2)

test_list_3 = [5]
result_3 = find_high_low(test_list_3)
print("Test 3 Result:", result_3)

test_list_4 = []
result_4 = find_high_low(test_list_4)
print("Test 4 Result:", result_4)


#Lab_6-6

def get_user_input():
    """
    This function gets input from the user for 5 unique words.
    """
    word_list = []  # empty list to store words

    # Get input from the user for 5 unique words
    word_list.append(input("Enter a unique word: "))  # Using append to add each word to the list
    word_list.append(input("Enter another unique word: "))
    word_list.append(input("Enter another unique word: "))
    word_list.append(input("Enter another unique word: "))
    word_list.append(input("Enter the last unique word: "))

    return word_list

def display_word_lengths(word_list):
    """
    This function displays a list of word lengths.
    """
    # Create a new list where each index corresponds to the length of the word at that index
    length_list = [len(word) for word in word_list]

    # Display the list of word lengths
    print("List of word lengths:", length_list)

# Test case
user_words = get_user_input()
display_word_lengths(user_words)


#Lab_6-7

def get_user_input():
    """
    This function gets input from the user for 3 numeric values.
    """
    num_list = []  # empty list to store numeric values

    # Get input from the user for 3 numeric values
    num_list.append(float(input("Enter a numeric value: ")))  # Using float for decimal inputs
    num_list.append(float(input("Enter another numeric value: ")))
    num_list.append(float(input("Enter the last numeric value: ")))

    return num_list

def display_doubled_integers(num_list):
    """
    This function displays a list of doubled integer values.
    """
    # Create a new list where each value is represented as an integer that has been doubled
    doubled_int_list = [int(value * 2) for value in num_list]

    # Display the list of doubled integer values
    print("List of doubled integer values:", doubled_int_list)

# Test case
user_numbers = get_user_input()
display_doubled_integers(user_numbers)


#Lab_6-8

def get_user_input():
    """
    This function gets input from the user for 3 numeric values.
    """
    num_list = []  # Initialize an empty list to store numeric values

    # Get input from the user for 3 numeric values
    num_list.append(float(input("Enter a numeric value: ")))  # Using float to handle decimal inputs
    num_list.append(float(input("Enter another numeric value: ")))
    num_list.append(float(input("Enter the last numeric value: ")))

    return num_list

def display_number_classification(num_list):
    """
    This function determines and displays the nature of the numbers in the list.
    """
    # Check if all numbers in the list are even
    if all(num % 2 == 0 for num in num_list):
        print("even")
    # Check if all numbers in the list are odd
    elif all(num % 2 != 0 for num in num_list):
        print("odd")
    # If the numbers in the list are both even and odd
    else:
        print("mixed")

# Test case
user_numbers = get_user_input()
display_number_classification(user_numbers)






