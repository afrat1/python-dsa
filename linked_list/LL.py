class Node:
    def __init__(self, value):
        self.value = value  # Initialize a Node with a value and set next to None initially
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Create a new Node with the given value
        self.head = new_node  # Set the head of the linked list to the new Node
        self.tail = new_node  # Set the tail of the linked list to the new Node
        self.length = 1  # Initialize the length of the linked list to 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)  # Print the value of the current Node
            temp = temp.next  # Move to the next Node in the linked list

    def append(self, value):
        new_node = Node(value)  # Create a new Node with the given value
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Set the next of the current tail to the new Node
            self.tail = new_node  # Update the tail to the new Node
        self.length += 1  # Increase the length of the linked list
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)  # Create a new Node with the given value
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Set the next of the new Node to the current head
            self.head = new_node  # Update the head to the new Node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next  # Update the head to the next Node
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next  # Move to the Node at the specified index
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value  # Set the value of the Node at the specified index to the given value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)  # Create a new Node with the given value
        temp = self.get(index - 1)  # Get the Node before the specified index
        new_node.next = temp.next  # Set the next of the new Node to the Node at the specified index
        temp.next = new_node  # Set the next of the Node before the index to the new Node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)  # Get the Node before the specified index
        temp = pre.next
        pre.next = temp.next  # Update the next of the Node before the specified index
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before  # Reverse the direction of the next pointer of the current Node
            before = temp
            temp = after
