##
# This file contains the class for displaying the player information to
# the user.
#
# Author: Jason Kamphaugh
#
# Date: March 9, 2012
#


from GUI import Frame
from GUI import Grid
from GUI import Label

import obscure_reference.reference_objects.player

class Player_Frame( Frame ):
   def __init__( self,
                 player_list,
                 player_keys ):
      """This method is the constructor for the object."""
      
      #call the parent constructor
      Frame.__init__( self )
      
      player_rows = []
      # The first row of the display will be the column headings for a player
      # TODO: This should probably be done differently
      
      label_row = []
      
      #create labels for the header information
      for key in player_keys:
         label_row.append( Label( key ) )
      #end loop through player keys

      player_rows.append( label_row )

      # Iterate through the list of players getting their data
      for player in player_list.values():
         current_row = [] # Just a list of Labels, not a Row
         current_row = player.Fill_Data(current_row)
         player_rows.append(current_row)
      #end for
      
      #The player list will be displayed in tabular format
      self._players_grid = Grid(player_rows)
      
      # Put the grid into the frame
      self.place(self._players_grid)

   #end __init__

   def _Create_Header_Label( self ):
      """This method will create the header label to be used at the
      top of the display of player information."""
      None
   #end _Create_Header_Label
   
   def _Display_Player_Row( self, player ):
      """This method will create a player row <where?> given a player."""
      None
   #end _Display_Player_Row

#end class Player_Frame