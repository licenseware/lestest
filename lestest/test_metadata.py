import inspect
from lestest import types


class TestMetadata:
    @staticmethod
    def get_mock_params_from_object(object: callable):

        object_params = list(dict(inspect.signature(object).parameters).values())

        mock_params = {}
        for op in object_params:
            if op.name == "self":
                continue
            if isinstance(op.annotation(), str):
                mock_params[op.name] = "'fill this'"
            elif isinstance(op.annotation(), dict):
                mock_params[op.name] = {"key": "fill this"}
            elif isinstance(op.annotation(), tuple):
                mock_params[op.name] = ("fill", "this")
            elif isinstance(op.annotation(), list):
                mock_params[op.name] = ["fill", "this"]
            else:
                mock_params[op.name] = "'specify type or fill this'"

        return mock_params

    @staticmethod
    def get_mock_params_string(mock_params: dict):
        params = ""
        for param, val in mock_params.items():
            params = f"{param}={val}, " + params
        params = params[:-2] if params.endswith(", ") else params
        return params

    @staticmethod
    def get_params_statement(object: callable):
        mock_params = TestMetadata.get_mock_params_from_object(object)
        paramsstr = TestMetadata.get_mock_params_string(mock_params)
        return paramsstr

    @staticmethod
    def get_test_template_vars(member: types.MemberDetails):

        params = TestMetadata.get_params_statement(member.object)
        object_name_lower = member.object_name.lower()
        file_test_name = member.module_name + "_" + object_name_lower
        filename = "test_" + file_test_name + ".py"

        class_methods = []
        if inspect.isclass(member.object):
            cls_methods = [m for m in dir(member.object) if not m.startswith("__")]
            for method_name in cls_methods:
                method_object = getattr(member.object, method_name)
                method_params = TestMetadata.get_params_statement(method_object)
                method_call = "res." + method_name + f"({method_params})"
                class_methods.append(method_call)

        object_call_statement = f"res = {member.object_name}({params})"

        tvars = types.TemplateVars(
            params=params,
            filename=filename,
            object_name_lower=object_name_lower,
            file_test_name=file_test_name,
            class_methods=tuple(class_methods),
            object_call_statement=object_call_statement,
            import_object_statement=member.import_statement,
        )

        return tvars
