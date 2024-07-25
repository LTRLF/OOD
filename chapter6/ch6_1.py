"""
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
ให้เขียน Recursive หาค่า Max ของ Input

Enter Input : 8 7 10 1 5 4 2 6 3 9
Max : 10
"""

x = [int(e) for e in input("Enter Input : ").split()]

def findMax(x):
    if len(x) == 1:
        return x[0]
    
    mid = len(x) //2
    rightMax = findMax(x[mid:])
    leftMax = findMax(x[:mid])

    return max(leftMax, rightMax)

print("Max :", findMax(x))