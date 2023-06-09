from src.com.jalasoft.compiler.common.validator.empty_or_none_validator import EmptyOrNoneValidator
from src.com.jalasoft.compiler.common.validator.file_validator import FileValidator
from src.com.jalasoft.compiler.common.validator.context import Context


class Parameter:
    def __init__(self, file_path: str, folder_path: str, binary_path: str):
        self.file_path: str = file_path
        self.folder_path: str = folder_path
        self.binary_path: str = binary_path

    def get_file_path(self) -> str:
        return self.file_path

    def get_folder_path(self) -> str:
        return self.folder_path

    def get_binary_path(self) -> str:
        return self.binary_path

    def validate(self):
        strategies: list = [
            EmptyOrNoneValidator("file_path", self.get_file_path()),
            EmptyOrNoneValidator("folder_path", self.folder_path),
            EmptyOrNoneValidator("binary_path", self.get_binary_path()),
            FileValidator(self.get_file_path(), True),
            FileValidator(self.get_folder_path(), False),
            FileValidator(self.get_binary_path(), False)
        ]
        context = Context(strategies)
        context.validate()
