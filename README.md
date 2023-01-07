Isolating Low SNR Water Information in Radiograph Sequence Using Machine Learning

The analysis here tackles the problem of revealing very low contrast and short duration temporal information from a sequence of radiographic images while elucidating spatial characteristics.

## Project Description

### The problem

Water management is a critical problem impacting fuel cell efficiency and X-ray imaging has proved a useful investigative technique. However, existing 3D imaging methods do not reveal useful temporal variations. 

### The proposed Solution

The idea is to acquire relatively rapid radiographs and extracting water breakthrough information from the images, using an unsupervised machine learning approach. Due to the low signal-to-noise (SNR) ratio, the liquid water informmation was extraceted from  processed and transformed dataset using the decomposition capability of the PCA. The result is tranformed back to the image space for analysis and interpretation. Further details can be found in the [analysis notebook ](notebook/01-water-signal-isolation.ipynb)

### The dataset

The dataset consist of a temporal sequence of grayscale radiographs acquired at regular intervals of 4 seconds. This exists as a 3D .tiff file of about 1GB. The images in the dataset appear as a grayscale image

![raw_radiograph](./reports/images/raw_radiograph.PNG?raw=true)

### Modelling

**Data preprocessing**:  The raw grayscale dataset is first denoised using a 2D (not 3D because the samples are indepedent) gaussian filter with a suitable kernel size for each radiographic image. This gets rid of random noise associated with the optical instrument.

**Modelling**: To extract temporal liquid water information, the processed dataset if first transformed to a temporal data structure, such that each corresponding pixel across the image sequences form a profile vector. PCA is used to decomposed the signal into components that enable the separation of systematic noise and useful liquid water information. Statistical error analysis is also carried out.

### Sample Results

**Vignette Removal Using First Principal Component**

![Vignette-Removal](./reports/images/vignette-removal.PNG?raw=true)

**Dominant Water Profile Extraction**

![pc1-major-break](/reports/images/pc1-major-break.PNG?raw=true)



## Project Organization

-------------------------
```
.
├── data
│   ├── processed
│   └── raw
├── models
├── notebook
├── reports
│   └── images
├── results
└── src
    ├── data
    ├── models
    └── visualization
```

## Technologies

- Numpy
- Scikit-image
- Scipy
- Scikit-learn
- matplotlib
- etc.