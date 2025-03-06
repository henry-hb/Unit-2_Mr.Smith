"""
Name: Mr. Smith
Date: 3/4/25
Description: Very basic car class
"""


class Car:
    """
    A simple attempt to represent a car
    """

    def __init__(self, make: str, model: str, year: int):
        """Constructor

        Args:
            make (str): Make of car
            model (str): Model of car
            year (int): Year the car was made
        """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self) -> str:
        """Returns a nicely formatted description of the car

        Returns:
            str: description of the car formatted in title case
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


def main():
    my_new_car = Car("audi", "a4", 2025)
    print(my_new_car.get_descriptive_name())
    my_new_car.year = 2026
    my_new_car.make = "Rivian"
    my_new_car.model = "R3X"
    print(my_new_car.get_descriptive_name())


if __name__ == "__main__":
    main()
