#greatings
print("Hello, Welcome to Asanka Hotel")

#cost of food for user
Foodcost = float(input("Charge for food: $"))

#calculate Tip 
tip_food = round(0.18 * Foodcost, 2)
print(f"Tip = ${tip_food}")

#calculate tax
tax_food = round(0.07 * Foodcost, 2)
print(f"Sales tax = ${tax_food}")

#calculate total cost
Total_amount = Foodcost + tip_food + tax_food
print(f"Total Amount = ${Total_amount}")


