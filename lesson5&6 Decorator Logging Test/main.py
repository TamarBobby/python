#region ex1
from hashlib import new

import datetime


def decorator(func):
    def wrapper():
        begin = datetime.datetime.now()
        func()
        finish = datetime.datetime.now()
        print(finish - begin)

    return wrapper


@decorator
def my_func():
    print('hi!')
    for i in range(1, 100):
        print(i)


#my_func()

#endregion

#region ex2

def cache(func):
    results = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in results:
            results[key] = func(*args, **kwargs)
        return results[key]
    return wrapper

@cache
def genfunc(num):
    x1, x2 = 1, 1
    for _ in range(num):
        x1, x2 = x2, x1 + x2
        print(x1 , x2)
    return x2

for _ in range(10):
    print(genfunc(_))
    print("-------------------------------------")
for _ in range(10):
    print(genfunc(_))
    print("-------------------------------------")
#endregion

