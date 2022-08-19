

secretWord = "CBTNuggets"
letterGuesed = ""
failureCount = 6

while failureCount > 0:
    guess = input("do a guesse: ")

    if guess in secretWord:
        
        print(f"correct letere {guess} is in de word")
    else:
        failureCount -= 1
        print(f"incorrect. thare are no {guess} in the secred word. {failureCount} turn(s) left.")

    letterGuesed = letterGuesed + guess
    wrongLetterCount = 0
    for letter in secretWord:
        if letter in letterGuesed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount +=1
    print("")

    if wrongLetterCount == 0:
        print(f"you won, the word was: {secretWord}")
        break

else:
    print("you lose")