#code_challenge3.py

#input

print("_____________________________________\n")
send_name = input("Enter Name ---> ")
type_of_item = input("Type of Item ---> ")
is_Fragile = bool(input("Fragile(True/False)? ---> "))
weight = float(input("Weight (in kg) ---> "))
distance = float(input("Distance (in km) ---- > "))
is_Express = bool(input("Express(True/False)? ---> "))
is_International = bool(input("International(True/False)? ---> "))

#calculationg base cost

base_cost = (weight * 2.5) + (distance * 0.15)

#free shipping

if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
	total = 0

#internaional express
elif is_International and is_Express:
	total = (base_cost * 1.40) + 50

#express or heavy international
elif weight > 20 and is_Express or is_International:
	total = (base_cost * 1.20) + 25

#oversized
elif distance > 1000 or weight > 30:
	total = (base_cost) + 30
else:
	total = base_cost

shipping_fee = total - base_cost

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
print("The total shipping cost is: ", shipping_fee)
print("_____________________________________")

