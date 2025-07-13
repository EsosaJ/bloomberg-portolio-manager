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
    
    # def __eq__(self, other):
    #     return isinstance(other, security) and self.name == other.name

    # def __hash__(self):
    #     return hash(self.name)

