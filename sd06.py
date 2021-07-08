# Assign a string to a variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# Assign a formatted string to a variable
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Another way of formatting strings
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Concatenating strings
print(w + e)
