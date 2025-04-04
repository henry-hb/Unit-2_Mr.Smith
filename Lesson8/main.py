from car import Car # from module import class
from electric_car import ElectricCar as EC # alias - nickname ElectricCar as EC
import random

def main():
    my_leaf = EC("Nissan","Leaf",2024,60)
    print(my_leaf.make)

if __name__ == '__main__':
    main()