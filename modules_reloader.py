import types
from imp import reload


def reloader(new_module, visited):
    visited.add(new_module)
    print(f"Reloading {new_module.__name__} in {new_module.__file__}")
    reload(new_module)
    for i in new_module.__dict__.values():
        if isinstance(i, types.ModuleType) and i not in visited:
            reloader(i, visited)


def tester(module, infinite=False):

    visited = set()

    import importlib
    new_module = importlib.import_module(module)

    if infinite:
        print("-" * 70)
        print("Reloading modules every 10 seconds.")
        print("-" * 70)

        import time

        while True:
            reloader(new_module, visited)
            print(f"Reloaded {len(visited)}.")
            print("-" * 70)
            visited.clear()
            time.sleep(10)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        sys.exit("Usage: [name.py] [argument]")

    tester(sys.argv[-1], True)
