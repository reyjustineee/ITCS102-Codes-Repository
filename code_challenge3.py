#code_challenge3.py

#input

print("_____________________________________")
send_name = input("Enter Name ---> ")
type_of_item = input("Type of Item ---> ")
is_Fragile = bool(input("Fragile?(Enter \"Yes\" of yes, enter \"No\" if no) ---> ") == "Yes")
weight = float(input("Weight (in kg) ---> "))
distance = float(input("Distance (in km) ---- > "))
is_Express = bool(input("Express (Enter \"Yes\" of yes, enter \"No\" if no) ---> ") == "Yes")
is_International = bool(input("International (Enter \"Yes\" of yes, enter \"No\" if no) ---> ") == "Yes")

#calculation

base_cost = (weight * 2.5) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
	total = 0

elif is_International and is_Express:
	total = (base_cost * 1.4) + 50

elif (is_Express or is_International) and weight > 20:
	total = (base_cost * 1.2) + 25

elif weight > 30 or distance > 1000:
	total = base_cost + 30
else:
	total = base_cost

print("_____________________________________\n")
print("COMPANY")
print("NAME: ", send_name)
print("ITEM: ", type_of_item)
print("FRAGILE: ", is_Fragile)
print("WEIGHT: ", weight)
print("DISTANCE: ", distance)
print("EXPRESS: ", is_Express)
print("INTERNATIONAL: ", is_International)
print("\nTOTAL: ", total)
print("_____________________________________")

