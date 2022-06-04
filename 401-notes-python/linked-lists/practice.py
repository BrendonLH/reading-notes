class Node:
  def __init__(self, data):
    self.data = None
    self.next = None
    

class Linked_List: 
  def __init__(self):
    self.head = None

  def insert_node(self, node):
    new_node = Node(node)
    if self.head == None:
      self.head = new_node
    return

if __name__=='__main__':
  list = Linked_List()
  list.insert_node(6)
  print(list.head)