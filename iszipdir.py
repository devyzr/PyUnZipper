'''
This script will check if an item in a zip file is a folder or not and
print them.

More of a proof-of-concept than anything useful.
'''

from zipfile import ZipFile

# Print all directories in a zip file.
zip_ref = ZipFile("File.zip")
for f in zip_ref.namelist():
    zinfo = zip_ref.getinfo(f)
    if(zinfo.is_dir()):
        print(f)

# Only print root directories of a zip file.
root_dirs = []
zip_ref = ZipFile("File.zip")
for f in zip_ref.namelist():
    zinfo = zip_ref.getinfo(f)
    if zinfo.is_dir():
        # This is will work in any OS because the zip format
        # specifies a forward slash.
        r_dir = f.split('/')
        r_dir = r_dir[0]
        if r_dir not in root_dirs:
            root_dirs.append(r_dir)
for d in root_dirs:
    print('Rood dirs: %s' % d)
