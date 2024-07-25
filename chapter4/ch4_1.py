'''
 * กลุ่มที่  : 24010117
 * 66010942 อิสรีย์ นิศยันต์
 * chapter : 4	item : 1	ครั้งที่ : 0001
 * Assigned : Thursday 11th of July 2024 01:58:29 PM --> Submission : Thursday 11th of July 2024 03:25:26 PM	
 * Elapsed time : 86 minutes.
 * filename : ch4_1.py
'''
"""
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E <value> ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE
D         ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1
*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

Enter Input : E 10,E 20,E 30,E 40,D,D
1
2
3
4
10 0
20 0
30 40
"""

x = (input("Enter Input : ").split(","))
y = []
new_x = []
queue = []
#loop for separating E and number
#'E 10' -> 'E', '10'
for i in x:
    y = i.split()
    # เอา ทั้งlist ไปยัดในอีกlist ให้เป็น list เดียวกัน
    new_x.extend(y)

for i in range(len(new_x)):
    if new_x[i] == "E":
        queue.append(new_x[i+1])
        print(len(queue))

    elif new_x[i] == "D":
        if len(queue) > 0:
            print(queue[0], "0")
            queue.pop(0)
        else:
            print("-1")

if len(queue) > 0:
    for i in queue:
        print(i, end=" ")
else:
    print("Empty")