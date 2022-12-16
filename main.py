from random import *
class Human:
  def __init__(self,name):
    self.name = name
    self.isalive = True
    self.money = 100
    self.satisfaction = 10
    self.exausted = 0
  def work(self):
    print( self.name + ' worked well!')
    print('money: ' + str(self.money) + " + 50")
    self.money += 50
    print('exausted: ' + str(self.exausted) +' + 5')
    self.exausted += 5
  def sleep(self):
    print(self.name + ' slept well!')
    print('satisfaction: ' + str(self.satisfaction) + ' + 5')
    self.satisfaction += 5
    if self.exausted >= 5 or self.exausted == 5:
      print('exausted: '  + str(self.exausted) + ' - 10')
      self.exausted -= 10
    else:
      print(self.name + ' are too relaxed!')
class student(Human):
  def __init__(self,name):
    super().__init__(name)
    self.progress = 10
  def study(self):
    print (self.name + ' studied well!')
    print('progress: ' + str(self.progress) + ' + 5')
    self.progress += 5
    print('satisfaction: ' + str(self.satisfaction) + ' - 5')
    self.satisfaction -=5
    print('exausted: ' + str(self.exausted) + ' + 5')
    self.exausted += 5
  def hangout(self):
    print(self.name + ' hanged out with friends')
    print('satisfaction: ' + str(self.satisfaction) + ' + 15')
    self.satisfaction += 15
    print('progress: ' + str(self.progress) + ' - 5')
    self.progress -= 5
    print('exausted: ' + str(self.exausted) + ' + 5')
    self.exausted += 5
    print('money: ' + str(self.money) + ' - 50')
    self.money -= 50
  def life(self):
    if self.satisfaction == -5:
      print(self.name  + ' Died of Cringe')
      self.isalive = False
    if self.exausted == 20:
      print(self.name + ' Died of Fatigue')
      self.isalive = False
    if self.progress == -5:
      print(self.name + ' Died of School debts')
      self.isalive = False
    if self.money == 0:
      print(self.name + ' Became a homeless')
      self.isalive = False
  def do_live(self,day):
    if self.isalive == True:
      cube = randint(1,4)
      if cube == 1:
        
        super().sleep()
        self.life()
      elif cube == 2:
        
        super().work()
        self.life()
      elif cube == 3:
        
        self.hangout()
        self.life()
      elif cube == 4:
        
        self.study()
        self.life()
  
      
class teacher(Human):
  def __init__(self,name):
    super().__init__(name)
    self.programme = 5
  def vacation(self):
    print(self.name + ' got a vacation')
    print('satisfaction: ' + str(self.satisfaction) + ' + 10')
    self.satisfaction += 10
    if self.exausted >=5:
      print('exausted: ' + str(self.exausted) + ' - 5')
      self.exausted -= 5
    else:
          print(self.name + ' are too relaxed!')
  def teach(self):
    print(self.name + ' teached children')
    print('programme: ' + str(self.programme) + ' + 5')
    self.programme += 5
    print('exausted: '+  str(self.exausted) + ' + 5')
    self.exausted += 5
  def life(self):
    if self.satisfaction == -5:
      print(self.name  + ' Died of Cringe')
      self.isalive = False
    if self.exausted == 20:
      print(self.name + ' Died of Fatigue')
      self.isalive = False
    if self.programme == 0:
      print(self.name + ' Died of Director')
      self.isalive = False
    if self.money == 0:
      print(self.name + ' Became a homeless')
      self.isalive = False
  def do_live(self,days):
    if self.isalive == True:
      cube = randint(1,4)
      if cube == 1:
        
        super().sleep()
        self.life()
      elif cube == 2:
        
        super().work()
        self.life()
      elif cube == 3:
        
        self.vacation()
        self.life()
      elif cube == 4:
        
        self.teach()
        self.life()

firsteacher = teacher('Giorno Giovanna')
firsstudent = student('Antonio Pripizduchi')
for day in range(10):
  if firsstudent.isalive == False:
    break
  firsstudent.do_live(day)
for days in range(10):
  if firsteacher.isalive == False:
    break
  firsteacher.do_live(days)

  



    
    
    
  