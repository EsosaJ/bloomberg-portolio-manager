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

#Portfolio Class
from typing import Set, Iterable, Optional, Dict
from interfaces.portfolioInterface import portfolioInterface
from interfaces.accountInterface import accountInterface
from generators.priceDataGenerator import priceData
pd = priceData()
class portfolio(portfolioInterface):
    # initialise the protfolio name and its the accounts inside the portfolio
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        self.portfolioName = portfolioName
        self.accounts : Dict[str, accountInterface] = {account.getName() : account for account in accounts}
        #convert to dictionary for greater efficiency 
        # match account name to the account object 

    def getAllAccounts(self) -> Iterable[accountInterface]: 
        return set(self.accounts.values())

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
    # get accounts that contains the security name 
    #Use a nested loop to go through account and securities and check if they are the same 
        result = set()
        for account in self.accounts.values(): 
            name_match = (not accountNamesFilter or account.getName() in accountNamesFilter)
            security_match = (not securitiesFilter or bool(account.getPositions(securitiesFilter)))
            # if there's an intersection between account.getPositions and security filter

            if name_match and security_match: #get accounts that match securities and account name 
                result.add(account)

        return result

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for account in accounts:
            self.accounts[account.getName()] = account
        #adds an entry if doesn't exist or replaces it 

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for name in accountNames:
            self.accounts.pop(name,None)

    def getCurrentMarketValue(self) -> float:
        qty = {}
        for account in self.accounts.values():
            for pos in account.getAllPositions():
                name = pos.getSecurity().getName()
                qty[name] = qty.get(name, 0) + pos.getPosition()
        
        total = 0.0
        for name, amount in qty.items():
            total += pd.getCurrentPrice(name) * amount
        return total

    def getCurrentFilteredMarketValue(self, securities: Set, accountNames: Set[str]) -> float: 
        total = 0.0
        sec_filter = None if not securities else {
            (s if isinstance(s, str) else s.getName()) for s in securities
        }
        acc_filter = None if not accountNames else set(accountNames)

        qty = {}
        for account in self.accounts.values(): 
            if acc_filter is not None and account.getName() not in acc_filter:
                continue
            for pos in account.getAllPositions(): #go through all pos under that acc name 
                # Create a dictionary of that security and get the amount of that spefific sec and then at end get the current val and 
                # multiply 
                name = pos.getSecurity().getName()
                if sec_filter is None or name in sec_filter:
                    qty[name] = qty.get(name, 0) + pos.getPosition()

        for name, amount in qty.items():
            total += pd.getCurrentPrice(name) * amount            
        return total