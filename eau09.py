##### Eau - Entre min et max #####
# Créez un programme qui affiche toutes les valeurs comprises
# entre deux nombres dans l’ordre croissant.
# Min inclus, max exclus.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def ascending_range(number_a, number_b):
    number_a_int, number_b_int = int(number_a), int(number_b)

    if number_a_int < number_b_int:
        min_int, max_int = number_a_int, number_b_int
    else:
        min_int, max_int = number_b_int, number_a_int

    number = min_int
    range_str = ""

    while(number < max_int):
        range_str += str(number) + " "
        number += 1

    return range_str[:-1]

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("error: Only 2 arguments are allowed.")
        exit()
    if not sys.argv[1].strip('-').isdigit() or not sys.argv[2].strip('-').isdigit():
        print("error: Please provide 2 numbers.")
        exit()
    if sys.argv[1] == sys.argv[2]:
        print("error: Both arguments are identical.")

### Error Handling ###
handle_argument_errors()

### Parsing ###
number_a_input, number_b_input = sys.argv[1], sys.argv[2]

### Problem Solving ###
ascending_range_result = ascending_range(number_a_input, number_b_input)

### Result ###
print(ascending_range_result)
