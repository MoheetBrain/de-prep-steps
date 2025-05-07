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
# Jurgen Klopp! (global 'name' unchanged by the
