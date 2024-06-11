class filter_class:
    ''' Provides the basic behavior to he filter funciton in Python '''

    def __init__(self, func, iterator):
        self.func = func
        self.iterator = iterator
        self._iterator = iter(iterator)

    def __iter__(self):
        return (self)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if self.func is None or self.func(item):
                return item

    def __repr__(self):
        return "< My very Own ft_filter>"


def ft_filter(func, iterator):
    '''ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
'''
    return (filter_class(func, iterator))
