from src.com.jalasoft.compiler.common.exceptions.parameter_invalid_exception import ParameterInvalidException
from src.com.jalasoft.compiler.common.validator.validator_strategy import ValidatorStrategy


class EmptyOrNoneValidator(ValidatorStrategy):
    def __init__(self, field, data):
        self.field = field
        self.data = data

    def validate(self):
        if self.data is None or str(self.data).strip() == "":
            message = "The field: " + self.field + " is invalid"
            raise ParameterInvalidException(message)
