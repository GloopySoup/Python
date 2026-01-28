class HashTable:
    def __init__ (self):
        self.collection = {}
    
    def hash(self, string):
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value
    
    def add(self, key, value):
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = {}
        self.collection[key_hash][key] = value
    
    def remove(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                del self.collection[key_hash][key]
    
    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        return None