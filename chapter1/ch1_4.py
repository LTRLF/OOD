"""
เขียนภาษา Python เพื่อวาดพีระมิด ซึ่งจะรับ input เป็นขนาดของพีระมิด โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

*** Fun with Drawing ***
Enter input : 5
#################
#...............#
#.#############.#
#.#...........#.#
#.#.#########.#.#
#.#.#.......#.#.#
#.#.#.#####.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#.#.#.#.#.#


#.#.#.#...#.#.#.#
#.#.#.#####.#.#.#
#.#.#.......#.#.#
#.#.#########.#.#
#.#...........#.#
#.#############.#
#...............#
#################

"""

print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
row = (x-1)*2
col = ((x-1)*4)+1

for i in range(row):
    for j in range(col):
        if j <= i:
            if j%2 != 0:
                print(".",end='')
            else:
                print("#",end='')

        elif i+j < col-1:
            if i%2 != 0:
                print(".",end='')
            else:
                print("#",end='')

        elif i+j >= col-1:
            if j%2 != 0:
                print(".",end='')
            else:
                print("#",end='')
    print("")
for i in range(row+1):
    for j in range(col):
        if j+i < row:
            if j%2 != 0:
                print(".",end='')
            else:
                print("#",end='')
        elif j-i < row:
            if i%2 != 0:
                print(".",end='')
            else:
                print("#",end='')
        else:
            if j%2 != 0:
                print(".",end='')
            else:
                print("#",end='')
    print("")
