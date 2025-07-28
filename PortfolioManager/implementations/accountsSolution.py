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

from interfaces.securityInterface import securityInterface
from interfaces.accountInterface import accountInterface
from interfaces.positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable
class account(accountInterface):
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.accountName = accountName
        self.positions = positions

    #Return the account's name
    def getName(self) -> str:
        return self.accountName

    #Return all positions currently within the account
    def getAllPositions(self) -> Iterable[positionInterface]:
        if not self.positions:
            raise Exception("Account is empty")
        #return positions as a list 
        return list(self.positions)

    #Return all positions that contain a security in a given input set
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        result = {}
        ticker_to_item = {}  # Maps ticker name -> original key (string or object)

        for item in securities:
            if isinstance(item, str):
                ticker_to_item[item] = item
            elif isinstance(item, securityInterface):
                ticker_to_item[item.getName()] = item

        for pos in self.positions:
            sec_name = pos.getSecurity().getName()
            if sec_name in ticker_to_item:
                original_key = ticker_to_item[sec_name]
                result[original_key] = pos

        return result
        #set security to the position object 

    #Add positions to the account
    def addPositions(self, positions: Set[positionInterface]) -> None:
        #   get the position in the position set and if it is in it, remove it and add that in??
          for position in positions:
            to_remove = None
            for existing in self.positions:
             if position.getSecurity().getName() == existing.getSecurity().getName():
               to_remove = existing
               break
            if to_remove:
                self.positions.remove(to_remove)       
            self.positions.add(position)
    
    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:

        names_to_remove = set()
        for security in securities:
            if isinstance(security, str):
                    names_to_remove.add(security)
            elif isinstance(security, securityInterface):
                    names_to_remove.add(security.getName())

        to_remove = set() 
        for position in self.positions:
            if position.getSecurity().getName() in names_to_remove:
                to_remove.add(position)
        self.positions.difference_update(to_remove)
