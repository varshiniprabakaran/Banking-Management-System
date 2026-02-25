class node:
 def __init__(self,key):
  self.key=key
  self.left=None
  self.right=None

def insert(root,key):
 if root is None:
  return node(key)
 if key<root.key:
  root.left=insert(root.left,key)
 else:
  root.right=insert(root.right,key)
 return root
 
def search(root,key):
 if root is None or root.key==key:
  return root
 if key<root.key:
  return search(root.left,key)
 return search(root.right,key)

def inorder(root):
 if root:
  inorder(root.left)
  print(root.key,end="")
  inorder(root.right)

def preorder(root):
 if root:
  print(root.key,end="")
  preorder(root.left)
  preorder(root.right)

def postorder(root):
 if root:
  postorder(root.left)
  postorder(root.right)
  print(root.key,end="")

def display(root,space=0,gap=8):
 if root is None:
  return
 space+=gap
 display(root.right,space)
 print()
 print(" "*(space-gap)+str(root.key))
 display(root.left,space)

root=None
while True:
 print("\n binary search tree")
 print("1.insert, 2.search, 3.inorder, 4.preorder, 5.postorder, 6.display 7.exit")
 choice=int(input("enter your choice:"))
 if choice==1:
  val=int(input("enter value to insert:"))
  root=insert(root,val)
  print(val,"inserted successfully")
 elif choice==2:
  val=int(input("enter value to search:"))
  if search(root,val):
   print(val,"found in tree")
  else:
   print(val,"not found")
 elif choice==3:
  print("inorder:",end="")
  print(root)
  print()
 elif choice==4:
  print("preorder:",end="")
  print(root)
  print()
 elif choice==5:
  print("postorder:",end="")
  print(root)
  print()
 elif choice==6:
  print("/n tree structure:")
  display(root)
 elif choice==7:
  print("thank you")
  break
 else:
  print("invalid")