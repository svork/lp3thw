# How many cars
cars = 100

# Space per each car
space_in_a_car = 4.0

# How many drivers
drivers = 30

# Amount of passengers
passengers = 90

# Cars sitting idle
cars_not_driven = cars - drivers

# Cars being driven
cars_driven = drivers

# Ride sharing
carpool_capacity = cars_driven * space_in_a_car

# Average people in a car
average_passengers_per_car = passengers / cars_driven


# Show the details and the data
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
