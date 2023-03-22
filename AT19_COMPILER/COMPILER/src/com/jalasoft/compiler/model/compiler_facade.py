from src.com.jalasoft.compiler.model.compiler_factory import CompilerFactory
from src.com.jalasoft.compiler.model.parameter import Parameter
from src.com.jalasoft.compiler.model.execute import Execute
from src.com.jalasoft.compiler.model.commands.command import Command


class CompilerFacade:
    def __init__(self):
        pass

    @staticmethod
    def compile(lang: str, file: str, folder: str, binary: str) -> str:
        parameter: Parameter = Parameter(file, folder, binary)
        command: Command = CompilerFactory.get_instance(lang)
        cmd: str = command.build(parameter)
        execute: Execute = Execute()
        return execute.run(cmd)
