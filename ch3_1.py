'''
 * กลุ่มที่  : 24010117
 * 66010942 อิสรีย์ นิศยันต์
 * chapter : 3	item : 1	ครั้งที่ : 0001
 * Assigned : Thursday 11th of July 2024 01:06:45 PM --> Submission : Thursday 11th of July 2024 02:25:07 PM	
 * Elapsed time : 78 minutes.
 * filename : ch3_1.py
'''
"""

ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้

def __init__()    // ใช้สำหรับสร้าง list ว่าง

def push(i)        // เก็บข้อมูลลง stack

def pop()          // นำข้อมูลออกจาก stack

def isEmpty()   // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false

def size()         // ตรวจสอบจำนวนข้อมูลใจ stack


แล้วให้โปรแกรมรับข้อมูล เพื่อเก็บใน stack และให้ทำงานตาม code คำสั่งต่อไปนี้

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)

 *** Stack implement by Python list***
Enter data to stack : K M I T L C E 2 5 6 3
11 Data in stack :  ['K', 'M', 'I', 'T', 'L', 'C', 'E', '2', '5', '6', '3']
0 Data in stack :  []
"""

class Stack():
    def __init__(self):    # ใช้สำหรับสร้าง list ว่าง
        self.items = []
        #self.size = 0

    def push(self, i):       # เก็บข้อมูลลง stack
        self.items.append(i)
        # self.size +=1

    def pop(self):         # นำข้อมูลออกจาก stack
        self.items.pop()

    def isEmpty(self):      # ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.items == []

    def size(self):         # ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.items)


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
    s.push(e)
print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.items)