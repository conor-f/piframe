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


# TODO: Put into a config file.
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = "adafruit-hat"


spotibar_client = SpotibarClient(
    client_id=os.environ.get("SPOTIBAR_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIBAR_CLIENT_SECRET"),
    config_file=os.environ.get("SPOTIBAR_CONFIG_FILE"),
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
