##### Eau - Prochain nombre premier #####
# Créez un programme qui affiche le premier
# nombre premier supérieur au nombre donné en argument.
#
# Afficher -1 si le paramètre est négatif ou mauvais.

import sys

### Functions ###
def is_prime_number(number):
    number_int = int(number)

    for divisor in range(2, number_int - 1):
        if number_int % divisor == 0 :
            return False

    return True

def get_next_prime_number(number):
    number_int = int(number)
    next_number = number_int + 1

    if number_int == 0 or number_int == 1:
        next_prime_number = 2
        return next_prime_number

    while(is_prime_number(next_number) is False):
        next_number += 1

    next_prime_number = next_number
    return next_prime_number

def handle_argument_errors():
    if len(sys.argv) != 2:
        print(-1)
        print("error: Only one argument is allowed.")
        exit()
    if not sys.argv[1].isdigit():
        print(-1)
        print("error: Please provide a positive integer number.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
next_prime_number_result = get_next_prime_number(number_input)

### Result ###
print(next_prime_number_result)
