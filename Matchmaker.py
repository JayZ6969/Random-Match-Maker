import random

# Read file contents
with open('C:\\1.txt', 'r') as file1:
    set1 = file1.read().splitlines()

with open('C:\\2.txt', 'r') as file2:
    set2 = file2.read().splitlines()

# Shuffle the second set to ensure randomness
random.shuffle(set2)

# Match strings
matches = {} #dict
for string1 in set1:
    if set2:
        string2 = set2.pop()
        matches[string1] = string2
    else:
        break

# Print the matches
for string1, string2 in matches.items():

    print("%s is matched with %s ! " %(string1, string2))
