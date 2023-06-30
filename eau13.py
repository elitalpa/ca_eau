##### Eau - Tri par sélection #####
# Créez un programme qui trie une liste de nombres.
# Votre programme devra implémenter l’algorithme du tri par sélection.
#
# Vous utiliserez une fonction de cette forme (selon votre langage) :
## my_select_sort(array) {
##     # votre algorithme
##     return (new_array)
##     }
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.
# Wikipedia vous présentera une belle description de cet algorithme de tri.

import sys

### Functions ###
def my_select_sort(array):
    new_array = [int(element) for element in array]

    for unsorted_index in range(len(new_array)):
        current_min_index = unsorted_index

        for current_item_index in range(current_min_index + 1, len(new_array)):
            if new_array[current_min_index] > new_array[current_item_index]:
                current_min_index = current_item_index
                
        new_array[unsorted_index], new_array[current_min_index] = new_array[current_min_index], new_array[unsorted_index]

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
my_select_sort_result = my_select_sort(array_input)

### Result ###
print(' '.join([str(element) for element in my_select_sort_result]))
