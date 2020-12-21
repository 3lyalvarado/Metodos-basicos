import tkinter as tk
from PIL import Image
from tkinter import ttk
from graphviz import render
import time

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=700, height=500, background="black")      
        self.canvas1.grid(column=0, row=0)
        nombre = "NombreArchivo"                           
        render('dot', 'png', f'{nombre}.dot')                    
        f = Image.open("NombreArchivo"+'.dot.png')
        f'{nombre}.png'
        time.sleep(3)
        archi1=tk.PhotoImage(file=f"{NombreArchivo sin}"+".dot.png")
        self.canvas1.create_image(0, 0, image=archi1, anchor="nw")
        self.ventana1.mainloop()
aplicacion1=Aplicacion()
 

