from pathlib import Path

from spotit import create_sheets
from spotit.utilities import generate_images


def get_images_path(path: Path) -> list:
    """Get all the images in the directory.

    :param path: path where the images are stored
    :type path: str
    :return: list of images
    :rtype: list
    """
    images_png = list(path.glob("*.png")) + list(path.glob("*.PNG"))
    images_jpg = list(path.glob("*.jpg")) + list(path.glob("*.JPG"))
    images_jpeg = list(path.glob("*.jpeg")) + list(path.glob("*.JPEG"))
    images = images_png + images_jpg + images_jpeg
    return sorted(images)


def main(images_path: Path, filename: str, order: int) -> None:
    # create a directory for generated images
    if not images_path.exists():
        images_path.mkdir()

    n_found_images = len(get_images_path(images_path))
    generate_images(
        images_path, order=order, n_found_images=n_found_images
    )  # generate images with numbers
    # get all the images in the directory
    images = get_images_path(images_path)
    create_sheets(filename, order, images)  # create the PDF with cards


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--filename", default="cards.pdf", help="")
    parser.add_argument("-o", "--order", default=7, type=int, help="")
    parser.add_argument("-p", "--path", default="./images", help="")
    args = parser.parse_args()
    main(Path(args.path), args.filename, args.order)
