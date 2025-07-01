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

from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable

class account(accountInterface):
# Accounts groups multiple posiitons in one 
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.accountName = accountName
        self.positions = positions

    #Return the account's name
    def getName(self) -> str:
        return self.accountName

    #Return all positions currently within the account
    def getAllPositions(self) -> Iterable[positionInterface]:
        #check if set is empty
        if not self.positions:
            raise Exception("Account is empty")
        #return positions as a list 
        return list(self.positions)

    #Return all positions that contain a security in a given input set
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        #set securities to a position object
        result = {}
        # get the string from set
        for position in self.positions: 
           security = position.getSecurity()
           if security in securities:
               result[security] = position
        #set security to the position object 
        return result
            

    #Add positions to the account
    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:
        pass
