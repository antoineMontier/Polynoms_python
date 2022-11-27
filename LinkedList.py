from Cell import *

class LinkedList:

    def __init__(self):
        self._head = Cell(None, None)
        self._tail = Cell(None, None)

    def isEmpty(self):
        return self._head == Cell(None, None)

    def push(self, content):
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

    def pop(self):#removes the head of the linked list and returns it
        if(self.isEmpty()):
            return None
        elif(self._head == self._tail):#one element exception
            res = self._head.get_content()#keep in memory the value
            self._head = Cell(None, None)#empty list
            self._tail = Cell(None, None)#empty list
            return res #end
        else:
            res = self._head.get_content()#keep in memory the value
            self._head = self._head.get_next()#shorten the list
            return res #end

    def popTail(self):
        if(self.isEmpty()):
            return None
        elif(self._head == self._tail):#one element exception
            res = self._head.get_content()#keep in memory the value
            self._head = Cell(None, None)#empty list
            self._tail = Cell(None, None)#empty list
            return res #end
        else:
            res = self._tail.get_content()#keep in memory the value
            #fin the cell previous to _tail
            walker = Cell(self._head.get_content(), self._head.get_next())
            while(walker.get_next() != self._tail):
                walker = walker.get_next()
            self._tail = walker
            return res #end






l = LinkedList()

l.push(5)
l.push(8)
l.push(-2)
l.push(-55.9)
l.push(13.2)
l.push(-1)

print(l)
print("h", l.get_head(), " t", l.get_tail())
print(l.popTail())
print(l)