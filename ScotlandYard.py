# ScotlandYard.py
#
# Code plays the role of Mr X
# Randomly selects where to move to
# Checks players move and tracks all peices
#
# Currently has arguments for SetupMap
# and RandomStartLocs to enable testing options.
# These can be stripped in the final version.
#
# Written by Stephen Outten and Aria Outten August 2018

import csv, random, tabulate

def SetupMap(Testing):
    '''
    SetupMap(Testing)
    Load the transport connections that map up the map
    as four dictionaries, one for each type of transport.
    Usage:
      taxi,bus,underground,ferry = SetupMap(True/False)
       arg=True - loads a smaller test map.
       arg=Flase - loads the full game board map.
    '''
    flag = -1
    map_dat = [{},{},{},{}]
    if Testing:
        map_fn = 'Map_ScotlandYard_Testing.dat'
    else: 
        map_fn = 'Map_ScotlandYard.dat'
    with open(map_fn, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader: 
            if len(rows)==1:
                flag=flag+1
                continue
            map_dat[flag][int(rows[0])] = list(map(int, rows[1:]))
    return map_dat[0], map_dat[1], map_dat[2], map_dat[3]
    


def RandomStartLocs(NoPlayers,Testing):
    '''
    RandomStartLocs(NoPlayes,Testing)
    Randomly assigns starting locations to each of the players and Mr X.
    Usage: MrXLoc, PlayerLocs = RandomStartLocs(NoPlayers,Testing)
      MrXLoc - Starting location for Mr X.
      PlayerLocs - Starting location for players.
      NoPlayers - Integer number of players.
      Testing - Boolean - True using locations for testing map, False uses locations from game. 
    '''
    if Testing:
        PossibleStartLocs = [1,3,5,7,9,13]    # for use with testing map
    else:
        PossibleStartLocs = [13,26,29,34,50,53,91,94,103,112,117,132,138,141,155,174,197,198]
    StartLocs = random.sample(PossibleStartLocs, NoPlayers+1)
    MrXStartLoc = [StartLocs[0]]     # creates list with first value random
    PlayerStartLocs = StartLocs[1:]
    for loc in range(len(PlayerStartLocs)):
      StartLocText = 'Player ' + str(loc+1) + ' starts at ' + str(PlayerStartLocs[loc])
      print(StartLocText)
    return MrXStartLoc, PlayerStartLocs


def MrXMove(curloc):
    '''
    MrXMove(curloc)
    Selects and returns Mr X's next location and th transport to get there.
    Usage: newloc,transport = MrXMove(curloc)
      curloc - Mr X's current location
      newloc - Location Mr X moves to
      transport - Transport Mr X used to move to new location
    This fuction get possible exits, randomly selects one, randomly selects mode of transport.
    '''

    if curloc in underground:
        pos_exits = taxi[curloc] + bus[curloc] + underground[curloc]
    elif curloc in bus:
        pos_exits = taxi[curloc] + bus[curloc]
    else:
        pos_exits = taxi[curloc]
        
    # Reduces list of exits
    pos_exits = tuple(set(pos_exits))

    # Randomly select exit
    RandMove = random.randint(0,len(pos_exits)-1)
    newloc = pos_exits[RandMove]
    print(pos_exits)        # FOR DEBUG
    print(newloc)  # FRO DEBUG
    
    # Create list of availabel modes of travel
    pos_travel = []
    if curloc in underground: pos_travel.append('underground')
    if curloc in bus: pos_travel.append('bus')
    if curloc in taxi: pos_travel.append('taxi')
    
    # Randomly select mode of transport to reach exit
    RandTran = random.randint(0,len(pos_travel)-1)
    transport = pos_travel[RandTran]
    
    print(transport)  # FOR DEBUG

    return newloc, transport


# Main Program Start Here 
if __name__ == '__main__':
    # Setup initial variables, including map dictionaries
    Testing = True
    taxi, bus, underground, ferry = SetupMap(Testing)
    NoPlayers = 5
    ttxt = 'taxi',
    btxt = 'bus',
    utxt = 'underground',
    MrXTransport = ['start']
    Turn = 1
 
    # Setup initial locations and transportations 
    Locations = [['Mr X']]
    for player in range(NoPlayers): Locations.append(['Player '+str(player+1)])
    MrXStartLoc,PlayerStartLocs = RandomStartLocs(NoPlayers,Testing)
    Locations[0].append(MrXStartLoc[0])
    for player in range(NoPlayers): Locations[player+1].append(PlayerStartLocs[player])
    Transports = [['Start']]
    for player in range(NoPlayers): Transports.append(['Start'])
    print(tabulate.tabulate(Locations))

    while Turn<10:
        newloc, transport = MrXMove(Locations[0][Turn])
        Locations[0].append(newloc)
        Transports[0].append(transport)
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
