import os
import glob
import ntpath
import spectrumExtractor as se


def generate():
    count = 0
    path = 'Data/'
    output_path = "Dataset/"

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    for x in range(len(subfolders)):

        subfolders_speakers = [f.name for f in os.scandir(subfolders[x]) if f.is_dir()]
        sentence = ntpath.basename(subfolders[x])

        for y in range(len(subfolders_speakers)):

            locutor = subfolders_speakers[y]
            ruta = locutor + "/*"
            recording = 0

            for filename in glob.glob(os.path.join(subfolders[x], ruta)):
                with open(os.path.join(os.getcwd(), filename), 'r') as f:

                    output_name = locutor + "_" + sentence + "_" + str(recording)
                    recording += 1
                    count += 1
                    percentage = (count / 45275) * 100
                    update = ["Extracting spectrogram ", str(count), " of 45275. [", str(round(percentage, 2)), "% completed.]"]
                    print("".join(update))

                    se.extract(filename, output_path + output_name)
