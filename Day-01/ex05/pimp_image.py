import numpy as np

def ft_invert(array: list) -> list:
    ''' Invert the colors of the Image Array given as Argument and Returns it.'''

    rgb = np.array(array)
    mx = rgb.max()
    return mx - rgb

def ft_red(array: list) -> list:
    '''Excludes the green and blue color channels of the Image Array given as Argument and Returns it.'''

    rgb = np.array(array)
    rgb[..., 1:] = 0
    r = rgb
    return r

def ft_green(array: list) -> list:
    '''Excludes the red and blue color channels of the Image Array given as Argument and Returns it.'''

    rgb = np.array(array)
    rgb[..., 0] = 0
    rgb[..., 2] = 0
    g = rgb
    return g

def ft_blue(array: list) -> list:
    '''Excludes the red and green color channels of the Image Array given as Argument and Returns it.'''

    rgb = np.array(array)
    rgb[..., :2] = 0
    b = rgb
    return b

def ft_grey(array: list) -> list:
    '''Excludes the red, green and blue color channels of the Image Array given as Argument and Returns it.'''

    grey = [[int(sum(pixel)/len(pixel)) for pixel in row] for row in array]
    return grey
