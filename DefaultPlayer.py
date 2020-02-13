import PlayerModule
import random

PlayerName = ""
while PlayerName == "":
    PlayerName = input("Please input your name!\n> ")

Player = PlayerModule.PlayerObject(PlayerName, random.randint(80, 1000), random.randint(15, 300), "Player OOP Test")
print("Type 'attack' to attack, 'damage' to take damage or 'heal' to regain health.")
    
while True:
    PlayerInput = input("> ")
    if PlayerInput == "attack":
        Player.Attack()
    if PlayerInput == "damage":
        damageamount = int(input("How much base damage do you want to receive?\n> "))
        Player.Damage(damageamount)
    if PlayerInput == "heal":
        healamount = input("How much health do you want to receive? (Type 'full' to fully heal)\n> ")
        if healamount == 'full':
            Player.Heal(Player.MaxHealth)
        else:
            Player.Heal(healamount)
    else:
        pass