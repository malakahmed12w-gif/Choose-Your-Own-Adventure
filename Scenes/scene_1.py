# scene_1.py
def play_scene():
    """
    Scene 1:
    - Section A: Player chooses to 'explore' or 'exit'.
    - Section B: Player chooses to 'follow' a noise or 'ignore' it.
    - Returns the name of the next scene ("scene_2") or "quit".
    """
    
    print("\n=== SCENE 1 ===\n")
    print("You awaken in a dimly lit, ancient library. The air is thick with dust, and the scent of old parchment fills your lungs.")
    print("Moonlight spills through cracks in the ceiling, revealing shelves lined with forgotten tomes.")
    print("A strange silence presses down on you.\n")

    # Section A - First choice
    while True:
        choice_a = input("Do you want to 'explore' the library or 'exit' through a nearby hallway? ").lower().strip()
        if choice_a == "explore":
            print("\nYou wander between towering bookshelves, your fingers brushing against faded titles.")
            print("You discover a strange book with glowing runes—it hums softly in your hands.")
            break
        elif choice_a == "exit":
            print("\nFeeling uneasy, you quickly head toward the hallway, the shadows seeming to follow you.")
            print("But before you can get far, a distant noise echoes behind you...")
            break
        else:
            print("Invalid choice. Please type 'explore' or 'exit'.")

    # Transition to Section B
    print("\n--- Moving to Section B of Scene 1 ---\n")
    print("You hear a faint, rhythmic thumping—like footsteps, but not quite human—echoing in the distance.")
    print("The sound seems to be coming from deeper within the library...\n")

    # Section B - Second choice
    while True:
        choice_b = input("Do you choose to 'follow' the strange noise or 'ignore' it and stay put? ").lower().strip()
        if choice_b == "follow":
            print("\nYou move cautiously toward the sound, every step amplifying your unease.")
            print("The air grows colder as you enter a long, dark corridor filled with whispering echoes.")
            return "scene_2"
        elif choice_b == "ignore":
            print("\nYou remain still, trying to calm your nerves.")
            print("Just then, a hidden door nearby creaks open on its own, revealing a passage you hadn't noticed...")
            return "scene_2"
        else:
            print("Invalid choice. Please type 'follow' or 'ignore'.")

