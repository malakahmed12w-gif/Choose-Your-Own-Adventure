

# scene_2.py

def play_scene():
    """
    Scene 2: The Forgotten Path
    Returns the name of the next scene or 'quit'.
    """

    print("\n=== SCENE 2: The Forgotten Path ===")
    print("You follow the trail deeper into the jungle. The trees form a tight canopy overhead,")
    print("casting eerie shadows across the path. A thick fog begins to roll in around your boots.")

    # Section A
    print("\nYou spot an overgrown stone altar just off the trail.")
    choice_a = input("Do you want to 'search' the area or 'move on'? ").lower().strip()

    if choice_a == "search":
        print("\nYou carefully push aside vines and inspect the altar...")
        print("You discover a small leather pouch with a strange green gem inside.")
        print("It hums faintly in your hand. Could it be a piece of the Eye of Zorak?")
    elif choice_a == "move on":
        print("\nYou decide not to waste time and continue down the trail, staying alert.")
    else:
        print("\nYou hesitate, unsure. The fog gets thicker, and you move on by instinct.")

    # Section B
    print("\nAs the trail narrows, you hear a faint noise behind the trees.")
    print("It sounds like chanting... or maybe whispering.")
    choice_b = input("Do you 'investigate' the noise or 'ignore' it and keep going? ").lower().strip()

    if choice_b == "investigate":
        print("\nYou quietly step off the trail and move toward the sound.")
        print("Peering through the brush, you see cloaked figures standing in a circle, humming around a fire.")
        print("Before they notice you, you back away and return to the trail, shaken but unharmed.")
        return "scene_3"
    elif choice_b == "ignore":
        print("\nYou keep your head down and move faster, leaving the strange sound behind.")
        print("Whatever it was... you’re not ready to deal with it yet.")
        return "scene_3"
    else:
        print("\nUnclear action. You pause for a second, then continue down the path.")
        return "scene_3"
play_scene()
