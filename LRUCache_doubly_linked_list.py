class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #sentinel nodes, used only for LURCache operations, never removed or assigned
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.previous = self.left

    ##########################
    # Node Operations
    ##########################
    #insert node at the end at the right
    def insert(self, node):
        previous = self.right.previous

        previous.next = node
        node.previous = previous

        node.next = self.right
        self.right.previous = node

    def remove(self, node):
        previous = node.previous
        next = node.next

        previous.next = next
        next.previous = previous

    ##########################
    # LRUCache Functions
    ##########################
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            #move the node to the right (most recently used)
            self.remove(node)
            self.insert(node)

            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        #prevents duplicate keys
        if key in self.cache:
            self.remove(self.cache[key])

        #put new node at the right (most recently used)
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        #remove LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Assuming your LRUCache class is already implemented

# Commands and inputs from your test case
commands = ["LRUCache","put","put","get","put","get","put","get","get","get"]
inputs   = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# This will store the results for get() operations
outputs = []

cache = None

for cmd, arg in zip(commands, inputs):
    if cmd == "LRUCache":
        cache = LRUCache(arg[0])
        outputs.append(None)  # Initialization doesn't return anything
    elif cmd == "put":
        cache.put(arg[0], arg[1])
        outputs.append(None)  # put() doesn't return anything
    elif cmd == "get":
        res = cache.get(arg[0])
        outputs.append(res)

print(outputs)