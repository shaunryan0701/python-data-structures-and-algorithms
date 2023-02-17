# head = {
#   "value": 11,
#   "next" : {
#     "value": 3,
#     "next" : {
#       "value": 23,
#       "next" : {
#         "value": 7,
#         "next" : None
#       }
#     }
#   }
# }

# print(head['next']['next']['value'])

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)