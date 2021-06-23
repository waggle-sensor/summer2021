
matplotlib.use('agg')
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import os
from datetime import datetime
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.optimizers import Adam
from keras.utils import np_utils, to_categorical
from keras.callbacks import ModelCheckpoint

def extract_features_mfcc(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T, axis=0)

    except Exception as e:
        print("Error encountered while parsing file: ", file)
        return None
    return mfccsscaled


# Set the path to the full UrbanSound dataset
fulldatasetpath = 'data/train_short_audio'
metadata = pd.read_csv('data/train_metadata.csv')
features = []

for index, row in metadata.iterrows():
    file_name = os.path.join(os.path.abspath(fulldatasetpath), 'fold' + str(row["fold"]) + '/',
                             str(row["file_name"]))
    class_label = row["primary_label"]
    data = extract_features_mfcc(file_name)
    features.append([data, class_label])

# Convert into a Panda dataframe 
featuresdf = pd.DataFrame(features, columns=['feature', 'class_label'])

# Convert features and corresponding classification labels into numpy arrays
# x_array = np.asarray(x_list)
X = np.asarray(featuresdf.feature.tolist())
y = np.asarray(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y))

# split the dataset 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.2, random_state=42)

num_labels = yy.shape[1]
filter_size = 2

# Construct model 
model = Sequential()

model.add(Dense(256, input_shape=(40,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_labels))
model.add(Activation('softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

num_epochs = 100
num_batch_size = 32

start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs, validation_data=(x_test, y_test), verbose=1)

duration = datetime.now() - start

print("Training completed in time: ", duration)

score = model.evaluate(x_train, y_train, verbose=0)
print('train accuracy: {}'.format(score))
# experiment.log_metric("train_acc", score)

score = model.evaluate(x_test, y_test, verbose=0)
print('test accuracy: {}'.format(score))
# experiment.log_metric("val_acc", score)
