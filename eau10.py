##### Eau - Index wanted #####
# Créez un programme qui affiche
# le premier index d’un élément recherché dans un tableau.
# Le tableau est constitué de tous les arguments sauf le dernier.
# L’élément recherché est le dernier argument.
#
# Afficher -1 si l’élément n’est pas trouvé.
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def find_index(arguments, searched_argument):
    arg_index = 0

    for arg in arguments:
        if arg == searched_argument:
            return arg_index

        arg_index += 1

    return -1

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("error: At least 2 arguments must be provided.")
        exit()
    for arg in sys.argv[1:]:
        if arg.strip('-').isdigit():
            print("error: Your arguments must be strings.")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
arguments_input = sys.argv[1:-1]
searched_argument_input = sys.argv[-1]

### Problem Solving ###
find_index_result = find_index(arguments_input, searched_argument_input)

### Result ###
print(find_index_result)
