from Monom import *
class Polynom:
    def __init__(self):
        self._monoms = LinkedList()
    def __str__(self):
        if(self._monoms.isEmpty()):
            return "0"
        s = "" + self._monoms.get(0).__str__()
        for i in range(1, self._monoms.length()):
            if(self._monoms.get(i).get_coef() >= 0):
                s += " + " + self._monoms.get(i).__str__() 
            else:
                s += " - " + (- self._monoms.get(i).get_coef()).__str__() + "x^" + self._monoms.get(i).get_pow().__str__()
        return s
    def add(self, coef, pow):
        #first, assert that the polynomial need a new monom (if no other one has the same power as the one in parameter)
        for i in range(self.length()):
            if(self._monoms.get(i).get_pow() == pow):
                self._monoms.get(i).set_coef(coef + self._monoms.get(i).get_coef())
                return
        self._monoms.pushTail(Monom(coef, pow))
    def clean(self):
        for i in range(self.length()):
            if(self._monoms.get(i).get_coef() == 0):
                self._monoms.popAtIndex(i)
        #sort by power
        self._monoms.bubble_sort(lambda a, b : a.get_pow() <= b.get_pow())
    def length(self):
        return self._monoms.length()
    def __add__(self, other):
        res = Polynom()
        for i in range(self.length()):
            res.add(self._monoms.get(i).get_coef(), self._monoms.get(i).get_pow())
        for i in range(other.length()):
            res.add(other._monoms.get(i).get_coef(), other._monoms.get(i).get_pow())
        res.clean()
        return res
    def __sub__(self, other):
        res = Polynom()
        for i in range(self.length()):
            res.add(self._monoms.get(i).get_coef(), self._monoms.get(i).get_pow())
        for i in range(other.length()):
            res.add(-other._monoms.get(i).get_coef(), other._monoms.get(i).get_pow())
        res.clean()
        return res
    def __mul__(self,other):
        res = Polynom()
        for i in range(self.length()):
            for j in range(other.length()):
                res.add(self._monoms.get(i).get_coef() * other._monoms.get(j).get_coef(), self._monoms.get(i).get_pow() + other._monoms.get(j).get_pow())
        res.clean()
        return res

p = Polynom()
p.add(-3, 1)
p.add(-2, 1)
p.add(-1, 1)
p.add(4, 2)
p.clean()


q = Polynom()
q.add(-3, 1)
q.add(-2, 0)
q.add(17, 3)
q.clean()


print("p = ", p)
print("q = ", q)
print("q + p", q + p)
print("q - p", q - p)
print("q * p", q * p)
