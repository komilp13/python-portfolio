'''
Rotating file handlers
'''
import logging.config
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs: app.log.1, app.log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# create log files based on time
handler = TimedRotatingFileHandler('app.log', when='s', interval=5, backupCount=5)

logger.addHandler(handler)

for i in range(100):
  logger.info(f'{i} - debug message')
  time.sleep(1)