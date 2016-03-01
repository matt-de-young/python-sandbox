class Link(object):

    def __init__(self, p, data, n):
        self.prev = p
        self.data = data
        self.next = n

    def __str__(self):
        return self.data

class LinkedList(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        i = self.first
        string = ""
        if i == None:
            return ""
        while True:
            string += "["+str(i.data)+"]"
            if i.next == None:
                break
            else:
                string += ","
            i = i.next

        return string

    def __add__(self, other):
        return self.__str__()+other

    def __radd__(self, other):
        return other+self.__str__()

    # Append to back of list
    def add(self, data):
        if self.length < 1:
            self.last = self.first = Link(None, data, None)
        else:
            self.last.next = self.last = Link(self.last, data, None)
        self.length += 1

    # Prepend to front of list
    def push(self, data):
        if self.length < 1:
            self.last = self.first = Link(None, data, None)
        else:
            self.first.prev = self.first = Link(None, data, self.first)
        self.length += 1

    # Remove from front
    def remove(self):
        if self.length == 0:
            return False

        data = self.first.data
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self.length -= 1
        return data

    # Remove from front
    def pop(self):
        self.remove()