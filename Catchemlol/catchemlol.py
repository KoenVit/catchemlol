from ast import Set
import challenges as challenge

def main():
    challenge.SetAPI()

    print("\nWelcome to Catch 'em LoL.")
    regionInput = (str)(input('Type in your region: '))
    nameInput = (str)(input('Type in your summoner name: '))
    
    challenge.PrintCatchEmAll(nameInput, regionInput)
    input("Press enter to quit")

if __name__ == "__main__":
    main()