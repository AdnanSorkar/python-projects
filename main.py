distance = float(input("\nEnter distance driven (km): "))
fuel = float(input("Enter fuel used (liters): "))
price = float(input("Enter fuel price per liter: "))

if(fuel == 0):
    print("\nPlease refill fuel")

elif(fuel > 0):

    dis0 = distance / fuel
    fuel0 = (fuel / distance) * 100
    prc0 = (fuel * price) / distance

    dis1 = round(dis0, 2)
    fuel1 = round(fuel0, 2)
    prc1 = round(prc0, 2)
    
    print(f"\nDistance driven {dis1} km/L")
    print(f"Fuel used {fuel1} L/100 km")
    print(f"Fuel price {prc1} TK/km\n")

    if(dis1 >= 15):
        print("Efficient")
    elif(dis1 >= 10):
        print("Average")
    elif(dis1 < 0):
        print("Wrong value")
    elif(dis1 == 0):
        print("Car has malfunction")
    else:
        print("High use")
    
print()
