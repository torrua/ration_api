# pylint: disable=C0103
import logging

detailed_format = "%(filename)s [LINE:%(lineno)03d] [%(asctime)s] %(levelname)-s %(funcName)s() %(message)s"
logging.basicConfig(
    format=detailed_format, level=logging.DEBUG, datefmt="%y-%m-%d %H:%M:%S"
)

log = logging.getLogger(__name__)
