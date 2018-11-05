import glob
import os
import shutil

misc_dir = "C:/Users/gurudk/Documents/behavioreconomics/readinggroup/"
tags = "behavioral economics "

tag_dir = misc_dir + tags.replace(" ", "_") + "/"
os.makedirs(tag_dir)

for name in glob.glob(misc_dir+"**/"+"*.pdf", recursive=True):
    shutil.copy(name, tag_dir + tags + "_" + os.path.basename(name))
    print(name + " has copied successfully!")

