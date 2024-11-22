import logging
import qconqc._version


__version__ = qconqc._version.__version__



logger = logging.getLogger(__name__)
logger.info(f'Imported qconqcversion: {__version__}')
