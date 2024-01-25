import random

def roll(num):
  return random.randint(0, num) == 0

def inputMenu(numOptions):
  ans = input(f'\tEnter selection (1 - {numOptions}): ').strip()
  while (not ans.isdigit()) or (not 1 <= int(ans) <= numOptions):
    ans = input(f'\tEnter valid selection (1 - {numOptions}): ').strip()
  return int(ans) - 1

def inputFloat():
  num = input("\tEnter value: ").strip()
  while not validFloat(num):
    num = input("\tEnter valid value: ").strip()
  return float(num)

def validFloat(str):
  validChars = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
  for char in str:
    if char not in validChars:
      return False
  return True

def goOliveGarden():
  entrees = [['Chicken Alfredo', 19.99, 10, roll(5)],
            ['Shrimp Scampi', 11.99, 15, roll(9)],
            ['Ravioli Carbonara', 17.99, 12, roll(13)]]
  commonDrinks = ['soda', 'tea', 'lemonade', 'coffee', 'water']

  drinkCost = round(random.uniform(1.99, 4.99), 2)
  
  print('\nYou walk over to the Olive Garden that’s close by.',
        '\nAs you enter, the host greets you and says, "Good afternoon! What’s your name?"')
  name = input('\tEnter your name: ')

  print(f'\n"Hello {name}," she says, "please follow me to your table!"', 
        f'\nYou have a seat and the host leaves after handing you the menu.',
        f'\nShortly after, the waiter appears and they ask, "Can I get you something to drink?"')
  drink = input('\tWhat do you ask for? ')
  
  if drink.lower().strip() in commonDrinks:
    print(f'\n"Good choice! The {drink.lower()} is pretty good here!" she says, "I’ll grab it for you while you look over the menu."')
  else: 
    print(f'\n"No problem, I’ll grab {drink} for you while you look over the menu."')

  print('You look at the menu for a few minutes and have settled on one of three options.', 
        '\nWhich one will you chose?',
        '\n\t1: Chicken Alfredo ($19.99)',
        '\n\t2: Shrimp Scampi ($11.99)',
        '\n\t3: Ravioli Carbonara ($17.99)')
  choice = inputMenu(3)
  
  entree = entrees[choice][0]
  mealCost = entrees[choice][1]
  waitTime = entrees[choice][2]
  poisoned = entrees[choice][3]

  total = round(mealCost + drinkCost, 2)

  print(f'\nThe waiter comes back with the {drink}, "Do you know what you would like to order yet?"',
        f'\nYou reply, "I’ll just have the {entree} please."',
        f'\n"Alright, it should be ready in about {waitTime} minutes."',
        f'\nAfter {waitTime - random.randint(-3, 3)} minutes pass the waiter comes back with the food.')

  if poisoned:
    print('Having been so hungry, you finished the entire meal in a matter of minutes, but noticed it kind of tasted funny.')
  else:
    print('Having been so hungry, you finished the entire meal in a matter of minutes!')

  # Input user's amount of money. Output a result depending on their abilty to afford.
  print(f'You soon ask for the check, which reads:',
        f'\n\t⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯',
        f'\n\t{entree}: ${mealCost}',
        f'\n\t{drink}: ${drinkCost}',
        f'\n\n\tTotal: ${total}'
        f'\n\t⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯',
        f'\n\tHow much money do you have on you?')
  money = inputFloat()

  if money >= total:
    print(f'\nHow much would you like to tip?')
    tip = inputFloat()   
    while tip > money - total:
      print('\tYou do not have enough to tip that amount, try again.')
      tip = inputFloat() 
    if tip >= total * 0.30:
      print(f'\nAfter tipping ${tip:.2f}, you leave Olive Garden noticing the grin on your waiter’s face',
            f'\nafter the act of generosity, and go on your way home with a happy stomach.') 
    elif tip >= total * 0.15:
      print(f'\nAfter tipping ${tip:.2f}, you leave Olive Garden and go', 
            f'on your way home with a happy stomach.')  
    else:
      print(f'\nAfter tipping ${tip:.2f}, you leave Olive Garden noticing the disheartened',
            f'\nlook on your waiter’s face, but go on your way home with a happy stomach.')  
  else:
    print(f'\nEmbarrassingly, you get kicked out of the restuarant after they realize you are unable to pay up.')   

  if poisoned:
    print('Shortly after arriving home you start to feel ill, and conclude that you got food poisoning.', 
          '\nYou swear to never go to an Olive Garden again.')

