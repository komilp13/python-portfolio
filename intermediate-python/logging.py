'''
Logging:
- logging docs: https://docs.python.org/3/library/logging.html#logging.basicConfig
- dictionary config docs: https://docs.python.org/3/library/logging.html#logging.config.dictConfig
- JSON log formatter: https://github.com/madzak/python-json-logger
'''

import logging
import logging.config
from logging.handlers import RotatingFileHandler
import traceback

# Log levels - 5 log levels
#   by default anything above warning are printed
logging.basicConfig(
  level = logging.DEBUG,
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  datefmt = '%m/%d/%Y %I:%M:%S %p',
)

logging.debug('debug message')        #
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


'''
# Create custom logger
- the following will create a new logger in a module using the module name
- by default, all log msgs will get propogated to the base logger (root). To stop this behavior,
    the 'propagate' flag must be set to False.
'''
logger = logging.getLogger(__name__)
# logger.propagate = False
logger.info('hello from new logger')



'''
Log Handlers: responsible for dispatching logs to a specific destination
'''
logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('test.log')

# set level & format for each logger
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# invoke the logging
logger.warning('this is a warning message')
logger.error('this is a error message')



'''
Using a config file
'''
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('debug message')



'''
Using a dict config file
'''
# logging.config.dictConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('debug message')



'''
Capturing stack traces
'''
try:
  a = [1, 2, 3]
  val = a[4]
except IndexError as e:
  logger.error(e, exc_info=True)


'''
Capturing stack traces with generic exception
'''
try:
  a = [1, 2, 3]
  val = a[4]
except IndexError as e:
  logger.error("error is %s", traceback.format_exc())



