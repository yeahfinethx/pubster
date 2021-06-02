import random

pubname_list_a = ["Red", "Golden", "Iron", "Silver", "King’s", "White", "Royal", "Black", "Hare &", "George &", "Rose &"]
pubname_list_b = ["Lion", "Horse", "Lamb", "Arms", "Hart", "Fox", "Crown", "Plough", "Swan", "Oak", "Bell", "Anchor"]

pubname_beg = random.choice(pubname_list_a)
pubname_end = random.choice(pubname_list_b)

print("The " + pubname_beg + " " + pubname_end)