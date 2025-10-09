from sys import argv


def analyze_text(text):
    """
    Prints the following information about the text:
    1. The number of characters in the text
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits

    Argument:

    text (input str): The given text to analyze
    """

    text_len = len(text)
    upper_count = 0
    lower_count = 0
    punctuation_marks = ".?!,:;-[]{}()'\"…"
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    for c in text:
        upper_count += c.isupper()
        lower_count += c.islower()
        punctuation_count += punctuation_marks.count(c)
        space_count += c.isspace()
        digit_count += c.isdigit()

    print(f"The text contains {text_len} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digit")


def main():
    """
    Analyzes the given text to print information about its composition

    Asks for user input if no argument is given

    Prints AssertionError: Too many arguments provided

    """
    try:
        # Check if we have argv[1], else prompt user input and handle Ctrl-C-D
        text = ""
        if len(argv) < 2:
            try:
                text = input("What is the text to count?\n")
                text += "\n"
            except (EOFError, KeyboardInterrupt):
                pass
        if len(argv) == 2:
            text = argv[1]
        if len(argv) > 2:
            raise AssertionError("more than one argument is provided")
        if text:
            analyze_text(text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
