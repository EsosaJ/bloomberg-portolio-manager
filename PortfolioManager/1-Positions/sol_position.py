# Copyright 2022 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
#rom implementations.securitySolution import security

class position(positionInterface):
    def __init__(self, securityIn, initialPosition: int) -> None:
        self.securityIn = securityIn
        self.initialPosition = int(initialPosition)
    
    def getSecurity(self) -> securityInterface:
        return self.securityIn

    def getPosition(self) -> int:
        return self.initialPosition # get the amount of shares client bought 
    
    def setPosition(self, inputValue: int) -> None:
        self.initialPosition = inputValue # amount of shares client has bought 
    
    #Add an integer amount to the current position.
    def addPosition(self, inputValue: int) -> None:
        inputValue = int(inputValue) 
        print(f"DEBUG: Current position: {self.initialPosition}, incoming: {inputValue}")
        if self.initialPosition + inputValue < 0:
            print("RAISING EXCEPTION NOW!")
            raise ValueError("Shares cannot be negative")
        self.initialPosition += inputValue # Client has bought more shares or sold shares 


    def __str__(self):
        return f"Position: {self.initialPosition} shares of {self.securityIn}"
