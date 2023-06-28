##### Eau - Par ordre Ascii #####
# Créez un programme qui trie les éléments donnés en argument par ordre ASCII.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def select_sort_ascii_order(array):
    new_array = array[:]

    for unsorted_index in range(len(new_array)):
        current_min_index = unsorted_index

        for current_item_index in range(current_min_index + 1, len(new_array)):
            if ord(new_array[current_min_index][0]) > ord(new_array[current_item_index][0]):
                current_min_index = current_item_index
                
        new_array[unsorted_index], new_array[current_min_index] = new_array[current_min_index], new_array[unsorted_index]

    return new_array

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("error: you need to enter at least 2 arguments")
        exit()
    for arg in sys.argv[1:]:
        if arg.strip('-').isdigit():
            print("error: your arguments must be strings")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
array_input = sys.argv[1:]

### Problem Solving ###
ascii_order_result = select_sort_ascii_order(array_input)

### Result ###
print(' '.join([str(element) for element in ascii_order_result]))