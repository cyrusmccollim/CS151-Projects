def inputInt(min, max):
  response = input(f'\tEnter value ({min} - {max}): ').strip()
  
  while (not response.isdigit()) or (not min <= int(response) <= max):
    response = input(f'\tEnter value ({min} - {max}): ').strip()
    
  return int(response)

def maxChoice(sticksLeft):
  if sticksLeft > 3:     
    return 3
  else:
    return sticksLeft

def bestMove(sticksLeft):
  bestMoves = [1, 1, 2, 3, 1, 2, 3]

  while sticksLeft > 7:
    sticksLeft -= 7

  return bestMoves[sticksLeft - 1]

def promptStart():
  keepPlaying = input('\nStart new game? [Y/N]: ').lower().strip()

  while keepPlaying == 'y':
    startGame()
    keepPlaying = input('\nStart new game? [Y/N]: ').lower().strip()

def startGame():
  print('\nChoose the number of sticks to start with.')
  sticksLeft = inputInt(10, 100)
  print('')

  player = 1
  while sticksLeft > 1:
    if player != 3:
      print(f'[Player {player}] How many sticks will you grab?')
      sticksLeft -= inputInt(1, maxChoice(sticksLeft))
      print(f'\n🡢  {sticksLeft} stick(s) remain on the table.')
      player += 1
    else:
      computerChoice = bestMove(sticksLeft)
      sticksLeft -= computerChoice
      print(f'[Computer] has grabbed {computerChoice} stick(s).',
            f'\n\n🡢  {sticksLeft} stick(s) remain on the table.')
      player = 1

  losses[player-1] += 1

  print(f'Uh-Oh, player {player} has lost!',
       f"\nHere are the tallies: ",
       f'\n---------------',
       f'\nPlayer 1: {losses[0]}',
       f'\nPlayer 2: {losses[1]}',
       f'\nPlayer 3: {losses[2]} (Computer)',
       f'\n---------------')

losses = [0, 0, 0]
print('\n~ WELCOME TO THE GAME OF STICKS! ~',
      '\nIn this game there are a pile of sticks on the table.', 
      '\nThree players alternate taking 1 to 3 sticks.',
      '\nThe player to take the last stick loses.',
      '\nThe third player is a computer.',
      '\nGood luck!')
promptStart()
print("\nThank you for playing. Goodbye!")