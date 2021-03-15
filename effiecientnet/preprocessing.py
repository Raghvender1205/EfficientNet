import numpy as np
from skimage.transform import resize

MAP_INTERPOLATION_TO_ORDER = {
    'nearest' : 0,
    'bilinear': 1, 
    'biquadratic': 2,
    'bicubic': 3,
}

def center_crop_and_resize(resize, image_size, crop_padding=32, interpolation='bicubic'):
    assert image.ndim in {2, 3}
    assert interpolation in MAP_INTERPOLATION_TO_ORDER.keys()

    h, w = image.shape[:2]

    padded_center_crop_size = int()