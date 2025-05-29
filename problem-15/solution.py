# Define a node of the doubly linked list
class Node:
    def __init__(self, key, value):
        self.key = key                  # Store the key
        self.value = value              # Store the value
        self.prev = self.next = None   # Initialize prev and next pointers
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity       # Maximum number of items cache can hold
        self.cache = {}                # Dictionary to map key -> node

        # Create dummy head and tail nodes
        self.head = Node(0, 0)         # Head dummy node (front of list)
        self.tail = Node(0, 0)         # Tail dummy node (end of list)

        # Connect head and tail
        self.head.next = self.tail     # Head points to tail initially
        self.tail.prev = self.head     # Tail points back to head
    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev = node.prev              # Get the node before the current one
        nxt = node.next               # Get the node after the current one
        prev.next = nxt               # Skip the current node in forward direction
        nxt.prev = prev               # Skip the current node in backward direction
    def _insert_at_front(self, node: Node):
        """Insert a node right after head (mark as most recently used)."""
        node.prev = self.head                # New node comes right after head
        node.next = self.head.next           # It points to the current first node
        self.head.next.prev = node           # The current first node points back to new node
        self.head.next = node                # Head points to new node
    def get(self, key: int) -> int:
        if key in self.cache:                         # Check if key exists in cache
            node = self.cache[key]                    # Get the node from dictionary
            self._remove(node)                        # Remove node from current position
            self._insert_at_front(node)               # Move it to the front (most recently used)
            return node.value                         # Return its value
        return -1                                     # If not found, return -1
    def put(self, key: int, value: int):
        if key in self.cache:                         # If key already exists
            self._remove(self.cache[key])             # Remove old node from list

        node = Node(key, value)                       # Create a new node with key-value
        self.cache[key] = node                        # Add node to dictionary
        self._insert_at_front(node)                   # Insert node at front of list

        if len(self.cache) > self.capacity:           # Check if cache exceeds capacity
            lru = self.tail.prev                      # Least recently used is before the tail
            self._remove(lru)                         # Remove it from the list
            del self.cache[lru.key]                   # Remove it from the dictionary
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # returns 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # returns -1 (not found)
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # returns -1 (not found)
print(cache.get(3))    # returns 3
print(cache.get(4))    # returns 4
