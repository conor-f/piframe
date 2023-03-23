import logging
import os
import requests
import sys
import time

from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from spotibar.client import SpotibarClient


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


options = RGBMatrixOptions()
options.rows = os.environ.get("MATRIX_ROWS", 64)
options.cols = os.environ.get("MATRIX_COLS", 64)
options.chain_length = os.environ.get("MATRIX_CHAIN_LENGTH", 1)
options.parallel = os.environ.get("MATRIX_PARALLEL", 1)
options.hardware_mapping = os.environ.get(
    "MATRIX_HARDWARE_MAPPING",
    "adafruit-hat"
)
options.pwm_bits = os.environ.get("MATRIX_PWM_BITS", 11)
options.pwm_lsb_nanoseconds = os.environ.get("MATRIX_PWM_LSB_NANOSECONDS", 130)
options.brightness = os.environ.get("MATRIX_BRIGHTNESS", 20)

spotibar_client = SpotibarClient(
    config_file=os.environ.get("SPOTIBAR_CONFIG_FILE"),
    auth_cache_path=os.environ.get("SPOTIBAR_AUTH_CACHE_FILE"),
)


def pull_image(url="https://picsum.photos/64"):
    """
    Write an image to /tmp/album_image from URL.
    """
    with open("/tmp/album_image", "wb") as fh:
        fh.write(requests.get(url).content)


def main():
    matrix = RGBMatrix(options=options)

    while True:
        logger.info("Running main method...")

        if not spotibar_client.is_live():
            matrix.Clear()
        else:
            album_art_url = spotibar_client.get_current_album_image_url()
            pull_image(album_art_url)

            image_file = "/tmp/album_image"
            image = Image.open(image_file)

            # Make image fit our screen.
            image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            matrix.SetImage(image.convert("RGB"))

        time.sleep(10)

if __name__ == "__main__":
    main()
