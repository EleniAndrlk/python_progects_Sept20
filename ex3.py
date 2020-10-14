word_given = input("Enter a word:")

# dimiourgia listas me ola ta grammata ths lexis poy dothike
letters_list=[]
for letter in word_given:
    letters_list.append(letter)
print(letters_list)

# words_list periexei mia lista keni gia kathe pithani lexi apo ta grammata tis letters_list
words_list =[]
for i in range(2**len(word_given)):
    words_list.append([])
print(words_list)

# oso oi paragomenes lexeis einai mikroteres apo auti poy dothike 
while len(words_list[0]) != len(word_given):
    i=0
   
    # se kathe lexi(lista) ths words_list ginetai prosthiki tou grammatos poy antistoixei se ayti ti thesi me basi to mod 
    for word in words_list:
        index_of_letter = i %(len(word_given))
        letter = letters_list[index_of_letter]
        word.append(letter)
        i+=1
      
    print(letters_list[-1])
    # anadiataxi listas to teleutaio gramma ginetai prvto
    letter_one = letters_list[-1]
    print("1: ",letter_one)
    other_letters = letters_list[0:-1]
    print("other: ",other_letters)
    letters_list.clear()
    letters_list.append(letter_one)
    for letter in other_letters:
        letters_list.append(letter)

    print("lust",letters_list)
print(words_list)
