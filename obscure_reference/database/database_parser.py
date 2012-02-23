##
# This file is used to unravel that data provided by 
# the database for the system
#
# Author: Jason Kamphaugh
#
# Date: February 16, 2012
#

import obscure_reference.common.string_definitions as string_definitions
import database_interaction

class Database_Parser( database_interaction.Database_Interaction ):

   def __init__( self,
                 username,
                 password, 
                 database_name ):

      #default the player table
      self._player_table = None

      #call the parent class's constructor
      database_interaction.Database_Interaction.__init__( self,
                                                          username,
                                                          password,
                                                          database_name )
   #end __init__

   def Reload_Players( self ):
      """This method will reload the player table"""
      
      #retrieve the player table
      self._player_table = \
         self.Get_Table( string_definitions.player_table_name )

      #get the feed 
      self._player_feed = self.Get_Feed( self._player_table )
         
   #end Reload_Players

   def Reload_Managers( self ):
      """This method will reload the managers table"""

      #retrieve the manager table
      self._manager_table = \
         self.Get_Table( string_definitions.manager_table_name )

      #get the feed
      self._manager_feed = self.Get_Feed( self._manager_table )

   #end Reload_Managers


   def Get_Manager_Line( self,
                         manager_login = None,
                         manager_name = None ):
      """This method will retrieve the manager specified by ether
      the login or the name."""

      manager_data = {}

      key_string = None
      search_key = None

      if manager_login <> None:
         key_string = manager_login
         search_key = string_definitions.manager_login_name
      #end if searching for manager_login
      elif manager_name <> None:
         key_string = manager_name
         search_key = string_definitions.manager_name
      #end if searching for manager_name
      else:
         print( "No valid search key for Get_Manager_Line" )
      #problem

      #retrieve the manager table if we haven't already
      if self._manager_table is None:
         self.Reload_Managers( )
      #end if manager table is none

      #make sure that we have the manager table
      if self._manager_table <> None:

         #loop through the managers, looking for the specified manager
         for index, manager in enumerate( self._manager_feed.entry ):

            #if we've found a match
            if manager.custom[search_key].text.upper() == key_string.upper():

               for key in manager.custom:
                  manager_data[key] = manager.custom[key].text
               #end loop through the keys
               manager_data["row_reference"] = manager
               manager_data["index"] = index

               #we found a match, so break out of the loop
               break
            #end if found a match
         #get the manager line
      #end if valid manager table
      else:
         print( "Invalid manager table." )
      #end if not valid manager table 

   #end Get_Manager_Line


   def Get_Player_Line( self,
                        player_name ):
      """This method will retrive the specified player."""      

      #default the player line
      player_data = {}

      #make a shorter variable for readability
      name_field = string_definitions.player_name_field

      #make sure that we received a valid player name
      if self._player_table is None:

         self.Reload_Players()

      #end if no player table

      #check to make sure we now have a player table
      if self._player_table <> None:

         #retrieve the player line
         player = self.Get_Line( self._player_feed,
                                 string_definitions.player_name_field,
                                 player_name )

         #if we've found a match
         if player <> None:

            for key in player.custom:
               player_data[key] = player.custom[key].text
            #end loop through the keys
            player_data["row_reference"] = player
            player_data["index"] = 0

            #we found a match, so break out of the loop
            break
         #end if found a match

      #end if player table is not none
      else:
         print( "Could not retrieve player table" )
      #end if no player table

      return player_data

   #end Get_Player_Line

   def Set_Player_Line( self,
                        player_data ):
      """This method will update the data of the specified player."""
      # Note: The parameter player_data needs to be a map of 
      # data in the same format as is retrieved from Get_Player_Data

      formatted_player_data = {}

      for key in player_data:

         #make sure that this is something that we're supposed to copy
         if key not in string_definitions.added_player_data:

            #save the data in the formatted structure
            formatted_player_data[key] = player_data[key]

         #end if something to copy
      #end loop through player data

      self.Set_Line( self._player_feed,
                     player_data["row_reference"],
                     formatted_player_data )

   #end Set_Player_Line

   def Add_Player( self,
                   player_data ):
      """This method will add a player to the player table."""

      #pass the data on to Add a generic row to the player table.
      self.Insert_Line( player_data, self._player_table._key )

   #end Add_Player                   

   def Get_Team_Table( self,
                       team_name ):
      """This method will retrieve the team of the specified name."""

      #near as I can tell, this is just a pass-through to get the table
      #with the team name.
      #We might want to beef this up so that it will pull all of the pertinent
      #data (players, salary, etc) in to a structure to be read outside of
      #this function.
      return self.Get_Table( team_name )

   #end Get_Team_Table

#end class Database_Parser
