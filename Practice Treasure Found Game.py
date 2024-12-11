def introduction():
    print(" Welcome to the Treasure Found Hunt Game. ")
    print(" Your Mission is to Found Hidden Treasure into The Forest. ")
    print(" Be Careful Among the Alone Way. ")
    print("\n")

def explore_area(location):
    if location == "north":
        print(" There is North Area and a River With Shiny Objects. ")
        return "shiny objects"
    elif location == "east":
        print(" There is East and Marking Strange Thigs. ")
        return "marking"
    elif location == "south":
        print(" There is South and a Dense Forest. ")
        return "dense forest"
    elif location == "west":
        print(" There is West and a Dark Cave. ")
        return "cave"
    else:
        print(" Invalid Choice. Please Select The Correct Location. ")
        return None
    

def check_treasure(found_item):
    if found_item == "shiny objects":
        print(" Congratulations. You Found The Treasure. ")
        return True
    elif found_item == "marking":
        print(" You Found The Strange Things But Not Found The Treasure. ")
        return False
    elif found_item == "dense forest":
        print(" Oh No, You Lost The Dense Forest and Lost Some Energy. ")
        return False
    elif found_item == "cave":
        print(" You Found An Empty Dark Cave. ")
        return False
    else:
        print(" You Found Nothing. Please Select Correct Direction. ")
        return False
    

def play_game():
    introduction()
    treasure_found_status=False

    while not treasure_found_status:
        print(" Where Would You Like To Go?(north/east/south/west)")
        direction=input(" Enter Your Choice: ").strip().lower()
        found_item=explore_area(direction)
        if found_item:
            treasure_found_status=check_treasure(found_item)

play_game()