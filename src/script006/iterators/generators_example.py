def subgenerator():
    yield 1
    return 2

def delegating_generator():
    x = yield from subgenerator()
    print("I'm inside delegating_generator: {}".format(x))
    # yield x

def coroutine():
    print("coroutine started!")
    while True:
        x = yield
        print("accepted new value: {}".format(x))
        yield x +1 #if x is not None else 0



if __name__ == '__main__':
    for _ in delegating_generator():print("I'm in main function: {}".format(_))

    c = coroutine()
    # next(c)
    while 1:
        counter = next(c)
        c.send(counter)
        if counter > 10: break