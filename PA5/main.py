# Programmers: Cyrus and Maria
# Course: CS151, Dr. Olsen
# Due Date: 12/10/2023
# Programming Assignment: 5
# Problem Statement: Analyze data about sustainability in Baltimore.
# Data In: Task to perform and corresponding parameters.
# Data Out: Data about the file: 
# Input Files: sustainability.csv
# Ouput File: voterData.png and others specified by user.

import os
import matplotlib.pyplot as plt

# -- Lead: Maria
# Purpose: Get file name that exists
# Parameters: N/A
# Return: file name that exists
def inputFileName():
  # Ask for file name, loop until file in directory is present.
  filename = input('\tFile name: ')
  while not os.path.isfile(filename):
    filename = input('\tFile name: ')
  return filename

# -- Lead: Cyrus
# Purpose: Create a 2-D list that contains file data
# Parameters: the file to read from
# Return: the data in a list
def fetch2DFileLines(filename):
  fd = open(filename, 'r')
  lines = []
  # Iterate through each line in the file and save a list of the line (seperated by comma) to lines.
  for line in fd:
    lines.append(line.strip("\n").split(","))
  fd.close()
  return lines

# -- Lead: Maria
# Purpose: Write a 2-D list to a file
# Parameters: the file to write to, list containing the data
def write2DListToFile(filename, data):
  fd = open(filename, 'w')
  # Iterate through each element in the 2-D list and write to the file.
  for line in data:
    for item in line:
      fd.write(str(item) + ' ')
    fd.write('\n')
  fd.close()

# -- Lead: Cyrus
def aggregateChangeOpenSpace(data):
  changes = []
  for neighborhood in data:
    originalSpaces = float(neighborhood[22])
    finalSpaces = float(neighborhood[25])
    
    if originalSpaces == 0:
      changes.append([neighborhood[0], 'Flat'])
    else:
      percentDifference = (((finalSpaces - originalSpaces) / originalSpaces)) * 100
      if percentDifference <= -75:
        metric = 'Extremely Down'
      elif percentDifference <= -50:
        metric = 'Significantally Down'
      elif percentDifference <= -10:
        metric = 'Down'
      elif percentDifference > 10:
        metric = 'Up'
      else:
        metric = 'Flat'
        
      changes.append([neighborhood[0], '--', metric])
      
  return changes

# -- Lead: Maria
# Purpose: Create a 2-D list containing change between the rate of dirty streets and alleys reports between 2010 and 2014 for each neighborhood
# Parameters: data
# Return: change
def aggregateChangeDirtyStreets(data):
  changes = []
  # Iterate through all neighborhoods in data and write to a list the change in dirty streets for each
  for neighborhood in data:
    dirtyStreetsOriginal = float(neighborhood[1])
    dirtyStreetsFinal = float(neighborhood[5])
    
    percentChange = ((dirtyStreetsFinal - dirtyStreetsOriginal) / dirtyStreetsOriginal) * 100
    if percentChange >= 25:
      metric = "Significantly Increased"
    elif percentChange >= 10:
      metric = "Increased"
    elif -10 < percentChange < 10:
      metric = "Flat"
    elif percentChange <= -10:
      metric = "Reduced"
    elif percentChange <= -25:
      metric = "Significantly Reduced"
      
    changes.append([neighborhood[0], '--', metric])
    
  return changes

# -- Lead: Cyrus
def aggregateVoterParticipationInfo(data):
  voterData = {'Low': 0, 'Moderate': 0, 'High': 0}
  # Iterate through all neighborhoods in data and tally the amount of neighborhoods that fall in each voter participation category
  for neighborhood in data:
    voterParticipation = float(neighborhood[38])
    
    if voterParticipation <= 35:
      voterData['Low'] += 1
    elif voterParticipation < 45:
      voterData['Moderate'] += 1
    else:
      voterData['High'] += 1
      
  return voterData

