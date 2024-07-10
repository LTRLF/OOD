"""
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา 
โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ 
เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

*** Fun with countdown ***
Enter List : 4 4 5 4 3 2 1 8 3 2 1
[2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
"""

print("*** Fun with countdown ***")
x = [int(e) for e in input("Enter List : ",).split()]
count = 0
cd = []
result = []

#enumerate เอามาทั้ง index และ ค่าข้างใน
#i = ตำแหน่งใน list, num = ค่าในตำแหน่งนั้นๆ
x = [i for i in reversed(x)]
for i, num in enumerate(x):
    if num == 1:
        count+=1
        order = []
        cur = 1
        for j in range(i, len(x)):
            if x[j] == cur:
                cur+=1
                order.insert(0, x[j])
            else:
                break
        cd.insert(0, order)

result.append(count)
result.append(cd)

print(result)

# for i in range(-1,-(len(x)+1),-1):
#     print(x[i])