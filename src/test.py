import logging
import requests
import sys
import time

from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions


log_filename = "/var/log/piframe.log"

logfile_handler = logging.FileHandler(filename=log_filename)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stderr_handler = logging.StreamHandler(stream=sys.stderr)

handlers = [logfile_handler, stdout_handler]

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger()


# TODO: Put into a config file.
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = "adafruit-hat"


def pull_image():
    """
    Write an image to /tmp/demo_image from picsum.
    """
    with open("/tmp/demo_image", "wb") as fh:
        fh.write(requests.get("https://picsum.photos/64").content)


def main():
    matrix = RGBMatrix(options=options)

    while True:
        logger.info("Running main method...")

        image_file = "/tmp/demo_image"
        pull_image()
        image = Image.open(image_file)

        # Make image fit our screen.
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
        matrix.SetImage(image.convert("RGB"))

        time.sleep(5)

if __name__ == "__main__":
    main()
