import os

from flask import Flask
from flask import request
from src.com.jalasoft.compiler.model.compiler_facade import CompilerFacade
from src.com.jalasoft.compiler.common.exceptions.command_exception import CommandException
app = Flask(__name__)


@app.route('/compiler', methods=['POST'])
def route():
    lang = request.form.get('lang')
    java_file = request.files['file']
    folder_path = os.getenv('FOLDER_UPLOAD_PATH')
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, java_file.filename)
    java_file.save(file_path)

    if 'java' in lang:
        binary_path = os.getenv('JAVA8_BINARY_PATH')

    if lang == 'python':
        binary_path = os.getenv('PYTHON_BINARY_PATH')
    try:
        return CompilerFacade.compile(lang, file_path, folder_path, binary_path)
    except CommandException as error:
        return error.get_message()


if __name__ == '__main__':
    app.run()
