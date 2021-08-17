import tkinter as tk
from tkinter.ttk import Combobox
root = tk.Tk()
canvas = tk.Canvas(root ,height = 500, width = 1000)
canvas.pack()
def buy():
    c1 = combo1.get()
    print("",c1)
    pass
combo1 = Combobox(canvas)
combo1['values'] = ["1","22","333"]
combo1.current(0)
combo1.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.05)
button3 = tk.Button(root, text = 'Кнопка', command =lambda: buy())
button3.place(relx=0.1,rely=0.9,relwidth=0.8,relheight=0.1)
root.mainloop()