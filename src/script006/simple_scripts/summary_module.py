
def summary(n: int=0)-> int:
    """n: last value in range from 0 to n (integer); cannot be negative
        :returns integer
    """
    if n < 0: raise ValueError
    return sum(range(0, n+1))
