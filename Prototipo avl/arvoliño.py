# Luis Espino 2020

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.altura = 0


class AVLTree:
    def __init__(self):
        self.raiz = None

    def add(self, valor):
        self.raiz = self._add(valor, self.raiz)

    def _add(self, valor, aux):
        if aux is None:
            return Node(valor)

        elif valor > aux.valor:
            aux.hijo_derecho = self._add(valor, aux.hijo_derecho)
            if (self.alturaNodo(aux.hijo_derecho)-self.alturaNodo(aux.hijo_izquierdo)) == 2:
                if valor > aux.hijo_derecho.valor:
                    aux = self.RotacionIzquierda(aux)
                else:
                    aux = self.RotacionDobleIzquierda(aux)
        else:
            aux.hijo_izquierdo = self._add(valor, aux.hijo_izquierdo)
            if (self.alturaNodo(aux.hijo_izquierdo)-self.alturaNodo(aux.hijo_derecho)) == 2:
                if valor < aux.hijo_izquierdo.valor:
                    aux = self.RotacionDerecha(aux)
                else:
                    aux = self.RotacionDobleDerecha(aux)
        r = self.alturaNodo(aux.hijo_derecho)
        l = self.alturaNodo(aux.hijo_izquierdo)
        m = self.maxi(r, l)
        aux.altura = m+1
        return aux

    def alturaNodo(self, aux):
        if aux is None:
            return -1
        else:
            return aux.altura

    def maxi(self, r, l):
        return (l, r)[r > l]

    def RotacionDerecha(self, t1):
        t2 = t1.hijo_izquierdo
        t1.hijo_izquierdo = t2.hijo_derecho
        t2.hijo_derecho = t1
        t1.altura = self.maxi(self.alturaNodo(
            t1.hijo_izquierdo), self.alturaNodo(t1.hijo_derecho))+1
        t2.altura = self.maxi(self.alturaNodo(t2.hijo_izquierdo), t1.altura)+1
        return t2

    def RotacionIzquierda(self, t1):
        t2 = t1.hijo_derecho
        t1.hijo_derecho = t2.hijo_izquierdo
        t2.hijo_izquierdo = t1
        t1.altura = self.maxi(self.alturaNodo(
            t1.hijo_izquierdo), self.alturaNodo(t1.hijo_derecho))+1
        t2.altura = self.maxi(self.alturaNodo(t2.hijo_izquierdo), t1.altura)+1
        return t2

    def RotacionDobleDerecha(self, aux):
        aux.hijo_izquierdo = self.RotacionIzquierda(aux.hijo_izquierdo)
        return self.RotacionDerecha(aux)

    def RotacionDobleIzquierda(self, aux):
        aux.hijo_derecho = self.RotacionDerecha(aux.hijo_derecho)
        return self.RotacionIzquierda(aux)

    def _Eliminar(self, valor):
        self.raiz = self.Eliminar(valor, self.raiz)

    def Eliminar(self, valor, nodo):

        if nodo is None:
            print("Elemento no encontrado")
            return None

        elif (nodo.valor > valor):
            nodo.hijo_izquierdo = self.Eliminar(valor, nodo.hijo_izquierdo)

        elif (nodo.valor < valor):
            nodo.hijo_derecho = self.Eliminar(valor, nodo.hijo_derecho)

        elif (nodo.hijo_izquierdo != None and nodo.hijo_derecho != None):
            aux = self.EncontrarMenor(nodo.hijo_derecho)
            nodo.valor = aux.valor
            nodo.hijo_derecho = self.Eliminar(nodo.valor, nodo.hijo_derecho)

        else:
            aux = nodo
            if (nodo.hijo_izquierdo is None):
                nodo = nodo.hijo_derecho

            elif (nodo.hijo_derecho is None):
                nodo = nodo.hijo_izquierdo

            del aux

        if (nodo is None):
            return nodo

        nodo.altura = self.maxi(self.alturaNodo(
            nodo.hijo_izquierdo), self.alturaNodo(nodo.hijo_derecho)) + 1
        balance = self.GetBalance(nodo)

        if (balance < -1):
            if (self.GetBalance(nodo.hijo_derecho) <= 0):
                return self.RotacionIzquierda(nodo)
            else:
                return self.RotacionDobleIzquierda(nodo)
        elif (balance > 1):
            if (self.GetBalance(nodo.hijo_izquierdo) >= 0):
                return self.RotacionDerecha(nodo)
            else:
                return self.RotacionDobleDerecha(nodo)

        return nodo

    def GetBalance(self, nodo):
        if (nodo is None):
            return 0

        return (self.alturaNodo(nodo.hijo_izquierdo) - self.alturaNodo(nodo.hijo_derecho))

    def EncontrarMenor(self, nodo):
        if nodo is None:
            return None

        elif (nodo.hijo_izquierdo is None):
            return nodo

        else:
            return self.EncontrarMenor(nodo.hijo_izquierdo)

    def preorder(self):
        self._preorder(self.raiz)

    def _preorder(self, aux):
        if aux:
            print(aux.valor, end=' ')
            self._preorder(aux.hijo_izquierdo)
            self._preorder(aux.hijo_derecho)

    def inorder(self):
        self._inorder(self.raiz)

    def _inorder(self, aux):
        if aux:
            self._inorder(aux.hijo_izquierdo)
            print(aux.valor, end=' ')
            self._inorder(aux.hijo_derecho)

    def postorder(self):
        self._postorder(self.raiz)

    def _postorder(self, aux):
        if aux:
            self._postorder(aux.hijo_izquierdo)
            self._postorder(aux.hijo_derecho)
            print(aux.valor, end=' ')

    def getValor(self, nodo):
        return nodo.valor
    CADENA=""
    Count=0
    def GetDotArbol(self, inicio):
        self.Count+=1
        # nodo = str(inicio.valor) + " [label=\"" + str(inicio.valor) + "]\n"
        nodo = ""
        if (inicio.hijo_izquierdo != None):
            nodo += str(inicio.valor) + " -> " + \
                str(self.getValor(inicio.hijo_izquierdo))+"\n"

            self.GetDotArbol(inicio.hijo_izquierdo)

        if (inicio.hijo_derecho != None):
            nodo += str(inicio.valor) + " -> " + \
                str(self.getValor(inicio.hijo_derecho)) + "\n"

            self.GetDotArbol(inicio.hijo_derecho)
        self.CADENA+=nodo
        return nodo
    def PRINT(self,raiz):
        self.GetDotArbol(raiz)

        x="\nDigraph Arbol{\nrankdir = TB;\nnode[shape = circle];\n"+self.CADENA+"}"
        print(x)

t = AVLTree()

t.add('1')
t.add('2')
t.add('3')
t.add('4')
t.add('5')
t.add('6')
t.add('7')
t.add('8')
t.add('9')
t.add('10')
t.add('11')
t.add('12')
t._Eliminar('11')
# t._Eliminar(10)
# t._Eliminar(9)

t.preorder()
print()
t.inorder()
print()
t.postorder()



# t.preorder()
# print()
# t.inorder()
# print()
# t.postorder()
t.PRINT(t.raiz)