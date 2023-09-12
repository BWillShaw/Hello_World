
print("Hello World!\n\n")

def print_chunky_letter(letter):
    if letter == " ":
        print("      ")
        return

    if letter == "H":
        print("HH  HH")
        print("HH  HH")
        print("HHHHHH")
        print("HH  HH")
        print("HH  HH")

    elif letter == "E":
        print("EEEEE")
        print("E    ")
        print("EEEEE")
        print("E    ")
        print("EEEEE")

    elif letter == "L":
        print("L    ")
        print("L    ")
        print("L    ")
        print("L    ")
        print("LLLLL")

    elif letter == "O":
        print(" OOO ")
        print("O   O")
        print("O   O")
        print("O   O")
        print(" OOO ")

    elif letter == "W":
        print("\n")
        print("W   W")
        print("W   W")
        print("W W W")
        print("WW WW")
        print("W   W")

    elif letter == "R":
        print("RRRR ")
        print("R   R")
        print("RRRR ")
        print("R  R ")
        print("R   R")

    elif letter == "D":
        print("DDD  ")
        print("D   D")
        print("D   D")
        print("D   D")
        print("DDD  ")

    print()


def print_chunky_text(text):
    for letter in text.upper():
        print_chunky_letter(letter)

print_chunky_text("Hello World")
