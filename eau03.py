##### Eau - Suite de Fibonacci #####
# Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci.
# (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.
#
# Afficher -1 si le paramètre est négatif ou mauvais.
#
# Définition: La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent.

import sys

### Functions ###
def get_fibonacci_number(fibonacci_index):
    fibonacci_sequence_list = [0, 1]
    fibonacci_index_int = int(fibonacci_index)
    for number_index in range(2, fibonacci_index_int + 1):
        next_fibonacci_number = fibonacci_sequence_list[number_index - 2] + fibonacci_sequence_list[number_index - 1]
        fibonacci_sequence_list.append(next_fibonacci_number)

    return fibonacci_sequence_list[fibonacci_index_int]

def handle_argument_errors():
    if len(sys.argv) != 2:
        print(-1)
        print("error: only one argument can be entered")
        exit()
    if not sys.argv[1].isdigit():
        print(-1)
        print("error: only a positive integer number can be accepted")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
fibonacci_index_input = sys.argv[1]

### Problem Solving ###
fibonacci_number_result = get_fibonacci_number(fibonacci_index_input)

### Result ###
print(fibonacci_number_result)
