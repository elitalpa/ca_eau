##### Eau - Majuscule sur deux #####
# Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères.
# Seule les lettres (A-Z, a-z) sont prises en compte.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def is_ascii_letter(char):
    ascii_A = 65
    ascii_Z = 90
    ascii_a = 97
    ascii_z = 122

    return (ord(char) >= ascii_a and ord(char) <= ascii_z) or (ord(char) >= ascii_A and ord(char) <= ascii_Z)

def capitalize_alternate_letters(string):
    capitalized_string = ""
    counter = 0

    for char in string:
        if counter % 2 == 0 and is_ascii_letter(char):
            capitalized_string += char.upper()
            counter += 1
        elif (is_ascii_letter(char)):
            capitalized_string += char
            counter += 1
        else:
            capitalized_string += char

    return capitalized_string

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: Only one argument is allowed.")
        exit()
    if sys.argv[1].strip('-').isdigit():
        print("error: Please provide a string argument.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
capitalize_alternate_letters_result = capitalize_alternate_letters(string_input)

### Result ###
print(capitalize_alternate_letters_result)
