class hashTable(object):

    def __init__(self, size):
        self.table = [None] * size

    def __str__(self):
        return str(self.table)

    def hash(self, key):
        return abs(hash(str(key))) % len(self.table)

    def add(self, key, value):
        dataHash = self.hash(key)
        if self.table[dataHash] == None:
            self.table[dataHash] = value
        else:
            print "Collision at "+str(dataHash)

    def get(self, key):
        return self.table[self.hash(key)]
