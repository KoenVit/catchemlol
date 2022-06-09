import cassiopeia as cass
from requirements import CatchEmAll
from constants import apiKey, championsChallenge

def PrintList(list, rank, region):
    sumPointsWithout = 0
    championsThreshold = len(cass.get_champions(region)) - championsChallenge
    if(len(list) == 0):
        print("You have every single champion on " + str(rank) + " mastery points. Amazing!")
    else:
        print("These champions are not yet at " + str(rank) + " mastery points: ")
        for cm in list:
            if(len(list) - list.index(cm) > championsThreshold):
                print("\033[1;33;40m" + cm.champion.name, cm.points)
                sumPointsWithout += cm.points
            else:
                print("\033[1;31;40m" + cm.champion.name, cm.points)
        remainingMasteryWithout = ((len(list) - championsThreshold) * rank) - sumPointsWithout
        championsToDo = str(len(list) - championsThreshold)

        if(remainingMasteryWithout > 0):
            print("\033[1;37;40mThis means that you still need a total of", str(remainingMasteryWithout), "mastery points over", championsToDo, "champions.")
        else:
            print("\033[1;37;40mCongratulations! You have at least " + str(championsChallenge) + " champions on " + str(rank) + " mastery points.")

def main():
    cass.set_riot_api_key(apiKey)

    print("\nWelcome to Catch 'em LoL.")
    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    rankInput = CatchEmAll[(input('Type in what rank of Catch em all you want to see: ').upper())].value

    masteries = cass.get_champion_masteries(nameInput, regionInput).filter(lambda cm: cm.points < rankInput)
    PrintList(masteries, rankInput, regionInput)
    input("Press enter to quit")

if __name__ == "__main__":
    main()