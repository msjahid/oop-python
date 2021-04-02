//---------------------integer sort-----------------------
data = []
data.insert(0, 8)
data.insert(1, 80)
data.insert(2, 17)
data.insert(3, 4)
data.insert(4, 90)
print("Before Sorting")
for i in data:
    print(i)

print("After Sorting")
for i in sorted(data):
    print(i)

//------------------------Float Sort-------------------------------

doubleList = [3.2, 2.14, 43.24, 66.23, 1.2, 5.6, 23.1, 34.2, 123]
print("Before Sorting")
for i in doubleList:
    print(i)

print("After Sorting")
for i in sorted(doubleList):
    print(i)

//--------------------------String Sort-------------------------------------------

stringList = ["Monkey", "Donkey", "Wolverine", "Elephant", "Lion", "Lamb"]
print("Before Sorting")
for i in stringList:
    print(i)

print("After Sorting")
for i in sorted(stringList):
    print(i)
