import sys
import os
from PIL import Image
p_folder = sys.argv[1]
o_folder = sys.argv[2]
if not os.path.exists(o_folder):
    os.makedirs(o_folder)
for i in os.listdir(p_folder):
    pic = Image.open(f'{p_folder}{i}')
    clean = os.path.splitext(i)[0]
    pic.save(f'{o_folder}{clean}.png', 'png')
