import turtle as tu
import tkinter as tk
root = tk.Tk()
def circle():
    tu.circle(50)
def square ():
    tu.forward(50) 
    tu.left(90) 
    tu.forward(50) 
    tu.left(90)
    tu.forward(50) 
    tu.left(90) 
    tu.forward(50) 
    tu.left(90) 
def triangle ():
    tu.forward(100)
    tu.left(120)
    tu.forward(100)
    tu.left(120)
    tu.forward(100)
def close():
    root.destroy()

btn = tk.Button(root, text="circle", command = circle).pack()
btn = tk.Button(root, text="square", command = square).pack()
btn = tk.Button(root, text="triangle", command = triangle).pack()
btn = tk.Button(root, text="close", command=close).pack()
root.mainloop()