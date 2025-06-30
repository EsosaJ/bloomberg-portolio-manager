
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
#rom implementations.securitySolution import security

class position(positionInterface):
    def __init__(self, securityIn, initialPosition: int) -> None:
        self.securityIn = securityIn
        self.initialPosition = initialPosition
    
    def getSecurity(self) -> securityInterface:
        return self.securityIn

    def getPosition(self) -> int:
        return self.initialPosition # get the amount of shares client bought 
    
    def setPosition(self, inputValue: int) -> None:
        self.initialPosition = inputValue # amount of shares client has bought 
    
    #Add an integer amount to the current position.
    def addPosition(self, inputValue: int) -> None:
        self.initialPosition += inputValue # Client has bought more shares or sold shares 

    
    def __str__(self):
        return f"Position: {self.initialPosition} shares of {self.securityIn}"
