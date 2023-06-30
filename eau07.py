##### Eau - Majuscule #####
# Créez un programme qui met en majuscule
# la première lettre de chaque mot d’une chaîne de caractères.
# Les autres lettres devront être en minuscules.
# Les mots ne sont délimités que par un espace,
# une tabulation ou un retour à la ligne.
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

def is_end_of_word(char):
    ascii_tab = 9
    ascii_new_line = 10
    ascii_space = 32

    return ord(char) == ascii_tab or ord(char) == ascii_new_line or ord(char) == ascii_space

def capitalize_each_word(string):
    char_index = 0
    capitalized_string = ""

    while(char_index < len(string)):
        if is_ascii_letter(string[char_index]):
            capitalized_string += string[char_index].upper()
            char_index += 1

            while(char_index < len(string) and not is_end_of_word(string[char_index])):
                capitalized_string += string[char_index].lower()
                char_index += 1
        
        else:
            capitalized_string += string[char_index]
            char_index += 1

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
capitalize_each_word_result = capitalize_each_word(string_input)

### Result ###
print(capitalize_each_word_result)
