import logging

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
)
# creating a logger
logger = logging.getLogger(__name__)

logger.debug("I'm debugging.")
logger.info("This is some useful info.")
logger.warning("This is a warning.")
logger.error("Houston... we have a problem")
logger.critical("This is the end of the line")
