import cassiopeia as cass
from rank import Rank

def PrintList(list, rank, region):
    sumPointsWithout = 0
    championsChallenge = 150
    championsThreshold = len(cass.get_champions(region)) - championsChallenge
    print("These champions are not yet at " + str(rank) + " mastery points: ")

    for cm in list:
        if(len(list) - list.index(cm) > championsThreshold):
            print("\033[1;33;40m" + cm.champion.name, cm.points)
            sumPointsWithout += cm.points
        else:
            print("\033[1;31;40m" + cm.champion.name, cm.points)
    remainingMasteryWithout = ((len(list) - championsThreshold) * rank) - sumPointsWithout
    print("\033[1;37;40mThis means that you still need a total of", str(remainingMasteryWithout), "mastery points over", str(len(list) - championsThreshold), "champions.")

def main():
    from apikey import apiKey
    cass.set_riot_api_key(apiKey)

    print("\nWelcome to Catch 'em LoL.")
    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    rankInput = Rank[(input('Type in what rank of Catch em all you want to see: ').upper())].value

    masteries = cass.get_champion_masteries(nameInput, regionInput).filter(lambda cm: cm.points < rankInput)
    PrintList(masteries, rankInput, regionInput)

    input("Press enter to quit")
    
if __name__ == "__main__":
    main()