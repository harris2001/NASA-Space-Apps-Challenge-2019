
import keras
import numpy as np
import matplotlib.pyplot as plt

keras.backend.backend()

fm = keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fm.load_data()

X_train.shape
X_test.shape

X_train[0]
y_train[0]

plt.matshow(X_train[0])
X_train = X_train/255
X_test = X_test/255

from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation

model = Sequential()
model.add(Flatten(input_shape=[28, 28]))
model.add(Dense(100, activation="relu"))
model.add(Dense(10, activation="softmax")
model.summary()

model.compile(loss="sparse_categorical_crossentropy", 
              optimizer="adam",
              metrics=["accuracy"])


model.fit(X_train, y_train)
model.evaluate(X_test, y_test)
plt.matshow(X_test[0])
yp = model.predict(X_test)
np.argmax(yp[0])
class_labels = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
class_labels[np.argmax(yp[0])]
