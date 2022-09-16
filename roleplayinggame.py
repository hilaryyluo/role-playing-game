import math
    
class Character:  
  '''''  
  Fields:  
     name(Str)  
     st(Nat) 
     hp(Nat) 
     max_hp(Nat) 
     mp(Nat) 
     max_mp(Nat) 
     level(Nat) 
      
  Requires:   
     st, max_hp are both strictly greater than 0. 
  '''  
  def __init__(self, new_name, strength,   
               maximumHP, maximumMP):  
    ''''' 
    Initializes a Character object self with  
    name new_name, st strength, 
    hp and max_hp of maximumHP, and 
    mp and max_mp of maximumMP, and 
    level should start at 1. 
     
    Effects: Mutates self 
     
    __init__: Character Str Nat Nat Nat -> None 
    Requires 
      0 < strength, maximumHP, level 
      maximumHP > hp 
      maximumMP > mp 
    '''  
    self.name = new_name  
    self.st = strength  
    self.hp = maximumHP  
    self.max_hp = maximumHP  
    self.mp = maximumMP  
    self.max_mp = maximumMP  
    self.level = 1  
      
  def __eq__(self, other):  
    ''''' 
    Returns True if self and other are equal and False otherwise 
     
    __eq__: Character Any -> Bool 
    '''  
    return self.name == other.name and self.st == other.st and self.hp == other.hp and self.max_hp == other.max_hp and self.mp == other.mp and self.max_mp == other.max_mp and self.level == other.level  
       
    
  def __repr__(self):  
    ''''' 
    Returns a string representation of self 
     
    __repr__: Character -> Str 
    '''  
    s = '{0.name}\n' + 'Level: {0.level}\n' +'Strength: {0.st}\n' + 'HP: {0.hp}/{0.max_hp}\n' + 'MP: {0.mp}/{0.max_mp}'  
    return s.format(self)  
  
    
  def cast_spell(self, cost, damage, enemy):  
    ''''' 
    Casts a spell if self is able that requires cost mp to cast and 
    deals damage to enemy. A message is printed if the enemy is  
    defeated or there was not enough mp to cast the spell. 
     
    Effects:  
       Prints to screen 
       Mutates self 
       Mutates enemy 
     
    cast_spell: Character Nat Nat Character -> None 
     
    Examples: 
       c = Character("Test", 1, 4, 5) 
       e = Character("Test", 1, 4, 5) 
       c.cast_spell(3, 10, e) => None 
       and e.hp is mutated to 0 
       and c.mp is mutated to 2 
       and "Enemy defeated" is printed (no quotes). 
        
       c = Character("Test", 1, 4, 5) 
       e = Character("Test", 1, 4, 5) 
       c.cast_spell(13, 10, e) => None 
       and "Not enough MP" is printed (no quotes). 
        
       c = Character("Test", 1, 4, 5) 
       e = Character("Test", 1, 4, 5) 
       c.cast_spell(3, 2, e) => None 
       and e.hp is mutated to 2 
       and c.mp is mutated to 2 
    '''  
    error_msg = "Not enough MP"  
    defeated_msg = "Enemy defeated"  
    if cost <= self.mp:  
      self.mp -= cost  
      enemy.hp -= damage  
      if enemy.hp <= 0:  
        enemy.hp = 0  
        print(defeated_msg)  
    else:  
      print(error_msg)  
    return None  
  
  
  def level_up(self):  
    ''''' 
    Performs a level-up for self. Increase stats 10% plus 1 
    via mutation of self. 
     
    Effects: Mutates self 
     
    level_up: Character -> None 
     
    Examples: 
       c = Character("Test", 1, 4, 5) 
       c.level_up() => None 
       and c.level is mutated to 2 
       and c.st is mutated to 2 
       and c.hp is mutated to 5 
       and c.max_hp is mutated to 5 
       and c.mp is mutated to 6 
       and c.max_mp is mutated to 6 
    '''  
    self.level += 1  
    self.st = 1 + math.floor(self.st * 1.1)  
    hp_increment = 1 + math.floor(self.max_hp * 0.1)  
    mp_increment = 1 + math.floor(self.max_mp * 0.1)  
    self.max_hp += hp_increment  
    self.max_mp += mp_increment  
    self.hp += hp_increment  
    self.mp += mp_increment  
  
  
def punch(players, enemy):  
  ''''' 
  Returns True if enemy has been defeated and False otherwise. All players  
    attack an enemy and do double their strength in damage to the enemy's hp. 
   
  punch: (listof Character) (Characters) -> Bool 
  '''  
  for i in players:  
    i.cast_spell(0, 2 * i.st, enemy)  
    if enemy.hp == 0:  
      return True  
  return False    
      
      
def all_punch(players, enemy):  
  ''''' 
  Returns None, but simulates all the players punching an enemy. 
   
  all_punch: (listof Character) (Characters) -> None 
   
  Examples: 
    d1 = Character("C1", 10, 10, 10) 
    d2 = Character("C2", 1, 10, 10) 
    d3 = Character("C3", 20, 20, 10) 
    e2 = Character("E2", 20, 20, 10) 
    L = [d1, d2, d3] 
    all_punch(L, e2) => None 
    and  
    d1.level => 2 
    d2.level => 2 
    d3.level => 2 
    e2.hp => 0 
     
    d1 = Character("C1", 10, 10, 10) 
    d2 = Character("C2", 50, 10, 10) 
    d3 = Character("C3", 20, 20, 10) 
    e2 = Character("E2", 20, 500, 10) 
    L = [d1, d2, d3] 
    all_punch(L, e2) => None 
    and  
    d1.level => 1 
    d2.level => 1 
    d3.level => 1 
    e2.hp => 340 
  '''  
  if punch(players, enemy) == True:  
    for i in players:  
      i.level_up()  
  return None   