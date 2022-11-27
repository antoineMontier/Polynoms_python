class Cell:

    def __init__(self, content, next):
        self._content = content
        self._next = next

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def get_next(self):
        return self._next
    
    def set_next(self, next):
        self._next = next

    def __eq__(self, cell):
        return self.get_content() == cell.get_content() and id(self.get_next()) == id(cell.get_next())#compare adress of the next cell

    def __str__(self):
        return "%s" % (self.get_content())