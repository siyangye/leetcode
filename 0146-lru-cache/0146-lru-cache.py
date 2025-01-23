class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self,node):
        # add node 
        pre = self.tail.prev
        pre.next = node
        node.prev = pre
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self,node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            curr_node= self.node_map[key]
            curr_node.val = value
            self.remove(curr_node)
        new_node = Node(key,value)
        self.add(new_node)
        self.node_map[key]= new_node
        if len(self.node_map)>self.capacity:
            remove_node = self.head.next
            self.remove(remove_node)
            # curr_key = remove_node.key
            del self.node_map[remove_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)