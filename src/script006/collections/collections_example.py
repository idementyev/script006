from collections import defaultdict, ChainMap, namedtuple
import traceback
"""
In [9]: defaults = {'USER':'unknown', 'SESSION': 'xfce'}

In [10]: from collections import ChainMap

In [11]: c = ChainMap(os.env)
os.environ   os.environb

In [11]: c = ChainMap(os.environ, def)
def       defaults

In [11]: c = ChainMap(os.environ, defaults)

In [12]: c.get('USER')
Out[12]: 'mkoshel'

In [13]: c2 = ChainMap(defaults, os.en)
os.environ   os.environb

In [13]: c2 = ChainMap(defaults, os.environ)

In [14]: c2.get('USER')
Out[14]: 'unknown'

In [15]:
"""

def with_default_dict():
    d = defaultdict(list)
    for k in 'longverylongstring':
        d[k].append(k)
    print(d)

def with_builtins_dict():
    d = {}
    for k in 'longverylongstring':
        d[k].append(k)
    print(d)



if __name__ == '__main__':

    with_default_dict()
    try:
        with_builtins_dict()
    except KeyError:
        print(traceback.format_exc())
    print("execution finished!")