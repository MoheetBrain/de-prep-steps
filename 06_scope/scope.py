'''Its important that you dont move any lines in this file. Follow the commented instructions below to clarify your understanding of scope in Python :) '''

# 1.a. Uncomment line 8. What will the function print? 
def favorite_drink():
    drink = "Tea"
    print(drink)

favorite_drink()
# Tea

# 1.b. Uncomment line 12. What happens if we try to print the drink variable outside the function? Re-comment out when done. 

# print(drink)  
# NameError: name 'drink' is not defined (because 'drink' is local to the function)

# 2.a. Uncomment line 20. Predict what the shout_manager function will print?
name = "Jurgen Klopp"

def shout_manager():
    print(name + '!')

shout_manager()
# Jurgen Klopp!

# 2.b. Uncomment line 27. What will show when we print the name variable on line 29 after calling modify_manager?
def modify_manager():
    name = "Pep Guardiola"

modify_manager()
print(name + "!")
# Jurgen Klopp! (global 'name' unchanged by the function)

# 3. Uncomment line 36. What will the nintendo_function print?
character = "Mario"

def nintendo_function():
    character = "Sonic"
    print(character)

nintendo_function()
# Sonic

# 4. Uncomment line 50. What will the outer_function print?

fast_food = "McDonald's"

def outer_function():
    fast_food = "Burger King"
    
    def inner_function():
        print(fast_food)
    
    inner_function()

outer_function()
# Burger King

# 5. Sorry if you are starting to get hungry. Uncomment Line 61. The invocation of the increase_nuggets function will throw an error.
# Uncomment line 57 to fix the error. What will the function print?
chicken_nugget_count = 6

def increase_nuggets():
    global chicken_nugget_count
    chicken_nugget_count += 14
    print(f"{chicken_nugget_count} nuggets")

increase_nuggets()
# 20 nuggets

# 6. Uncomment lines 70 and 71. What will the numbers and i print statements output?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
print(i)
# [0, 1, 2, 3, 4]
# 4

# 6.b. How do comprehensions differ from the for loop above? Uncomment lines 76 and 77. What will be output by the print statements?
numbers = [j for j in range(5)]

print(numbers, "<< NUMBERS")
# print(j)
# [0, 1, 2, 3, 4] << NUMBERS
# NameError: name 'j' is not defined (j doesn't exist outside the comprehension)

# NICE JOB! You are done with this exercise. Great work! :)
# To see what your final output should look like, check the expected_scope_outputs.txt file.
