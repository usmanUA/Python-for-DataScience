import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    ''' doc '''

    return [w/(h * h) for w, h in zip(weight, height)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ''' doc '''
    return [num > limit for num in bmi]

bmi = give_bmi([2.71, 1.15],[165.3, 38.4])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
