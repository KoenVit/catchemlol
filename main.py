import random

import cassiopeia as cass

cass.set_riot_api_key("RGAPI-6bc918ac-5018-4933-8e30-6b9df80e2569")

summoner = cass.get_summoner(name="KoenVit", region="EUW")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))

champions = cass.get_champions(region="NA")
random_champion = random.choice(champions)
print("He enjoys playing champions such as {name}.".format(name=random_champion.name))