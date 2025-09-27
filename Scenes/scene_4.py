# scene_4.py

print("\nAs you reach for the orb, the floor beneath you starts to crack.")
choice_4 = input("Do you 'grab' the orb quickly or 'step back' to assess the danger? ").lower().strip()

if choice_4 == "grab":
    print("\nYou snatch the orb just as the floor crumbles beneath you.")
    print("You manage to leap to safety on a stable platform.")
    print("The orb pulses with power in your hand.")
    print("\nCongratulations! You have completed your quest successfully.")
    # return "quit" or next scene
elif choice_4 == "step back":
    print("\nYou hesitate, stepping back slowly.")
    print("The floor gives way, and you fall into a hidden pit.")
    print("Luckily, you survive but lose the chance to take the orb.")
    print("\nGame Over.")
    # return "quit" or game over
else:
    print("\nYou hesitate too long, then quickly grab the orb just as the floor collapses.")
    print("You leap to safety, clutching the glowing prize.")
    print("\nCongratulations! You have completed your quest successfully.")
    # return "quit" or next scene
def play_scene():
    """ Scene 4: The Ancient Chamber        
    Returns the name of the next scene or 'quit'.
    """
    return "quit"