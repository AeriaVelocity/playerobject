import random
from time import sleep

class PlayerError(Exception):
    pass

class PlayerObject:
    
    def __init__(self, Name, MaxHealth, BaseAttack, GameName):
        
        self.Name = Name
        self.MaxHealth = MaxHealth
        self.CurrentHealth = self.MaxHealth
        self.BaseAttack = BaseAttack
        self.TotalAttack = self.BaseAttack * 2
        self.GameName = GameName
        
        print(f"Welcome to {self.GameName}, {self.Name}!")
        print(f"Your maximum health is {self.MaxHealth} and your attack strength varies from {self.BaseAttack} to {self.TotalAttack}.")

        
    def Attack(self, AttackBonus: int):
        AttackValue = random.randint(self.BaseAttack,self.TotalAttack)+AttackBonus
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
            print(f"The specified heal amount was greater than {self.Name}'s maximum health; healing to max instead.")
            print(f"{self.Name}'s health is now {self.CurrentHealth}/{self.MaxHealth}.")
        elif HealAmount < 1:
            print("Cannot heal by a non-positive value.")
        else:
            self.CurrentHealth = self.CurrentHealth + HealAmount
            if self.CurrentHealth > self.MaxHealth:
                print(f"Health was healed to greater than {self.Name}'s maximum health; healing to max instead.")
                self.CurrentHealth = self.MaxHealth
            print(f"{self.Name}'s health is now {self.CurrentHealth}/{self.MaxHealth}.")
