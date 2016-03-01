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
            return
        while True:
            string += "[%d]" % i.data
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

    def add(self, data):
        if self.first is None:
            self.first = self.last = Link(None, data, None)
        else:
            self.last.next = Link(self.last, data, None)
            self.last = self.last.next
        self.length += 1

    def peek(self):
        return self.first.data

    def remove(self):
        if self.first is None:
            return False
        else:
            data = self.first.data
            self.first = self.first.next
            self.first.prev = None
            self.length -= 1
            return data

    def push(self, data):
        self.add(data)

    def pop(self):
        if self.last is None:
            return False
        else:
            data = self.last.data
            self.last = self.last.prev
            self.last.next = None
            self.length -= 1
            return data

    def subList(self, i, k):
        if i > k or self.length < k:
            return False
        link = self.first
        newList = LinkedList()
        for num in range(0, i):
            link = link.next
        for num in range(i, k):
            newList.add(link.data)
            link = link.next
        return newList

def tests():
    q = LinkedList();
    for num in range(0,10):
        q.add(num);
    print q