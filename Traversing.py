# Traversing in linked list:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    # Creating Nodes:
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

    #Connect nodes to form a linked list:
node1.next=node2
node2.next=node3
node3.next=node4

    #Printing the linked list:
    # For traversing we using head->it's a pointer or we can say reference
head=node1    
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")    
    
     

    