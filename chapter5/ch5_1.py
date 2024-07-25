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
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class List():
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        cur = self.head
        s = ''
        for i in range(self.size):
            s += str(cur.next.data) + ' '
            cur = cur.next
        return s

    def append(self, data):
        inp = Node(data, None)              
        cur = self.head
        while cur.next != None:
            cur = cur.next  
        cur.next = inp
        self.size += 1
        
    def delete(self, data):
        inp = self.head
        while inp.next != None:
            if inp.next == data:
                inp.next = inp.next.next
        self.size -= 1
                     
    def isEmpty(self):
         return self.head.next == None
    
    def dup(self):
        count = 0
        #cur ชี้ตัวแรก
        cur = self.head
        #ถ้าตัวแรกและตัวต่อไปไม่เป็นค่าว่าง
        while cur and cur.next != None:
            #สร้าง post ขึ้นมาไล่เช็คจากตัวแรกสุด
            post = self.head
            found = False
            #ถ้าpost ยังวิ่งไปไม่ถึง cur.next (check ที่ object)
            while post is not cur.next:
                #check data
                if post.data == cur.next.data:
                    #ให้ cur.next ชี้ไปที่ตัวถัดไป
                    cur.next = cur.next.next
                    count+=1
                    self.size -=1
                    #ดักว่าถ้าเจอตัวซ้ำไม่ให้ cur วิ่งต่อ
                    found = True
                #ให้ post วิ่งต่อ
                post = post.next
            #ถ้าไม่เจอให้วิ่งต่อ
            if not found:     
                cur = cur.next
        #เอาค่าออกมาแสดงทีหลัง
        return count


x = [int(e) for e in input("Enter Input : ").split()]
print("Linked list now is ", end='')
[print(e, end=' ') for e in x]
print(end="\n")

lst = List()

for i in x:
    lst.append(i)

# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         if x[j] == x[i]:
#             lst.delete(x[j])
#             # count +=1

print(f"there are {lst.dup()} duplicates that been remove")
            
print("Remove duplicates Linked list", lst)



# print(f"there are", 0, "duplicates that been remove")