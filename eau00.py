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
def generate_combinations_of_3_digits_ascending():
    valid_combinations = []

    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i < j < k:
                    valid_combinations.append(f"{i}{j}{k}")

    return valid_combinations

### Error Handling ###

### Parsing ###

### Problem Solving ###
combinations_of_3_digits_ascending_result = ', '.join(generate_combinations_of_3_digits_ascending())

### Result ###
print(combinations_of_3_digits_ascending_result)
