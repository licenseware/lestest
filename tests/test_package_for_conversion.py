import unittest
import os
import random
import shutil
import tempfile

from lestest.absolute_imports import (
    get_module_paths,
    to_absolute_imports,
)


# python3 -m unittest tests/test_package_for_conversion.py


class TestAbsImports(unittest.TestCase):
    def setUp(self):
        tmppath = os.path.join(
            tempfile.gettempdir(), "pytest" + str(random.randint(1000, 9999))
        )
        os.makedirs(tmppath)

        self.tmpdir = tmppath

    def test_get_module_paths(self):

        cwd = os.getcwd()
        assert os.path.isdir(self.tmpdir)

        srcpkgpath = os.path.join(cwd, "tests", "data", "package")
        assert os.path.isdir(srcpkgpath)
        pkgpath = os.path.join(self.tmpdir, "package")
        shutil.copytree(srcpkgpath, pkgpath)
        assert os.path.exists(pkgpath)

        os.chdir(str(self.tmpdir))

        module_paths = get_module_paths(package_name="package")

        assert len(module_paths) == 4

        for path in module_paths:
            assert os.path.exists(path)

        shutil.rmtree(pkgpath)
        os.chdir(cwd)

    def test_to_absolute_imports(self):

        cwd = os.getcwd()
        srcpkgpath = os.path.join(cwd, "tests", "data", "package")
        pkgpath = os.path.join(self.tmpdir, "package")
        shutil.copytree(srcpkgpath, pkgpath)
        assert os.path.exists(pkgpath)

        os.chdir(str(self.tmpdir))

        module_paths = to_absolute_imports("package")

        assert len(module_paths) == 4

        for path in module_paths:
            assert os.path.exists(path)
            if path.endswith("n3_module.py"):
                with open(path) as f:
                    flines = f.readlines()
                assert "from package.n2.n2_module import func3" == flines[0].strip()

        shutil.rmtree(pkgpath)
        os.chdir(cwd)
