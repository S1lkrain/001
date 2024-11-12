import time
import random
from random import randint
traveled = 0
money = 10000
health = 100
food = 0
numofppl = 6
Q9 = 0
foodintake = 2
vehicles = 1
NofFeul1 = 0
jkl4 = 0
point1 = 0
point2 = 0
health1 = ("good")
NofAmo1 = 0
score = 0
nofwea = 0
NofFood1 = 0

print("you have a team")
Naofteam = input("the name of the team is ")
print("you have 6 people")
print("thier name is")
Teamppl1 = input("1. ")
Teamppl2 = input("2. ")
Teamppl3 = input("3. ")
Teamppl4 = input("4. ")
Teamppl5 = input("5. ")
Teamppl6 = input("6. ")

while Q9 == 0:
  if traveled == 0 or traveled == 200 or traveled == 600 or traveled == 900:
    Q1 = input("A. shopping")
    print("")
    if Q1 == ("yes"):
      Q0 = 0
      while Q0 == 0:
        print("You have", money, "dollars")
        print("1. food")
        print("2. ammunition")
        print("3. weapons")
        print("4. feul")
        print("5. vehicals")
        print("6. exit")
        print("")
        Q2 = input("what do you want to buy")
        if Q2 == ("1"):
          print("" + str(money) + "$")
          print("12$ = 1 pack of food")
          NofFood1 = int(input("How many packs of food do you want"))
          if NofFood1 * 12 > money:
            print("You don't have enough money")
          if NofFood1 >= 1000:
            print("You can't buy that much food")
          else:
            money = money - (NofFood1 * 12)
        if Q2 == ("2"):
          print("" + str(money) + "$")
          print("53$ = 1 box of ammunition")
          print("1 box of ammunition = 100 bullets")
          NofAmo1 = int(input("How many boxes of ammunition do you want"))
          if NofAmo1 * 53 > money:
            print("You don't have enough money")
          if NofAmo1 >= 500:
            print("You can't buy that much ammunition")
          else:
            money = money - (NofAmo1 * 12)
        if Q2 == ("3"):
          print("" + str(money) + "$")
          print("700$ = 1 gun")
          nofwea = int(input("How many guns do you want"))
          if nofwea * 700 > money:
            print("You don't have enough money")
          if nofwea >= 20:
            print("You can't buy that much weapons")
          else:
            money = money - (nofwea * 700)
        if Q2 == ("4"):
          print("" + str(money) + "$")
          print("3$ = 1 gallon of feul")
          NofFeul1 = int(input("How many gallons of feul do you want"))
          if NofFeul1 * 3 > money:
            print("You don't have enough money")
          if NofFeul1 >= 3000:
            print("You can't buy that much feul")
          else:
            money = money - (NofFeul1 * 3)
        if Q2 == ("5"):
          print("" + str(money) + "$")
          print("1000$ = 1 vehicle")
          NofVeh1 = int(input("How many vehicles do you want"))
          if NofVeh1 * 1000 > money:
            print("You don't have enough money")
          else:
            money = money - (NofVeh1 * 1000)
        if Q2 == ("6"):
          Q0 = 1
            
  speed = 2
  Z1 = input("B. change speed") 
  print("")
  if Z1 == ("yes"):
    Q8 = 0
    while Q8 == 0:
      print("You can change your speed")
      print("1. slow")
      print("2. normal")
      print("3. fast")
      print("4. exit")
      Z2 = input("choose speed")
      print("")
      if Z2 == ("1"):
        speed = 1
      if Z2 == ("2"):
        speed = 2
      if Z2 == ("3"):
        speed = 3
      if Z2 == ("4"):
        Q8 = 1
    #do the "traveled" after the whole code

  Z5 = input("B. change food intake")
  print("")
  if Z5 == ("yes"):
    Qq8 = 0
    while Qq8 == 0:
      print("You can change your food intake")
      print("1. less")
      print("2. normal")
      print("3. large")
      print("4. exit")
      Z6 = input("choose food intake")
      print("")
      if Z6 == ("1"):
        foodintake = 1
      if Z6 == ("2"):
        foodintake = 2
      if Z6 == "3":
        foodintake = 3
      if Z6 == "4":
        Qq8 = 1

  Z7 = input("C. tutorial")
  print("")
  
  #vehicals
  Maxppl = vehicles * 10
  NofFeul1 = NofFeul1 - vehicles*3.5 
  
  Z3 = input("search around")
  print("")
  if Z3 == ("yes"):
    if traveled == 0:
      print("this is the starting point, there are many tents next to you")
    print("you can search around")
    print("1. search surrounding ruins")
    print("2. search surrounding trenches")
    print("3. search surrounding storehouse")
    E1 = input("choose where to search")
    print("")
    if E1 == "1":
      list111 = [1,2,3,4,5]
      Ee1 = random.choice (list111)
      if Ee1 == 1:
        print("you find some foods")
        print("now you have", NofFood1 + 10, "food")
        print("")
      if Ee1 == 2:
        print("you find many foods")
        print("now you have", NofFood1 + 30, "food")
        print("")
      if Ee1 == 3:
        print("you find nothing")
        print("now you have", NofFood1 , "food")
        print("")
      if Ee1 == 4:
        print("you find some ammunition")
        print("now you have", NofAmo1 + 10, "ammunition")
        print("")
      if Ee1 == 5:
        print("you find a refugee")
        print("")
        Eeq1 = randint(1,3)
        if Eeq1 == 1:
          print("he is a refugees who have been hiding here for a long time")
          print("he is willing us to take him to a safety place")
          print("whats your choice")
          print("                 ")
          print("1. take him")
          print("2. give him some food")
          print("3. leave him")
          print("4. kill him")
          Eeq2 = int(input("choose"))
          print("")
          if Eeq2 == 1:
            if Maxppl >= numofppl + 1:
              numofppl = numofppl + 1
              print("you take him to a safety place")
              print("")
            else:
              print("you can't take him")
              print("the car is full")
              print("")
          if Eeq2 == 2:
            print("you give him some food")
            print("now you have", NofFood1 - 10, "food")
            print("")
          if Eeq2 == 3:
            print("you leave him")
            print("")
          if Eeq2 == 4:
            print("you kill him")
            print("others are confused by your choice")
            print("you get some food and ammunation in his shelter")
            print("now you have", NofFood1 + 10, "food and", NofAmo1 + 50, "ammunations")
            print("")
        if Eeq1 == 2:
          print("she is a woman with a child who have been hiding here for a long time")
          print("she is willing us to take them to a safety place")
          print("whats your choice")
          print("                 ")
          print("1. take them")
          print("2. give them some food")
          print("3. leave them")
          print("")
          Eeq2 = int(input("choose"))
          if Eeq2 == 1:
            numofppl = numofppl + 2
            print("you chose to take them to a safety place")
            print("")
          if Eeq2 == 2:
            print("you give them some food")
            print("now you have", NofFood1 - 15, "food")
            print("")
          if Eeq2 == 3:
            print("you leave them")
            print("")
        if Eeq1 == 3:
          print("he is a deserter who have been hiding here for a long time")
          print("he is willing us dont tell anyone he's here")
          print("he was tired of war")
          print("whats your choice")
          print("                 ")
          print("1. expose him")
          print("2. give him some food")
          print("3. leave him")
          print("4. kill him")
          print("")
          Eeq2 = input("choose")
          if Eeq2 == "1":
            print("you expose him")
            print("the chief said he would give you a promotion")
            print("you feel bad looking at his desperate eyes")
            print("he committed suicide when he was being led away by other soldiers")
            print("however, in the eyes of others, this is a just decision")
            print("")
          if Eeq2 == "2":
            print("you give him some food")
            print("now you have", NofFood1 - 10, "food")
            print("")
          if Eeq2 == "3":
            print("you leave him")
            print("")
          if Eeq2 == "4":
            print("you kill him")
            print("others are confused by your choice")
            print("you get some food and ammunation in his shelter")
            print("now you have", NofFood1 + 10, "food and", NofAmo1 + 50, "ammunations")
            print("")
      else:
        print("you find some foods")
        print("now you have", NofFood1 + 10, "food")
        print("")
      if E1 == "2":
        Ee2 = randint(1,5)
        if Ee2 == 1:
          print("you find some food")
          print("now you have", NofFood1 + 10, "food")
          print("")
        if Ee2 == 2:
          print("you find some ammunition")
          print("now you have", NofAmo1 + 10, "ammunition")
          print("")
        if Ee2 == 3:
          print("you find nothing")
          print("")
        if Ee2 == 4:
          print("you find a gun")
          print("now you have", nofwea + 1, "guns")
          print("")
        if Ee2 == 5:
          print("you find a dying casualty")
          print("you can't find any information about him")
          print("do you want to save him")
          print("1. yes")
          print("2. leave him")
          print("3. kill him")
          print("4.give him some food")
          print("")
          Ee2q1 = input("choose")
          if Ee2q1 == "1":
            Ee2q2 = randint(1,3)
            if Ee2q2 == 1:
              print("you save him")
              print("he is a sergeant in our camp")
              print("if you take him to the end, he will promote your rank")
              print("1. take him")
              print("2. leave him")
              Ee2q3 = input("choose")
              print("")
              if Ee2q3 == "1":
                print("you take him to the end")
                print("now you have", numofppl + 1, "peoples")
                print("")
              if Ee2q3 == "2":
                print("you leave him")
                print("he was confused by your choice")
                print("")
            if Ee2q2 == 2:
              print("you save him")
              print("he is a sergeant in enemy camp")
              print("he is begging you dont kill him")
              print("1. kill him")
              print("2. leave him")
              print("3. give him some food")
              print("")
              Ee2q4 = input("choose")
              if Ee2q4 == "1":
                print("you kill him")
                print("you feel so bad")
                print("but others think you are a hero")
                print("you get some food and ammunation surranding the corpse")
                print("now you have", NofFood1 + 10, "food and", NofAmo1 + 50, "ammunations")
                print("")
              if Ee2q4 == "2":
                print("you leave him")
                print("nothing happens")
                print("")
              if Ee2q4 == "3":
                print("he is very grateful")
                print("but when you turn around")
                print("he suddenly stabbed" ,Teamppl1, "with a knife")
                print("he died soon under your siege")
                print("he is cursing you all the time before he die")
                print("you feel bad")
                print("but no matter what, ", Teamppl1, "cant be saved")
                print("you are confused")
                print("now you have",NofFood1 - 10 ,"food")
                print("")
            if Ee2q2 == 3:
                print("you cant save him")
                print("but you've done enough for him")
                print("")
          if Ee2q1 == "2":
            print("you leave him")
            print("nothing happens")
            print("")
          if Ee2q1 == "3":
            print("you kill him")
            print("you feel so bad")
            print("others are confused by your choice")
            print("you get some food and ammunation surranding the corpse")
            print("now you have", NofFood1 + 10, "food and", NofAmo1 + 50, "ammunations")
            print("")
          if Ee2q1 == "4":
            print("he is grateful")
            print("he gives your some weapons from enemies")
            print("now you have", nofwea + 1, "guns and ", NofFood1 - 10, "food")
            print("")
      if E1 == "3":
        Ee3 = randint(1,5)
        if Ee3 == 1:
          print("you find some food")
          print("now you have", NofFood1 + 10, "food")
          print("")
        if Ee3 == 2:
          print("you find some ammunition")
          print("now you have", NofAmo1 + 10, "ammunition")
          print("")
        if Ee3 == 3:
          print("you find nothing")
          print("")
        if Ee3 == 4:
          print("you find a gun")
          print("now you have", nofwea + 1, "guns")
          print("")
        if Ee3 == 5:
          print("you find a scrapped armored vehicle")
          print("you try to fix it")
          print("")
          Eeq2 = randint(1,5)
          if Eeq2 == 1:
            print("succses")
            print("now you have", vehicles + 1, "vehicles")
            print("")
          if Eeq2 == 2:
            print("fail")
            print("you can't fix it")
            print("")
          if Eeq2 == 3:
            print("fail")
            print("you can't fix it")
            print("")
          if Eeq2 == 4:
            print("fail")
            print("you can't fix it")
            print("")
          if Eeq2 == 5:
            print("fail")
            print("you can't fix it")
            print("")
          
  jkl111 = randint(1,20)
  if jkl111 == 1:
    print("you see a enemy")
    print("1. attack")
    print("2. run")    
    print("3. hide")
    jkl2 = int(input("choose"))
    print("")
    if jkl2 == 1:
      jkl4 = 0
      print("fight!")
      while point1 < 5 or point2 < 5:
        jkl5 = randint(1,3)
        if jkl5 == 1:
          print("they use R!")
        if jkl5 == 2:
          print("they use P!")
        if jkl5 == 3:
          print("they use S!")
        print(NofAmo1, "ammunitions")
        print("1. use R")
        print("2. use P")
        print("3. use S")
        print("4. how to play")
        jkl3 = input("choose")
        print("")
        if jkl3 == "4":
          print("thier are 3 type of gun you can use")
          print("they are R, P, and S")
          print("R is rifles")
          print("P is pistols")
          print("S is shotguns")
          print("you can only use one gun at a time")
          print("P restrains R")
          print("R restrains S")
          print("S restrains P")
          print("each choice need 10 amunations")
          print("now, lets fight!")
          print("'hint: same as Rock, Paper, Scissors'")
          print("")
        if jkl3 == "1" and jkl5 == "1":
          print("draw")
          print("")
        if jkl3 == "2" and jkl5 == "2":
          print("draw")
          print("")
        if jkl3 == "3" and jkl5 == "3":
          print("draw")
          print("")
        if jkl3 == "1" and jkl5 == "2":
          print("lose")
          print("")
          point1 = point1 + 1
        if jkl3 == "2" and jkl5 == "3":
          print("lose")
          print("")
          point1 = point1 + 1
        if jkl3 == "3" and jkl5 == "1":
          print("lose")
          print("")
          point1 = point1 + 1
        if jkl3 == "1" and jkl5 == "3":
          print("win")
          print("")
          point2 = point2 + 1
        if jkl3 == "2" and jkl5 == "1":
          print("win")
          print("")
          point2 = point2 + 1
        if jkl3 == "3" and jkl5 == "2":
          print("win")
          print("")
          point2 = point2 + 1
      if point2 == nofwea:
        print("you lose")
        print("you got hurt by the enemy")
        print("but you killed him any way")
        print("")
        health = health - 10
      if point1 == 5:
        print("you win! you killed the enemy")
        print("you find some food and ammunation")
        print("now you have", food + 10, "food and", NofAmo1 + 50, "am")
        print("")

  print("            ")
  print("traveling...")
  print("            ")
  time.sleep(1)

  traveled = traveled + speed*5
  #health
  
  if foodintake == 3:
    health = health + 5
  if foodintake == 2:
    health = health - 5
  if foodintake == 1:
    health = health - 10
  if health >= 80:
    health1 = ("good")
  if health >= 50 and health <= 79:
    health1 = ("fine")
  if health >= 20 and health <= 49:
    health1 = ("poor")
  if health >= 1 and health <= 19:
    health1 = ("dying")
  NofFood1 = NofFood1 - (numofppl*foodintake)
  if NofFood1 < 0:
    Nofood1 = 0
    health = health - 10
  if nofwea <= 0:
    nofwea = 0
  if NofFeul1 <= 0:
    NofFeul1 = 0
  if health <= 0:
    health = 0
    print("You died")
    Q9 = 1

  if traveled == 1000:
    print("you have arrived to the end")
    print("you can see the camp")    
    print("you can see the sergeant")
    print("you can see the soldiers")
    print("you can see the end")
    print("game over")

    score =  + (health*100) + (food*10) + (NofAmo1*3) + (nofwea*5) + (numofppl*500) 
    score = score + (vehicles*100)
                                          
    Q9 = 1
  
  print("health =", health1)
  print("traveled =", traveled)
  print("food =", NofFood1)
  print("vehicles =", vehicles)
  print("NofFeul1 =", NofFeul1)
  
print("do you have a secret code?")
code = input("please enter it")
#secret code: upupdowndownlefleftrightrightbaba
if code == "upupdowndownlefleftrightrightbaba":
  score = 100000000
if code == "it":
  print("???")

if score <= 100:
  score1 = ("private")
if score <= 500:
  score1 = ("private first class")
if score <= 1000:
  score1 = ("sergant")
if score <= 1500:
  score1 = ("sergant first class")
if score <= 2000:
  score1 = ("sergant major")
if score <= 2500:
  score1 = ("Five -star general")

print("")