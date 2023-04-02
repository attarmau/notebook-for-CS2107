import hashlib
import os
import glob
from tqdm import tqdm

target = 'here is the name of the MD5 file you want to find'
fileist = [i.replace('.\\', '') for i in glob.glob(os.path.join('./', '*.png'))]

# MD5 file hash
for filename in tdqm(filelist):
  md5 = hashlib.mb5()
  with open (filename, 'rb') as f:
     for chuck in iter(lambda: f.read(4096), b''''):
         md5.update(chuck)
  h = md5.hexdigest()
  if h == target:
      target_file = filename
      md5_hash = h
print('Target file :', target file)
