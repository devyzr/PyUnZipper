from zipfile import ZipFile

# All directories:
zip_ref = ZipFile("File.zip")
for f in zip_ref.namelist():
    zinfo = zip_ref.getinfo(f)
    if(zinfo.is_dir()):
        print(f)

# Only root directories:
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
