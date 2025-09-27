def show_inventory(inventory):
    print("\n📦 Your Inventory:")
    for item in inventory:
        print(f"- {item}")
    print()

def section_1(inventory):
    print("\n🌲 SECTION 1: Arrival at the Jungle")
    print("""
Your rusty cargo plane touches down on a makeshift runway in the middle of the dense jungle. 
The pilot, a grizzled man named Luis, hands you a crumpled map.

  “The temple’s somewhere west of here. Watch out for traps, wildlife, and... whatever else is still guarding it.”

You shoulder your backpack. Inside are a few items.
    """)

    while True:
        print("\nWhat do you do?")
        print("A. Head west immediately toward the supposed temple location")
        print("B. Climb a tree to scout the area")
        print("C. Search the surrounding area for a guide or any local help")
        print("Type 'inventory' to check your gear.")

        choice = input(">> ").strip().lower()

        if choice == 'a':
            print("\n🧭 You head west, hacking through the jungle with your machete. The heat is oppressive.")
            section_2_west_path(inventory)
            break
        elif choice == 'b':
            print("\n🌴 You climb a nearby tree. From the top, you spot a faint structure to the west and smoke to the north.")
            section_2_tree_path(inventory)
            break
        elif choice == 'c':
            print("\n🧓 You circle back toward a nearby village and find an old local willing to trade guidance for supplies.")
            section_2_village_path(inventory)
            break
        elif choice == 'inventory':
            show_inventory(inventory)
        else:
            print("❗ Invalid input. Please choose A, B, or C, or type 'inventory'.")

def section_2_west_path(inventory):
    print("""
🪓 The jungle thickens. After hours of cutting through vines, you stumble into a clearing. 
Ahead is a dark stone wall, partly covered in moss — it looks like the edge of a ruin.

Suddenly, you hear rustling in the bushes behind you.
    """)
    print("What do you do?")
    print("A. Hide behind a tree and ready your flare gun")
    print("B. Turn and shout to scare off whatever it is")
    print("C. Run straight toward the ruin")

    choice = input(">> ").strip().lower()
    if choice == 'a':
        print("\n🔥 You fire the flare — it scares off a jungle cat stalking you. The flare is now gone.")
        inventory.remove("Flare gun with 1 flare")
        section_3_ruin_entrance(inventory)
    elif choice == 'b':
        print("\n🗣️ Your shout startles a jungle cat — it lunges at you! You manage to fight it off but suffer a wound.")
        inventory.append("Wounded arm")
        section_3_ruin_entrance(inventory)
    elif choice == 'c':
        print("\n🏃 You sprint toward the ruin and trip a vine — a dart shoots past your head. That was close.")
        section_3_ruin_entrance(inventory)
    else:
        print("❗ Invalid input.")
        section_2_west_path(inventory)

def section_2_tree_path(inventory):
    print("""
📍 From your vantage point, you spot:
- A structure to the west
- A trail of smoke to the north

You can now choose:
A. Head west toward the structure
B. Investigate the smoke to the north
    """)
    choice = input(">> ").strip().lower()
    if choice == 'a':
        section_2_west_path(inventory)
    elif choice == 'b':
        print("\n🚬 You follow the smoke trail and find a hidden camp — possibly treasure hunters or bandits. They haven’t seen you yet.")
        # You could add another decision branch here
    else:
        print("❗ Invalid input.")
        section_2_tree_path(inventory)

def section_2_village_path(inventory):
    print("""
🏘️ At the village, an old local named 'Tuma' offers to guide you if you give him something useful.

You have:
- Machete
- Compass
- Bottle of water
- Flare gun with 1 flare
- Notebook

Which item will you trade?
A. Bottle of water
B. Flare gun
C. Notebook
D. Refuse to trade
    """)
    choice = input(">> ").strip().lower()
    if choice == 'a':
        print("\n💧 You give Tuma your water. He agrees to guide you through a safer path to the temple.")
        inventory.remove("1 bottle of water")
        section_3_ruin_entrance(inventory)
    elif choice == 'b':
        print("\n🚨 You hand over your flare gun. Tuma laughs and pockets it. 'Let’s go,' he says.")
        inventory.remove("Flare gun with 1 flare")
        section_3_ruin_entrance(inventory)
    elif choice == 'c':
        print("\n📘 Tuma seems intrigued by the myths in your notebook. 'Zorak was real,' he mutters. He joins you.")
        inventory.remove("Notebook with Zorak notes")
        section_3_ruin_entrance(inventory)
    elif choice == 'd':
        print("\n🚶‍♂️ You refuse. Tuma shrugs and walks off. You head out alone.")
        section_2_west_path(inventory)
    else:
        print("❗ Invalid input.")
        section_2_village_path(inventory)

def section_3_ruin_entrance(inventory):
    print("""
🧱 You stand before the entrance to the ruined temple of Zorak. It looms in silence, ancient and foreboding.

You’ve made it — but the real danger lies ahead.

(To be continued...)
    """)

# Start the game
def start_game():
    print("🎮 Welcome to The Lost Temple of Zorak!")
    inventory = [
        "Machete",
        "Compass",
        "1 bottle of water",
        "Flare gun with 1 flare",
        "Notebook with Zorak notes"
    ]
    section_1(inventory)

# Run the game
if __name__ == "__main__":
    start_game()