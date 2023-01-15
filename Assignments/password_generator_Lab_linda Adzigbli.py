"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""
####################################################################################################
######################## DO NOT CHANGE THIS SECTION OF THE CODE ####################################
# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)

all_digits = list(string.digits)

all_symbols = list(string.punctuation)

#########################################################################################################



####################################### TYPE YOU CODE IN HERE! ##########################################
# Ask user for how many letters they would like in their password and cast to integer and store as no_of_letters
no_of_letters = int(input("How many letters would you like in your password? "))

# Ask user for how many symbols they would like in their password and cast to integer and store as no_of_symbols
no_of_symbols = int(input("How many symbols would you like in your password? "))

# Ask user for how many digits they would like in their password and cast to integer and store as no_of_digits
no_of_digits = int(input("How many numbers would you like in your password? "))

# Set Accumulator for Password Characters List
password_character_list = []

# Get the random letter for the password
# Randomly Select the characters
for number in range(no_of_letters):
#       select a random characer from list of alphabets and append to the password characters list 
    random_letter = random.choice(all_alphabets)
    password_character_list.append(random_letter)

print(password_character_list)


# Get the Random Symbols for the password symbols

# Set Accumulator for the Number of Symbols List
password_symbols_list = []

# Randomly Select the characters
for number in range(no_of_symbols):
#       select a random symbol from list of symbols and append to the password symbols list 
    random_symbol = random.choice(all_symbols)
    password_symbols_list.append(random_symbol)

print(password_symbols_list)

# Get the Random Digits for the password

# Set Accumulator for the Number of Digits List
password_digits_list = []

# Randomly Select the characters
for number in range(no_of_digits):
#       select a random digit from list of digits and append to the password digits list 
    random_digit = random.choice(all_digits)
    password_digits_list.append(random_digit)

print(password_digits_list)

# Add the lists to get the final_password_list and shuffle the final_password_list
final_password_list = password_character_list + password_symbols_list + password_digits_list

# To shuffle, items in a list https://www.w3schools.com/python/ref_random_shuffle.asp 
random.shuffle(final_password_list)

# Now that we have our password in a list lets change that to a string then print it
string_password = "".join(final_password_list)

# accumulator for string_password
string_password = ''

for character in final_password_list:
#       append the character to the string_password
     string_password += ''+ character
# Print the string password
print('Here is your password: '+ string_password)
