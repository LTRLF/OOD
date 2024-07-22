"""
สมชายกำลังนั่งคิดโจทย์ Linked list อยู่ด้วยความจนปัญญาสมชายที่คิดเนื้อเรื่องของโจทย์ไม่ออกสมชายก็เลยให้โจทย์มาเลยแบบไม่มีเนื้อเรื่องเท่าไหร่ว่าให้สร้าง linked list ที่รับค่า input เป็นตัวเลขเข้ามาแล้วใส่ลง linked list จากนั้นทำการลบเลขที่ซ้ำทั้งหมดออกไปโดยเหลือตัวแรกสุดไว้ เช่น 

Input 1 2 3 2 2 

Output 1 2 3 โดยตัดเอาเลข 2 สองตัวท้ายออก
ซึ่งมาถึงจุดนี้สมชายก็ไม่รู้จะเขียนอะไรต่อแล้วที่เหลือน้องๆก็ไปเขียนโปรแกรมกันเองนะสู้ๆ

**อย่าลืมเขียนให้เหมือนข้างล่าง

Enter Input : 1 2 3 4 5
Linked list now is 1 2 3 4 5 
there are 0 duplicates that been remove
Remove duplicates Linked list 1 2 3 4 5 

"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class List():
    def __init__(self):
        self.head = None

    def append(self, data):
        p = Node(data)
        if self.head == None: #null list
            self.head = p   # เพิ่มเข้าไปใน list
        else:               # มีค่าอยู่ใน list อยู่แล้ว
            t = self.head   # ให้ t(ail) เริ่มที่หัว (head) ของลิส
            while t.next != None: #ถ้าค่าต่อไปในลิสต์ไม่ใช่องว่าง
                t = t.next  # ให้ t เลื่อนไปช่องถัดไป
            t.next = p      # เมื่อช่องต่อไปเป็นช่องว่างให้เพิ่มช่องต่อไปเป็น nodeตัวที่เพิ่มเข้ามา 
        
    def delete(self, data):
        if self.head != None:
            p = self.head
            while p.next != None:
                if p.next == data:

            


x = [int(e) for e in input("Enter Input : ").split()]
print("Linked list now is ", end='')
[print(e, end=' ') for e in x]

n = Node()
lst = List()

for i in 