from typing import Any
from dataclasses import dataclass


@dataclass
class TemplateVars:
    params: Any
    object_name_lower: str
    file_test_name: str
    filename: str
    class_methods: tuple
    object_call_statement: str
    import_object_statement: str
