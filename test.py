lst = [10, 30, 25, 413, 241]
print([e-99 if 10<e<40 else e for e in lst if 10<e<40 or e>300])

lst = [10, 30, 25, 413, 241]
[print(e-99) if 10<e<40 else print(e) for e in lst if 10<e<40 or e>300]
# 30 25 413 if num<100 = -99

x = 100
# print(x) if x>99 else print("h")