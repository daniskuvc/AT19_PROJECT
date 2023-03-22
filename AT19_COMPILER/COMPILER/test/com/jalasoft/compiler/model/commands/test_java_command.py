import unittest

from src.com.jalasoft.compiler.model.commands.java_command import JavaCommand
from src.com.jalasoft.compiler.model.parameter import Parameter


class TestJavaCommand(unittest.TestCase):
    def test_build_success(self):
        parameter = Parameter('d:/test/util.java', 'd:/test/', 'd:/java8/java/')
        command = JavaCommand()
        expected = 'd:/java8/java/javac d:/test/util.java && d:/java8/java/java  -cp d:/test/ util'
        self.assertEqual(command.build(parameter), expected)

    def test_build_invalid_file(self):
        parameter = Parameter(None, 'd:/test/', 'd:/java8/java/')
        command = JavaCommand()
        print(command.build(parameter))

    def test_build_success_v(self):
        parameter = Parameter('d:/AT19/EjemploJava8.java', 'd:/AT19/', 'd:/AT19/')
        command = JavaCommand()
        expected = 'd:/AT19/javac d:/AT19/EjemploJava8.java && d:/AT19/java  -cp d:/AT19/ EjemploJava8'
        self.assertEqual(command.build(parameter), expected)
