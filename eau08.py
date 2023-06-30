##### Eau - Chiffres only #####
# Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def is_digit(char):
    ascii_0 = 48
    ascii_9 = 57

    return ord(char) >= ascii_0 and ord(char) <= ascii_9

def is_only_digits(string):
    for char in string:
        if not is_digit(char):
            return False
    
    return True

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: You must provide 1 argument.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
is_only_digits_result = is_only_digits(string_input)

### Result ###
print(is_only_digits_result)
