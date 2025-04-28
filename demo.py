from ElectricMeter.logger import logging
from ElectricMeter.exception import ElectricMeterException
# logging.info("Welcome to our custom log")
import sys


try:
    a = 2/0
except Exception as e:
    raise ElectricMeterException(e,sys)