def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print("This is the Office, you hear parrots!")
    elif answer == "right" or answer == "r":
        print("Of course this is the Work Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()


clinic()
