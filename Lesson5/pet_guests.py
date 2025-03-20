class PetGuests:

    num_pet_guests = 0 # class variable

    def __init__(self,pet_info,owner_info):
        self.pet_info = pet_info
        self.owner_info = owner_info
        PetGuests.num_pet_guests += 1
        
    
    def check_in(self):
        print("Checked in")

    def check_out(self):
        print("Checked out")

    def guest_fed(self,time):
        print(f"Guest {self.name} fed at {time}")
