# Iterate a given list and check if a given element exists as a key’s value in a dictionary. Ifnot, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]

sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

#will modify the original list
roll_number[:]=[item for item in roll_number if item in sample_dict.values()]

print(roll_number)