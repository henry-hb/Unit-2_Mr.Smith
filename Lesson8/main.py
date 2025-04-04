from car import Car
from electric_car import ElectricCar as EC #alias (nickname)
import random

def main():
    my_leaf = EC("Nissan", "Leaf", 2024,60)
    print(my_leaf.make)

if __name__ == "__main__":
    main()