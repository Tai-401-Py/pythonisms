
class LinkedList:
    """
    This module allows us to create a linked list by creating nodes and adding them to the beginning of the linked list, all while setting thier value. It is singly linked and only goes one direction. 
    """

    def __init__(self, data = []):
        self.head = None
        self.list = []
        self.length = 0
        if data:
            for item in data:
                self.append(item)

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += 'NULL'
        return string

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self):
        self.length = 0
        for item in self:
           self.length += 1
        return self.length
    
    def __repr__(self):
        return self.__str__()

    def __getitem__(self, idx):
        if idx > len(self)-1:
            raise TargetError
        return list(self)[idx]

# Begin standard methods

    def insert(self, data=None):
        """
        Insert a new node to the beginning of Linked_list
        """
        self.head = Node(data, self.head)

    def append(self, data):
        """
        Append Node to end of Linked List
        """
        new_node = Node(data)
        current = self.head

        if not self.head:
            self.head = new_node
            return

        while current.next:
            current = current.next

        current.next = new_node

    def insert_before(self, query, value):
        """
        Insert Node before target value
        """
        if self.head is None:
            raise TargetError
        elif self.head.value == query:
            self.insert(value)
            return
        current = self.head
        while current:
            try:
                if current.next.value == query:
                    old_next = current.next
                    current.next = Node(value, old_next)
                    break
                current = current.next
            except:
                raise TargetError


    def insert_after(self, query, value):
        """
        Insert Node after target value
        """
        if self.head is None:
            raise TargetError
        current = self.head
        while current:
            if current.value is query:
                current.next = Node(value, current.next)
                break
            if current.next is None:
                raise TargetError
            current = current.next
 
    def kth_from_end(self, index):
        idx_archive = []
        current = self.head
        while current:
            idx_archive.append(current.value)
            current = current.next
        idx_archive.reverse()
        if index >= len(idx_archive):
            raise TargetError
        if index < 0:
            raise TargetError
        return idx_archive[index]            

    def includes(self, query):
        """
        Does the linked list have queried value? 
        """
        current = self.head
        while current:
            if current.value is query:
                return True
            current = current.next
        return False

    def display(self):
        return self.head.value


class Node:
    """
    Node the base of a linked list.
    """
    def __init__(self, data=None, next_=None):
        self.value = data
        self.next = next_


class TargetError(Exception):
    """
    Custom Exception
    """
