from src.com.jalasoft.compiler.model.commands.command import Command
from src.com.jalasoft.compiler.model.node.node_cmd import Node
from src.com.jalasoft.compiler.common.exceptions.command_exception import CommandException
from src.com.jalasoft.compiler.model.parameter import Parameter


class NodeAdapter(Command):
    def build(self, parameter: Parameter) -> str:
        try:
            node = Node(parameter.get_file_path())
            return node.create_command()
        except Exception as error:
            raise CommandException("node adapter error")
