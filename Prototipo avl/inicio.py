from pruebas import *

class Table:
    def __init__(self):
        #database, table, columns
         #database, table, id, columnNumber, value
          #database, tableName, id
           #database, tableName
            #database, table, id
        self.database = None  # Nombre db 
        self.table = None # Nombre Tbl
        self.columns = None # Numero Col
        
        self.id = None # Id Tbl
        self.columnNumber = None # Numero Col
        self.value = None # Nuevo valor


        self.arbolAVltupla = ArbolAVL()
    
    # insert(database, table, columns): method 1
    def insert(self, database,table,columns): # por el momento no me envian id para saber si insertar o no
        #idDictionary= {'1': ['Facebook','0001','zucaritas']}
        self.arbolAVltupla.add(columns)
    
    #update(database, table, id, columnNumber, value): method 2
    def update(self,database,table,id,columnNumber,value):
        lista = [5,"cosdoasdas"]
        print(self.arbolAVltupla.search(lista))

    def crete_table(self, database, tableNmae, numColumns):  # No hay sobrecarga de metodos :(
        self.tableName = tableNmae
        self.numColums = numColumns
        self.database = database

    def get_arbol(self):
        return self.arbolAVltupla



diccionario = list()

table1 = Table()
table1.insert("db1", "usuario", [4, "Clarinda", "Toffolini", "ctoffolini0@mapy.cz"])
table1.insert("db1", "usuario", [5, "Clarinda", "Toffolini", "ctoffolini0@mapy.cz"])
table1.insert("db1", "usuario", [6, "Clarinda", "Toffolini", "ctoffolini0@mapy.cz"])


table1.get_arbol().grafica()