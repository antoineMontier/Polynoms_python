from Cell import *

class LinkedList:

    def __init__(self):
        self._head = Cell(None, None)
        self._tail = Cell(None, None)

    def isEmpty(self):
        return self._head == Cell(None, None)

    def addHead(self, content):
        #handle empty list
        if(self.isEmpty()):
            newHead = Cell(content, None)
            self._head = newHead
            self._tail = newHead
        #handle one element list
        elif(self._head == self._tail):
            newHead = Cell(content, self._tail)
            self._head = newHead
        else:
            newHead = Cell(content, self._head)
            self._head = newHead

    def __str__(self):
        if(self.isEmpty()):
            return "[empty]"
        elif(self._head == self._tail):
            return "[" +self._head.__str__()+"]"
        else:
            res = "["
            walker = Cell(self._head.get_content(), self._head.get_next())
            while(walker != self._tail):
                res += walker.__str__() + ", "
                walker = walker.get_next()
            return res + self._tail.__str__() + "]"

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail










l = LinkedList()
l.addHead(5)
l.addHead(8)
l.addHead(-2)
l.addHead(-2)
l.addHead(-2)
l.addHead(-2)

print(l)
#print("head", l.get_head(), " tail", l.get_tail)