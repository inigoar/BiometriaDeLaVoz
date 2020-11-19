import ntpath
import os

import numpy
from keras import backend as K
from keras import models as m
from keras.preprocessing import image

import spectrumExtractor


def analyze(file):
    print('Loading latest model...')

    img_width, img_height = 160, 120
    sentence_path = 'Model/Sentence/'
    speaker_path = 'Model/Speaker/'
    dataset_path='Dataset/Validate/'

    files = [f.path for f in os.scandir(sentence_path) if (f.path.endswith('.h5') or f.path.endswith('.hdf5'))]
    num_files_sentence = len(files)

    files = [f.path for f in os.scandir(speaker_path) if (f.path.endswith('.h5') or f.path.endswith('.hdf5'))]
    num_files_speaker = len(files)

    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    model_sentence_name = [sentence_path, 'model_sentence_', str(num_files_sentence - 1), '.hdf5']
    model_speaker_name = [speaker_path, 'model_speaker_', str(num_files_speaker - 1), '.h5']

    model_sentence = m.load_model("".join(model_sentence_name), custom_objects=None, compile=True)
    model_speaker = m.load_model("".join(model_speaker_name), custom_objects=None, compile=True)

    print('Opening file ' + file + 'for analysis...')

    temp_file = sentence_path + 'temp.png'
    spectrumExtractor.extract(file, temp_file)
    spectrogram = image.load_img(temp_file, target_size=(img_width, img_height))
    spectrogram = image.img_to_array(spectrogram)
    spectrogram = numpy.expand_dims(spectrogram, axis=0)

    print('Running sentence prediction...\n')

    result_sentence = model_sentence.predict(spectrogram)

    arrayAux = numpy.array(result_sentence).tolist() # convertimos el numpy en un array, por cosas curiosas el numpy trae doble [[]], aqui lo dividimos en diferentes numeros

    arrayNum = max(arrayAux) # aquí nos quedamos con el array con un solo []
    maxValue = max(arrayNum) # cogemos el maximo valor del array

    sentence_prediction = arrayNum.index(maxValue) + 1 # vemos en que posicion se encuentra el valor maximo
    sentence_confidence = round(maxValue*100,4)

    print('Running speaker prediction...\n')

    result_speaker = model_speaker.predict(spectrogram)

    arrayAux = numpy.array(
        result_speaker).tolist()  # convertimos el numpy en un array, por cosas curiosas el numpy trae doble [[]], aqui lo dividimos en diferentes numeros

    arrayNum = max(arrayAux)  # aquí nos quedamos con el array con un solo []
    maxValue = max(arrayNum)  # cogemos el maximo valor del array

    speaker_prediction = arrayNum.index(maxValue)  # vemos en que posicion se encuentra el valor maximo
    speaker_confidence = round(maxValue * 100,4)

    speaker_check = [f.path for f in os.scandir(dataset_path) if f.is_dir()]
    speaker_name = ntpath.basename(speaker_check[speaker_prediction])

    output = ['Sentence: ', str(sentence_prediction), '. Confidence: ', str(sentence_confidence), '%.\nSpeaker: ', speaker_name,'. Confidence: ', str(speaker_confidence), '%.']
    print("".join(output))

    os.remove(temp_file)


