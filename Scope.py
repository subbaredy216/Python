#Two types of variabes scope - Global and Local
#In Python, functions create local variables
a = 100
def F1():
    b = 200
    print(a+b)
#for we F2 we get an error as b is local variable of F1
#def F2():
 #   print(a+b)
F1()
#F2()

b = [1,2,3]
def F3():
    b[0] = 10
    print(b)
F3()
print(b)
