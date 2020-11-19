import os
import shutil
import ntpath

print('Extracting Data for Speaker Trainer...')

sourcePath = "Dataset/"
sourcePathValidate = sourcePath + "Validate/"
sourcePathTrain = sourcePath + "Train/"

destinationPath = "Dataset/"

if os.path.exists(sourcePathValidate):
    speakersValidate = [f.path for f in os.scandir(sourcePathValidate) if f.is_dir()]
if os.path.exists(sourcePathValidate):
    speakersTrainers = [f.path for f in os.scandir(sourcePathTrain) if f.is_dir()]

speakers = [f.path for f in os.scandir(sourcePath) if f.is_dir()]

if sourcePathValidate in speakers:
    speakers.remove(sourcePathValidate)

if sourcePathTrain in speakers:
    speakers.remove(sourcePathTrain)

for z in range(len(speakers)):

    speakerS = ntpath.basename(speakers[z])
    extractSpkData = sourcePath + speakerS + "/"

    for filename in os.listdir(extractSpkData):

      if filename.endswith(".png"):

        shutil.move(extractSpkData + filename, destinationPath, )

    try:
        os.rmdir(extractSpkData)
    except OSError as e:
        print("Error: %s : %s" % (extractSpkData, e.strerror))

for x in range(len(speakersValidate)):

    speakerV = ntpath.basename(speakersValidate[x])
    extractValidatePath = sourcePathValidate + speakerV + "/"

    for filename in os.listdir(extractValidatePath):

      if filename.endswith(".png"):

        shutil.move(extractValidatePath + filename, destinationPath, )

    try:
        os.rmdir(extractValidatePath)
    except OSError as e:
        print("Error: %s : %s" % (extractValidatePath, e.strerror))

try:
    os.rmdir(sourcePathValidate)
except OSError as e:
    print("Error: %s : %s" % (sourcePathValidate, e.strerror))

for y in range(len(speakersTrainers)):

    speakerT = ntpath.basename(speakersTrainers[y])
    extractTrainPath = sourcePathTrain + speakerT + "/"

    for filename in os.listdir(extractTrainPath):

      if filename.endswith(".png"):

        shutil.move(extractTrainPath + filename, destinationPath, )

    try:
        os.rmdir(extractTrainPath)
    except OSError as e:
        print("Error: %s : %s" % (extractTrainPath, e.strerror))

try:
    os.rmdir(sourcePathTrain)
except OSError as e:
    print("Error: %s : %s" % (sourcePathTrain, e.strerror))