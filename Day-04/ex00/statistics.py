from typing import Any

def mean(tot: int, *args: Any, **kwargs: Any) -> bool:
    '''Calculates and Prints the mean of the given arguments'''

    if "mean" in kwargs.values():
        mean = float(sum(args)/tot)
        print(f"mean: {mean}")

def median(tot: int, *args: Any, **kwargs: Any):
    '''Finds and Prints the median of the given arguments'''

    if "median" in kwargs.values() and tot > 0:
        sorted_args = sorted(args)
        median = sorted_args[tot//2]
        print(f"median: {median}")

def quartile(tot: int, *args: Any, **kwargs: Any) -> None:
    '''Find and Prints the list of quartiles of the given arguments'''

    if "quartile" in kwargs.values():
        sorted_args = sorted(args)
        lower_half = sorted_args[:tot//2]
        upper_half = sorted_args[tot//2:]
        quartiles = [lower_half[len(lower_half)//2], upper_half[len(upper_half)//2]]
        print(f"quartile : {quartiles}")

def std(tot: int, *args: Any, **kwargs: Any) -> None:
    '''Calculates and Prints the std of the given arguments'''

    if "std" in kwargs.values():
        mean = float(sum(args)/tot)
        std = (sum([(x - mean) ** 2 for x in args])/tot) ** 0.5
        print(f"std : {std}")

def variance(tot: int, *args: Any, **kwargs: Any) -> None:
    '''Calculates and Prints the variance of the given arguments'''

    if "std" in kwargs.values():
        mean = float(sum(args)/tot)
        var = sum([(x - mean) ** 2 for x in args])/tot
        print(f"var : {var}")

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''Accepts Unknown number of positional arguments
and Unknown number of keyword arguments.
Performs Basic statistics on the numbers based on the keyword arguments'''

    tot = len(args)
    if tot > 0:
        mean(tot, *args, **kwargs)
        median(tot, *args, **kwargs)
        quartile(tot, *args, **kwargs)
        std(tot, *args, **kwargs)
        variance(tot, *args, **kwargs)
    else:
        values = ["mean", "median", "quartile", "std", "var"]
        tot_errors = len([val for val in values if val in kwargs.values()])
        for error in range(tot_errors):
            print("ERROR")
