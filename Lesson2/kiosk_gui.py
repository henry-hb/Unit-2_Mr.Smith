import tkinter as tk
import kiosk

def main():
    my_kiosk = kiosk.Kiosk()
    
    root = tk.Tk()
    root.title("Self Service Checkout Kiosk")
    root.geometry('640x480+300+300') # +300+300 sets the position of the window on the screen 
                                     # in this case, 300 pixels from the top and 300 pixels from the left
    root.resizable(False, False)
    
    button = tk.Button(root,text="Add item",command=my_kiosk.add_item("bread",5.35))
    button.grid(row=5,column=3) #puts button on window
    
    root.mainloop()
    
    print(my_kiosk.get_total_cost())
    
    
if __name__ == '__main__':
    main()
