from PIL import Image
__copyright__ = "Copyright (C) 2020 Author Luis Fernando Espinino Barrios"
__copyright__ = "Copyright (C) 2020 Author 2018101719"


class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value):
        self.root = self._add(value, self.root)
    
    def _add(self, value, tmp):
        if tmp is None:
            return Node(value)        
        elif value>tmp.value:
            tmp.right=self._add(value, tmp.right)
            if (self.height(tmp.right)-self.height(tmp.left))==2:
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<tmp.left.value:
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1
        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.heigh(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.heigh(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = self.srr(tmp.left)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.right = self.srl(tmp.right)
        return self.srr(tmp)

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.value,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(tmp.value,end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.value,end = ' ')

    # Buscar :)
    def buscar(self, value):
        return self._buscar(value, self.root)
    
    def _buscar(self, value,tmp):
        
        if value>tmp.value:
            return self._buscar(value, tmp.right)
        elif value<tmp.value:
            return self._buscar(value, tmp.left)
        elif value == tmp.value:
            return tmp
        else:
            return None

    # Borrar
    def borrar(self, value):
        self._borrar(value, self.root)

    def _borrar(self, value,tmp):
        if tmp == None:
            return tmp
        if value>tmp.value:
            tmp.right = self._borrar(value, tmp.right)
        elif value<tmp.value:
            tmp.left = self._borrar(value, tmp.left)
        elif value == tmp.value:
            if tmp.right==None and tmp.left==None:
                del tmp
                return None
            if not tmp.right:
                NodoT = tmp.left
                del tmp
                return NodoT
            elif not tmp.left:
                NodoT = tmp.right
                del tmp
                return NodoT
            #return value
            NodoT = self.mayordemenores(tmp.left) # toma el lado izquierdo y busca el mas a la derecha esto par visualizar en https://www.cs.usfca.edu/~galles/visualization/AVLtree.html 
            tmp.value = NodoT.value # nota: me dio problema sin el value 
            tmp.left = self._borrar(NodoT.value,tmp.left) # cambiamos
        if not tmp:
            return tmp

        tmp.height = self.maxi(self.heightt(tmp.left),self.heightt(tmp.right))+1 #
        tmpbalanceo = self.balanceo(tmp)
        if tmpbalanceo > 1 and self.balanceo(tmp.left)>=0:
            return self.srl(tmp)
        elif tmpbalanceo > 1 and self.balanceo(tmp.left)<0:
            tmp.left = self.srr(tmp.left)
            return self.srl(tmp)
        if tmpbalanceo < -1 and self.balanceo(tmp.right)<=0:
            return self.srr(tmp)
        elif tmpbalanceo < -1 and self.balanceo(tmp.right)>0:
            tmp.right = self.srl(tmp.right)
            return self.srr(tmp)

        return tmp # este logre borrar por fin ## revisar

    def mayordemenores(self,tmp):
        if tmp.right: # para la recursividad podria modificar y buscar el mas a la izquieda de los mayores
            return self.mayordemenores(tmp.right) # busca el mas a la derecha d elos menores
        return tmp

    def heightt(self, tmp):
        if not tmp:
            return -1
        return tmp.height

    def balanceo(self, tmp):
        if tmp != None:
            return 0
        return self.heightt(tmp.left)-self.heightt(tmp.right)
        
t = AVLTree()
# [50, 10, 60, 20, 70, 30, 80, 40, 90] 
#add

t.add(5)
t.add(10)
t.add(20)
t.add(25)
t.add(30)
t.add(35)
t.add(50)
t.add(51)
t.add(52)
t.add(53)
t.add(54)

#t.add(5)
#t.add(100)
#t.add(41)
#t.add(13)
#t.add(15) al eliminar la raiz busco el mayor de los menores pero en dado caso este tenga un nodo derecho
#t.add(67) si elimino la raiz se debe de tomar en cuenta este caso.
#t.add(46) # https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
#t.add(11)
#t.add(55)
#t.add(21)
#t.add(29)
#t.add(83)
#t.add(71)
#t.add(22)
#t.add(3)


#print traversals
t.preorder()
print()
t.inorder()
print()
t.postorder()
t.borrar(50) # es un nodo hoja
t.borrar(35) # 35 es es raiz de sub arbol y nodo con dos hojas 
print()

t.preorder()
print()
t.inorder()
print()
t.postorder()

import sys

print (sys.getsizeof(t))
#print(t.buscar(25))