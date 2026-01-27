class Node:
    def __init__ (self, e, n = None):
        self.element = e
        self.next_node = n


    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n
    
    def get_element (self):
        return self.get_element
    
    def set_element (self, e):
        self.element = e
    
    def has_next (self):
        if self.get_next() is None:
            return False
        return True
    
    def to_string (self):
        return str(self.element)

class LinkedList ():
    def __init__ (self, h = None):
        self.head = h
        self.size = 0
    
    def get_size (self):
        return self.size
    
    def add (self, e):
        new_node = Node(e, self.head)
        self.head = new_node
        self.size += 1
    
    def remove(self, e):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.get_element() == e:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.head = current_node
                self.size -= 1
                return True
        return False
    
    def find (self, e):
        current_node = self.head
        while current_node:
            if current_node.get_element() == e:
                return e
            else:
                current_node = current_node.get_next
            return None
    
    def print_list (self):
        if self.head is None:
            return
        current_node = self.head
        size = self.get_size()
        for i in range(size):
            print(f"Node {i+1}: {current_node.to_string()}")
            current_node = current_node.get_next()
    
    def get_middle_node (self):
        length = self.get_size()
        middle_node = self.head
        if length & 1 == 0:
            length = (length / 2) + 1
        else:
             length = (length / 2) + 0.5
        for i in range(int(length) - 1):
            if middle_node.get_next is not None:
                middle_node = middle_node.get_next()
        print(f"The Node is Node {int(length)}: {middle_node.to_string()}")



myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()
myList.get_middle_node()



        