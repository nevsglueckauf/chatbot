
user_inp = input('Bitte gib was ein: ')
print(user_inp)


meine_liste = ["Hallo", "Python", "wie", "geht's"]
for laufvariable in meine_liste:
    print(laufvariable, " dies ist ein item")

print(meine_liste)



while user_inp != 'end':
    user_inp = input('Gib etwas ein: ')
    #print('Du hast eingegeben: ',  user_inp)
    # Hilfe -> A; Danke ->B, sonst C
    if user_inp == 'Hilfe':
        print("A")
    elif user_inp == 'Danke':
        print("B")
    else:
        print("C")


print('Ende der Diskussion')