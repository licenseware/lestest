def func1(param1: str, param2: dict, *, param3):
    return param1, param2


async def cofunc1():
    return "ok"


class Class1:
    def __init__(self, param1: str) -> None:
        self.param1 = param1

    def method1(self, method_param: str):
        return "classic response" + method_param

    def method2(self):
        return "classic response" + self.param1
