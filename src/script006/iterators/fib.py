import typing


def gen_fib(n: int) -> typing.Generator:
    x,y = 0,1
    while n>0:
        yield y
        x,y = y, x+y
        n-=1
    # place your code here
    pass

def func_fib(n: int) -> typing.List:
    x,y = 0,1
    result = []
    while n > 0:
        result.append(y)
        x,y = y, x+y
        n-=1
    return result
    # place your code here
    pass
    return 1
