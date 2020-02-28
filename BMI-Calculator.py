from tkinter import *

root = Tk()
root.geometry("350x250")

root.title("BMI Calculator")

def calculate():
    gather_f = feet_e.get()
    gather_i = inches_e.get()
    gather_w = weight_e.get()
    try:
        calculation = float(gather_f) * 12 + float(gather_i)
        calculation1 = 703 * float(gather_w)
        calculation2 = float(calculation) * float(calculation)
        answer = float(calculation1) // float(calculation2)
        BMI = Label(root, text = "BMI: " + str(answer), padx = 10, pady = 10, font = ("Ariel", 10))
        BMI.grid(row = 3, column = 0)
    except ValueError:
        error = Label(root, text = "Please enter a number instead of a letter")
        error.grid(row = 4, column = 1)
    #BMI.grid(row = 3, column = 0)

feet = Label(root, text = "Feet", padx = 20, pady = 20)
inches = Label(root, text = "Inches", padx = 20, pady = 20)
feet_e = Entry(root)
inches_e = Entry(root)
weight = Label(root, text = "Weight", padx = 20, pady = 20)
weight_e = Entry(root)
result = Button(root, text = "Calculate", command = calculate)

feet.grid(row = 0, column = 0)
inches.grid(row = 1, column = 0)
feet_e.grid(row = 0, column = 1)
inches_e.grid(row = 1, column = 1)
weight.grid(row = 2, column = 0)
weight_e.grid(row = 2, column = 1)
result.grid(row = 2, column = 2)

root.mainloop()