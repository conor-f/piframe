import logging
import sys
import time

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


def main():
    while True:
        logger.info("Running main method... (and testing caching!)")
        time.sleep(5)

if __name__ == "__main__":
    main()
