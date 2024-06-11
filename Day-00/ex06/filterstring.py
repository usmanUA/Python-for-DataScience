import sys


def main():
    ''' Takes a string and a number as argument
Outputs the words from the string with length greater than the
number given.
    '''

    if (len(sys.argv) > 3 or len(sys.argv) < 3):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    string = sys.argv[1]
    str_length = sys.argv[2]
    try:
        length = int(str_length)
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    words = string.split(" ")
    words = [word for word in words if (lambda w: len(w) > length)(word)]
    print("{}".format([word for word in words]))


if __name__ == "__main__":
    main()
