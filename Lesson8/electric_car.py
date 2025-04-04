from car import Car

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity
        self.battery_charge = 0

    def fill_gas_tank(self,amount):
        print("Electric cars don't have gas tanks")
        print("Charging your car instead...")
        self.charge_car(amount)
    
    def charge_car(self,amount):
        self.battery_charge += amount