from sys import argv


def raiseError():
    raise AssertionError("the arguments are bad")


def main():
    """
    Takes a single argument:

    1. string (S)

    Encodes its content as Morse Code.

    It supports space and alphanumeric characters.

    Complete morse characters are separated by a single space.

    A space character is represented by a slash /
    """
    NESTED_MORSE = {
        " ": "/ ", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        }

    try:
        if len(argv) != 2:
            raise AssertionError("the arguments are bad")
        text = argv[1].upper()
        morse_text = \
            [NESTED_MORSE[c] if c in NESTED_MORSE else raiseError()
             for c in text]
        print(''.join(morse_text))
    except AssertionError as error:
        print(AssertionError.__name__ + "", error)


if __name__ == "__main__":
    main()




