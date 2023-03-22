from pathlib import Path
from src.com.jalasoft.compiler.model.commands.command import Command
from src.com.jalasoft.compiler.common.exceptions.command_exception import CommandException
from src.com.jalasoft.compiler.model.parameter import Parameter

JAVA_CP_PARAM = ' -cp '
JAVA_AND = ' && '
SPACE = ' '


class JavaCommand(Command):

    def build(self, parameter: Parameter) -> str:
        parameter.validate()
        try:
            java_compiler: str = parameter.get_binary_path() + 'javac '
            java_execute: str = parameter.get_binary_path() + 'java '
            file_name: str = Path(parameter.get_file_path()).stem
            cmd: str = java_compiler + parameter.get_file_path() + JAVA_AND + java_execute + JAVA_CP_PARAM +\
                parameter.get_folder_path() + SPACE + file_name
            return cmd
        except Exception as error:
            raise CommandException("java command error")
