##
# This file is used to unravel that data provided by 
# the database for the system
#
# Author: Jason Kamphaugh
#
# Date: February 16, 2012
#

import database_interaction

class Database_Parser( database_interaction.Database_Interaction ):


   def Reload_Players( self ):
      """This method will reload the player table"""
      
      #retrieve the player table
      self._player_table = self.Get_Table( _player_table_name )

      #get the feed 
      self._player_feed = \
         self._client.GetListFeed( self._key,
                                   self._player_table.key )
   #end Reload_Players

   def Get_Player_Line( self,
                        player_name ):
      """This method will retrive the specified player."""      

      #default the player line
      player_data = {}

      #make sure that we received a valid player name
      if self._player_table is None:

         self.Reload_Players()

      #end if no player table

      #check to make sure we now have a player table
      if self._player_table <> None:

         #loop through the players, looking for the specified player
         for index, player in enumerate( self._player_feed.entry ):

            #if we've found a match
            if player.title.text.upper() == player_name.upper():

               for key in player.custom:
                  player_data[key] = player.custom[key].text
               #end loop through the keys
               player_data["row_reference"] = player
               player_data["index"] = index
            #end if found a match
         #get the player line
                  

      #end if player table is not none
      else:
         print( "Could not retrieve player table" )
      #end if no player table

      return player_data

   #end Get_Player_Data

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
