#
# @logger_.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from common.logger.singleton import SingletonMeta
import logging
import logging.config


class LoggerManager(metaclass = SingletonMeta):
    """Wrappes Logger Method"""
    logging.config.fileConfig('logging.conf')

    def debug(message):
        """Writes logger debug level"""
        logging.debug(message)
    
    def info(message):
        """Writes logger info level"""
        logging.info(message)

    def warning(message):
        """Writes logger warning level"""
        logging.warning(message)

    def error(message):
        """Writes logger error level"""
        logging.error(message)

    def critical(message):
        """Writes logger critical level"""
        logging.critical(message)

    def enter_method(method_name):
        """Writes logger to enter a method"""
        logging.debug('Enter Method >' + str(method_name))

    def exit_method(method_name):
        """Writes logger to exit a method"""
        logging.debug('Exit Method >' + str(method_name))
