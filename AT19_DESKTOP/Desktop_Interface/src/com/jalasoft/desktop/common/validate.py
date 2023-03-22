#
# @validate.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from Desktop_Interface.src.com.jalasoft.desktop.common.exception.input_exception import InvalidInputException
from pathlib import Path
import os


class ValidateInput:
    """validate the text that is introduced"""
    def __init__(self):
        """Defines the constructor"""
        self.extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]

    def validate_video_path(self, videopath):
        """Validates the video path value"""
        if videopath == '':
            raise InvalidInputException("Complete the boxes")
        if not Path(videopath).is_file():
            raise InvalidInputException("Invalid Video Path")
        _, file_extension = os.path.splitext(videopath)
        if file_extension not in self.extensions:
            raise InvalidInputException("Invalid Video Path extension")

    def validate_word(self, word):
        """Validates the word value"""
        if word == '':
            raise InvalidInputException("Complete the boxes")
        if word.isdigit():
            raise InvalidInputException("Invalid object to search")

    def validate_percentage(self, percentage):
        """Validates the percentage value"""
        if percentage == '':
            raise InvalidInputException("Complete the boxes")
        if not percentage.isdigit():
            raise InvalidInputException("Invalid Percentage")
        if float(percentage) < 1:
            raise InvalidInputException("Invalid Percentage")
        if float(percentage) > 100:
            raise InvalidInputException("Invalid Percentage, please enter a number less than 100")