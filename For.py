let = input("Please enter the wor")
vowels = 0
consonants = 0
for letter in let:
    if letter.lower() in "aeiou":
        vowels = vowels+1
    elif letter =="":
        pass
    else:
        consonants = consonants+1
print("there are {} vowels".format(vowels))
print("there are {} consonants".format(consonants))

friends = {
    "male":["shiv","praveen","nitheesh"]
    "female":["sukan","kasi","ramya"]
    }
for key in friends.keys():
    print(friends.key)
        
