class calculator:
    ''' A simple calculator to perform + - * /'''

    def __init__(self, vector):
        ''' Initializes the Calculator Class'''
        self.vector = vector

    def __add__(self, object) -> None:
        ''' Performs the addition.'''
        updated_vector = [scalar + object for scalar in self.vector]
        self.vector = updated_vector
        print(updated_vector)

    def __mul__(self, object) -> None:
        ''' Performs the multiplication.'''
        updated_vector = [scalar * object for scalar in self.vector]
        self.vector = updated_vector
        print(updated_vector)

    def __sub__(self, object) -> None:
        ''' Performs the subtraction.'''
        updated_vector = [scalar - object for scalar in self.vector]
        self.vector = updated_vector
        print(updated_vector)

    def __truediv__(self, object) -> None:
        ''' Performs the true division.'''
        if (object == 0):
            print(f"Division is not possible with {object}")
        else:
            updated_vector = [scalar / object for scalar in self.vector]
            self.vector = updated_vector
            print(updated_vector)
