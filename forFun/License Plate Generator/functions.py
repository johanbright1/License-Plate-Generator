import random


def generatePlate():
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Change 26 to 25 because Python lists are 0-indexed (26 items total, max index is 25)
    a1 = random.randint(0, 25)
    a2 = random.randint(0, 25)
    a3 = random.randint(0, 25)

    na1 = alphabet[a1]
    na2 = alphabet[a2]
    na3 = alphabet[a3]

    # Use return instead of print so the GUI can receive the string
    return f"{na1.upper()}{na2.upper()}{na3.upper()}-{n1}{n2}{n3}{n4}"