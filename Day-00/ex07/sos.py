import sys

morse = {
    ' ': '/ ',     'A': '.- ',    'B': '-... ',  'C': '-.-. ',
    'D': '-.. ',   'E': '. ',     'F': '..-. ',  'G': '--. ',
    'H': '.... ',  'I': '.. ',    'J': '.--- ',  'K': '-.- ',
    'L': '.-.. ',  'M': '-- ',    'N': '-. ',    'O': '--- ',
    'P': '.--. ',  'Q': '--.- ',  'R': '.-. ',   'S': '... ',
    'T': '- ',     'U': '..- ',   'V': '...- ',  'W': '.-- ',
    'X': '-..- ',  'Y': '-.-- ',  'Z': '--.. ',
    '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
    '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
    '8': '---.. ', '9': '----. '
}


def main():
    ''' Takes a string as Argument
    Outputs the morse code for the given string
    '''

    if (len(sys.argv) > 2 or len(sys.argv) < 2):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    string = sys.argv[1]
    if not isinstance(string, str):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    print("{}".format(''.join(morse.get(c.upper(), '') for c in string)))


if __name__ == "__main__":
    main()
