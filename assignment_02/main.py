from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV123", 60)
motorbike = Motorbike("Honda", "CBR500", "MB456", 500)


# Create a renter
renter = Renter("John", 12345)

print("=== Renter ===")
print("Name:", renter.name)
print("License:", renter.license_no)
print("Rented vehicles:", renter.rented)


# Rent and return a vehicle
print("\n=== Rent and Return ===")

print("Before renting:")
print(car)

car.rent()

print("After renting:")
print(car)

car.return_vehicle()

print("After returning:")
print(car)


# Test invalid renter information
print("\n=== Invalid Renter Tests ===")

try:
    Renter("", 12345)
except ValueError as e:
    print("Caught ValueError:", e)

try:
    Renter("Alice", 0)
except ValueError as e:
    print("Caught ValueError:", e)


# Test inheritance and polymorphism
print("\n=== Polymorphism ===")

vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)