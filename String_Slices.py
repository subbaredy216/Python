Subba = "Garem Venkata Subba Reddy"
print(Subba[2])
#Syntax -- variable[start:end:step]
print(Subba[0:5:1])
# If the end is blank, default it will take till end
print(Subba[0::1])
#If start is blank, Default is 0
print(Subba[::1])
#We can reverse the string
print(Subba[::-1])
#End can start with -1
print(Subba[-1])
print(Subba[Subba.index("Subba"):Subba.index("Reddy"):1])
#index will always gives the first instance
print(Subba[Subba.index("Venkata"):Subba.index("a"):1])
