#This program will run a text-based adventure game about escaping Hades’ realm in the Underworld

def intro():
    print("Hello, as you know Zeus sent you on a mission to retrieve his lightning bolt that his brother, Hades, stole and is keeping in the Underworld. You went as instructed and had the lightning bolt in your hand, but as you were leaving, Persephone and her hellhound, Cerberus, caught you. They brought you to Hades, he took back the lightning bolt and threw you into the dungeon. You managed to escape the dungeon, but now must find a way out of hell.")



print()

def slide_path():
    print()
    print("1. Take the right tunnel")
    print("2. Take the left tunnel")
    end = int(input("You walk up to two different tunnels that both seem pretty dark. Which tunnel do you take?"))
    if end == 1:
        print("At first the tunnel was pitch black, but as you walked further in there were beautiful bioluminescent crystals that lit up the tunnel so much so that you could see. As you get closer to the end of the tunnel it’s brighter. You walk through the blinding light and realize you’re on soil, back on Earth. Congrats! You made it out of hell.")
    elif end == 2:
        print("The tunnel is pitch black, you can’t see anything. You feel like there’s something watching you so you start to run. Out of nowhere Cerberus is in front of you and chases you until you accidentally run off the end of the building into the fiery pits of hell")
        exit
    
def left_path():
    print()
    print("1. Take the spiral staircase up")
    print("2. Take the slide down")
    path2 = int(input("You make it out of the hallway and see two different paths. Which do you take?"))
    if path2 == 1:
        print("You walk up the staircase as quietly as possible, but then you find yourself in Hades’ chamber. You hear someone coming and try to hide quickly but Hades finds you and as punishment for trying to escape he throws you off the building and into the deepest, darkest fires of hell.")
        exit
    elif path2 == 2:
        print("You take the slide down, and fall onto the edge of the building, but manage to catch yourself. You start walking, looking for another path that could potentially lead you out.")
        slide_path()
        print()
    
def right_path():
    print()
    print("1. Grab the sword")
    print("2. Grab the nunchucks")
    print("3. Grab the bow and arrows")
    death = int(input("At the end of the path, you end up in the armory. You may need a weapon for later. Which weapon do you take?"))
    if death == 1:
        print("You pick up the sword, it’s heavier than it looks, so you decide to drag it. Hades hears you. He snuck up on you and stabbed you in the gut with the sword.")
        exit
    elif death == 2:
        print("You grab the nunchucks, but since you don’t know how to use them you quickly try to use them. Instead you end up choking yourself. Persephone finds you and helps you out of your predicament and you think she’s helping you escape by telling you where to go. However, you end up in Hades’ chamber and he chokes you with the nunchucks, but right before you pass out he throws you into the river of lost souls where you will suffer for eternity.")
        exit
    elif death == 3:
        print("You grab the bow and arrows, but accidentally drop the quiver of arrows and one stabs you in the foot and you scream in pain. Hades casually walks in laughing, takes an arrow from the floor, then stabs you in the gut and watches as you begin to bleed out.")
        exit
        
def main():
    print("Welcome to Hell Bound")
    print()
    play = 'y'

    while play == 'y':
        intro()
        print()
        print("1. Take path on the left")
        print("2. Take path on the right")
        print("3. Go straight down the hallway")
        path1 = int(input("You find yourself in a hallway with three different paths. Which path do you take?"))
        if path1 == 1:
            print("This path is crawling with spiders and bats that are chasing you, but thankfully you manage to outrun them.")
            left_path()
        elif path1 == 2:
            print("You walk through this path with no issues and you see a light up ahead that you hope is your way out.")
            right_path()
        elif path1 == 3:
            print("You start walking through the path without any problems, but then you fall down a hole into the cage where Cerberus is sleeping. Cerberus wakes up, stares you down, then eats you")
            exit
        print()
        play = input("Would you like to play again? 'y/n'").lower()
        print()
main()

