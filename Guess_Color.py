# Author: Ahmad_Ibrahim_AbuDanckash

import random,string as st
x = ["red","yellow","green","black","white","gray","orange","brown","pink","rose","golden","violet","grey","olive","indigo"]
random.shuffle(x)
# select the random color
x1=random.choice(x)
# create the _ for characters number
lst = ["_" for i in x1]
num = len(x1)
print("\aThis game depends on sellection random color and giving the user attempts by the characters number double")
print("\nThe word consists of",num,"letters.")

# giving the user attempts by the characters number double
num*=2
print("You have",num,"attempts.")
z=[]
while num:
    chose = input("\nPlease, enter a character: ").lower().strip()
    while len(chose)!=1 or (chose not in st.ascii_letters):
        chose = input("Your input is not valid.\nPlease, enter a one character: ").lower().strip()

    if chose not in z:
        num-=1
    z.append(chose)
    print("You chose "," ".join(z))
    if chose in x1:
        c=-1
        for n in x1:
            c+=1
            if n == chose:
                lst[c]=n
    else:print("Best guess!")
    #check winer
    if "_" not in lst:
        print("The word was ",x1,"""\n
               **********
                You Win!
               **********\n""")
        break
    #print the rest characters
    print(" ".join(lst),f"\n{num} attempts left.")
    if not(num):
        print("good Luck!\nThe word was ",x1)
print("Thanks fot using my program. See You Soon!")
# Thanks fot reading my code. See You Soon!
