##### Eau - Tri à bulle #####
# Créez un programme qui trie une liste de nombres.
# Votre programme devra implémenter l’algorithme du tri à bulle.
#
# Vous utiliserez une fonction de cette forme (selon votre langage) :
## my_bubble_sort(array) {
##     # votre algorithme
##     return (new_array)
## }
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.
# Wikipedia vous présentera une belle description de cet algorithme de tri.

import sys

### Functions ###
def my_bubble_sort(array):
    new_array = [int(element) for element in array]

    for sorted_limit_index in range(len(new_array)):
        for comparison_index in range(len(new_array) - sorted_limit_index - 1):
            if new_array[comparison_index] > new_array[comparison_index + 1]:
                new_array[comparison_index], new_array[comparison_index + 1] = new_array[comparison_index + 1], new_array[comparison_index]

    return new_array

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("error: At least 2 arguments must be provided.")
        exit()
    for arg in sys.argv[1:]:
        if not arg.strip('-').isdigit():
            print("error: Your arguments must be numbers.")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
array_input = sys.argv[1:]

### Problem Solving ###
my_bubble_sort_result = my_bubble_sort(array_input)

### Result ###
print(' '.join([str(element) for element in my_bubble_sort_result]))
