from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    '''Class for False King: "Joffery Baratheon".'''

    def __init__(self, first_name, is_alive=True, family_name = 'Baratheon', eyes = 'brown', hairs = 'dark'):
        ''' Initializes the Class King as sets the name of the King'''
        super().__init__(first_name)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name, self.eyes, self.hairs = (family_name, eyes, hairs)

    def set_eyes(self, eyes_color):
        ''' Sets the eyes color of the King'''
        self.eyes = eyes_color

    def set_hairs(self, hair_color):
        ''' Sets the hairs color of the King'''
        self.hairs = hair_color

    def get_eyes(self):
        ''' Returns the Eyes color of the King'''
        return self.eyes

    def get_hairs(self):
        ''' Returns the Hairs color of the King'''
        return self.hairs
