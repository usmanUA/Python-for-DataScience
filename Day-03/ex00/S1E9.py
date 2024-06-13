from abc import ABC, abstractmethod

class Character(ABC):
    ''' Class to represent a Character '''

    def  __init__(self, first_name, is_alive=True):
        '''
Constructor for Character.

Parameters:
first_name (str): The first name of the character.
is_alive (bool, optional): The health state of the character.
Default is True.
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''
Method to change the health state of the character.

This method should be implemented by subclasses to change the
health state of the character.
        '''
        pass

class Stark(Character):
    ''' 
Inherits the Character Class
Represents a Stark
    '''

    def __init__(self, first_name, is_alive=True):
        '''
Creates (Initialize) a Stark
        '''
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''
Method to change the health state of the character.
        '''
        self.is_alive = False
