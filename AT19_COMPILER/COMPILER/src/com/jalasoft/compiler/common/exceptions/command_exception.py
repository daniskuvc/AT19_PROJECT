class CommandException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self):
        return self.message
