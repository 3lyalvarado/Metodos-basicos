class NodoAVL:
    def __init__(self, element):
        self.element = element
        self.right = None
        self.left = None
        self.factor = 0

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element

    def set_factor(self, factor):
        self.factor = factor

    def get_factor(self):
        return self.factor


class ArbolAVL:
    def __init__(self):
        self.root = None
        self.cadena = ""
        self.scape = False

    def add(self, element):
        self.root = self.__add(self.root, element)

    def __add(self, raiz, elemeneto):
        if raiz is None:
            raiz = NodoAVL(elemeneto)
            self.scape = True
        elif elemeneto[0] < raiz.get_element()[0]:
            izq = self.__add(raiz.get_left(), elemeneto)
            raiz.set_left(izq)
            if self.scape is True:
                if raiz.get_factor() == 1:
                    raiz.set_factor(0)
                    self.scape = False
                elif raiz.get_factor() == 0:
                    raiz.set_factor(-1)
                elif raiz.get_factor() == -1:
                    n1 = raiz.get_left()
                    if n1.get_factor() == -1:
                        raiz = self.__rotacion_ii(raiz, n1)
                    else:
                        raiz = self.__rotacion_id(raiz, n1)
                    self.scape = False
        elif elemeneto[0] > raiz.get_element()[0]:
            der = self.__add(raiz.get_right(), elemeneto)
            raiz.set_right(der)
            if self.scape:
                if raiz.get_factor() == 1:
                    n1 = raiz.get_right()
                    if n1.get_factor() == 1:
                        raiz = self.__rotacion_dd(raiz, n1)
                    else:
                        raiz = self.__rotacion_di(raiz, n1)
                    self.scape = False
                elif raiz.get_factor() == 0:
                    raiz.set_factor(1)
                elif raiz.get_factor() == -1:
                    raiz.set_factor(0)
                    self.scape = False

        return raiz

    def __rotacion_ii(self, n, n1):
        n.set_left(n1.get_right())
        n1.set_right(n)

        if n1.get_factor() == -1:
            n.set_factor(0)
            n1.set_factor(0)
        else:
            n.set_factor(-1)
            n1.set_factor(1)

        return n1

    def __rotacion_dd(self, n, n1):
        n.set_right(n1.get_left())
        n1.set_left(n)

        if n1.get_factor() == 1:
            n.set_factor(0)
            n1.set_factor(0)
        else:
            n.set_factor(1)
            n1.set_factor(-1)

        return n1

    def __rotacion_id(self, n, n1):
        n2 = n1.get_right()
        n.set_left(n2.get_right())
        n2.set_right(n)
        n1.set_right(n2.get_left())
        n2.set_left(n1)

        if n2.get_factor() == 1:
            n1.set_factor(-1)
        else:
            n1.set_factor(0)

        if n2.get_factor() == -1:
            n.set_factor(1)
        else:
            n.set_factor(0)

        n2.set_factor(0)
        return n2

    def __rotacion_di(self, n, n1):
        n2 = n1.get_left()
        n.set_right(n2.get_left())
        n2.set_left(n)
        n1.set_left(n2.get_right())
        n2.set_right(n1)

        if n2.get_factor() == 1:
            n.set_factor(-1)
        else:
            n.set_factor(0)

        if n2.get_factor() == -1:
            n1.set_factor(1)
        else:
            n1.set_factor(0)

        n2.set_factor(0)
        return n2

    def grafica(self):
        self.cadena = "digraph G{\n"
        self.cadena += "node[shape=\"record\"]\n"
        if self.root is not None:
            self.cadena += f"node{self.root.get_element()[0]} [label=\"<f0>|<f1> Valor:{self.__get_values_list(self.root.get_element())} |<f2>\" ] \n"
            self.__graficar(self.root, self.get_root().get_left(), True)
            self.__graficar(self.root, self.get_root().get_right(), False)

        self.cadena += "}\n"
        print(self.cadena)

    def get_root(self):
        return self.root

    def __graficar(self, padre, actual, left):
        if actual is not None:
            self.cadena += f"node{actual.get_element()[0]} [label=\"<f0>|<f1> Valor:{self.__get_values_list(actual.get_element())} |<f2>\"] \n"
            if left is True:
                self.cadena += f"node{padre.get_element()[0]}:f0->node{actual.get_element()[0]}:f1 \n"
            else:
                self.cadena += f"node{padre.get_element()[0]}:f2->node{actual.get_element()[0]}:f1 \n"

            self.__graficar(actual, actual.get_left(), True)
            self.__graficar(actual, actual.get_right(), False)

    def __delete_nodo(self, raiz=NodoAVL, value=0):
        if raiz is None: return None
        if value == raiz.get_element():
            # No tiene ningun Hijo
            if raiz.get_left() is None and raiz.get_right() is None:
                return None
            # Tiene un Hijo
            if raiz.get_right() is None:
                raiz.set_factor(-1)
                return raiz.get_left()
            if raiz.get_left() is None:
                raiz.set_factor(1)
                return raiz.get_right()

            # Have 2 Son
            small_value = self.__find_nodo(raiz.get_right())
            raiz.set_element(small_value)
            raiz.set_right(self.__delete_nodo(raiz.get_right(), small_value))
            raiz.set_factor(-1)
            return raiz
        if value < raiz.get_element():
            raiz.set_left(self.__delete_nodo(raiz.get_left(), value))
            return raiz
        raiz.set_right(self.__delete_nodo(raiz.get_right(), value))
        return raiz

    def delete_nodo(self, value):
        self.root = self.__delete_nodo(self.root, value)

    def __find_nodo(self, raiz=NodoAVL):
        if raiz.get_left() is None:
            return raiz.get_element()
        else:
            return self.__find_nodo(raiz.get_left())

    def __get_values_list(self, lista):
        cadena = ""
        for value in lista:
            cadena += f"{value} \n"

        return cadena

    # BUSCAR

    def search(self, element):
        return self.__search(self.root, element)

    def __search(self, raiz, elemeneto):

        if elemeneto[0] < raiz.get_element()[0]:
            return self.__search(raiz.get_left(), elemeneto)
        elif elemeneto[0] > raiz.get_element()[0]:
            return self.__search(raiz.get_right(), elemeneto)
        elif elemeneto[0]==raiz.get_element()[0]:
            return elemeneto[0]
        else:
            return "cola"