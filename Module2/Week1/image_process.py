import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('dog.jpeg')


def convert_to_grayscale_lightness(image):
    # Lấy các kênh màu R, G, B
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    # Tính giá trị xám bằng phương pháp Lightness
    gray_image = (np.maximum(np.maximum(R, G), B) +
                  np.minimum(np.minimum(R, G), B)) / 2.0

    return gray_image


def convert_to_grayscale_average(image):
    # Tính giá trị xám bằng phương pháp Average
    gray_image = np.mean(image[:, :, :3], axis=2)
    return gray_image


def convert_to_grayscale_luminosity(image):
    # Lấy các kênh màu R, G, B
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    # Tính giá trị xám bằng phương pháp Luminosity
    gray_image = 0.21 * R + 0.72 * G + 0.07 * B

    return gray_image


# Chuyển đổi ảnh
gray_img_01 = convert_to_grayscale_lightness(img)
gray_img_02 = convert_to_grayscale_average(img)
gray_img_03 = convert_to_grayscale_luminosity(img)
print(gray_img_03[0, 0])
