import hashlib
import os
import glob
from tqdm import tqdm

target = 'here is the name of the MD5 file you want to find'

fileist = [i.replace('.\\', '') for i in glob.glob(os.path.join('./', '*.png'))]
