"""
Name: Mr. Smith
Date: 3/4/25
Description: A car with an odometer
"""


class Car:
    """
    A simple attempt to represent a car
    """

    def __init__(self, make: str, model: str, year: int):
        """Constructor. Odometer is set to 0 for all new cars

        Args:
            make (str): Make of car
            model (str): Model of car
            year (int): Year the car was made
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self) -> str:
        """Returns a nicely formatted description of the car

        Returns:
            str: description of the car formatted in title case
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """Prints the number of miles on the car"""

        print(f"This car has {self.odometer} miles on it")

    def update_odometer(self, mileage: int) -> None:
        """Update the odometer to any value greater than its current reading

        Args:
            mileage (int): _description_
        """
        if mileage >= self.odometer:
            old_mileage = self.odometer
            self.odometer = mileage
            print(f"The odometer was updated from {old_mileage} to {mileage}.")
        else:
            print("You cannot roll back an odometer")

    def increment_odometer(self, miles: int) -> None:
        """Increment the odeometer by a positive amount of miles

        Args:
            miles (int): number of miles to increase the odometer by
        """
        if miles >= 0:
            self.odometer += miles
        else:
            print("You cannot rollback an odometer")


            print("You cannot rollback an odometer")
        
 
def main():
    my_new_car = Car("audi", "a4", 2025)
    print(my_new_car.get_descriptive_name())
    my_new_car.update_odometer(100)
    my_new_car.update_odometer(50)
    my_new_car.increment_odometer(25)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(-20)
    my_new_car.read_odometer()


if __name__ == "__main__":
    main()
