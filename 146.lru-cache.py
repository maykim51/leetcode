'''
MEDIUM 20.03.13
실수원인: 자료형을 잘 몰랐음! OrderedDict = hash map + linked list = Java's LinkedHashMap

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        
    # returns value of the key, -1 if no such key
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
        
    # update the key's value if did not exist. remove LRU item.
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)