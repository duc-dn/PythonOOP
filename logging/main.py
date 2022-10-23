import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M',
                    level=logging.INFO)
logging.info('Admin logged in')
logging.warning('Warning')