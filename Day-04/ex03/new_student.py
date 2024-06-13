import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    '''Generates and returns an ID string for the new student'''
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    '''doc'''
    name: str
    surname: str
    active: bool = True
    login: str = None
    id: str = generate_id()

    def __post_init__(self):
        '''Initializes make_login method to make the student login'''

        self.make_login()

    def make_login(self):
        '''Creates Login Name of the Student'''

        self.login = self.name[0] + self.surname
