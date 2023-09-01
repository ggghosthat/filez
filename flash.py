import shutil, os
from concurrent.futures import ThreadPoolExecutor

source = input('please, enter your source path: ')
dest = input('please entere your destination (USB drive) path: ')


def copy_to_usb(dest, root, file):
    print(f'---{root}/{file}')

    root_dir = os.path.dirname(root)
    base_root = os.path.basename(root_dir)

    dest_base = os.path.join(dest, base_root)
    if not os.path.exists(dest_base):
        os.mkdir(dest_base)

    shutil.copy(os.path.join(root, file), os.path.join(dest, dest_base, file))

for root, dirs, files in os.walk(source):
    with ThreadPoolExecutor(5) as executor:
        x = [executor.submit(copy_to_usb(dest, root, file)) for file in files]
        