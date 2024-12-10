import random
import time

#Global Variables
player_health=100
treasure_found=False
inventory=[]

#Function to Display Game Status
def display_position():
    print(f"\n Health : {player_health} ")
    print(f" Inventory : {inventory} ")
    print(f" Treasure Found : { 'Yes' if treasure_found else 'No'}\n ")

#Function to game over
def game_over():
    print("\n Game Over! Best of Luck For Nest Time. ")
    exit()

#Function to Encounter Enemy
def encounter_enemy():
    global player_health
    print("\n An Enemy Appeared ")
    choice=input(" (1) Do You Want to Fight or (2) You Want to Run Away to Save Yourself? ")
    if choice==" 1 ":
        if " sword " in inventory:
            print(" You Fought Bravely and Kill The Enemy With Your Sword! ")
        else:
            print(" You Fought Bravely, But You Got Hurt So Much. ")
            player_health -= 30
            if player_health<=0:
                game_over()
    elif choice==" 2 ":
        print(" You Run Away Safely, But The Enemy Attacked You So Much and You Lost Some Energy.                                                 ")
        player_health-=10
        if player_health<=0:
            game_over()
    else:
        print(" Invalid Choice. The Enemy Attacked You. ")
        player_health=20
        if player_health<=0:
            game_over()

#Function To Explore The Forest
def eplore_the_forest():
    global treasure_found
    print("\n You are Eploring The Forest...  ")
    time.sleep
    encounter=["Nothing", " Enemy ", " Treasure ", " Item "]
    result= random.choice(encounter)

    if result== " Nothing ":
        print(" You Found Nothing Here. Try Again. ")
    elif result== " Enemy ":
        encounter_enemy()
    elif result== " Treasure ":
        print(" Congratulations You Found The Treasure! You Win! ")
        treasure_found=True
    elif result== " Item ":
        item=random.choice[" potion ", " sword "]
        print(" \n You Found {item}! ")
        inventory.append(item)


#Function to Display Game Name
def game_name():
    print("\n Welcome To Random Treasure Hunt Game. ")
    print(" Your Mission is To Find Treasure Hidden In The Forest. ")
    global treasure_found
    while not treasure_found:
        display_position()
        print("\n What Do You Have In Mind? ")
        print(" 1. Vanture Into The Forest. ")
        print(" 2. Activate A Potion ( If Available). ")
        print(" 3. Leave The Game. ")

        choice=input(" Enter Your Choice: ")
        if choice== " 1 ":
            eplore_the_forest()
        elif choice== " 2 ":
            if " potion " in inventory:
                print(" By Using Potion, You Restored Your Health. ")
                player_health=100
                inventory.remove(" potion ")
            else:
                print(" There are No Position in Your Inventory. ")
        elif choice== " 3 ":
            print(" Thanks For Playing. Good Bye!" )
            break
        else:
            print(" Invalid Choice. Please Try Again. ")
    else:
        print(" Congratulations! You Completed The Game. ")



#Start The Game
if __name__== "__main__":
    import random
    game_name()