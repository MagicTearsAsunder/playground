"""
Pass an instance of any class to instance() function.
Returns recursevely all subclasses and superclasses.
"""


def inspector(instance):
    print("Instance attributes:")

    for i in sorted(instance.__dict__.keys()):
        print(f"{i}: {instance.__dict__[i]}")

    print("-" * 65)
    print(" Attributes    | Value")
    cache = set()
    recsearch(instance.__class__, cache)


def recsearch(the_class, cache):
    print("-" * 65)
    cache.add(the_class)

    for i in sorted(the_class.__dict__.keys()):
        placeholder = " " * (15 - len(i))
        print(f"{i}{placeholder}| {the_class.__dict__[i]}")

    if the_class.__bases__ == (object,):
        print("-" * 65)
        print("Max superclasses origin depth was reached.\n")
    else:
        for i in the_class.__bases__:
            if i not in cache:
                recsearch(i, cache)
