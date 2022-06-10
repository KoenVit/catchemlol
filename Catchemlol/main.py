from ast import Set
import challenges as challenge

def main():
    #from requirements import CatchEmAllRequirement
    from requirements import OneTrickRequirement
    challenge.SetAPI()

    print("\nWelcome to Catch 'em LoL.")
    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    #rankInput = CatchEmAllRequirement[(input('Type in what rank of Catch em all you want to see: ').upper())].value     # Ask for user input for rank
    rankInput = OneTrickRequirement[(input('Type in what rank of Catch em all you want to see: ').upper())].value     # Ask for user input for rank
    
    #challenge.CatchEmAll(nameInput, regionInput, rankInput)
    challenge.OneTrick(nameInput, regionInput, rankInput)
    input("Press enter to quit")

if __name__ == "__main__":
    main()