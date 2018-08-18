# ScotlandYard_Map.py
# File defines libraries for the map based on
# taxi, bus and underground connections

    
taxi_part1 = {1:(2,5), 2:(1,3,5), 3:(2,4,6), 4:(3,6,9), 5:(1,2,7,8), 6:(3,4,8,12), 7:(5,8,10), 8:(5,6,7,11,12), 9:(4,13)}
taxi_part2 = {10:(7,11), 11:(8,10,12), 12:(6,8,11,13), 13:(9,12,14), 14:(12,13)}

taxi = dict(list(taxi_part1.items()) + list(taxi_part2.items()))

bus = {1:(4,10), 4:(1,8,9), 8:(4,10,12), 9:(4,12), 10:(1,8,12), 12:(8,9,10,14), 14:(12,)}

underground = {4:(10,14), 10:(4,14), 14:(4,10)}
