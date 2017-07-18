cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capasity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print ("There are", cars, "cars availeble")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty cars today")
print ("We can transport", carpool_capasity, "people today")
print ("We have", passengers, "the carloop today")
print ("we need to put about", average_passenger_per_car, "in each car")
