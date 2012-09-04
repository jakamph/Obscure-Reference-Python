##
# This module contains the definition of the manager object.
#
# Author: Jason Kamphaugh
#
# Date: March 23, 2012
#

import obscure_reference.common.string_definitions as string_definitions

import obscure_reference.reference_objects.team as team

import obscure_reference.reference_objects.reference_object as reference_object

class Manager( reference_object.Reference_Object ):

   def __init__( self,
                 raw_manager_data ):

      self._email_address = \
         raw_manager_data.custom[string_definitions.manager_login_name].text

      self._manager_username = \
         string_definitions.Extract_Username( self._email_address )

      self._manager_name = \
         raw_manager_data.custom[string_definitions.manager_name].text

      self._team_name = \
         raw_manager_data.custom[string_definitions.team_name].text

      self._raw_data = raw_manager_data
      
      #create the team for this manager
      self._team = None

      #create the manager's team object
      self._team = team.Team( self._team_name,
                              self )

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

   def Get_Team( self ):
      """This method will retrieve the team object this manager is in charge
      of."""
      
      return self._team

   #end Get_Team

   def Add_Player( self,
                   player ):
      """This method will add the specified player to this manager's team."""
      
      #give this player to the team
      self._team.Add_Player(player)

   #end Add_Player

   def Drop_Player( self,
                    player ):
      """This method will drop the specified player from this manager's 
      team."""
      
      #give this player to the team
      self._team.Drop_Player( player )
      
   #end Drop_Player
   
   def Get_Email( self ):
      """This method will retrieve the email address of this manager."""

      return self._email_address
   
   #end Get_Email

#end class Manager