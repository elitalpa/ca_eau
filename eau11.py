##### Eau - Différence minimum absolue #####
# Créez un programme qui affiche la différence minimum absolue
# entre deux éléments d’un tableau constitué uniquement de nombres.
# Nombres négatifs acceptés.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def get_minimal_absolute_difference(args):
    index_a = 1
    index_b = 0
    difference_result = []
    absolute_difference = []
    sorted_args = sorted(args, key=int)

    while(index_a < len(sorted_args)):
        difference_result.append(int(sorted_args[index_a]) - int(sorted_args[index_b]))
        index_a += 1
        index_b += 1

    minimal_absolute_difference = difference_result[0]

    for number in difference_result:
        if number < 0:
            number = number * -1

        if number < minimal_absolute_difference:
            minimal_absolute_difference = number

    return minimal_absolute_difference

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("error: you need to enter at least 2 arguments")
        exit()
    for arg in sys.argv[1:]:
        if not arg.strip('-').isdigit():
            print("error: your arguments must be numbers")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
arguments = sys.argv[1:]

### Problem Solving ###
minimal_absolute_difference_result = get_minimal_absolute_difference(arguments)

### Result ###
print(minimal_absolute_difference_result)
