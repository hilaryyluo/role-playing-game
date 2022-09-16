import roleplayinggame as rpg

##Examples for all_punch:  
def test1():
  d1 = rpg.Character("C1", 10, 10, 10)  
  d2 = rpg.Character("C2", 1, 10, 10)  
  d3 = rpg.Character("C3", 20, 20, 10)  
  e2 = rpg.Character("E2", 20, 20, 10)  
  L = [d1, d2, d3]  
  assert rpg.all_punch(L, e2) == None  
  assert d1.level == 2
  assert d2.level == 2  
  assert d3.level == 2 
  assert e2.hp == 0  
  assert d1 != rpg.Character("C1", 10, 10, 10)  
  assert d2 != rpg.Character("C2", 1, 10, 10)
  assert d3 != rpg.Character("C3", 20, 20, 10)
  assert e2 != rpg.Character("E2", 20, 20, 10)  

def test2():
  d1 = rpg.Character("C1", 10, 10, 10)  
  d2 = rpg.Character("C2", 50, 10, 10)  
  d3 = rpg.Character("C3", 20, 20, 10)  
  e2 = rpg.Character("E2", 20, 500, 10)  
  L = [d1, d2, d3]  
  assert rpg.all_punch(L, e2) == None
  assert d1.level == 1
  assert d2.level == 1 
  assert d3.level == 1 
  assert e2.hp == 340 
  assert d1 == rpg.Character("C1", 10, 10, 10)
  assert d2 == rpg.Character("C2", 50, 10, 10) 
  assert d3 == rpg.Character("C3", 20, 20, 10) 
  assert e2 != rpg.Character("E2", 20, 500, 10)  
  
def test3():  
  ##Tests for all_punch:  
  d1 = rpg.Character("C1", 0, 10, 10)  
  d2 = rpg.Character("C2", 100, 10, 10)  
  d3 = rpg.Character("C3", 100, 20, 10)  
  e2 = rpg.Character("E2", 20, 400, 10)  
  L = [d1, d2, d3]  
  assert rpg.all_punch(L, e2) == None
  assert d1.level == 2 
  assert d2.level == 2  
  assert d3.level == 2  
  assert e2.hp == 0
  assert d1 != rpg.Character("C1", 0, 10, 10)
  assert d2 != rpg.Character("C2", 100, 10, 10)
  assert d3 != rpg.Character("C3", 100, 20, 10)
  assert e2 != rpg.Character("E2", 20, 400, 10)    
    
def test4():
  d1 = rpg.Character("C1", 0, 10, 10)  
  d2 = rpg.Character("C2", 0, 10, 10)  
  d3 = rpg.Character("C3", 0, 20, 10)  
  e2 = rpg.Character("E2", 0, 10, 10)  
  L = [d1, d2, d3]  
  assert rpg.all_punch(L, e2) == None 
  assert d1.level == 1 
  assert d2.level == 1  
  assert d3.level == 1  
  assert e2.hp == 10 
  assert d1 == rpg.Character("C1", 0, 10, 10) 
  assert d2 == rpg.Character("C2", 0, 10, 10) 
  assert d3 == rpg.Character("C3", 0, 20, 10) 
  assert e2 == rpg.Character("E2", 0, 10, 10) 