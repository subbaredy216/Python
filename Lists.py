#lists
subba = [216, "Reddy", True, False]
print(subba[0])
print(type(subba))
print(subba[-1])
# syntax to retuurn multiple values from list
#list[start:end:step]
print(subba[1:3])
#list can have a list inside the list
reddy = ["Garem",subba,"kanna"]
print(reddy[1])
#syntax to return values list withing the list is list[masterindex][childindex]
print(reddy[1][1:3:2])

# we can add list with another list
a = [1, 2, 3]
print(a+[1])
print(list("ABC"))
#insert will be used to add te item in the list at a particular position
a = a.insert(1,4)
print(a)
