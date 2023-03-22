import abc
from src.com.jalasoft.compiler.model.parameter import Parameter


class Command(abc.ABC):

    @abc.abstractmethod
    def build(self, parameter: Parameter) -> str:
        """ build method should be implemented. """
