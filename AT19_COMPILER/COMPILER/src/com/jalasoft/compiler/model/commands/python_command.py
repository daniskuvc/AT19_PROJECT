from src.com.jalasoft.compiler.model.commands.command import Command
from src.com.jalasoft.compiler.model.parameter import Parameter


class PythonCommand(Command):
    def build(self, parameter: Parameter) -> str:
        python_compiler: str = parameter.get_binary_path() + 'python '
        return python_compiler + parameter.get_file_path()
