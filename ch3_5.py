"""
กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  
แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น 
ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) 
กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น 
และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป

เขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :   A  <Heights>  ความสูงของต้นไม้,   B  คือการหันมามอง,    S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case : กฤษฎาจะเดินผ่านต้นไม้ความสูง 4 ก่อนแล้วตามด้วย 3 แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น 
                  ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  
                  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

ความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def Hallu(self):
        #ใช้คำสั่งใน Stack() เพราะไม่ใช่ประเภท Stack
        self.temp = []
        for e in s.items:
            if e%2 != 0:
                self.temp.append(e+2)
                print('eOdd = ', e)
            else:
                self.temp.append(e-1)
                print('eEven = ', e)
        self.items = self.temp
        return self.items

x = input("Enter Input : ").split(",")
y = []
new_x = []
for i in x:
    y = i.split()
    new_x.extend(y)

s = Stack()

for i in range(len(new_x)):
    if new_x[i] == 'A':
        s.push(int(new_x[i+1]))

    if new_x[i] == 'B':
            
        # for j in range(len(s.items) -1):
            j = 0
            # print(s.items,s.items[j],s.items[j+1],j)
            while not s.isEmpty() and s.items[j] < s.items[j+1]:
                s.pop()
                j +=1
                
                # print(s.items)
            print(len(s.items))

    if new_x[i] == 'S':
        s.Hallu()
                

        # if int(new_x[i+1])%2 != 0:
        #    new_x[i+1] = int(new_x[i+1]) + 2
        # #    print(new_x[i+1])
        # elif int(new_x[i+1])%2 == 0 and int(new_x[i+1]) > 1:
        #     new_x[i+1] = int(new_x[i+1]) - 1
        #     # print(new_x[i+1])