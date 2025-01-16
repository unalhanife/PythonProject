class Vehicle:
    def __init__(self, merk, model, year):
        self.merk=merk
        self.model=model
        self.year=year

class OffRoadVehicle(Vehicle):
    def __init__(self, merk, model, year, four_wheel_drive):
        super().__init__(merk,model,year)
        self.four_wheel_drive=four_wheel_drive

class SportCar(Vehicle):
    def __init__(self,merk, model, year, max_speed):
        super().__init__(merk,model,year)
        self.max_speed=max_speed


orv= OffRoadVehicle("Jeep", "Wrangler", 2022, True)
sports_car=SportCar("Ferrari", "488", 2021, 330)

print(f"ORV (Off-Road Vehicle): Make={orv.merk}, Model={orv.model}, Year={orv.year}, Four-Wheel Drive={orv.four_wheel_drive}")
print(f"Sports Car: Make={sports_car.merk}, Model={sports_car.model}, Year={sports_car.year}, Max Speed={sports_car.max_speed} km/h")