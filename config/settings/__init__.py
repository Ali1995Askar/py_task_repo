import logging
from .base import env

logger = logging.getLogger(__name__)

if env.str('WORKING_SETTINGS') == 'DEV':
    from .local import *

elif env('WORKING_SETTINGS') == 'TEST':
    from .testing import *


else:
    raise ImportError("The settings specified are not available, check WORKING_SETTINGS is set correctly")

logger.info(f"Starting server with {env('WORKING_SETTINGS')} settings ..")
