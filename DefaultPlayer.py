import PlayerModule

PlayerName = input("Please input your name!\n> ")
Player = PlayerModule.PlayerObject(PlayerName, 100, 15)
print("Type 'attack' to attack, 'damage' to take damage or 'heal' to regain health.")
    
while True:
    PlayerInput = input("> ")
    if PlayerInput == "attack":
        Player.Attack()
    if PlayerInput == "damage":
        damageamount = int(input("How much damage do you want to receive?\n> "))
        Player.Damage(damageamount)
    if PlayerInput == "heal":
        healamount = int(input("How much health do you want to receive?\n> "))
        Player.Heal(healamount)
    else:
        pass
