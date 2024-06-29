name= input("Eneter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end. You can go left or right. Which way would you like to go?").lower()

if answer== "left":
    answer= input("You've come to a river, you can walk around it or swin across! Type 'walk' to walk around and 'swim' to swim across: ")
    
    if answer=="swim":
        print("You swam across and were eaten by an alligator.")
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else: 
        print("Not a valid option. You lose!")

elif answer=="right":
    answer = input("You've come to a bridge, it looks woobly, do you want to cross it or head back (cross/back)?")
    if answer=="back":
        print("You you have gone back to the main road and lost. ")
    elif answer=="cross":
        talk_stranger=input("You cross the bridge and meet a stranger. Do you wish to talk to them (yes/no)?")
        if talk_stranger=="yes":
            print("You talked to the stranger and they gave you gold! You win!!!")
        elif talk_stranger =="no":
            print("You ignored the stranger and you lost the game")
        else: 
            print("Not a valid option. You lose!")

    else: 
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)