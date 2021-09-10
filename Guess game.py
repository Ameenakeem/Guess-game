win = 0
lose = 0
while True:
    import random
    comp = random.randint(1,5)     

    choose = int(input("Guess any number 1-5: "))
    if comp == 1:
        print("bot = 1")
    elif comp == 2:
        print("bot = 2")
    elif comp == 3:
        print("bot = 3")
    elif comp == 4:
        print("bot = 4")
    elif comp == 5:
        print("bot = 5") 



    if comp == 1 and choose == 1:
        print("You win")
        win = +1 
    elif comp == 2 and choose == 2:
        print("You win")
        win = +1
    elif comp == 3 and choose == 3:
        print("You win")
        win = +1
    elif comp == 4 and choose == 4:
        print("You win")
        win = +1
    elif comp == 5 and choose == 5:
        print("You win")
        win = +1
    else:
        print("You lose")
        lose = +1

    print('''(a) Score
(b) Continue
(c) Quit''')
    ch = input("Decide please: ") 
    if ch == "a":
        print("win = ",win," and lose = ",lose,)
    elif ch == "b":
        continue
    elif ch == "c":
        break
    else:
        print("invalid input")
        exit()
    
