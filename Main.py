class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
  def push(self, data) -> None:
    # Write your code here
    new=Node(data)
    new.data=data
    new.next=self.top
    self.top=new
  def pop(self) -> None:
    # Write your code here
    if self.top==None:
      return None
    else:
      temp=self.top
      self.top=self.top.next
      temp.next=None
      return temp
      
      
  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    if self.top==None:
      print("None")
    else:
      ptr=self.top
      while(ptr!=None):
        print(ptr.data,end="")
        print("=>",end="")
        ptr=ptr.next
        if(ptr==None):
          print("None")
          
# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[] == "pop":
    stack.pop()
stack.status()
