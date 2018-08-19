# ScotlandYard.py
#
# Code plays the role of Mr X
# Randomly selects where to move to
# Checks players move and tracks all peices
#
# Written by Stephen Outten August 2018

import sys
sys.path.append('/home/everlone/Python/ScotlandYard')

import random, operator, csv
#from ScotlandYard_Map import taxi, bus, underground


def SetupMap():
    flag = -1
    map_dat = [{},{},{},{}]
    with open('Map_ScotlandYard.dat', mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader: 
            if len(rows)==1:
                flag=flag+1
                continue
            map_dat[flag][int(rows[0])] = list(map(int, rows[1:]))
    return map_dat[0], map_dat[1], map_dat[2], map_dat[3]
    


def RandomStartLocs(NoPlayers):
    global MrXLoc, PlayerLocs
    PossibleStartLocs = [13,26,29,34,50,53,91,94,103,112,117,132,138,141,155,174,197,198]
    StartLocs = random.sample(PossibleStartLocs, NoPlayers+1)
    MrXLoc = [StartLocs[0]]     # creates list with first value random
    PlayerLocs = StartLocs[1:]
    i = 0
    while i<len(PlayerLocs):
      StartLocText = 'Player ' + str(i+1) + ' starts at ' + str(PlayerLocs[i])
      print(StartLocText)
      i += 1


def MrXMove():
    '''
    Create list of Mr X's posisble exists 
    Reduce list removing duplicates
    Radnomly select one of the exits
    Create list of available modes to reach exit
    Randomly seelct one of the modes
    Update MrXLoc and MrXTransport with exit and mode
    '''

    global MrXLoc, MrXTransport

    if MrXLoc[Turn-1] in underground:
        pos_exits = taxi[MrXLoc[Turn-1]] + bus[MrXLoc[Turn-1]] + underground[MrXLoc[Turn-1]]
    elif MrXLoc[Turn-1] in bus:
        pos_exits = taxi[MrXLoc[Turn-1]] + bus[MrXLoc[Turn-1]]
    else:
        pos_exits = taxi[MrXLoc[Turn-1]]
        
    # Reduces list of exits
    pos_exits = tuple(set(pos_exits))

    # Randomly select exit
    RandMove = random.randint(0,len(pos_exits)-1)
    NextMove = pos_exits[RandMove]
    print(pos_exits)        # FOR DEBUG
    print(NextMove)  # FRO DEBUG
    
    # Create list of availabel modes of travel
    pos_travel = []
    if MrXLoc[Turn-1] in underground: pos_travel.append('undergorund')
    if MrXLoc[Turn-1] in bus: pos_travel.append('bus')
    if MrXLoc[Turn-1] in taxi: pos_travel.append('taxi')
    
    # Randomly select mode of transport to reach exit
    RandTran = random.randint(0,len(pos_travel)-1)
    NextTran = pos_travel[RandTran]
    
    # Update MrXLoc and MrXTransport
    MrXLoc.append(NextMove)
    MrXTransport.append(NextTran)
    print(NextTran)  # FOR DEBUG




# Main Program Start Here 
if __name__ == '__main__':
    taxi, bus, underground, ferry = SetupMap()
    NoPlayers = 5
    ttxt = 'taxi',
    btxt = 'bus',
    utxt = 'underground',
    MrXTransport = ['start']
    Turn = 1
    RandomStartLocs(NoPlayers)

    while Turn<10:
        MrXMove()
        Turn += 1



'''
Players moves can be taken with a=input('Player move: ')
The input needs to be checked to be integer
for CurPlayer in range(NoPlayers):
  try:
     userInput = int(input("Enter something: "))       
  except ValueError:
     print("Not an integer!")
     continue
  else:
     if userInput in taxi(PlayerLocs[CurPlayer]):  # NOT COMPELTE
         print('update playerlocs')
     else:
     break 
'''
    



'''
# Examples for checking and accessing grid
4 in taxi   # checks value exists in as key in dictionary, not in data
taxi[8]    # returns exits
'''
