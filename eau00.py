##### Eau - Combinaisons de 3 chiffres #####
# Créez un programme qui affiche
# toutes les différentes combinaisons possibles de trois chiffres
# dans l’ordre croissant, dans l’ordre croissant.
# La répétition est volontaire.
#
# 987 n’est pas là parce que 789 est présent.
# 020 n’est pas là parce que 0 apparaît deux fois.
# 021 n’est pas là parce que 012 est présent.
# 000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.

### Functions ###
def generate_combinations_of_3_digits():
    iteration_count = 0
    digit_a = 0
    digit_b = 0
    digit_c = 1
    #all_combinations = ""
    valid_combinations = ""

    while(iteration_count < 999):
        #all_combinations += f"{digit_a}{digit_b}{digit_c}\n"
        
        if digit_a < digit_b < digit_c:
            valid_combinations += f"{digit_a}{digit_b}{digit_c}, "
        
        iteration_count += 1

        if digit_a == 9 and digit_b == 9 and digit_c == 9:
            break
        elif digit_b == 9 and digit_c == 9:
            digit_b = 0
            digit_c = 0
            digit_a += 1
        elif digit_c == 9:
            digit_c = 0
            digit_b += 1
        else:
            digit_c += 1

    return valid_combinations[:-2]

### Error Handling ###

### Parsing ###

### Problem Solving ###
combinations_of_3_digits_result = generate_combinations_of_3_digits()

### Result ###
print(combinations_of_3_digits_result)
