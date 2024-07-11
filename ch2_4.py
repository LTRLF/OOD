x = [int(e) for e in input("Enter Your List : ").split()]
result = []
if len(x) < 3:
    print("Array Input Length Must More Than 2")
    exit()
temp = []

for e in range(0,len(x)):
    if len(temp) == 3:
        result = [[-5, 5, 5]]
        print(result)
        exit()
    if x[e] == 5 or x[e] == -5:
        temp.append(x[e])

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        for k in range(j+1,len(x)):
            if x[i]+x[j]+x[k] == 5 :
                result.append([x[i],x[j],x[k]])  
print(result)
