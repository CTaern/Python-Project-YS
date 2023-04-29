meal_cost = float(input("Enter your cost of meal: "))
meal_tax = float(input("Enter your tax percentage: "))
meal_tip = float(input("Enter your tip percentage: "))

meal_tax_cost = ( meal_cost / 100 ) * meal_tax

meal_tip_cost = ( meal_cost / 100 ) * meal_tip

total_cost = meal_cost + meal_tax_cost + meal_tip_cost

print("Meal    :", meal_cost)
print("Tax     :", meal_tax_cost)
print("Tip     :", meal_tip_cost)

print("Total   :", total_cost)
