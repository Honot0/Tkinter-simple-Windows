import tkinter as tk
from tkinter.ttk import Combobox
root = tk.Tk()
canvas = tk.Canvas(root ,height = 300, width = 800)
canvas.pack()
def buy():
    c1 = combo1.get()
    c2 = combo2.get()
    print("",c1,c2)
    pass

def nd():

    import subprocess
    subprocess.Popen("C:/Windows/system32/mspaint.exe")

combo1 = Combobox(canvas)
combo1['values'] = ['1',"22","333"]
combo1.current(0)
combo1.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.05)

combo2 = Combobox(canvas)
combo2['values'] = ['aaa',"bbb","ccc"]
combo2.current(2)
combo2.place(relx=0.1,rely=0.65,relwidth=0.8,relheight=0.05)

button3 = tk.Button(root, text = 'кнопка1', command =lambda: buy())
button3.place(relx=0.1,rely=0.9,relwidth=0.4,relheight=0.1)

button4 = tk.Button(root, text = 'кнопка2', command =lambda: nd())
button4.place(relx=0.5,rely=0.9,relwidth=0.4,relheight=0.1)

root.mainloop()
