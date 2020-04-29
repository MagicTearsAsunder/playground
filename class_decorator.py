import time
from functools import wraps


def decorated(max_cache=3):
    def new_method(method):
        nonlocal max_cache
        method.max_cache = max_cache
        return method
    return new_method


def method_decorator(method, cache):
    @wraps(method)
    def new_method(self):
        if self.value not in cache[method.__name__]:
            if len(cache[method.__name__]) > method.max_cache:
                cache[method.__name__].pop(next(iter(cache[method.__name__])))
            cache[method.__name__][self.value] = method(self)
        return cache[method.__name__][self.value]
    return new_method


def cache(cache_name="CACHE"):
    def class_decorator(cls):
        nonlocal cache_name
        setattr(cls, cache_name, {})
        cache = getattr(cls, cache_name)
        for method_name in cls.__dict__:
            method = getattr(cls, method_name)
            if hasattr(method, 'max_cache'):
                cache[method_name] = {}
                setattr(cls, method_name, method_decorator(method, cache))
        return cls
    return class_decorator


@cache(cache_name="MY_NAME")
class Counter:
    def __init__(self, value):
        self.value = value

    @decorated(max_cache=4)
    def sqr(self):
        print("Calculating..")
        time.sleep(1)
        return type(self)(self.value**2)

    def sqrt(self):
        print("Calculating..")
        time.sleep(1)
        return type(self)(self.value**0.5)

    def half(self):
        print("Calculating..")
        time.sleep(1)
        return type(self)(self.value // 2)

    def __repr__(self):
        return f"Value is {self.value}"
