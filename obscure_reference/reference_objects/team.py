##
# This module contains the definition of the team object.
#
# Author: Jason Kamphaugh
#
# Date: April 5, 2012
#

class Team:
   
   def __init__( self,
                 team_name,
                 manager ):
      """This method is the constructor of this object."""
      
      self._team_name = team_name
      self._manager = manager
      
      self._player_list = []
      
   #end __init__
   
   def Add_Player( self,
                   player ):
      """This method will add a player to the team."""
      
      self._player_list.append( player )
   #end Add_Player
   
   def Get_Player_List( self ):
      """This method will retrieve the list of players on this team."""
      return self._player_list
   #end Get_Player_list
   
   def Get_Team_Name( self ):
      """This method will retrieve the name of this team."""
      
      return self._team_name
   
   #end Get_Team_Name
   
   def Get_Manager( self ):
      """This method will retrieve the manager of this team."""
      
      return self._manager
   
   #end Get_Manager
#end Team