##OrderedDict remembers the order in which keys were inserted
from collections import OrderedDict 

#defines a new class LRUCache
class LRUCache:
    
    #the constructor method of the LRUCache class in Python.
    # #This line starts the constructor for your cache object and prepares it with the maximum number of items (capacity) it can hold
    def __init__(self, capacity: int):
        
        #Our toy box
        self.cache = OrderedDict()
        
        #self.capacity = capacity    # How many toys it can hold
        self.capacity = capacity
     
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # If toy not found
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Update usage
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used

cache = LRUCache(3)

cache.put(1, '🐻')     # Add bear
cache.put(2, '🚗')     # Add car
cache.put(3, '🎲')     # Add dice
cache.get(1)          # Use bear again
cache.put(4, '🪁')     # Add kite, remove least used (car)

print(cache.cache)    # Output will be: {3: '🎲', 1: '🐻', 4: '🪁'}