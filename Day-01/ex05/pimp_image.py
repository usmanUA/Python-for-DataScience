import numpy as np

def ft_invert(array: list) -> list:
    ''' doc '''

    rgb = np.array(array)
    mx = rgb.max()
    return mx - rgb

def ft_red(array: list) -> list:
    ''' doc '''

    rgb = np.array(array)
    rgb[..., 1:] = 0
    r = rgb
    return r

def ft_green(array: list) -> list:
    ''' doc '''

    rgb = np.array(array)
    rgb[..., 0] = 0
    rgb[..., 2] = 0
    g = rgb
    return g

def ft_blue(array: list) -> list:
    ''' doc '''

    rgb = np.array(array)
    rgb[..., :2] = 0
    b = rgb
    return b

def ft_grey(array: list) -> list:
    ''' doc '''

    weights = np.array([0.2989, 0.5870, 0.1140])
    rgb = np.array(array)
    mx = rgb.max()
    print(f"before: {rgb[:1, :1, :]}")
    grey = rgb / 0
    print(f"before: {grey[:1, :1, :]}")
    return grey
