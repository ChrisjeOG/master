#asking for the names
name_1 = input("What is your name? ")
name_2 = input("What is your lovers name? ")

#lowering the letters
name_1 = name_1.lower()
name_2 = name_2.lower()

#deleting the spaces
name_1 = name_1.strip()
name_2 = name_2.strip()

#this is the basic assignment 
#if name_1 == name_2:
#    print("Match made in heaven")

#elif name_1 > name_2:
#    print("Matchiematchie")

#else:
#    print ("Neup, download tinder")

#Count the letters
count_name_1 = len(name_1)
count_name_2 = len(name_2)
count_dif = abs(count_name_1 - count_name_2)

#turning it into %
if count_dif == 0:
    print("You're a 100% match")
elif count_dif == 1:
    print("You're a 80% match")
elif count_dif == 2:
    print("You're a 60% match")
elif count_dif == 3:
    print("You're a 40% match")
elif count_dif == 4:
    print("You're a 20% match")
elif count_dif == 5:
    print("You're a 10% match")
else:
    print("Download Tinder,Grindr or She")




#onderstaand is uitgebreide versie van letterstellen
#count_name_1 = 0
#count_name_2 = 0

#for i in name_1:
#    count_name_1 += len(i)

#for i in name_2:
#    count_name_2 += len(i)
