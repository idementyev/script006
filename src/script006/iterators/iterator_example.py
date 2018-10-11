from typing import Iterable, List, Iterator, Any

def iter_through(i: Iterable) -> List:
    l: List = []
    iterator: Iterator = iter(i)
    while True:
        try:
            l.append(next(iterator))
        except StopIteration:
            break
    return l
