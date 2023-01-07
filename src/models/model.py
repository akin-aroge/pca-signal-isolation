import numpy as np
from sklearn.utils import resample
from sklearn.decomposition import PCA

def get_component_error(features, n_samples=1000):
    

    mean_samples = [np.mean(resample(features), axis=0) for i in range(n_samples)]
    mean_std = np.std(mean_samples, axis=0)

    pca = get_model()
    comp_samples = [pca.fit(resample(features)).components_ for i in range(n_samples)]
    comp_std = np.std(comp_samples, axis=0)

    return mean_std, comp_std


def get_model():

    pca = PCA()

    return pca





