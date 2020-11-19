import keras.callbacks as kc
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import os

model_path = 'Model/'
sentence_path = model_path + 'Speaker/'
checkpoint_path = sentence_path + 'Checkpoints/'

if not os.path.exists(model_path):
    os.makedirs(model_path)
if not os.path.exists(sentence_path):
    os.makedirs(sentence_path)
if not os.path.exists(checkpoint_path):
    os.makedirs(checkpoint_path)

files = [f.path for f in os.scandir(sentence_path) if f.path.endswith('.h5')]
num_files = len(files)

model_name = [sentence_path, 'model_speaker_', str(num_files), '.h5']

train_data_dir = 'Dataset/Train'
validation_data_dir = 'Dataset/Validate'

img_width, img_height = 160, 120
nb_train_samples = 36486
nb_validation_samples = 8789
epochs = 10
batch_size = 128

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (7, 7), input_shape=input_shape, strides=(2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

model.add(Conv2D(32, (4, 4), strides=(2, 2)))
model.add(Activation('relu'))

model.add(Conv2D(64, (2, 2)))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('sigmoid'))
model.add(Dropout(0.2))

model.add(Dense(50, input_dim=2))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1. / 255)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size=(img_width, img_height),
                                                    batch_size=batch_size)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size)

filepath = checkpoint_path + "model_" + str(num_files) + "-{epoch:02d}-{val_accuracy:.2f}.hdf5"

checkpoint_callback = kc.ModelCheckpoint(
    filepath, monitor='val_accuracy', verbose=1,
    save_best_only=False, save_weights_only=False)

callback_list = [checkpoint_callback]

model.fit(train_generator,
          steps_per_epoch=nb_train_samples // batch_size,
          epochs=epochs, validation_data=validation_generator,
          validation_steps=nb_validation_samples // batch_size,
          validation_freq=1,
          initial_epoch=0,
          callbacks=callback_list
          )

model.save("".join(model_name))
