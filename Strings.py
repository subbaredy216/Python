print("Subbareddy".count("d"))
X = "subbareddy".upper()
print(X)
Y = X.lower()
print(Y)
Z = Y.capitalize()
print(Z)
print(Y.title())
print(Z.istitle())

a = "1"
print(a.isalpha())

b = "123"
print(b.isdigit())

c = "Subbu216"
print(b.isalnum())

#index&find function
print("Subba is a good boy".find("is"))
#find will give -1 if String is not available
print("Subba is a good boy".find("how"))
print("Subba is a good boy".index("good"))
#index will throw error is String is not availabe
#print("Subba is a good boy".index("how"))

#Strip
i = "+++++Subba++++++"
print(i.strip("+"))
print(i.lstrip("+"))
print(i.rstrip("+"))
#the below will delete the blank spaces
j = input("What is your name")
print(len(j))
j = j.strip()
print(j)
print(len(j))
      
