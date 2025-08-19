import random

bestTeamEver = ["Tom Brady", "Steph Curry", "Victor Tsoi"]

def getRandomPlayer(playerList):
    return playerList[random.randint(0,len(playerList)-1)] 
    #Returns element of playerList array at a random index between 0 and len(playerList).

print(getRandomPlayer(bestTeamEver))
