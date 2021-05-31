class PyLarkError(Exception):
    def __init__(self, scope: str, func: str, code: int, msg: str):
        super().__init__(
            f"pylark error, scope={scope}, func={func}, code={code}, msg={msg}"
        )

        self.scope = scope
        self.func = func
        self.code = code
        self.msg = msg
