##
# This module contains the definition of the team object.
#
# Author: Jason Kamphaugh
#
# Date: April 5, 2012
#

import obscure_reference.common.number_constants as number_constants

class Team:
   
   def __init__( self,
                 team_name,
                 manager ):
      """This method is the constructor of this object."""
      
      self._team_name = team_name
      self._manager = manager
      
      #create an empty player list
      self._player_list = {}
      
      #create a variable for keeping track of the number of players
      self._player_count = 0
      
      #create a variable for storing the team's salary
      self._salary = 0
      
   #end __init__
   
   def Add_Player( self,
                   player ):
      """This method will add a player to the team."""
      
      #add the player's salary to the team's salary
      self._salary += player.Get_Current_Salary( )
      
      # this player only counts against the roster max if they're not on
      # the disabled list
      if not player.On_Disabled_List( ):
      
         self._player_count += 1
      
      #end if player is not on the disabled list
      
      #put the player in the team's list
      self._player_list[player.Get_Name( )] = player

   #end Add_Player
   
   def Drop_Player( self,
                    player ):
      """This method will drop the player from the team's list."""

      
      #add the player's salary to the team's salary
      self._salary -= player.Get_Current_Salary( )
      
      # this player only counts against the roster max if they're not on
      # the disabled list
      if not player.On_Disabled_List( ):
      
         self._player_count -= 1
      
      #end if player is not on the disabled list
      
      #remove the player in the team's list
      self._player_list.pop(player.Get_Name( ))
      
   #end Drop_Player
   
   def Get_Player_List( self ):
      """This method will retrieve the list of players on this team."""
      return self._player_list
   #end Get_Player_list
   
   def Get_Player_Count( self ):
      """This method will retrieve the number of players currently counted as
      on the roster."""
      
      return self._player_count
   
   #end Get_Player_Count
   
   def Get_Team_Name( self ):
      """This method will retrieve the name of this team."""
      
      return self._team_name
   
   #end Get_Team_Name
   
   def Get_Manager( self ):
      """This method will retrieve the manager of this team."""
      
      return self._manager
   
   #end Get_Manager
   
   def Team_Is_Full( self ):
      """This method will return the condition where this team has a full 
      roster."""
      
      return (self._player_count == number_constants.max_roster_size)
   
   #end Team_Is_Full
   
   def Get_Team_Salary( self ):
      """This method will retrieve the salary of this team."""
      
      return self._salary
   
   #end Get_Team_Salary
#end Team