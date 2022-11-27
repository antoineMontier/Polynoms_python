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

    def pushTail(self, content):
        #handle empty list
        if(self.isEmpty()):
            newTail = Cell(content, None)
            self._head = newTail
            self._tail = newTail
        #handle one element list
        elif(self._head == self._tail):
            newTail = Cell(content, None)
            self._head.set_next(newTail)
            self._tail = newTail
        else:
            #find cell before tail
            newTail = Cell(content, None)
            self._tail.set_next(newTail)
            self._tail = newTail

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

    def length(self):
        if(self.isEmpty()):
            return 0
        elif(self._head == self._tail):#one element exception
            return 1
        else:
            res = 2
            walker = Cell(self._head.get_content(), self._head.get_next())
            while(walker.get_next() != self._tail):
                res += 1
                walker = walker.get_next()
            return res




    def pushAtIndex(self, content, index):  #returns 1 if sucessful ; 0 if not
        if(index < 0 or index > self.length()):
            return 0 #error
        elif(index == 0):
            self.push(content)
            return 1
        elif(index == self.length()):
            self.pushTail(content)
            return 1
        else:
            """
            if(self.length() == 2 and index == 1):
                toInsert = Cell(content, self._tail)
                self._head.set_next(toInsert)
                return 1
            """
            walker1 = self._head
            walker2 = self._head
            i = 0
            while(i < index):
                walker1 = walker2
                walker2 = walker2.get_next()
                i += 1
            #here walker1 is just before the index and walker2 just after
            toInsert = Cell(content, walker2)
            walker1.set_next(toInsert)
            return 1#success


    def get(self, index):
        assert not(index < 0 or index >= self.length())
        i = 0
        walker = self._head
        while(i < index):
            walker = walker.get_next()
            i+= 1
        return walker.get_content()

    def popAtIndex(self, index):
        assert not(index < 0 or index >= self.length())
        if(index == 0):
            return self.pop()#head
        elif(index == self.length()-1):
            return self.popTail()
        else:
            walker1 = self._head
            walker2 = self._head
            i = 0
            while(i < index):
                walker1 = walker2
                walker2 = walker2.get_next()
                i += 1
            print(walker1, walker2)
            #here walker1 is just before the index and walker2 on the index
            walker1.set_next(walker2.get_next())
            return walker2.get_content()


l = LinkedList()

l.pushTail(5)
l.pushTail(8)

l.pushTail(-2)

l.pushTail(-55.9)
l.push(13.2)
l.push(-1)


print(l)
"""
print("head", l.get_head(), "tail", l.get_tail(), "length", l.length())
print(l)
for i in range(l.length()):
    print(l.get(i))
"""
print(l.popAtIndex(1))
print(l)