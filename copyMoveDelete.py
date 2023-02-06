import shutil
import os

src = 'D:\Taimoor'
dst = 'G:\dest/all'

# copy all files and folders

shutil.copytree(src=src, dst=dst)

# Copy File + folder with permission bits

shutil.copy(src=src + "/1.png", dst = dst)

# copy file only data
shutil.copyfile(src=src + '/1.png', dst=dst+ '/1.png')

#  move file
shutil.move(src=src + "/1.png", dst=dst)

# remove folder
shutil.rmtree(src)

#  remove file
os.remove(src+ '/1.png')



