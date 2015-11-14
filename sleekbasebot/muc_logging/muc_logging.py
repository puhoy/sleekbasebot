__author__ = 'meatpuppet'

import logging
from logging.handlers import RotatingFileHandler
import os

formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log_folder = 'muc_logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

def log(msg):
    room = msg.get('from').bare
    logger = logging.getLogger(room)
    filehandler = RotatingFileHandler(os.path.join(log_folder, room + '.log'))
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.info('%s: %s' % (msg['mucnick'], msg['body']))
