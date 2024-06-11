import sys


def main():
    ''' Takes a string as Argument, Count and Prints
        Total characters
        Total UpperCase character
        Total lowercase characters
        Total Punctuation marks
        Total Spaces
        Total Digits
                    in the provided string
    '''

    if (len(sys.argv) == 2):
        string = sys.argv[1]
    elif (len(sys.argv) == 1):
        string = input("FT_STRING: ")
    if (len(sys.argv) > 2):
        print("Error")
        sys.exit(1)
    tot = len([c for c in string])
    print(f"The text contains {tot} characters:")
    tot = len([c for c in string if c.isupper()])
    print(f"{tot} upper letters")
    tot = len([c for c in string if c.islower()])
    print(f"{tot} lower letters")
    punc_marks = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~\\'''
    tot = len([c for c in string if c in punc_marks])
    print(f"{tot} punctuation marks")
    tot = string.count(" ")
    print(f"{tot} spaces")
    tot = len([c for c in string if c.isdigit()])
    print(f"{tot} digits")


if __name__ == "__main__":
    main()
