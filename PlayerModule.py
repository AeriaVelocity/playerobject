import random
from time import sleep

class PlayerError(Exception):
    pass

class PlayerObject:
    
    def __init__(self, Name, MaxHealth, BaseAttack):
        
        self.Name = Name
        self.MaxHealth = MaxHealth
        self.CurrentHealth = self.MaxHealth
        self.BaseAttack = BaseAttack
        self.TotalAttack = self.BaseAttack * 2
        
        print(f"Welcome to the realm, {self.Name}!")
        print(f"Your maximum health is {self.MaxHealth} and your attack strength varies from {self.BaseAttack} to {self.TotalAttack}.")

        
    def Attack(self):
        
        AttackValue = random.randint(self.BaseAttack,self.TotalAttack)
        
        if AttackValue == self.TotalAttack:
            print(f"{self.Name} dealt maximum damage!")
        else:
            print(f"{self.Name} dealt {AttackValue} points of damage.")

            
    def Damage(self, InitialDamageAmount):
        
        MaxDamageAmount = InitialDamageAmount * 3
        DamageAmount = random.randint(InitialDamageAmount, MaxDamageAmount)
        
        if DamageAmount == MaxDamageAmount:
            print(f"{self.Name} suffered {DamageAmount} points of damage!")
        else:
            print(f"{self.Name} suffered {DamageAmount} points of damage.")
        self.CurrentHealth = self.CurrentHealth - DamageAmount
        
        if self.CurrentHealth < 1:
            print(f"{self.Name} has died.")
            print("Respawning...")
            sleep(3)
            self.CurrentHealth = self.MaxHealth
        else:
            print(f"{self.Name}'s health is now {self.CurrentHealth}/{self.MaxHealth}.")


    def Heal(self, HealAmount):
        if HealAmount > self.MaxHealth:
            self.CurrentHealth = self.MaxHealth
            raise PlayerError(f"The specified heal amount was greater than {self.Name}'s maximum health; healing to max instead.")
            print(f"{self.Name}'s health is now {self.CurrentHealth}/{self.MaxHealth}.")
        elif HealAmount < 1:
            raise PlayerError("Cannot heal by a non-positive value.")
        else:
            self.CurrentHealth = self.CurrentHealth + HealAmount
            if self.CurrentHealth > self.MaxHealth:
                self.CurrentHealth = self.MaxHealth
            print(f"{self.Name}'s health is now {self.CurrentHealth}/{self.MaxHealth}.")


PlayerName = input("Please input your name!\n> ")
Player = PlayerObject(PlayerName, 100, 15)
