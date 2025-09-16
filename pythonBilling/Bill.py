# importing libraries
import tkinter as tk


WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X//2


def genrate_bill():
     bill_text = ""
     for i in LABLES:
          a =  LABLES[i][2].get()
          print(a)
          qty = None
          if str(a).strip().isdigit():
               qty = int(str(LABLES[i][2].get()).strip())
               qty = qty or 0

               total += LABLES[i][1] * qty
          bill_text += f'{i} :₹ {LABLES[i][1]} X {qty} = {LABLES[i][1]* qty} \n'
          
          bill_text += f"Total bill is ₹ {total}"
          print(bill_text)
   

# creating a window 
root = tk.Tk()


#####################################
########### root functions ##########
#####################################
# resizing window
root.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}")

# changing title
root.title("Billing System")

# no resizing
root.resizable(True, False)

SOFTWARE_TITLE = "BILLING SYSTEM"
myTitle = tk.Label(text=SOFTWARE_TITLE)
myTitle.place(x=center - (len(SOFTWARE_TITLE)*6//2), y=20)



LABLES = {}

Namkeen = tk.Label(text = "Namkeen", font=("arial" , 12, "bold" ))
Q_Namkeen = tk.Entry()
LABLES["Namkeen"] = [Namkeen,50, Q_Namkeen ]



SoftDrink = tk.Label(text = "SoftDrink", font=("arial" , 12, "bold" ))
Q_SoftDrink = tk.Entry()
LABLES["SoftDrink"] = [SoftDrink,90, Q_SoftDrink]



Chips = tk.Label(text = "Chips", font=("arial" , 12, "bold" ))
Q_Chips = tk.Entry()
LABLES["Chips"] = [Chips,50, Q_Chips]




Chocolate = tk.Label(text = "Chocolate", font=("arial" , 12, "bold" ))
Q_Chocolate = tk.Entry()
LABLES["Chocolate"] = [Chocolate,100, Q_Chocolate]



Toothpaste = tk.Label(text = "Toothpaste", font=("arial" , 12, "bold" ))
Q_Toothpaste = tk.Entry()
LABLES["Toothpaste"] = [Toothpaste,200, Q_Toothpaste]


B_Total = tk.Button(text="Calculate Bill", font =("arial", 12), command = genrate_bill)
B_Total.place(x= 250 , y = 250)



Lable_position_x = 12
Lable_position_y = 50
increment = 0

for i in LABLES:
     #print(LABLES[i])
     # LABLES have Lable object 
     # 

     # placing the lables at position according to x and y axis
     LABLES[i][0].place(x=Lable_position_x , y=Lable_position_y + increment)
     # placing the price at position according to x and y
     tk.Label(text=f"₹ {LABLES[i][1]}", font=("arial, 10")).place (x=Lable_position_x + 150, y=Lable_position_y + increment)
     # placing the Entry at the position according to x and y
     LABLES[i][2].place (x=Lable_position_x + 250, y=Lable_position_y + increment)
     # placing every item after 30 pixels below the preceding
     increment += 30



# running the window
root.mainloop()