import pickle
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray


neigh = pickle.load(open('knnpickle_file', 'rb'))

def predict_image(file_path):
    image = io.imread(file_path)
    if len(image.shape) == 4:
        image = image.squeeze(0)
    image = rgb2gray(resize(image, (200,200)))
    image = image.reshape(1, -1)

    res = neigh.predict(image)[0]
    if res == 0:
        print("Cat")
    else:
        print("Dog")

if __name__=='__main__':
    predict_image("../data/PetImages/cat/3004.jpg")