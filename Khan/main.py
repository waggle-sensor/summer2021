from random_forest_model import create_random_forest
from GuassianMixtureModel import createGaussianMixtureModel

MODEL_TYPE = "random_forest"  # set to 'gaussian_mixture_model' if you wish to run the gaussian mixture model

def main():
    if (MODEL_TYPE == 'random_forest'):
        create_random_forest()
    elif (MODEL_TYPE == 'gaussian_mixture_model'):
        createGaussianMixtureModel()

if __name__ == '__main__':
    main()
