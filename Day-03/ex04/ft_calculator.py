class calculator:
    '''A simple calculator to perform vector operations.'''

    def __init__(self):
        ''' Initializes the Calculator Class'''

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Performs dot product of 2 vectors'''
        print(f"Dot product is: {sum([scalar1 * scalar2 for scalar1, scalar2 in zip(V1, V2)])}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Performs vector addition'''
        print(f"Add Vector is : {[scalar1 + scalar2 for scalar1, scalar2 in zip(V1, V2)]}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Performs vector subtraction'''
        print(f"Add Vector is : {[scalar1 - scalar2 for scalar1, scalar2 in zip(V1, V2)]}")
