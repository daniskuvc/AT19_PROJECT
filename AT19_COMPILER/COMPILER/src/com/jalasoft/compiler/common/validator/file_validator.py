import os

from src.com.jalasoft.compiler.common.exceptions.parameter_invalid_exception import ParameterInvalidException
from src.com.jalasoft.compiler.common.validator.validator_strategy import ValidatorStrategy


class FileValidator(ValidatorStrategy):
    def __init__(self, data, is_file):
        self.data = data
        self.is_file = is_file

    def validate(self):
        if self.is_file:
            is_file = os.path.isfile(self.data)
            if not is_file:
                raise ParameterInvalidException('Invalid file path')
        else:
            is_folder = os.path.isdir(self.data)
            if not is_folder:
                raise ParameterInvalidException('Invalid folder path')