import os
import shutil


def organize():

    print('Moving files...')

    source_path = "Dataset/"
    destination_validate = source_path + "Validate/"
    destination_train = source_path + "Train/"

    if not os.path.exists(destination_validate):
        os.makedirs(destination_validate)
    if not os.path.exists(destination_train):
        os.makedirs(destination_train)

    if not os.path.exists(destination_validate + 'S1'):
        os.makedirs(destination_validate + 'S1')

    if not os.path.exists(destination_validate + 'S2'):
        os.makedirs(destination_validate + 'S2')

    if not os.path.exists(destination_validate + 'S3'):
        os.makedirs(destination_validate + 'S3')

    if not os.path.exists(destination_validate + 'S4'):
        os.makedirs(destination_validate + 'S4')

    if not os.path.exists(destination_validate + 'S5'):
        os.makedirs(destination_validate + 'S5')

    if not os.path.exists(destination_train + 'S1'):
        os.makedirs(destination_train + 'S1')

    if not os.path.exists(destination_train + 'S2'):
        os.makedirs(destination_train + 'S2')

    if not os.path.exists(destination_train + 'S3'):
        os.makedirs(destination_train + 'S3')

    if not os.path.exists(destination_train + 'S4'):
        os.makedirs(destination_train + 'S4')

    if not os.path.exists(destination_train + 'S5'):
        os.makedirs(destination_train + 'S5')

    for filename in os.listdir(source_path):
        if filename.endswith(".png"):
            if int(filename[4:10]) > 749:
                dest = destination_validate
            else:
                dest = destination_train

            sentence = filename[11:13]
            if sentence == 'S1':
                dest = dest + "S1/"
            elif sentence == 'S2':
                dest = dest + "S2/"
            elif sentence == 'S3':
                dest = dest + "S3/"
            elif sentence == 'S4':
                dest = dest + "S4/"
            elif sentence == 'S5':
                dest = dest + "S5/"

            shutil.move(source_path + filename, dest, )


