import os
import unittest
from typer.testing import CliRunner
from lestest.cli import app


# python3 -m unittest tests/test_cli_lestest_generate.py


class TestGenerateBaseFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.cli = CliRunner()

    def test_cli_lestest_generate(self):

        # result = self.cli.invoke(app, ["generate", "--help"])
        # print(result.stdout)
        result = self.cli.invoke(app, ["generate", "--package", "package"])
        print(result.stdout)

        assert result.exit_code == 0
        assert "Generated unittest boilerplate files" in result.stdout

        assert os.path.isfile("tox.ini")
        assert os.path.isfile("pytest.ini")
        assert os.path.isfile("requirements-dev.txt")

        files_to_delete = ["tox.ini", "pytest.ini", "requirements-dev.txt"]

        for file in os.listdir("tests"):
            test_filepath = os.path.join("./tests", file)
            if test_filepath.endswith(
                (
                    "1.py",
                    "2.py",
                    "3.py",
                    "4.py",
                )
            ):
                assert os.path.isfile(test_filepath)
                files_to_delete.append(test_filepath)

        for fp in files_to_delete:
            os.remove(fp)
