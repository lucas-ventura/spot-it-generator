import os

import cv2
import numpy as np

from ..cards import create_cards


def generate_numbered_image(number, path, height=256, width=256):
    """Generates the images with numbers to be used as placeholder images.

    :param number: number to be drawn in the image
    :param path: path where to save the image
    :param height: height of the image in pixels
    :param width: width of the image in pixels
    """

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 4
    thickness = 4
    color = (0, 0, 0, 255)
    text_size = cv2.getTextSize(str(number), font, font_scale, thickness)
    text_width = text_size[0][0]
    text_height = text_size[0][1]
    x = int((width - text_width) / 2)
    y = int((height + text_height) / 2)

    image = np.zeros((height, width, 4), np.uint8)
    image = cv2.putText(
        image,
        str(number),
        (x, y),
        fontFace=font,
        fontScale=font_scale,
        color=color,
        thickness=thickness,
    )
    cv2.imwrite(path, image)


def generate_images(path, order, n_found_images=0):
    """Generate images with numbers.

    :param path: path where to store the images
    :type path: str
    :param order: order of the game
    :type order: int
    """

    _, num_pictures = create_cards(order)

    if n_found_images > num_pictures:
        raise ValueError(
            f"Number of images found is greater than the number of images to be generated: {n_found_images} > {num_pictures}"
        )
    if n_found_images == num_pictures:
        return

    for i in range(n_found_images + 1, num_pictures + 1):
        filename = str(i).zfill(len(str(num_pictures + 1))) + ".png"
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            generate_numbered_image(i, filepath)
