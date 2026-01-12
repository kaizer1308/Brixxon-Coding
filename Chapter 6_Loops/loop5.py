import os
os.system("cls")

# Exercise: sword loop

sword_types = ["Aerondight", "Zireael", "Goblin Cleaver", "Anduril"]
finished_swords = []

while sword_types:
    current_sword = sword_types.pop()
    print(f"forging your sword: {current_sword}")
    finished_swords.append(current_sword)
    finished_swords.sort()
    finished_swords.reverse()
    
    print("\n")
    for sword in finished_swords:
        print(f"Completed sword: {sword}")
        