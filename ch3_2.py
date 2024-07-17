"""
นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน
โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่าแตก
จานจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่าหรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว
อ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ ซึ่งรวมถึงขนาดของจานและความถี่ของจาน 
จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด
อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

Enter Input : 1 10,5 20,3 30,3 40,4 50
10
40
30
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self, i = None):
        if i == None:
            return self.items.pop()
        else:
            return self.items.pop(i)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
# input("Enter Input : ").split(",")
# รับ input 1 10,5 20,3 30,3 40,4 50  มาแล้วแยกเป็น ['1 10', '5 20', '3 30', '3 40', '4 50']
# [e.split() for e in input     ("Enter Input : ").split(",")]
# เอาค่าในลิสต์มาแยกออกจากกันโดยใช้ช่องว่าง    ['1 10', '5 20'] -> [['1', '10'], ['5', '20']]
# [[int(j) for j in e.split()]  for e in input("Enter Input : ").split(",")]
# เปลี่ยนค่าข้างในแต่ละลิสต์เล็กๆให้เป็นค่า int    [['1', '10'], ['5', '20']] -> [[1, 10], [5, 20]]
dish = [[int(j) for j in e.split()] for e in input("Enter Input : ").split(",")]

tower = Stack()

for i in range(len(dish)):
    if tower.isEmpty() or tower.items[-1][0] >= dish[i][0]:
        tower.push(dish[i])
    else:
        while not tower.isEmpty() and tower.items[-1][0] < dish[i][0]:
            print(tower.pop()[1])
        tower.push(dish[i])