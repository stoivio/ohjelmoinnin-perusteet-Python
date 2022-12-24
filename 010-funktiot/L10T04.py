def calc_consumption(lenght_km, price, consumption):
    fuel_spent = lenght_km * (consumption / 100)
    cost = price * fuel_spent
    return fuel_spent, cost


trip_lenght_km = float(input("Enter trip lenght in km: "))
fuel_price = float(input("Enter fuel price/liter: "))
fuel_consumption = float(input("Enter fuel consumption per 100km: "))

fuel, cost = calc_consumption(trip_lenght_km, fuel_price, fuel_consumption)
print("Fuel: ", round(fuel, 2), "liters")
print("Cost: ", round(cost, 2), "€")
