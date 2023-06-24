##### Eau - String dans string #####
# Créez un programme qui détermine
# si une chaîne de caractère se trouve dans une autre.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def is_substring_in_string(string, substring):
    #return substring in string
    chr_index = 0
    substring_len = len(substring)
    for chr in string:
        if chr == substring[0] and string[chr_index:substring_len + chr_index] == substring:
            return True
        else:
            chr_index += 1
                                                              
    return False 

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("error: you need to enter (only) 2 arguments")
        exit()
    if sys.argv[1].strip('-').isdigit() or sys.argv[2].strip('-').isdigit():
        print("error: the 2 arguments needs to be strings")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]
substring_input = sys.argv[2]

### Problem Solving ###
is_substring_in_string_result = is_substring_in_string(string_input, substring_input)

### Result ###
print(is_substring_in_string_result)
