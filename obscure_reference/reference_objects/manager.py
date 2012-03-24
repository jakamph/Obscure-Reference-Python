##
# This module contains the definition of the team object.
#
# Author: Jason Kamphaugh
#
# Date: March 23, 2012
#

import obscure_reference.common.string_definitions as string_definitions

import obscure_reference.reference_objects.reference_object as reference_object

class Manager( reference_object.Reference_Object ):

   def __init__( self,
                 raw_manager_data ):

      self._email_address = \
         raw_manager_data.custom[string_definitions.manager_login_name].text

      char_index = self._email_address.index("@")

      #pull out the username of the manager
      self._manager_username = \
         self._email_address[0:char_index]

      self._manager_name = \
         raw_manager_data.custom[string_definitions.manager_name].text

      self._team_name = \
         raw_manager_data.custom[string_definitions.team_name].text

      self._raw_data = raw_manager_data

   #end __init__

   def Get_Username( self ):
      """This method will retrieve the username of the manager associated
      with this team."""
      
      return self._manager_username
      
   #end Get_Username

   def Get_Team_Name(self):
      """This method will retrieve the team name for this manager."""

      return self._team_name

   #end Get_Team_Name

   def Get_Manager_Name( self ):
      """This method will retrieve the full name of the manager."""
      
      return self._manager_name
      
   #end Get_Manager_Name

   def Get_Raw_Data(self):
      """This method will retrieve the raw data from the database that was
      received at initialization."""
      
      return self._raw_data
   
   #end Get_Raw_Data

#end class Manager