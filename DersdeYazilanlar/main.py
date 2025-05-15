list1 = ["*"]
for i in range(1, 4):
    list1.append(" " + str(i))

list2 =  ["a"]
for i in range(1, 4):
    list2.append(" " + str("x"))

list3 = ["b"]
for i in range(1, 4):
    list3.append(" " + str("x"))

list4 = ["c"]
for i in range(1, 4):
    list4.append(" " + str("x"))

print(''.join(list1))
print(''.join(list2))
print(''.join(list3))
print(''.join(list4))

