import random  
from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(bg="#212120")
root.geometry("600x750")
root.resizable(False, False)
root.title("Генератор паролей")
root.iconbitmap(default="B:\Projects\PYTHON\password_gen\img\icon.ico")



label_start = ttk.Label(text="Приветствую, давайте начнем работу", font=("Arial", 14),
                    foreground="#ffffff",
                    background="#212120"
                    ) 
label_start.place(x=110, y=25)

lower = "abcdefghijklmnopqrstuvwxyz"  
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
symb = "!@#$%^&*" 
numbers = "0123456789"  
 

#together = lower + upper + numbers + symb  
#length = int(input('Enter length of password: ')) 
#password = "".join(random.sample(together, length))  
#print(password)  

root.mainloop()