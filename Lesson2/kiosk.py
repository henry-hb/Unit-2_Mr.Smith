class Kiosk:
    def __init__(self):
        self.transcation_total = 0
        self.item_total = 0
        self.items_ = {}
        self.payment = 0
        self.change = 0
    
    def add_item(self,item:str,price:float):
        self.item_total += 1
        self.transcation_total += price
        if item not in self.items_.keys():
            self.items_[item] = []
        self.items_[item].append(price)
    
    def get_total_cost(self):
        return(f"${self.transcation_total:.2f}")
    
    def get_total_items(self):
        if self.item_total == 1:
            return(f"{self.item_total} item")
        else:
            return(f"{self.item_total} items")

    
    def take_payment(self):
        print(f"Your total is ${self.transcation_total:.2f}.\n\
Please enter your payment amount.")
        try:
            self.payment = float(input("> "))
            if self.payment <= 0:
                print("Invalid amount")
            if self.payment <= self.transcation_total:
                print("You need to enter more money")
        except ValueError:
            print("Invalid")
        
    def give_change(self):
        self.change = self.payment - self.transcation_total
    
    def finalize_transcation(self):
        self.take_payment()
        self.give_change()
    
    def print_receipt(self,):
        print("Smith Supercenter".center(39,'-'))
        print()
        for item,prices in self.items_.items():
            # print(f"{item}\t")
            for price in prices:
                print(f"{item}\t${price:.2f}")
        print("-"*20)
        print(f"Total items: {self.item_total}")
        print(f"Balance: {self.get_total_cost()}")
        print()
        print(f"Cash: ${self.payment:.2f}")
        print(f"Change: ${self.change:.2f}")
            
            
        
def main():
    self_checkout1 = Kiosk()
    while True:
        print("Add an item or enter q to quit")
        item = input("> ")
        if item.lower() == 'q':
            break
        print("What is the price of this item?")
        price = float(input("> "))
        self_checkout1.add_item(item,price)
    self_checkout1.finalize_transcation()
    self_checkout1.print_receipt()
    

if __name__ == '__main__':
    main()