from src.com.jalasoft.compiler.model.commands.java__command_proxy import JavaCommandProxy
from src.com.jalasoft.compiler.model.commands.java_command import JavaCommand
from src.com.jalasoft.compiler.model.commands.node_adapter import NodeAdapter
from src.com.jalasoft.compiler.model.commands.python_command import PythonCommand
from src.com.jalasoft.compiler.model.commands.command import Command

code_map = {
    'java': JavaCommand(),
    'python': PythonCommand(),
    'node': NodeAdapter(),
    'java-proxy': JavaCommandProxy()
}


class CompilerFactory:
    @staticmethod
    def get_instance(lang: str) -> Command:
        return code_map[lang]
