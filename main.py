# Programmer: Cyrus
# Course: CS151, Dr. Olsen
# Due Date: 9/20/2023
# Programming Assignment: 0
# Problem Statement: Determine the total volume of cake needed for any event.
# Data In: The number of attendees, number of slices per attendee, volume of cake per slice,
#          amount of leftover slices, expense of the cake, and budget.
# Data Out: The total volume of cake needed and its estimated cost.

def wantsOptionMenu():
  response = input('\tWould you like to use one of the recommendend options? [Y/N] ')
  return (response.lower() == 'y' or response.lower() == 'yes')

def inputMenuOption(a, b, c):
  optionValues = [a, b, c]
  selectedOption = 0
  while not 1 <= selectedOption <= 3:
    selectedOption = int(input("\tEnter response (1, 2, or 3): "))
  return optionValues[selectedOption - 1]

def printResult():
  print("\n~ The results are in! ~",
        f"\nYou need to buy {totalVolume:.2f} in³ of cake at an estimated ${cost:.2f}.",
        f"\nThe cake will contain {totalSlices} slice(s) of {sliceVolume:.2f} in³ cake.")

print("~ WELCOME TO THE CAKE CALCULATOR! ~",
      "\nFind out how much cake you need for any event.",
      "\n\nPlease enter the following:")

attendees = int(input("\tNumber of attendees: "))
slicesPer = int(input("\tNumber of slices per attendee: "))
leftOver = int(input("\tDesired number of leftover slices: "))
budget = float(input('\tBudget for the entire cake. Type "0" for no budget: $'))

print('\nSize of each cake slice?')
if wantsOptionMenu():
  print('\t\n1: Small (6 in³)', 
        '\t\n2: Average (8 in³)',
        '\t\n3: Large (10 in³)')
  sliceVolume = inputMenuOption(6, 8, 10)
else:
  sliceVolume = float(input("\tEnter slice amount (in³): "))

print('\nHow expensive of a cake?')
if wantsOptionMenu():
  print('\t\n1: On-Sale (Cheap) [$0.05 per in³]',
        '\t\n2: Average [$0.10 per in³]', 
        '\t\n3: Custom-Made (Expensive) [$0.15 per in³]')
  cakeRate = inputMenuOption(0.05, 0.10, 0.15)
else:
  cakeRate = float(input("\tEnter cost per in³: $"))

totalSlices = (attendees * slicesPer) + leftOver
totalVolume = totalSlices * sliceVolume
cost = totalVolume * cakeRate

overBudget = (budget <= 0 or cost <= budget)
if (overBudget):
  printResult()
else:
  totalVolume = budget / cakeRate 
  sliceVolume = totalVolume / totalSlices
  cost = totalVolume * cakeRate
  printResult()