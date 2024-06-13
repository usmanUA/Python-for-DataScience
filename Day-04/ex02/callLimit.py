def callLimit(limit: int):
    '''Call Limiter'''
    count = 0
    def callLimiter(function):
        ''' doc'''
        def limit_function(*args: any, **kwds: any):
            '''doc'''
            nonlocal count

            if (count >= limit):
                print(f"{function} call too many times")
            else:
                count += 1
                function(*args, **kwds)

        return limit_function
    return callLimiter
