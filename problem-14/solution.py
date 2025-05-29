from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # Create an empty ordered dictionary to store cache items
        self.cache = OrderedDict()
        self.capacity = capacity  # Maximum number of items allowed

    def get(self, key: int) -> int:
        # If the key is not in the cache, return -1
        if key not in self.cache:
            return -1
        else:
            # Move the accessed key to the end to mark it as most recently used
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value of the key

    def put(self, key: int, value: int) -> None:
        # If key already exists, move it to end and update the value
        if key in self.cache:
            self.cache.move_to_end(key)
        # Insert or update the key-value pair
        self.cache[key] = value

        # If the cache exceeds its capacity, remove the least recently used item (first item)
        if len(self.cache) > self.capacity:
            # popitem(last=False) pops the first inserted (least recently used) item
            self.cache.popitem(last=False)
            
cache = LRUCache(2)   # Cache with capacity of 2

cache.put(1, 1)       # Cache: {1=1}
cache.put(2, 2)       # Cache: {1=1, 2=2}
print(cache.get(1))   # Returns 1 and marks 1 as recently used, Cache: {2=2, 1=1}

cache.put(3, 3)       # Evicts 2, Cache: {1=1, 3=3}
print(cache.get(2))   # Returns -1 (not found)
