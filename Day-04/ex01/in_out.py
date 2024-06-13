from typing import Union

def square(x: Union[int, float]) -> Union[int, float]:
    '''Calculates and returns the square of the Argument'''
    return x * x

def pow(x: Union[int, float]) -> Union[int, float]:
    '''Calculates and returns the power of the Argument'''
    return x ** x

def outer(x: Union[int, float], function) -> object:
    '''Returns a pointer to the inner function'''
    count = 0
    def inner() -> float:
        '''Calls the function given as argument in the outer function each time the object to
this Inner function is called. Uses nonlocal scope for the variable x to save the previous state of the variable'''
        nonlocal x

        count = function(x)
        x = count
        return count

    return inner
