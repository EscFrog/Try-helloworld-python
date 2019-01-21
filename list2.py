list2 = [37, 23, 10, 33, 29, 40]
print(list2)

list2.append(16)
print(list2)

list3 = list2 + [18]
print(list3)

print(4 in list3)

del list3[4]
del(list3[4])
print(list3)

if 23 in list3:
    print(True)
    list3.remove(23)
print(list3)
