def NULL_not_found(object: any) -> int:
    ''' Prints the value and type of objects if they're NULL '''

    obj_type = type(object)
    obj_name = obj_type.__name__
    if (object is None):
        print(f"Nothing: {obj_name.capitalize()[:4]} {obj_type}")
    elif (isinstance(object, bool) and not object):
        print(f"Fake: False {obj_type}")
    elif (isinstance(object, float) and object != object):
        print(f"Cheese: {object} {obj_type}")
    elif (isinstance(object, int) and object == 0):
        print(f"Zero: {object} {obj_type}")
    elif (isinstance(object, str) and not object):
        print(f"Empty: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1
    return 0
