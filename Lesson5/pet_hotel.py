from pet_guests import PetGuests
def main():
    Millie = PetGuests(["Millie"],["Mr. Smith"])
    Millie.check_in()
    print(PetGuests.num_pet_guests)
    print(Millie.num_guests)
    Winston = PetGuests(["Wiston"],["Mr. Smith"])
    Winston.check_in()
    print(Winston.num_guests)
    print(PetGuests.num_pet_guests)

if __name__ == '__main__':
    main()