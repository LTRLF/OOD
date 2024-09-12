"""
จงเขียนโปรแกรมเพื่อรับข้อมูล แล้วสร้าง AVL tree และแสดงการแวะผ่านโหนดต่าง ๆ แบบ post-order

โดยแก้ไข 
method add       คือการเพิ่มข้อมูลเข้าใน AVLTree 
method postOrder คือ บริการแวะผ่านโหนดทุกโหนดแบบหลังลำดับ 
จากส่วนของโปรแกรมต่อไปนี้

Enter Input : AD 10,AD 5,AD 15,PR,PO,AD 20,AD 8,PR,PO
      15
 10
      5

AVLTree post-order : 5 15 10 
           20
      15
 10
           8
      5

AVLTree post-order : 8 5 20 15 10 
"""

class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a,b)
            return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.right) - self.getHeight(self.left)


    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        pass
        # code here

    def _add(root, data):
        pass
        # code here

    def rotateLeftChild(root) :
        pass
         # code here

    def rotateRightChild(root) :
        pass
          # code here  

    def postOrder(self):
        pass
         # code here

    def _postOrder(root):
        pass
         # code here

    def printTree(self):
        AVLTree._printTree(self.root)
        print()  

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":   #Add
        avl1.add(i[3:])

    elif i[:2] == "PR": #Print
        avl1.printTree()

    elif i[:2] == "PO": #Post
        avl1.postOrder()