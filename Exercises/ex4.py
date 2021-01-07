cars = 100 #tells the computer number of cars
space_in_a_car = 4 #tells the computer space per car
drivers = 30 #tells the computer number of drivers
passengers = 90 #tells the computer number of passengers
cars_not_driven = cars - drivers #tells the computer equation to work out number of cars not driven
cars_driven = drivers #tells the computer equation to work out number of cars driven
carpool_capacity = cars_driven * space_in_a_car #tells the computer equation to work out carpool_capacity
average_passengers_per_car = passengers / cars_driven #tells the computer equation to work out average passenger per car

#prints texts and relevant numbers related to each text
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
