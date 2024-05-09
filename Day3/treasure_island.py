print("The Haunted Manor. \nYou find yourself standing in front of a decrepit old manor, its windows boarded up and ivy creeping up the crumbling walls. Despite the warnings from locals about its haunted reputation, you feel compelled to investigate.")

first_pick = input("Do you Enter the manor through the front door(yes)?  or Turn around?(no): ")
if first_pick == "yes":
    print("You cautiously push open the creaking front door and step into the darkness of the manor's foyer. The air feels heavy with the weight of years gone by. Suddenly, you hear a faint whisper coming from the staircase.")

    second_pick = input("Do you Investigate the source of the whisper?(yes) or Walk back out?(no) ")
    if second_pick == "yes":
        print("You follow the sound of the whisper up the staircase, each step groaning under your weight. At the top, you find a dusty old mirror that seems to shimmer with an otherworldly light. Suddenly, your reflection begins to speak, revealing secrets of the manor's past.")

        if second_pick == "yes":
            print("You went mad at the sight of your reflection speaking to you.")
        else:
            print("You found a balcony and jump off. You died. Game Over.!!!")
    else:
        print("You attempted to walk out but fell in a hole. Game over!!")
else:
    print("GAME OVER!!!.You decided to go home")


