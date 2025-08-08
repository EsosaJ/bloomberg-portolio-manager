
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from generators.priceDataGenerator import priceData
from implementations.securitySolution import security

pd = priceData()
class position(positionInterface):
    def __init__(self, securityIn, initialPosition: int) -> None:
        if isinstance(securityIn, str):
            self.securityIn = security(securityIn)
        else:
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
        if self.initialPosition + inputValue < 0:
            raise Exception("Shares cannot be negative")
        self.initialPosition += inputValue # Client has bought more shares or sold shares 

    def __str__(self):
        return f"Position: {self.initialPosition} shares of {self.securityIn}"
    
    def getCurrentMarketValue(self) -> float:
        # specific quantity of a security 
        asset = pd.getCurrentPrice(self.securityIn.getName()) * self.initialPosition
        return asset
    

