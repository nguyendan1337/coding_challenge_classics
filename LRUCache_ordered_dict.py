from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


od = OrderedDict()
od['ford'] = 'mustang'
od['chevy'] = 'camaro'
od['dodge'] = 'charger'
od.move_to_end('chevy')
od.popitem(last=False)
print(od)

# class LRUCache:
#
#     def __init__(self, capacity):
#         self.cache = OrderedDict()
#         self.capacity = capacity
#
#
#     def get(self, key):
#
#         if key not in self.cache:
#             return -1
#
#         self.cache.move_to_end(key)
#
#         return self.cache[key]
#
#
#     def put(self, key, value):
#
#         if key in self.cache:
#             self.cache.move_to_end(key)
#
#         self.cache[key] = value
#
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)