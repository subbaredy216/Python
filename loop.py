original = input("please eneter the sentence").strip().lower()
#Split wll dfault using spaces
words = original.split()
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word+"yay"
        new_words.append(new_word)
    else:
        vow_pos = 0
        for letter in word:
           if letter not in "aeiou":
               vow_pos = vow_pos+1
            else:
                break
        cons = word[:vow_pos]
        the_rest = word[vow_pos]
        new_word = the_rest+cons+"yay"
        new_words.append(new_word)
print(new_words)
