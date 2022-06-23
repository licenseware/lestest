import os
import inspect
import importlib.util as importutil
from dataclasses import dataclass
from types import ModuleType
from typing import Tuple
from importlib._bootstrap import ModuleSpec


@dataclass
class MemberDetails:
    module: ModuleType
    module_spec: ModuleSpec
    module_name: str
    module_path: str
    object_name: str = None


@dataclass
class ModuleMembers:
    functions: Tuple[MemberDetails]
    classes: Tuple[MemberDetails]


class DiscoverPackage:
    @staticmethod
    def get_package_name(package_name: str = None):

        if package_name:
            return package_name

        folders = [d for d in os.listdir("./") if os.path.isdir(d)]

        for folder in folders:
            if folder == "tests":
                continue
            if "__init__.py" in os.listdir(os.path.join("./", folder)):
                return folder

    @staticmethod
    def get_module_paths(package_name: str):

        package_path = os.path.join("./", package_name)

        file_modules = []
        for root, _, files in os.walk(package_path):

            if root.endswith("__pycache__"):
                continue

            files = [
                os.path.join(root, f)
                for f in files
                if f.endswith(".py") and f != "__init__.py"
            ]

            file_modules.extend(files)

        return file_modules

    @staticmethod
    def _get_module_functions(member_details: MemberDetails, moduletext: str):

        functions = [
            i[0] for i in inspect.getmembers(member_details.module, inspect.isfunction)
        ]

        non_imported_funcs = []
        for func_name in functions:
            if moduletext.count("def " + func_name) == 1:
                md = MemberDetails(
                    object_name=func_name,
                    module=member_details.module_name,
                    module_spec=member_details.module_spec,
                    module_name=member_details.module_name,
                    module_path=member_details.module_path,
                )
                non_imported_funcs.append(md)

        return tuple(non_imported_funcs)

    @staticmethod
    def _get_module_classes(member_details: MemberDetails, moduletext: str):

        classes = [
            i[0] for i in inspect.getmembers(member_details.module, inspect.isclass)
        ]

        non_imported_classes = []
        for cls_name in classes:
            if moduletext.count("class " + cls_name) == 1:
                md = MemberDetails(
                    object_name=cls_name,
                    module=member_details.module_name,
                    module_spec=member_details.module_spec,
                    module_name=member_details.module_name,
                    module_path=member_details.module_path,
                )
                non_imported_classes.append(md)

        return tuple(non_imported_classes)

    @staticmethod
    def get_module_members(module_path: str):

        module_name = os.path.basename(module_path).split(".py")[0]
        spec = importutil.spec_from_file_location(module_name, module_path)
        module = importutil.module_from_spec(spec)
        spec.loader.exec_module(module)

        with open(module_path, "r") as f:
            moduletext = f.read()

        md = MemberDetails(
            module=module,
            module_spec=spec,
            module_name=module_name,
            module_path=module_path,
        )

        return ModuleMembers(
            functions=DiscoverPackage._get_module_functions(md, moduletext),
            classes=DiscoverPackage._get_module_classes(md, moduletext),
        )

    @staticmethod
    def get_module_imports(module_members: ModuleMembers):
        """

        module_members: ModuleMembers(
            functions=(),
            classes=(
                MemberDetails(
                    module='tox_creator',
                    module_spec=ModuleSpec(name='tox_creator', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f2166b09fd0>, origin='/home/acmt/Documents/lware/lestest/./lestest/tox_creator.py'),
                    module_name='tox_creator',
                    module_path='./lestest/tox_creator.py',
                    object_name='ToxCreator'),)
            )

        For each module member we should get a full import like this:
        - from lestest.lestest import Lestest
        - from lestest.tox_creator import ToxCreator

        Transformations:
        module_path='./lestest/nested/n1/n1_module.py' -> from lestest.nested.n1.n1_module import object_name

        """

        # './lestest/nested/n1/n1_module.py'
        dst_import = (
            lambda path: path.replace(".py", "")
            .replace(".", "")
            .replace(os.path.sep, ".")[1:]
        )

        classes_import_statements = []
        for item in module_members.classes:
            importstatement = (
                f"from {dst_import(item.module_path)} import {item.object_name}"
            )
            classes_import_statements.append(importstatement)

        functions_import_statements = []
        for item in module_members.functions:
            importstatement = (
                f"from {dst_import(item.module_path)} import {item.object_name}"
            )
            functions_import_statements.append(importstatement)

        return classes_import_statements + functions_import_statements
