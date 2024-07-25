class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class noTailList():
    def __init__(self):
        temp = Node()
        self.head = temp
        self.size = 0

    def append(self, x):
        ins = Node(x,None)
        cur = self.head
        for i in range(self.size):
            cur = cur.next
        cur.next = ins
        self.size +=1


class tailList():
    def __init__(self):
        temp = Node()
        self.head = temp
        self.tail = temp
        self.size = 0

    def append(self, x):
        ins = Node(x,None)
        cur = self.tail
        cur.next = ins
        self.size +=1



def append(self, data):
        p = Node(data, None)
        if self.head == None: #null list
            self.head = p   # เพิ่มเข้าไปใน list
        else:               # มีค่าอยู่ใน list อยู่แล้ว
            t = self.head   # ให้ t(ail) เริ่มที่หัว (head) ของลิส
            while t.next != None: #ถ้าค่าต่อไปในลิสต์ไม่ใช่องว่าง
                t = t.next  # ให้ t เลื่อนไปช่องถัดไป
            t.next = p      # เมื่อช่องต่อไปเป็นช่องว่างให้เพิ่มช่องต่อไปเป็น nodeตัวที่เพิ่มเข้ามา 
        

        

        

