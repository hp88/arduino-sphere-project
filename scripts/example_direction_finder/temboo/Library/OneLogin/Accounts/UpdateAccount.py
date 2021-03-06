# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccount
# Updates an existing account.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateAccount, self).__init__(temboo_session, '/Library/OneLogin/Accounts/UpdateAccount')


    def new_input_set(self):
        return UpdateAccountInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountChoreographyExecution(session, exec_id, path)

class UpdateAccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        super(UpdateAccountInputSet, self)._set_input('APIKey', value)
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The account name.)
        """
        super(UpdateAccountInputSet, self)._set_input('AccountName', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) The street address for the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city associated with the address.)
        """
        super(UpdateAccountInputSet, self)._set_input('City', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) The country associated with the address of the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('Country', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address for the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((required, string) The first name on the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('FirstName', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The id of the account to update.)
        """
        super(UpdateAccountInputSet, self)._set_input('ID', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((required, string) The last name on the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('LastName', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) The phone number for the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('Phone', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((required, string) Indicates which plan the new account has (i.e. enterprise).)
        """
        super(UpdateAccountInputSet, self)._set_input('Plan', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state associated with the address of the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) The postal code associated with the address of the new account.)
        """
        super(UpdateAccountInputSet, self)._set_input('Zip', value)

class UpdateAccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class UpdateAccountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateAccountResultSet(response, path)
