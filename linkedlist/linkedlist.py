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

    # inserting at the end
    def at_the_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail = new_node
        self.length +=1

    #inserting at the begning
    def at_the_begining(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head= new_node
        self.length +=1

    def __str__(self):
        temp_node = self.head
        result=""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result





new_linked_list = LinkedList()
new_linked_list.at_the_end(10)
new_linked_list.at_the_end(20)
new_linked_list.at_the_end(30)
new_linked_list.at_the_begining(6)
new_linked_list.at_the_begining(4)
print(new_linked_list.head.value)
print(new_linked_list.head.next)
print(new_linked_list.tail)
print(new_linked_list.tail.value)
print(new_linked_list.tail.next)
print(new_linked_list)
