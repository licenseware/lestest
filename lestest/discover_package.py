import os
import inspect
import importlib.util as importutil
from typing import List
from lestest import types
from lestest.absolute_imports import to_absolute_imports


class DiscoverPackage:
    """
    Given or not a package name get all objects details (import statements, the object itself, etc)
    """

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
    def _get_module_functions(member_details: types.MemberDetails, moduletext: str):

        functions = [
            i[0] for i in inspect.getmembers(member_details.module, inspect.isfunction)
        ]

        non_imported_funcs = []
        for func_name in functions:
            if moduletext.count("def " + func_name) == 1:
                md = types.MemberDetails(
                    object_name=func_name,
                    module=member_details.module,
                    object=getattr(member_details.module, func_name),
                    module_spec=member_details.module_spec,
                    module_name=member_details.module_name,
                    module_path=member_details.module_path,
                )
                non_imported_funcs.append(md)

        return tuple(non_imported_funcs)

    @staticmethod
    def _get_module_classes(member_details: types.MemberDetails, moduletext: str):

        classes = [
            i[0] for i in inspect.getmembers(member_details.module, inspect.isclass)
        ]

        non_imported_classes = []
        for cls_name in classes:
            if moduletext.count("class " + cls_name) == 1:
                md = types.MemberDetails(
                    object_name=cls_name,
                    module=member_details.module,
                    object=getattr(member_details.module, cls_name),
                    module_spec=member_details.module_spec,
                    module_name=member_details.module_name,
                    module_path=member_details.module_path,
                )
                non_imported_classes.append(md)

        return tuple(non_imported_classes)

    @staticmethod
    def _update_module_imports(
        module_members: types.ModuleMembers,
    ) -> List[types.MemberDetails]:
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

        """

        # Convert from: './lestest/nested/n1/n1_module.py' to: 'lestest.nested.n1.n1_module'
        dst_import = (
            lambda path: path.replace(".py", "")
            .replace(".", "")
            .replace(os.path.sep, ".")[1:]
        )

        import_statements = []

        for item in module_members.classes:
            importst = f"from {dst_import(item.module_path)} import {item.object_name}"

            md = types.MemberDetails(
                module=item.module,
                module_spec=item.module_spec,
                module_name=item.module_name,
                module_path=item.module_path,
                object=item.object,
                object_name=item.object_name,
                import_statement=importst,
            )

            import_statements.append(md)

        for item in module_members.functions:
            importst = f"from {dst_import(item.module_path)} import {item.object_name}"
            md = types.MemberDetails(
                module=item.module,
                module_spec=item.module_spec,
                module_name=item.module_name,
                module_path=item.module_path,
                object=item.object,
                object_name=item.object_name,
                import_statement=importst,
            )
            import_statements.append(md)

        return import_statements

    @staticmethod
    def get_module_members(
        module_path: str,
        package_name: str = None,
        absolute_imports_converter: callable = to_absolute_imports,
    ) -> List[types.MemberDetails]:

        if module_path.startswith("./") and package_name is None:
            package_name = module_path.split(os.path.sep)[1]

        absolute_imports_converter(package_name or "app")

        mp = os.path.abspath(module_path)

        module_name = os.path.basename(module_path).split(".py")[0]
        spec = importutil.spec_from_file_location(module_name, mp)
        module = importutil.module_from_spec(spec)
        spec.loader.exec_module(module)

        with open(module_path, "r") as f:
            moduletext = f.read()

        md = types.MemberDetails(
            module=module,
            module_spec=spec,
            module_name=module_name,
            module_path=module_path,
        )

        module_members = types.ModuleMembers(
            functions=DiscoverPackage._get_module_functions(md, moduletext),
            classes=DiscoverPackage._get_module_classes(md, moduletext),
        )

        module_details_updated = DiscoverPackage._update_module_imports(module_members)

        return module_details_updated

    @staticmethod
    def get_package_members(package_name: str = None) -> List[types.MemberDetails]:

        package_name = DiscoverPackage.get_package_name(package_name)
        module_paths = DiscoverPackage.get_module_paths(package_name)

        allmm = []
        for module_path in module_paths:
            mm = DiscoverPackage.get_module_members(module_path)
            allmm.extend(mm)
            print(f"Inspected module: `{module_path}`")

        return allmm
