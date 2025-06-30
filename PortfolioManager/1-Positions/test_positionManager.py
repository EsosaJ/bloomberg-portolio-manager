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

import sys
import os

# Add the root of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import pytest
from PortfolioManager.implementations.positionSolution import position
from PortfolioManager.implementations.securitySolution import security
from PortfolioManager.generators.positionDataGenerator import positionUpdates

def test_positionManagerInits():
    #GIVEN
    EXPECTED_NAME = "DSAQ US Equity"
    EXPECTED_POSITION = 1000
    INPUT_SEC = security(EXPECTED_NAME) #initialise the security 
   

    #WHEN
    testObjA = position(INPUT_SEC, EXPECTED_POSITION)
    testObjB = position(EXPECTED_NAME, EXPECTED_POSITION)
    print("Security: ", testObjA.getSecurity().getName())
    print("Position: ", testObjA.getPosition())

    #EXPECT
    assert (testObjA.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjB.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjA.getPosition() == EXPECTED_POSITION)
    assert (testObjB.getPosition() == EXPECTED_POSITION)
    

def test_positionUpdates(): #test adding posiiton 
    #GIVEN
    secData = positionUpdates()
    EXPECTED_POSITION = sum(secData.getTransactionList()) #shares that the buyer has bought or sold 
    
    #WHEN
    testObj = position("TEST", 0) #set amount of securities that they've bought to 0
    for update in secData.getTransactionList():
        testObj.addPosition(update) #go through transaction list and update the positions 

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION) 

def test_positionSet():
    #GIVEN
    testObj = position("TEST", 0) #set the position to a number check that 
    EXPECTED_POSITION = 1000
    
    #WHEN
    testObj.setPosition(EXPECTED_POSITION)

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION)
    
def test_positionUpdateShortBlock():
    #GIVEN
    BASE_POSITION = 100
    UPDATE_POSITION = -101
    testObj = position("TEST", BASE_POSITION)


    #EXPECT
    with pytest.raises(Exception):
        testObj.addPosition(UPDATE_POSITION)

def test_position_str():
    #Given
    NAME = "AAPL"
    SHARES = 50
    sec = security(NAME)
    pos = position(sec, SHARES) #setting the position object 
    EXPECTED_STRING = f"Position: {SHARES} shares of {NAME}"

    #When 
    result = str(pos)

    #Expected
    assert result == EXPECTED_STRING
    print("Test worked!")
