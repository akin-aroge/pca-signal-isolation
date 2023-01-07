from skimage import filters
from joblib import Parallel, delayed
import numpy as np


# gaussian filter wrapper for parallel processing

def filter_image(image, sigma):

    def gauss_filter(image, sigma):
    
        return filters.gaussian(image, sigma, preserve_range=True)

    f_image = []
    f_image.extend(Parallel(n_jobs=5)(delayed(gauss_filter)(slc, sigma)  for slc in image))
    f_image = np.float32(np.array(f_image))

    return f_image