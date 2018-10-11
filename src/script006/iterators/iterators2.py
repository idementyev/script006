from types import GeneratorType

def fib_gen(n):
    cntr = n
    x,y = 0,1
    while cntr > 0:
        yield y
        x,y = y, x+1
        cntr-=1



if __name__ == '__main__':
    g = fib_gen(10)
    while 1:
        print(next(g))


