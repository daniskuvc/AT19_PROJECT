class Node:
    def __init__(self, file):
        self.file = file

    def create_command(self):
        return f"node {self.file}"
