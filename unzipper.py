from zipfile import ZipFile
from os import listdir
from os import mkdir

directories = listdir()

for d in directories:
    # Check if zipfile
    d_ext = d.split('.')
    if 'zip' in d_ext[-1]:
        # Check what root dir name should be
        zip_name = d_ext[:-1]
        zip_name = '.'.join(zip_name)
        zip_ref = ZipFile(d)
        # Get root dir names
        root_dirs = []
        for f in zip_ref.namelist():
            zinfo = zip_ref.getinfo(f)
            if zinfo.is_dir():
                r_dir = f.split('/')
                r_dir = r_dir[0]
                if r_dir not in root_dirs:
                    root_dirs.append(r_dir)

        print('Extracting %s...' % d)
        # Unzip in new dir if more than one root dir
        if len(root_dirs) > 1 or root_dirs[0] != zip_name:
            mkdir(zip_name)
            zip_ref.extractall(zip_name)
        else:
            zip_ref.extractall()
