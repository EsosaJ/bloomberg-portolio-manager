from interfaces.securityInterface import securityInterface

class security(securityInterface):
    def __init__(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def setName(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Security: {self.name}"
