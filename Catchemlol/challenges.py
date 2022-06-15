import cassiopeia as cass
from apikey import apiKey

def SetAPI():
    cass.set_riot_api_key(apiKey)

def CatchEmAll(name, region, rank):
    from requirements import catchEmAllChallenge
    sumPointsWithout = 0

    masteries = cass.get_champion_masteries(name, region).filter(lambda cm: cm.points < rank)                           # List with correct filter depending on input                                                                                   
    championsThreshold = len(cass.get_champions(region)) - catchEmAllChallenge                                          # See threshold for challenge
     
    if(len(masteries) == 0):
        print("You have every single champion on " + str(rank) + " mastery points. Amazing!")
    else:
        print("These champions are not yet at " + str(rank) + " mastery points: ")
        from constants import TextColor as color
        for cm in masteries:
            if(len(masteries) - masteries.index(cm) > championsThreshold):
                print(color.YELLOW + cm.champion.name, cm.points)
                sumPointsWithout += cm.points
            else:
                print(color.RED + cm.champion.name, cm.points)

        remainingMasteryWithout = ((len(masteries) - championsThreshold) * rank) - sumPointsWithout
        championsToDo = str(len(masteries) - championsThreshold)

        if(remainingMasteryWithout > 0):
            print(color.WHITE + "This means that you still need a total of", str(remainingMasteryWithout),
             "mastery points over", championsToDo, "champions.")
        else:
            print(color.WHITE + "Congratulations! You have at least " + str(catchEmAllChallenge) + 
            " champions on " + str(rank) + " mastery points.")

def OneTrick(name, region, rank):
    masteries = cass.get_champion_masteries(name, region).filter(lambda cm: cm.points >= 0)
    highestChamp = masteries[0]
    print("Your current highest mastery champion is " + highestChamp.champion.name + " with " + str(highestChamp.points) + " mastery points.")
    masteryNeeded = rank - highestChamp.points
    if(masteryNeeded <= 0):
        print("You already have this medal, congratulations!")
    else:
        print("You need " + str(masteryNeeded) + " more mastery points to get to " + str(rank) + " mastery points!")