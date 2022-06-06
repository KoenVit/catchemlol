from doctest import master
from enum import IntEnum
import cassiopeia as cass

class Rank(IntEnum):
    IRON = 100
    BRONZE = 500
    SILVER = 1000
    GOLD = 5000
    PLATINUM = 10000
    DIAMOND = 50000
    MASTER = 100000
    GRANDMASTER = 107500
    CHALLENGER = 115000

def SetAPIKey(APIKey):
    cass.set_riot_api_key(APIKey)

def PrintList(list, rank):
    sumPointsWithout = 0
    print("These champions are not yet at " + str(rank) + " mastery points: ")
    for cm in list:
        if(len(list) - list.index(cm) > 9):
            print("\033[1;33;40m" + cm.champion.name, cm.points)
            sumPointsWithout += cm.points
        else:
            print("\033[1;31;40m" + cm.champion.name, cm.points)
    remainingMasteryWithout = ((len(list) - 9) * rank) - sumPointsWithout
    print("\033[1;37;40mThis means that you still need a total of ", str(remainingMasteryWithout), "mastery points.")

def main():
    print("\nWelcome to Catch 'em LoL.")
    SetAPIKey("RGAPI-417dfde6-b188-4d82-8020-0d13e6801181")

    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    rankInput = Rank[(input('Type in what rank of Catch em all you want to see: ').upper())].value

    masteries = cass.get_champion_masteries(nameInput, regionInput).filter(lambda cm: cm.points < rankInput)
    PrintList(masteries, rankInput)

    input("Press enter to quit")
    
if __name__ == "__main__":
    main()