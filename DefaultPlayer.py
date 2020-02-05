import PlayerModule

PlayerName = input("Please input your name!\n> ")
Player = PlayerModule.PlayerObject(PlayerName, 100, 15)
print("Type 'Attack' to attack, 'Damage' to take damage or 'Heal' to regain health.")
    
while True:
    PlayerInput = input("> ")
    if PlayerInput == "Attack":
        Player.Attack()
    if PlayerInput == "Damage":
        damageamount = int(input("How much damage do you want to receive?\n> "))
        Player.Damage(damageamount)
    if PlayerInput == "Heal":
        Player.Heal(10)
    else:
        pass
