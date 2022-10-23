import logging

name = 'John'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.error('%s raised an error', name)