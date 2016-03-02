class hashMap(object):

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
            for entry in self.table[dataHash]:
                if entry[0] == key:
                    # just a re-write
                    entry[1] = value
                    break
            else:
                # collision
                self.table[dataHash].append([key, value])

    def get(self, key):
        entry = self.table[self.hash(key)]
        if entry == None:
            return None
        elif len(entry) < 2:
            return entry[0][1]
        else:
            for i in entry:
                if i[0] == key:
                    return i[1]
