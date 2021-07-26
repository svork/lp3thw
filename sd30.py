# Variables
people = 21
cars = 19
trucks = 102


# Boolean logic
if cars > people or trucks >= cars:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")

if trucks > cars or not people > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks and cars < trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
