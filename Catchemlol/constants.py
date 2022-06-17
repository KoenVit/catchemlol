from struct import Struct

class TextColor(Struct):
    WHITE = "\033[1;37;40m"
    RED = "\033[1;31;40m"
    YELLOW = "\033[1;33;40m"

regions = "EUW", "NA", "EUNE", "BR", "JP", "KR", "LAN", "LAS", "OCE", "RU", "TR"
regionsSet = set(regions)

supportedChallenges = "CATCHEMALL", "ONETRICK"
supportedChallengesSet = set(supportedChallenges)