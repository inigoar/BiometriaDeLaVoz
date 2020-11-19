import math
import os
import shutil
import random

print('Moving files...')

sourcePath = "Dataset/"
destinationValidate = sourcePath + "Validate/"
destinationTrain = sourcePath + "Train/"

if not os.path.exists(destinationValidate):
    os.makedirs(destinationValidate)
if not os.path.exists(destinationTrain):
    os.makedirs(destinationTrain)

for filename in os.listdir(sourcePath):
    if filename.endswith(".png"):

        speaker = filename[4:10]
        dest = destinationTrain + "spk_" + speaker + "/"
        if not os.path.exists(dest):
            os.makedirs(dest)

        shutil.move(sourcePath + filename, dest, )

for folderName in os.listdir(destinationTrain):
    files = [f.path for f in os.scandir(destinationTrain + folderName) if f.is_file()]
    num_files = len(files)
    val_num = max(math.ceil(0.2 * num_files), 1)
    to_move = []
    for x in range(0, val_num):
        repeated = True
        while repeated:
            rnd = random.randint(0, num_files - (x + 1))
            file = files[rnd]
            if not file in to_move:
                to_move += [file]
                repeated = False

    for file in to_move:
        speaker = file[29:35]
        dest = destinationValidate + "spk_" + speaker + "/"
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(file, dest,)
