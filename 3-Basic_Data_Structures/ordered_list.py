#implementing orderedlist using node class

from node import Node

class OrderedList:
  def __init__(self):
    self.head = None
  
  def is_empty(self):
    return not self.head

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.get_next()
    return count

  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.get_data() == item:
         found = True
      else:
         if current.get_data() > item:
            stop = True
         else:
            current = current.get_next()
    return found

  def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.get_data() > item:
         stop = True
      else:
         previous = current
         current = current.get_next()

    temp = Node(item)
    if previous == None:
       temp.set_next(self.head)
       self.head = temp
    else:
       temp.set_next(current)
       previous.set_next(temp)
