# linkedlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# empty linkedlist
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result


    # inserting at the end
    def at_the_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # inserting at the beginning
    def at_the_begining(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_any(self, value, place):
        new_node = Node(value)
        if place < 0 or place > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif place == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(place - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current= current.next

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current=current.next
            index += 1
        return "not in linked list"




new_linked_list = LinkedList()
new_linked_list.insert_at_any(1, 0)
new_linked_list.at_the_end(10)
new_linked_list.at_the_end(20)
new_linked_list.at_the_end(30)
new_linked_list.at_the_begining(6)
new_linked_list.at_the_begining(4)
new_linked_list.insert_at_any(2, 0)
print(new_linked_list.head.value)
print(new_linked_list.head.next)
print(new_linked_list.tail)
print(new_linked_list.tail.value)
print(new_linked_list.tail.next)
print(new_linked_list)
print(new_linked_list.traverse())
print(new_linked_list.search(1))
