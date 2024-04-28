import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from sklearn.neighbors import KNeighborsClassifier
import pickle

from preprocess import PrepareDataset

x_train, y_train = PrepareDataset("../data/PetImages/Cat/", "../data/PetImages/Dog/").preprocess_train()
x_test, y_test = PrepareDataset("../data/PetImages/Cat/", "../data/PetImages/Dog/").preprocess_test()

x_train = x_train.reshape(x_train.shape[0], -1)
x_test = x_test.reshape(x_test.shape[0], -1)
print("DATA PREPARED")

neigh = KNeighborsClassifier(n_jobs=-1)
neigh.fit(x_train,y_train)
print("MODEL LOADED")

print("START TRAINING")
score_train = neigh.score(x_train, y_train)
print("Training score: {:.2f}%".format(score_train*100))

score_test = neigh.score(x_test, y_test)
print("Test score: {:.2f}%".format(score_test*100))

with open('knnpickle_file', 'wb') as knnPickle:
    pickle.dump(neigh, knnPickle)
    print("MODEL SAVED")