##### Eau - Paramètres à l’envers #####
# Créez un programme qui affiche ses arguments reçus à l’envers.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def reverse_lines_of_arguments(arguments):
    reversed_lines = ""
    for argument_index in range(1, len(arguments) + 1):
        reversed_lines += f"{arguments[-argument_index]}\n"

    return reversed_lines[:-1]

def handle_argument_errors():
    if len(sys.argv) < 2:
        print("error: no arguments were entered")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
arguments_input = sys.argv[1:]

### Problem Solving ###
reversed_lines_of_arguments_result = reverse_lines_of_arguments(arguments_input)

### Result ###
print(reversed_lines_of_arguments_result)
