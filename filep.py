import os, pathlib

path = input('please, enter your path: ')
dest = input('please enter your destination: ')
cache = set()

point_start = os.path.join(dest, 'point')


def entry_point(point_start):
    if not os.path.exists(point_start):
        os.mkdir(point_start)

entry_point(point_start)

def pass_files(path, point_start):
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = pathlib.Path(file).suffix
            branch = os.path.join(point_start, ext)
            if not os.path.exists(branch):
                os.mkdir(branch)

            os.rename(f'{root}/{file}', os.path.join(branch, file))

pass_files(path, point_start)