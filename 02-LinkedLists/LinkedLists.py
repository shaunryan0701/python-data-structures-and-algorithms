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


  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next	


  def append(self, value) -> bool:
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:  
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
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


  def prepend(self, value) -> bool:
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node

    self.length += 1
    return True  


  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
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
      temp = temp.next
    return temp

  def set_value(self, index, value) -> bool:
    temp = self.get(index) 
    if temp:
      temp.value = value
      return True
    return False


  def insert(self, index, value) -> bool:
    if index < 0 or index > self.length:
      return False
    elif index == 0:
      return self.prepend(value)
    elif index == self.length:
      return self.append(value)
    
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    elif index == 0:
      return self.pop_first()
    elif index == self.length - 1:
      return self.pop()
    prev = self.get(index - 1)
    temp = prev.next
    prev.next = temp.next
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
      temp.next = before
      before = temp
      temp = after

    return True
  
# Interview questions
  def find_middle_node(self):
      slow = self.head
      fast = self.head
  
      while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next
  
      return slow.value  
  
  def has_loop(self):
    slow = self.head
    fast = self.head
    
    list_has_loop = False
    
    while fast is not None and fast.next is not None:
        fast = fast.next
        if fast == slow:
            list_has_loop = True
            break
        else:
            fast = fast.next 
        slow = slow.next
    
    return list_has_loop
  
  def find_kth_from_end(self, k):
    slow = self.head
    fast = self.head

    for _ in range(k):
      if fast is None:
        return None
      fast = fast.next


    while fast is not None:
      slow = slow.next
      fast = fast.next

    return slow

  def reverse_between(self, m, n):
      if self.head is None or self.length == 1:
          return None  
          
      dummy_node = Node(0)
      dummy_node.next = self.head
      
      prev = dummy_node
      
      for i in range(m):
          prev = prev.next
  
      current = prev.next

      for i in range(n - m):
          temp = current.next
          current.next = temp.next
          temp.next = prev.next
          prev.next = temp
  
      self.head = dummy_node.next
    

my_linked_list = LinkedList(4)
my_linked_list.append(15)
my_linked_list.append(129)
my_linked_list.append(2098)
my_linked_list.append(5077) 
my_linked_list.append(651) 

print(my_linked_list.print_list())
print(my_linked_list.find_middle_node())

print(my_linked_list.has_loop()) # Returns False
# my_linked_list.tail.next = my_linked_list.head
# print(my_linked_list.has_loop()) # Returns True

my_linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
my_linked_list.print_list()

# print(my_linked_list.print_list())

# my_linked_list.pop()
# print(my_linked_list.print_list())

# my_linked_list.prepend(1)
# print(my_linked_list.print_list())

# my_linked_list.pop_first()
# print(my_linked_list.print_list())

# print(my_linked_list.get(2))

# my_linked_list.set_value(1, 188)
# print(my_linked_list.print_list())

# my_linked_list.insert(2, 77)
# print(my_linked_list.print_list())
# my_linked_list.insert(0, 1)
# print(my_linked_list.print_list())

# my_linked_list.remove(4)
# print(my_linked_list.print_list())

# my_linked_list.reverse()
# print(my_linked_list.print_list())

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# # Returns None
# print(my_linked_list.pop_first())

