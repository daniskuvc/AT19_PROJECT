import abc


class ValidatorStrategy(abc.ABC):

    @abc.abstractmethod
    def validate(self):
        """ Validate method should be implemented """
