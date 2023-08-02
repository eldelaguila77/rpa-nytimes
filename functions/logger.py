"""
Loggin tracker
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

formatter = logging.Formatter(
    r"%(asctime)s - %(levelname)-7s -> %(filename)s:%(lineno)s - %(funcName)s() - %(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

if __name__ == "__main__":
    logger.info("Info logging test")
    logger.warning("Warning logging test")
    logger.error("Error logging test")
    try:
        raise RuntimeError("Exception logging test")
    except RuntimeError:
        logger.exception("Exception logging test")
