import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    ''' doc '''

    try:
        isinstance(family, list)
    except ValueError:
        return []
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    new_arr = arr[start:end]
    print(f"My new shape is : {new_arr.shape}")
    return new_arr
