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
# limitatdions under the License.

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)
    
import implementations.securitySolution

def test_securityInit():
    #GIVEN
    EXPECTED_NAME = "DSAQ US Equity"
    EXPECTED_STRING = "Security: DSAQ US Equity"

    #WHEN
    testObj = implementations.securitySolution.security(EXPECTED_NAME)


    #EXPECT
    assert (testObj.getName() == EXPECTED_NAME)
    assert str(testObj) == EXPECTED_STRING
    print("🤏🏾Test worked!")