# -- Lead: Maria 
# Purpose: Determine which carpooling category most Baltimore neighborhoods fall within
# Parameters: data file
# Return: most frequent category
def findHighestCarpoolCategory(data):
  categoryFreq = {}
  # Iterates through each neighborhood in data and adds totals for each category of carpooling
  for neighborhood in data:
    carpool = neighborhood[39]
    if carpool not in categoryFreq:
      categoryFreq[carpool] = 1
    else:
      categoryFreq[carpool] += 1
  return max(categoryFreq, key=categoryFreq.get)

# -- Lead: Cyrus 
# Purpose: Graph categorical data
# Parameters: the data, whether the data is formatted as a dict, name of x-axis, name for y-axis, file to send to
# Return: N/A
def graphCategoricalData(data, formatted, xLabel, yLabel, outputFile):
  if formatted:
    categories = data
  else:
    # Place the unformatted data into a dictionary to total counts for each category.
    categories = {}
    for row in data:
      category = row[-1]
      if category in categories:
        categories[category] += 1
      else:
        categories[category] = 1
    
  # Graph the categorical data.
  x = [category for category in categories]
  y = [categories[category] for category in categories]
  plt.bar(x, y)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.savefig(outputFile, dpi=500)

# -- Lead: Maria 
# Purpose: Asks the user for a menu option until a valid option is entered
# Parameters: list of valid options
# Return: user's selected option
def fetchMenuOption(options):
  # Ask for option, loop until option is valid.
  option = input("\nEnter an option: ").upper()
  while option not in options:
    option = input("\nInvalid. Enter an option: ").upper()
  return option

# -- Lead: Maria & Cyrus
# Runs the program
def main():
  print('This program tracks information about sustainability in Baltimore.')
  print('What is the data file?')

  # Get valid file name and save data.
  filename = inputFileName()
  neighborhoods = fetch2DFileLines(filename)

  # The options loop.
  cont = True
  while cont:
    # Output the menu options and get a valid option from user.
    print('\nMenu Options:\n\t1. Aggregate Change in Open Spaces\n\t2. Aggregate Change in Dirty Streets\n\t3. Aggregate Voter Participation\n\t4. Highest Carpool Category\n\tQ. Quit')
    options = ['1', '2', '3', '4', '5', 'Q']
    option = fetchMenuOption(options)
    
    match(option):
      # Write data about the change in open spaces to a file. Graph the data.
      case '1':
        outputFile = input('\nWhere to send data? \n\tEnter file name: ')
        outputGraphFile = outputFile + '_graph.png'
        
        changeOpenSpace = aggregateChangeOpenSpace(neighborhoods)
        
        write2DListToFile(outputFile, changeOpenSpace)
        print(f'\nSuccess! Data saved to {outputFile}!')

        graphCategoricalData(changeOpenSpace, False, 'Change in Open Space (2011 - 2014)', '# of Neighborhoods', outputGraphFile)
        print(f'\nSuccess! Graph saved to {outputGraphFile}!')
        
      # Write data about the change in dirty streets to a file. Graph the data.
      case '2':
        outputFile = input('\nWhere to send data? \n\tEnter file name: ')
        outputGraphFile = outputFile + '_graph.png'
        
        changeDirtyStreets = aggregateChangeDirtyStreets(neighborhoods)
        
        write2DListToFile(outputFile, changeDirtyStreets)
        print(f'\nSuccess! Data saved to {outputFile}!')
        
        graphCategoricalData(changeDirtyStreets, False, 'Change in Dirty Streets (2010 - 2014)', '# of Neighborhoods', outputGraphFile)
        print(f'\nSuccess! Graph saved to {outputGraphFile}!')

      # Graph the data about voter participation.
      case '3':
        outputFile = input('\nWhere to send graph? \n\tEnter file name: ')
        
        voterData = aggregateVoterParticipationInfo(neighborhoods)
        
        graphCategoricalData(voterData, True, 'Voter Participation Category (2014)', '# of Neighborhoods', outputGraphFile)
        print(f'\nSuccess! Graph saved to {outputFile}!')

      # Output the highest carpool category.
      case '4':
        highestCarpoolCategory = findHighestCarpoolCategory(neighborhoods)
        print(f'\nThe carpool category which occurs most frequently is {highestCarpoolCategory}.')
      case 'Q':
        cont = False

  print('Bye!')

main()