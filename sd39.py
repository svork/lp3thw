# d&d inspired character sheet
char1 = {
    "name": "Adaon",
    "class": "Rogue",
    "alignment": "Chaotic Good",
    "level": "20",
    "armor_class": 99,
    "constituion": 5,
    "dexterity": 20,
    "strength": 8,
    "intelligence": 15,
    "main_skill": "Stab",
    "luck": "Medium"
}

# Testing dictionaries' functions
print(char1.items())

# Trying to get values from a dictionaries
# these should work
print(char1["name"])
print(char1["class"])

# This, should not
# print(char1["nope"])

# this one, does work
print(char1.get("alignment", "Chaotic Neutral"))
