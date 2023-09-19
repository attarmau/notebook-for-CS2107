import hashlib
import os
import glob
from tqdm import tqdm

target = 'here is the name of the MD5 file you want to find'
filelist = [i.replace('.\\', '') for i in glob.glob(os.path.join('./', '*.png'))]

# MD5 file hash
for filename in tqdm(filelist):
    md5 = hashlib.md5()  # Fix the typo: hashlib.mb5() should be hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
    h = md5.hexdigest()
    if h == target:
        target_file = filename
        md5_hash = h

print('Target file:', target_file)  # Fix the typo: target file should be target_file
print('The MD5 file hash:', md5_hash)
print('The target hash:', target)
