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
    def pushAtIndex(self, content, index=int):  #returns 1 if sucessful ; 0 if not
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
    def get(self, index=int):
        assert not(index < 0 or index >= self.length())
        i = 0
        walker = self._head
        while(i < index):
            walker = walker.get_next()
            i+= 1
        return walker.get_content()
    def popAtIndex(self, index=int):
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
            #here walker1 is just before the index and walker2 on the index
            walker1.set_next(walker2.get_next())
            return walker2.get_content()
    def set(self, content, index=int):
        assert not(index < 0 or index >= self.length())
        i = 0
        walker = self._head
        while(i < index):
            walker = walker.get_next()
            i+= 1
        walker.set_content(content)
    def reverse(self):
        if(self.isEmpty() or self._head == self._tail):
            return
        else:
            i = 0
            while(i < self.length()/2):
                tmp = self.get(self.length()-i-1)
                self.set(self.get(i), self.length()-i-1)
                self.set(tmp, i)
                i += 1
    def contains(self, content):
        if(self.isEmpty()):
            return 0
        walker = self._head
        if(walker.get_content() == content):
                return True
        while(walker!= self._tail):
            walker = walker.get_next()
            if(walker.get_content() == content):
                return True
        return False
    def maximum_index(self, superior):
        if(self.isEmpty()):
            return -1 #error
        elif(self._head == self._tail):
            return self._head.get_content()
        else:
            ind = 0
            walker = self._head
            i = 0
            while(walker!= self._tail):
                if(superior(walker.get_content(), self.get(ind)) == True):
                    ind = i
                walker = walker.get_next()
                i += 1
            if(superior(walker.get_content(), self.get(ind)) == True):
                    ind = i
            return ind
    def bubble_sort(self, superior):
        if(self.isEmpty() or self._head == self._tail):
            return self
        else:
            for i in range(self.length() - 1):
                for j in range(self.length()-1 - i):
                    if(superior(self.get(j), self.get(j+1)) == True):
                        tmp = self.get(j)
                        self.set(self.get(j+1), j)
                        self.set(tmp, j+1)
        return self
    def merge(self, other):
        if(self.isEmpty() and other.isEmpty()):
            return None
        elif(self.isEmpty()):
            return other
        elif(other.isEmpty()):
            return self
        else:
            for i in range(other.length()):
                self.pushTail(other.get(i))
    def takeWhile(self, predicate):
        res = LinkedList()
        if(self.isEmpty()):
            return res
        else:
            walker = self._head
            while(predicate(walker.get_content()) == True):
                res.pushTail(walker.get_content())
                walker = walker.get_next()
            return res
    def dropWhile(self, predicate):
        res = LinkedList()
        if(self.isEmpty()):
            return res
        else:
            walker = self._head
            while(predicate(walker.get_content()) == True):
                walker = walker.get_next()
            while(walker != self._tail):
                res.pushTail(walker.get_content())
                walker = walker.get_next()
            return res
    def filter(self, predicate):
        if(self.isEmpty()):
            return
        else:
            #fist remove the header part :
            while(predicate(self._head.get_content()) == False):
                self.pop()
                if(self.isEmpty()):
                    return
            #then remove the tail part :
            while(predicate(self._tail.get_content()) == False):
                self.popTail()
                if(self.isEmpty()):
                    return
            if(self.length() < 3):
                return #the list is filtered
            #then remove the body :
            walker1=self._head
            walker2=self._head.get_next()
            while(walker2 != self._tail):
                if(predicate(walker2.get_content()) == False):
                    walker1.set_next(walker2.get_next())
                    walker2.set_content(None)
                    walker2.set_next(None)
                    walker2 = walker1.get_next()
                else:
                    walker1 = walker2
                    walker2 = walker2.get_next()
    def map(self, fonction):
        if(self.isEmpty()):
            return
        else:
            walker = self._head
        while(walker != self._tail):
            walker.set_content(fonction(walker.get_content()))
            walker = walker.get_next()
        self._tail.set_content(fonction(self._tail.get_content()))
    def mapIf(self, predicate, fonction):
        if(self.isEmpty()):
            return
        else:
            walker = self._head
        while(walker != self._tail):
            if(predicate(walker.get_content())):
                walker.set_content(fonction(walker.get_content()))
            walker = walker.get_next()
        if(predicate(self._tail.get_content())):
            self._tail.set_content(fonction(self._tail.get_content()))
    def clear(self):
        self._tail = Cell(None, None)
        self._head = Cell(None, None)
    def indexOf(self, content):
        if(self.isEmpty()):
            return -1
        else:
            walker = self._head
            i = 0
            while(walker != self._tail):
                if(walker.get_content() == content):
                    return i
                walker = walker.get_next()
                i += 1
            if(walker.get_content() == content):
                return i
            return -1
    def toArray(self):
        res = []
        if(self.isEmpty()):
            return res
        else:
            walker = self._head
            while(walker != self._tail):
                res.append(walker.get_content())
                walker = walker.get_next()
            res.append(walker.get_content())
        return res
    @staticmethod
    def toLinkedList(array):
        res = LinkedList()
        if(len(array) == 0):
            return res
        else:
            for i in range(len(array)):
                res.pushTail(array[i])
        return res
    @staticmethod
    def copyOf(linkedlist):
        res = LinkedList()
        if(linkedlist.isEmpty()):
            return res
        else:
            for i in range(linkedlist.length()):
                res.pushTail(linkedlist.get(i))
        return res