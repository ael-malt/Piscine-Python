from sys import argv
from ft_filter import ft_filter


def main():
    """
    Program accepts only 2 arguments:

    1. string (S)
    2. int (N)

    It will output a list of words from S that have a length greater than N.
    Words are separated from each other by space characters.
    Strings do not contain any special characters. (Punctuation or invisible)

    """
    try:
        # Check if we have exactly 2 arguments (+program name)
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")
        S = argv[1]
        # Check if argv[1] is a string and argv[2] is an int
        if type(S) is not str or not argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        N = int(argv[2])

        filtered_list = \
            list(ft_filter(lambda word: len(word) > N, S.split()))

        print(filtered_list)

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
