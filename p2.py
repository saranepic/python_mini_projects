import sys
import os
from PIL import Image
r_folder = sys.argv[1]
o_folder = sys.argv[2]
if not os.path.exists(o_folder):
    os.makedirs(o_folder)
for i in os.listdir(r_folder):
    pic = Image.open(f'{r_folder}{i}')
    pic = pic.convert('L')
    pic.save(f'{o_folder}{i}')
