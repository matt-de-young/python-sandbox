class HashMap(object):

    def __init__(self, size):
        self.table = [None] * size

    def __str__(self):
        return str(self.table)

    def hash(self, key):
        return abs(hash(str(key))) % len(self.table)

    def add(self, key, value):
        dataHash = self.hash(key)
        if self.table[dataHash] == None:
            self.table[dataHash] = [[key, value]]
        else:
            # posible collision
            for x in self.table[dataHash]:
                if x[0] == key:
                    # just a re-write
                    x[1] = value
                    break
            else:
                # collision
                self.table[dataHash].append([key, value])

    def remove(self, key):
        dataHash = self.hash(key)
        if self.table[dataHash] != None:
            for x in self.table[dataHash]:
                if x[0] == key:
                    self.table[dataHash].remove(x)

    def containsKey(self, key):
        dataHash = self.hash(key)
        if self.table[dataHash] == None:
            return False
        else:
            # posible collision
            for x in self.table[dataHash]:
                if x[0] == key:
                    return True
            else:
                return False

    def get(self, key):
        entry = self.table[self.hash(key)]
        if entry == None:
            return None
        elif len(entry) < 2:
            return entry[0][1]
        else:
            for x in entry:
                if x[0] == key:
                    return x[1]
