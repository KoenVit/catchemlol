from enum import IntEnum

catchEmAllChallenge = 150

class CatchEmAllRequirement(IntEnum):
    IRON = 100
    BRONZE = 500
    SILVER = 1000
    GOLD = 5000
    PLATINUM = 10000
    DIAMOND = 50000
    MASTER = 100000
    GRANDMASTER = 107500
    CHALLENGER = 115000

class OneTrickRequirement(IntEnum):
    IRON = 850
    BRONZE = 1500
    SILVER = 9000
    GOLD = 38000
    PLATINUM = 110000
    DIAMOND = 280000
    MASTER = 840000
    GRANDMASTER = 1000000
    CHALLENGER = 1500000