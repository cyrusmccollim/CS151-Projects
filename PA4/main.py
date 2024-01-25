import os

def inputExistingFileName():
  fileName = input('\tEnter file: ').strip()
  while not os.path.isfile(fileName):
    fileName = input('\t[Invalid] Enter file: ').strip()
  return fileName

def readFileLines(fileName):
  file = open(fileName, 'r')
  lines = file.read().splitlines()
  file.close()
  return lines

def writeLinesToFile(fileName, list):
  file = open(fileName, 'w')
  for item in list:
    file.write(item + '\n')
  file.close()

def inputMenuSelection(options):
  option = input('\tEnter selection: ').upper().strip()
  while option not in options:
    option = input('\t[Invalid] Enter selection: ').upper().strip()
  return option

def averageLength(list):
  charSum = 0
  for item in list:
    charSum += len(item)
  averageLength = charSum / len(list)
  return averageLength

def numOccurances(list, key):
  keyPadded = (' ' + key + ' ')
  count = 0
  for item in list:
    itemPadded = (' ' + item + ' ')
    if keyPadded in itemPadded:
      count += 1
  return count

def shortestLongest(list):
  shortest = min(list, key=len)
  longest = max(list, key=len)
  return [shortest, longest]

def extractLinesContaining(list, extractFile, key):
  keyPadded = (' ' + key + ' ')
  filteredList = []
  for item in list:
    itemPadded = (' ' + item + ' ')
    if keyPadded in itemPadded:
      filteredList += [item]
  writeLinesToFile(extractFile, filteredList)
  print('\nExtraction successful.')

def main():
  print('Use this program to analyze a file.')
  fileName = inputExistingFileName()
  fileLines = readFileLines(fileName)
  cont = True
  while cont:
    print('\nOptions:',
          '\n1: Average Line Length',
          '\n2: Count Word Occurances',
          '\n3: Extract Lines Containing',
          '\n4: Output Longest/Shortest',
          '\nN: New File',
          '\nQ: Quit')
    options = ['1', '2', '3', '4', '5', 'N', 'Q']
    option = inputMenuSelection(options)
    match(option):
      case '1':
        avg = averageLength(fileLines)
        print(f'\nAverage: {round(avg, 2)}')
      case '2':
        key = input('\tEnter search word: ').strip().lower()
        numOcc = numOccurances(fileLines, key)
        print(f'\nThere are {numOcc} instances.')
      case '3':
        print('\tExtract to what file?')
        extractFile = input('\tEnter file: ').strip()
        key = input('\tEnter word: ').strip().lower()
        extractLinesContaining(fileLines, extractFile, key)
      case '4':
        extremes = shortestLongest(fileLines)
        print(f'\nShortest: {extremes[0]}',
              f'\nLongest: {extremes[1]}')
      case 'N':
        fileName = inputExistingFileName()
        fileLines = readFileLines(fileName)
        print('\nFile updated.')
      case 'Q':
        cont = False

main()

