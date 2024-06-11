def all_thing_is_obj(object: any) -> int:
    ''' Prints the name of the type of an object and its
    type and returns an int (42)'''

    obj_type = type(object)
    obj_name = obj_type.__name__

    print(f"{obj_name.capitalize()} : {obj_type}")
    return 42