def goSubway():
  proteins = [['chicken', 10.29],
              ['tuna', 9.56],
              ['meatball', 8.59],
              ['steak', 12.24],
              ['roast beef', 13.99]]
  sizes = ['6"', 'footlong']
  breads = ['artisan', 'multigrain', 'flatbread']
  cheeses = ['american', 'pepperjack', 'provolone']
  
  print('\nYou drive over to the Subway since it is a little too far to walk to.',
        '\nAs you enter, you get in line and start to think about what you’ll order.',
        '\nOnce it’s your turn, the guy behind the counter asks, "What can I get for you?"', 
        '\n\t1: 6”',		
        '\t\t2: Footlong')
  size = sizes[inputMenu(2)]

  print('\n\t1: Chicken ($9.29)',
        '\t\t2: Tuna ($8.56)',
        '\t\t\t3: Meatball ($7.59)',
        '\n\t4: Steak ($11.24)',
        '\t\t5: Roast Beef ($12.99)')
  choice = inputMenu(5)
  
  protein = proteins[choice][0]
  cost = proteins[choice][1]
  
  if size == '6”': 
    cost /= 2

  print(f'\n"I’ll get a {size} of the {protein} sandwich please," you say.')
  
  if protein == 'steak': 
    print('"That’s my favorite one," he exclaims, "', end='')
  elif protein == 'tuna': 
    print('"That’s kind of gross, but whatever," he remarks, "', end='')
  else:
    print('"Sure thing, ', end='')

  print('what type of bread do you want?"',
        '\n\t1: Artisan',
        '\t\t2: Multigrain',
        '\t\t3: Flatbread')
  bread = breads[inputMenu(3)]

  print(f'\nYou say, "{bread.title()} please."',
        '\n"Gotcha, and what type of cheese?"',
        '\n\t1: American', 
        '\t2: Pepperjack',	
        '\t\t3: Provolone')
  cheese = cheeses[inputMenu(3)]

  print(f'\n"Let me get the {cheese}," you say.', end=' ')

  if cheese == 'pepperjack':
    print('\n"Nothing beats the spicy kick of pepperjack!" he says in approval.')

  print('"I’ll also finish it off with lettuce, tomato, and onion."', 
        '\nHe replies, "Great!", then adds the remaining ingredients, and walks over to ring you up at the register.')

  if (protein == 'meatball' and cheese == 'provolone'):
    cost = round(cost * 0.85, 2)
    print(f'"Guess what?" he says, "you’ll get 15% off because of the discount we offer',
          f'for the Meatball and Provolone combination!"', 
          f'\n"Your total is ${cost}."',
          f'\n"Wow, that’s awesome," you say, "thank you!"') 
  elif (protein == 'steak' and cheese == 'pepperjack'):
    cost = round(cost * 0.8, 2)
    print(f'"Guess what?" he says, "You’ll get 20% off because of the discount we offer',
          f'for the Steak and Pepperjack combination!"',
          f'\n"Your total is ${cost}."',
          f'\nYou reply, "From what you said before, I’m sure it’s well-deserved, thanks!"')
  elif (protein != 'tuna'):
    cost = round(cost * 0.9, 2)
    print('"You know what," he says, "just because you didn’t get that yucky tuna, I’ll give you a little discount."',
          f'\n"How does 10% off sound?"', 
          f'\n"I’ll take it," you say.',
          f'\n"Alright, your total is ${cost}."')
  else: 
    print(f'"Alright, your total is ${cost}."')
    
  print('\tHow much money do you have on you? ')
  money = inputFloat()

  if money >= cost:
    print(f'\nYou drive back home to enjoy your {size} {protein} sandwich with {bread} bread, {cheese} cheese, lettuce, tomato, and onion.')
  else:
    print(f'\nSadly, because you could not afford it, you drive back home without your Subway sandwich.')

print('\nWelcome to an adventure game where you choose your own path through the story!', 
      '\nYou are starving after a long day of work and you decide to grab something to eat before heading home.',
      '\n\nThere are two places close by, which one will you choose?', 
      '\n\t1: Olive Garden', 
      '\t2: Subway')

if inputMenu(2) == 0: 
  goOliveGarden()
else: 
  goSubway()