##### Eau - Combinaisons de 2 nombres #####
# Créez un programme qui affiche toutes les différentes combinaisons
# de deux nombre entre 00 et 99 dans l’ordre croissant.

### Functions ###
def generate_combinations_of_2_numbers_ascending():
    iteration_count = 0
    digit_a = 0
    digit_b = 0
    digit_c = 0
    digit_d = 1
    valid_combinations = ""

    while(iteration_count < 9999):
        if digit_b == 9 and digit_c == 9 and digit_d == 9:
            digit_b = 0
            digit_c = 0
            digit_d = 0
            digit_a += 1
        elif digit_c == 9 and digit_d == 9:
            digit_c = 0
            digit_d = 0
            digit_b += 1
        elif digit_d == 9:
            digit_d = 0
            digit_c += 1
        else:
            digit_d += 1
        
        if int(f"{digit_a}{digit_b}") < int(f"{digit_c}{digit_d}"):
            valid_combinations += f"{digit_a}{digit_b} {digit_c}{digit_d}, "
        
        iteration_count += 1

    return valid_combinations[:-2]

### Error Handling ###

### Parsing ###

### Problem Solving ###
combinations_of_2_numbers_ascending = get_combinations_of_2_numbers_ascending()

### Result ###
print(combinations_of_2_numbers_ascending)
