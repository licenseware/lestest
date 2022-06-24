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
    object: callable = None
    object_name: str = None
    import_statement: str = None


@dataclass
class ModuleMembers:
    functions: Tuple[MemberDetails]
    classes: Tuple[MemberDetails]
