from math import log10
import sys
from Monom import *
class Polynom:
    MIN = -100
    PRECISION = 0.01
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
        for i in range(self._monoms.length()):
            if(self._monoms.get(i).get_pow() == pow):
                self._monoms.get(i).set_coef(coef + self._monoms.get(i).get_coef())
                return
        self._monoms.pushTail(Monom(coef, pow))
    def clean(self):
        if(self._monoms.isEmpty()):
            return
        for i in range(self._monoms.length()-1):
            if(self._monoms.get(i).get_coef() == 0):
                self._monoms.popAtIndex(i)
        if(self._monoms.get(0).get_coef() == 0):
            self._monoms.clear()
            return
        #sort by power
        self._monoms.bubble_sort(lambda a, b : a.get_pow() <= b.get_pow())
    def length(self):
        self.clean()
        return self._monoms.length()
    def __add__(self, other):
        res = Polynom()
        for i in range(self._monoms.length()):
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
    def __eq__(self, other) -> bool:
        self.clean()
        other.clean()
        if(self.length() != other.length()):
            return False
        else:
            tmp = self - other
            tmp.clean()
            if(tmp.length() == 0):
                return True
            else:
                return False
    def derivate(self):
        res = Polynom()
        if(self.length() == 0):
            return res
        else:
            for i in range(self.length()):
                if(self._monoms.get(i).get_pow() > 0):
                    res.add(self._monoms.get(i).get_coef()*self._monoms.get(i).get_pow(), self._monoms.get(i).get_pow()-1)
            res.clean()
            return res
    def primitive(self):
        res = Polynom()
        if(self.length() == 0):
                    return res
        else:
            for i in range(self.length()):
                res.add(self._monoms.get(i).get_coef()/(self._monoms.get(i).get_pow() + 1), self._monoms.get(i).get_pow()+1)
        res.clean()
        return res
    def evaluate(self, x):
        if(self.length() == 0):
            return 0
        else:
            res = 0
            for i in range(self.length()):
                res += self._monoms.get(i).get_coef()*pow(x, self._monoms.get(i).get_pow())
            return res
    def tangent(self, a):#y = f'(a)(x-a) + f(a)
        res = Polynom()
        if(self.length() == 0):
            return res
        else:
            tmp = Polynom() # tmp = x - a
            tmp.add(1, 1)
            tmp.add(-a, 0)
            res.add(self.derivate().evaluate(a), 0) #f'(a)
            res = res * tmp#f'(a)(x-a)
            res.add(self.evaluate(a), 0) #f(a)
            res.clean()
            return res
    def max_deg(self):
        res = 0
        for i in range(self.length()):
            res = max(res, self._monoms.get(i).get_pow())
        return res
    def roots(self) -> LinkedList:
        res = LinkedList()
        if(self.length() == 0):
            return res
        else:
            #store signe
            prev_sign = sign = self.evaluate(Polynom.MIN)>=0
            deep_search = False
            prev_x = x = Polynom.MIN
            while(x < -Polynom.MIN):
                if(sign != prev_sign):
                    deep_search = True
                    #relauch a loop
                    i = prev_x
                    sign = prev_sign 
                    while(i < x and deep_search):
                        if(prev_sign != sign):
                            res.push(round(i - Polynom.PRECISION*Polynom.PRECISION/2, round(2*log10(1/Polynom.PRECISION))))
                            deep_search = False
                        prev_sign = sign
                        sign = self.evaluate(i) >= 0
                        i+= pow(Polynom.PRECISION, 5)

                prev_sign = sign
                sign = self.evaluate(x) >= 0
                prev_x = x
                #print calcul progression bar :
                if(abs(x % -2*Polynom.MIN/100) < Polynom.PRECISION):
                    print(".", end="")
                    sys.stdout.flush()
                x += Polynom.PRECISION
            print("")
            res.bubble_sort(lambda a, b : a >= b)
            return res