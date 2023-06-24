##### Eau - Majuscule sur deux #####
# Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères.
# Seule les lettres (A-Z, a-z) sont prises en compte.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def capitalize_alternate_letters(string):
    A_letter = 65
    Z_letter = 90
    a_letter = 97
    z_letter = 122
    capitalized_string = ""
    counter = 0
    for char in string:
        if counter % 2 == 0 and (ord(char) >= a_letter and ord(char) <= z_letter) or (ord(char) >= A_letter and ord(char) <= Z_letter):
            capitalized_string += char.upper()
            counter += 1
        elif (ord(char) >= a_letter and ord(char) <= z_letter) or (ord(char) >= A_letter and ord(char) <= Z_letter):
            capitalized_string += char.lower()
            counter += 1
        else:
            capitalized_string += char

    return capitalized_string

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: you need to enter (only) 1 argument")
        exit()
    if sys.argv[1].strip('-').isdigit():
        print("error: the argument is not a string")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
capitalize_alternate_letters_result = capitalize_alternate_letters(string_input)

### Result ###
print(capitalize_alternate_letters_result)
