#remove will be used when we know particular name/vaue in the list
#del can used to delete from the index when you knows the index and not the values
#Syntax of del is del(list[index])
clos_frnds = ["Sukan","Shiva","Kasi","Ramya","Trinath","Praveen","Nitheesh"]
while True:
    name = input("What is your name:").strip().capitalize()
    if name in clos_frnds:
        print("{} is there in your frnds list".format(name))
        remove = input("Do you remove from list(Y/N)").strip().lower()
        if remove == "y":
            print(clos_frnds)
            clos_frnds.remove(name)
            print(clos_frnds)
        break
    else:
        print("{} is there in not your frnds list".format(name))
        added = input("Would you like to add in the list(Y/N)").strip().lower()
        if added == "y":
            print(clos_frnds)
            clos_frnds.append(name)
            print(clos_frnds)


    
