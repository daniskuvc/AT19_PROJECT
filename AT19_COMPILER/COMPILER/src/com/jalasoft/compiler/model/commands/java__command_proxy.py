from src.com.jalasoft.compiler.model.commands.command import Command
from src.com.jalasoft.compiler.common.exceptions.command_exception import CommandException
from src.com.jalasoft.compiler.model.commands.java_command import JavaCommand
from src.com.jalasoft.compiler.model.parameter import Parameter
from datetime import datetime


class JavaCommandProxy(Command):
    def __init__(self):
        self.java = JavaCommand()

    def build(self, parameter: Parameter) -> str:
        now = datetime.now()
        if now.hour < 17:
            command = self.java.build(parameter)
            return command
        raise CommandException('No permission')
