import time
import sys
import math
import random

def inputMenuOption(options):
  response = input('\tEnter choice: ').strip()
  while response not in options:
    response = input('\tEnter choice: ').strip()
  return int(response)

def inputInteger():
  response = input('\tEnter value: ').strip()
  while not response.isdigit():
    response = input('\tEnter value: ').strip()
  return int(response)

def inputChar():
  response = input('\tEnter character: ').strip()
  while len(response) != 1:
    response = input('\tEnter character: ').strip()
  return str(response)

# Credit: Dr. Kenyon
# Link: https://onlinegdb.com/a3MrtocLU
def slowPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)
  print()

def drawCircle():
  print('')
  slowPrint("              ******               ")
  slowPrint("         ****************          ")
  slowPrint("      ***********************      ")
  slowPrint("    ***************************    ") 
  slowPrint("  *******************************  ")
  slowPrint(" ********************************* ")
  slowPrint("***********************************")
  slowPrint("***********************************")
  slowPrint("***********************************")
  slowPrint("***********************************")
  slowPrint(" ********************************* ")
  slowPrint("  *******************************  ")
  slowPrint("    ***************************    ")
  slowPrint("     ***********************       ")
  slowPrint("         ****************          ")
  slowPrint("              ******               ")
    
  
def drawLines():
  print('\nGive me a character!')
  char = inputChar()
  
  print('\nHow many lines do you want of that?')
  numLines = inputInteger()
  
  print('\nHow many characters per line?')
  numChars = inputInteger()

  print('')
  for i in range(numLines):
    slowPrint(char * numChars)

def drawTree():
  #Prints leaves of the tree.
  numSpacesIntial = random.randint(7, 15)
  numSpaces = numSpacesIntial
  numLeaves = 1
  print('')
  while numSpaces > 0:
    slowPrint(' ' * numSpaces + '^' * numLeaves)
    numSpaces -= 1
    numLeaves += 2

  #Prints the trunk of the tree.
  for i in range(random.randint(2, 4)):
    slowPrint(' ' * (numSpacesIntial - 1) + '|||')

def drawCube():
  rand = random.randint(1, 3)
  print('')
  if rand == 1:
    slowPrint('    +--------+ ')
    slowPrint('   /////////|| ')  
    slowPrint('  /////////||| ')
    slowPrint(' +-------+|||| ') 
    slowPrint(' |  |----||||+ ')  
    slowPrint(' | /     |||/  ')     
    slowPrint(' |/      ||/   ')       
    slowPrint(' +-------+     ')  
  elif rand == 2:
    slowPrint('    +--------+ ')     
    slowPrint('   ///////// | ')    
    slowPrint('  /////////  | ')  
    slowPrint(' +-------+   | ')   
    slowPrint(' |  |----|---+ ')    
    slowPrint(' | //////|///  ')    
    slowPrint(' |///////|//   ') 
    slowPrint(' +-------+     ')
  else:
    slowPrint('    +--------+ ')
    slowPrint('   /|      /|| ')
    slowPrint('  / |     /||| ')
    slowPrint(' +-------+|||| ')
    slowPrint(' ||||||||||||+ ')
    slowPrint(' |||||||||||/  ')
    slowPrint(' ||||||||||/   ')
    slowPrint(' +-------+     ')

# Credit: Forrest Cook
# Link: https://asciiart.website/index.php?art=music/pianos
def drawKeyboard():
  slowPrint('      ________________________________  ')
  slowPrint('     /   o   oooo ooo oooo   o o o   /\ ')
  slowPrint('    /   oo  ooo  oo  oooo   o o o   / / ')
  slowPrint('   /    _________________________  / /  ')
  slowPrint('  / // / // /// // /// // /// / / / /   ')
  slowPrint(' /___ //////////////////////////_/ /    ')
  slowPrint(' \____\________________________\_\/     ')

def main():
  print('\nWelcome to a program that generates art!')

  option = None 
  options = ['-1', '1', '2', '3']
  while option != -1:
    print('\nChoose a design option:',
       '\n\t 1: Circle',
       '\n\t 2: Lines',
       '\n\t 3: Random Design',
       '\n\t-1: [Exit]')
    option = inputMenuOption(options)
    
    if option == 1:
      drawCircle()
    elif option == 2:
      drawLines()
    elif option == 3:
      rand = random.randint(1, 3)
      if rand == 1:
        drawTree()
      elif rand == 2:
        drawCube()
      else:
        drawKeyboard()
        
  print('\nGoodbye!')

main()