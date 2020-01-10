def find_langest_file(base_dir, regexp=r'*'):
    import os
    import glob

    if not os.path.exists(base_dir):
        return None

    find_max = {'name': None, 'abspath': None, 'size': 0}

    for (dirname, subdirs, fileshere) in os.walk(base_dir):
        for file in glob.glob1(dirname, regexp):
            try:
                temporal = os.stat(os.path.join(dirname, file)).st_size
            except (FileNotFoundError, PermissionError):
                continue
            else:
                if temporal > find_max['size']:
                    find_max = {
                        'name': file,
                        'abspath': os.path.join(dirname, file),
                        'size': os.stat(os.path.join(dirname, file)).st_size
                    }
                    print('Current maximum: ', find_max)

    return find_max


if __name__ == "__main__":
    base_dir = input('Enter base directory:\n')
    test_regexp = input('Regexp\n') or r'*.py'
    max_file = find_langest_file(base_dir, test_regexp)

    if max_file:
        print('MAX SIZE FILE: ')
        for i in max_file.keys():
            print(f'{i} -> {max_file[i]}')
    else:
        print('path does not exist')
