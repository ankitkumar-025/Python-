class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# Create node 1 as head.
head=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

head.next=node2
node2.next=node3
node3.next=node4

# Deletion from begining:
if head is not None:
    head=head.next


#Printing the linked list after inserting a node at begining:
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")    