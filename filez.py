import os, zipfile

cache = list()
path = input('please, enter your ZIP path: ')
tmp = input('please, enter your UNZIP path: ')

def find_zip(cache, path):
    for root, dirs, files in os.walk(path):
        for zfile in files:
            if zfile.endswith('.zip'):
                cache.append(root + zfile)

find_zip(cache, path)


def unzip(cache, tmp):
    for zipy in cache:
        print()
        print(f'Current zip file: {zipy}')
        print(f'Size of the current zip file: {os.path.getsize(zipy)}')
        with zipfile.ZipFile(zipy, 'r') as zipster:
            zipster.extractall(tmp)
        print('Completed!')
        print('='*50)

unzip(cache, tmp)
