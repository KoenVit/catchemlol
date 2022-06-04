from doctest import master
import random

import cassiopeia as cass

cass.set_riot_api_key("RGAPI-507c4d57-4178-46d3-a668-10c56da1717d")

nameInput = input("Enter your summoner name: ")
print("For the following question, please write your region in capital letters (e.g. EUW or NA)")
regionInput = input("Enter your region: ")
rankInput = input("Silver or Platinum challenge: ")
lastNineInput = input("Do you want to include the bottom 9 champions, Y or N: ")

if(rankInput == "Silver"):
    masteryPointLimit = 1000
else:
    masteryPointLimit = 5000
summoner = cass.get_summoner(name=nameInput, region=regionInput)

masteryList = cass.get_champion_masteries(nameInput, regionInput).filter(lambda cm: cm.points < masteryPointLimit)

if(lastNineInput == "Y"):
    for i in range(9):
        masteryList.pop()

print("You still need to get the following champions up in mastery level:")
for cm in masteryList:
    print(cm.champion.name, cm.points)

sumPoints = 0

for cm in masteryList:
    sumPoints += cm.points

remainingPoints = (len(masteryList) * 5000) - sumPoints
print("This means that you still need a total of ", remainingPoints, "mastery points.")

#print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
#                                                                          level=summoner.level,
#                                                                          region=summoner.region))
#
#champions = cass.get_champions(region="NA")
#random_champion = random.choice(champions)
#print("He enjoys playing champions such as {name}.".format(name=random_champion.name))