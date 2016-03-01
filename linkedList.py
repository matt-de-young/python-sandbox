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

    def add(self, data):
        if self.first is None:
            self.first = self.last = Link(None, data, None)
        else:
            self.last.next = Link(self.last, data, None)
            self.last = self.last.next

    def remove(self):
        if self.first is None:
            return False
        else:
            data = self.first.data
            self.first = self.first.next
            self.first.prev = None
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
            return data

def tests():
    q = LinkedList();
    for num in range(0,10):
        q.add(num);
    print q