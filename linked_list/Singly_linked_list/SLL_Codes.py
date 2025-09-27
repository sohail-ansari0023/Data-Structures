class Node:
    """Create the Nodes."""
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    """Create the Singly Linked List with the head object, and the methods."""
    def __init__(self, head=None):
        self.head = head
    
    # Checking the list is empty.
    def is_empty(self):
        return self.head == None # Returns the boolian value (True/False).
    
    # Inserting at the first position AKA to the head.
    def insert_at_first(self, data):
        # The node which contains data as item and the pointer will be the previous value of head.
        n = Node(item=data, next=self.head)
        self.head = n # Asigning the new node to the head.
    
    # Inserting at the end position AKA to the tail.
    def insert_at_last(self, data):
        # The node contains data as item and since it will attach at the tail so pointer points to None.
        n = Node(item=data, next=None)
        if self.is_empty():
            self.head = n
        # Since we cannot directly jump to the tail we have to go through each node.
        # The process is called Traverse.
        temp = self.head # creating the imaginary Node which will traverse. start from the head.
        while temp.next is not None: # Traverse until it's pointer will point to None. AKA to the tail.
            temp = temp.next 
        # Now the loop will only end at the tail. just add the node to tail.
        temp.next = n
    
    # Now for inserting after any element first we have to create a search method which will help me to
    # search through each nodes

    # Search method.
    def search(self, data): # takes the value which we are searching.
        if self.is_empty():
            return None
        temp = self.head
        # Since we have to look through every node's item, so we'll loop until the temp become None.
        while temp != None:  
            if temp.item == data: # If the item will match the data we are looking for, return the temp.
                return temp
            temp = temp.next    
        return None # Else when the item is nowhere return (None).
    
    # Now I can use the search method to go to that particular node after which we'll add the new Node.
    def insert_after(self, data, desired_value):
        temp = self.search(data=desired_value) # return the required temp.
        if temp is not None:
            # the node contain item and points to next node which is pointed by the required temp.
            n = Node(item=data, next=temp.next) 
            temp.next = n # Just add created node to the required temp.
        else:  
            print(f"Item Not Found! {desired_value} - Empty list/No such item inside list.")
    
    # I have to print the list.
    def print_list(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.item, end="-->")
                temp = temp.next
        else:
            print("Empty List!")
    
    # Deletion of the list.
    # The first Node.
    def del_the_first(self):
        if self.is_empty():# Checking wether the list is empty.
            print("Empty List!")
        else:
            self.head = self.head.next # Removing the first Node
    # The last Node.
    def del_the_last(self):
        if self.head is not None:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        else:
            print("Empty List!")
    # After the desired Node.
    def del_after(self, desired_value):
        if self.head is None:
            print("Empty List!")
        elif self.head.next is None:
            if self.head.item == desired_value:
                self.head = None
            else:
                print("Item Not Found!")
        else:
            temp = self.head
            if temp.item == desired_value:
                    self.head = temp.next
            else:
                while temp is not None:
                    if temp.next.item == desired_value:
                        temp.next = temp.next.next
                        break
                    else:
                        temp = temp.next

    def __iter__(self):
            return SLL_Iterator(self.head)
    
class SLL_Iterator:
        
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data
            


my_list = SLL()
my_list.insert_at_first(6)
my_list.insert_at_last(8)
my_list.insert_after(5, 8)
my_list.insert_at_first(3)
my_list.insert_at_last(4)
# 3-->6-->8-->5-->4-->


for i in my_list:
    print(i)
    