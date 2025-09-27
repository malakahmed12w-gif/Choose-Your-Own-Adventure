
# scene_1.py

def play_scene():
    """
    Scene 1: Jungle Landing
    - Section A: Explore or Exit the jungle
    - Section B: Follow or Ignore a strange noise
    - Returns the name of the next scene (e.g., "scene_2") or "quit"
    """

    print("\n=== SCENE 1: The Jungle Landing ===")
    print("You step off the rusty cargo plane into the sweltering heat of the jungle.")
    print("Birds chirp. Insects buzz. The trees are dense and the air feels heavy.")
    print("Luis, the pilot, hands you a worn-out map and gives you a nod before flying off.")
    
    # --- Section A: First Choice ---
    print("\nYou look around the clearing where the plane dropped you off.")
    choice_a = input("Do you want to 'explore' the area or 'exit' into the jungle right away? ").lower().strip()

    if choice_a == "explore":
        print("You decide to look around the area, searching for anything of interest...")
        print("After a few minutes, you find a small, abandoned campsite with a fire pit and some old supplies.")
        print("You take a moment to rest and gather your thoughts before heading into the jungle.")
    elif choice_a == "exit":
        print("You decide to leave immediately, feeling uneasy...")
        print("As you step into the dense jungle, the sounds of wildlife surround you.")    