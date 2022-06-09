import cassiopeia as cass
from requirements import CatchEmAll
from constants import apiKey, catchEmAllChallenge

def PrintList(name, region):
    rankInput = CatchEmAll[(input('Type in what rank of Catch em all you want to see: ').upper())].value    # Ask for user input for rank
    masteries = cass.get_champion_masteries(name, region).filter(lambda cm: cm.points < rankInput)          # List with correct filter depending on input
    sumPointsWithout = 0                                                                                    
    championsThreshold = len(cass.get_champions(region)) - catchEmAllChallenge                              # See threshold for challenge

    if(len(masteries) == 0):
        print("You have every single champion on " + str(rankInput) + " mastery points. Amazing!")
    else:
        print("These champions are not yet at " + str(rankInput) + " mastery points: ")
        from constants import Color as color
        for cm in masteries:
            if(len(masteries) - masteries.index(cm) > championsThreshold):
                print(color.YELLOW + cm.champion.name, cm.points)
                sumPointsWithout += cm.points
            else:
                print(color.RED + cm.champion.name, cm.points)

        remainingMasteryWithout = ((len(masteries) - championsThreshold) * rankInput) - sumPointsWithout
        championsToDo = str(len(masteries) - championsThreshold)

        if(remainingMasteryWithout > 0):
            print(color.WHITE + "This means that you still need a total of", str(remainingMasteryWithout),
             "mastery points over", championsToDo, "champions.")
        else:
            print(color.WHITE + "Congratulations! You have at least " + str(catchEmAllChallenge) + 
            " champions on " + str(rankInput) + " mastery points.")

def main():
    cass.set_riot_api_key(apiKey)

    print("\nWelcome to Catch 'em LoL.")
    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    

    
    PrintList(nameInput, regionInput)
    input("Press enter to quit")

if __name__ == "__main__":
    main()