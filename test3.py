x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mid = len(x) //2
print(x[mid:])
print(x[:mid])


x = [int(e) for e in input("Enter Input : ").split()]

# def Max(fromI, toI):
#     if fromI > toI:
#         return 0
#     elif fromI == toI:      #base case
#         return sorted[0]
#     else:   #fromI < toI    #recursive
#         x = sorted[fromI]
#         y = sorted[toI]

# def Sort(x):
#     if len(x) == 1:
#         return x
    
#     if len(x) >1:
#         mid = len(x) //2
#         leftL = x[mid:]
#         rightL = x[:mid]

#         Mergeleft = Sort(leftL)
#         Mergeright = Sort(rightL)
#         resultMerge = popMin(Mergeleft, Mergeright)

#         return resultMerge

# def Max(x):
#     result = []
#     left = 0
#     right = left+1
#     if x[left] > x[right]: