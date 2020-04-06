def inspect_object(instance, build_ins=False, docs=False, dir_redirect=None):
    """
        Custom inspect object tool.

        Arguments:
            'instance': any instance of any class
            'build_ins=False': show '__magic__'
            'docs': show '__doc__' value
    """
    import io
    import os
    import sys

    redirected = False
    if dir_redirect:
        if not os.path.exists(dir_redirect):
            print('Path does not exist.')
            return None

        redirected = True
        temp = sys.stdout
        buff = io.StringIO()
        sys.stdout = buff

    DIRS = dir(instance)

    separator = '-' * 111
    print(separator)
    print(f'INSTANCE: {instance}')
    print(separator)
    print(f'TYPE: {type(instance)}')
    print(separator)
    print(f'ALL DIR:\n{DIRS}')
    print(separator)

    DOC_INST = None
    if '__doc__' in DIRS:
        DIRS.pop(DIRS.index('__doc__'))
        DOC_INST = instance.__doc__

    if not build_ins:
        DIRS = list(filter(lambda x: not x.startswith('_'), DIRS))

    print('                  Attributes                  |                            Values                            ')
    print(separator)
    for attribute in DIRS:
        placeholder = " " * (46 - len(attribute))
        try:
            print(f'{attribute}{placeholder}| {getattr(instance, attribute)}')
        except AttributeError:
            pass
    print(separator)

    if docs:
        print('DOCS:')
        print(separator)
        print('INSTANCE DOCS')
        print(DOC_INST)
        print(separator)
        for attribute in DIRS:
            print(f'ATTRIBUTE "{attribute}"\n')
            try:
                print(f'{getattr(instance, attribute).__doc__}')
            except AttributeError:
                pass
            print(separator)

    if redirected:
        with open(dir_redirect, 'a') as file:
            file.write(buff.getvalue())

        sys.stdout = temp


def remove_pycache(pyc=False):
    import os
    import re
    import shutil

    base_dir = input('Enter basedir (leave empty for current):\n')

    if not base_dir:
        base_dir = os.getcwd()

    if not os.path.exists(base_dir):
        print('Path does not exist.')
        return None

    if pyc:
        pattern = r'(?:.*)\.pyc$'
        counter = 0
        for (dirname, subdirs, fileshere) in os.walk(base_dir):
            pyc_files = list(filter(lambda x: re.match(pattern, x), fileshere))
            counter += len(pyc_files)
            list(os.remove(os.path.join(dirname, file)) for file in pyc_files)
        print(f"Removed {counter} .pyc files.")
    else:
        counter = 0
        for (dirname, subdirs, fileshere) in os.walk(base_dir):
            if '__pycache__' in subdirs:
                current_directory = os.path.join(dirname, '__pycache__')
                shutil.rmtree(current_directory)
                counter += 1
                print('Removing', current_directory)
        print(f'Removed {counter} __pycache__.')


if __name__ == '__main__':
    import socket
    inspect_object(socket, docs=True)
