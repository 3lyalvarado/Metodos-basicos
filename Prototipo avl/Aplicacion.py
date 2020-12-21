import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="GRUPO 11 EDD ARVOL AVL")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        
        self.login()
        self.labelframe2=ttk.LabelFrame(self.ventana1, text="Operaciones")        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        
        self.operaciones()
        self.ventana1.mainloop()

    def login(self):
        self.label1=ttk.Label(self.labelframe1, text="Eliezer Abraham Zapeta Alvarado - 201801719")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Carlos Vivar")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1, show="*")
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Ingresar")
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        None

        ## SEGUNDA LINEA 

    

aplicacion1=Aplicacion()