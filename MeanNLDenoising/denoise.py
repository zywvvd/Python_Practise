import cv2
from mtutils import to_gray_image
from mtutils import cv_rgb_imread
from mtutils import PIS


if __name__ == '__main__':
    noise_image_path = 'assets/noise.jpg'
    noise_img = cv_rgb_imread(noise_image_path)

    # h -> 6
    denoised_img = cv2.fastNlMeansDenoisingColored(noise_img, None, 6, 10, 7, 21)
    PIS([noise_img, 'with noise'], [denoised_img, 'denoised'])
    
    pass