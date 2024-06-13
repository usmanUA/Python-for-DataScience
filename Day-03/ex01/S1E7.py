from S1E9 import Character

class Baratheon(Character):
    '''Representing the Baratheon family.'''

    def __init__(self, first_name, is_alive=True, family_name = 'Baratheon', eyes = 'brown', hairs = 'dark'):
        '''Creates the Baratheon family. '''
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name, self.eyes, self.hairs = (family_name, eyes, hairs)

    def die(self):
        ''' Method to change the health state of the character.'''
        self.is_alive = False

    def __str__(self):
        '''Returns the string representation of Baratheon family suitable for debugging'''
        vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {vector}"

    def __repr__(self):
        '''Returns the string representation of Baratheon family'''
        vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {vector}"


class Lannister(Character):
    '''Representing the Lannister family.'''

    def __init__(self, first_name, is_alive=True, family_name = 'Lannister', eyes = 'blue', hairs = 'light'):
        '''Creates the Lannister family.'''
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name, self.eyes, self.hairs = (family_name, eyes, hairs)

    def die(self):
        '''Method to change the health state of the character.'''
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        '''Create a new instance of the Class Lannister'''
        new_obj = cls(first_name, is_alive)
        new_obj.first_name = first_name
        new_obj.is_alive = is_alive
        return new_obj

    def __str__(self):
        '''Returns the string representation of Baratheon family'''
        vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {vector}"

    def __repr__(self):
        '''Returns the string representation of Baratheon family suitable for debugging'''
        vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {vector}"
