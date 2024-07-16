"""
จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ string.items ที่รับมาโดยให้ทำเป็นรูปแบบ Queue
รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string.items ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ string.items ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก 
หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 
ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน string.items ครบ 
ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร 
เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ string.items เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string.items)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)

Enter string.items and Code : i love Python,256183
Encode message is :  ['k', 'q', 'u', 'w', 'm', 'S', 'a', 'y', 'n', 'p', 'v']
Decode message is :  ['i', 'l', 'o', 'v', 'e', 'P', 'y', 't', 'h', 'o', 'n']

"""

class Queue():
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
             self.items = lst
    
    def enqueue(self, i):
        self.items.append(i)
    
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

def decodemsg():
        pass

def encodemsg(string, number):
    lst = []
    num = 0
    for i in range(len(string.items)):
        #check ว่า string.items ที่รับมาอยู่ในช่วงที่กำหนดหรือไม่
        if 'a' <= string.items[i] <= 'z' or 'A' <= string.items[i] <= 'Z':
            new_str = ord(string.items[i])
            if num > (len(number.items)-1):
                num = 0
            #ถ้าค่าตอนแรกน้อยกว่า Z (อยู่ในช่วงของตัวใหญ่ ทำเพื่อเช็คเคสตัวใหญ่) และ บวกแล้วเกิน Z หรือ ค่าเดิมบวกแล้วเกินค่า z (ค่าตัวเล็ก)
            if (new_str <= ord('Z') and new_str + int(number.items[num]) > ord('Z')) or (new_str + int(number.items[num]) > ord('z')):
                # print(f"old: {chr(new_str)}")
                new_str -= 26  
                # print(f"new: {chr(new_str)}")
            lst.append(chr(new_str + int(number.items[num])))
            num+=1
    return lst
    # chr(65)
    # 'A'
    # ord(p)
    # 112
    # chr(ord('S') + 1)
    # 'T'

string, number = input("Enter string and Code : ").split(",")

q1 = Queue(string)
q2 = Queue(number)

print(encodemsg(q1, q2))
# decodemsg(q1, q2)

# c = Cipher()