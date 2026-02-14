import random

player_health = 100
cpu_health = 100

print("👹 Welcome to Terminal Fighters!")

while player_health > 0 and cpu_health > 0:
    print("\nYour Health:", player_health)
    print("CPU Health:", cpu_health)

    print("\nChoose your move:")
    print("1 - Jab (10 damage)")
    print("2 - Kick (15 damage)")
    print("3 - Heavy attack (5-25 damage)")

    choice = input("Enter you move number: ")
    if choice == "1":
        damage = 10
    elif choice == "2":
        damage = 15
    elif choice == "3":
        damage = random.randint(5, 25)
    else:
        print("Invalid move! Lose your turn!")
        damage = 0

    cpu_health -= damage
    print(f"You dealt {damage} damage!")

    if cpu_health <= 0:
        print("\n👌YOU WIN!")
        break

    cpu_damage = random.choice([8, 12, 18])
    player_health -= cpu_damage
    print(f"CPU hits you for {cpu_damage} damage!")

    if  player_health <= 0:
        print("\n😒YOU LOSE! ")
