##
# This file contains the class for displaying the player information to
# the user.
#
# Author: Jason Kamphaugh
#
# Date: March 9, 2012
#


from GUI import ScrollableView
from GUI import Grid
from GUI import Label
from GUI import Font

import obscure_reference.reference_objects.player

class Player_Frame( ScrollableView ):
   def __init__( self,
                 player_list,
                 player_keys,
                 **kwds ):
      """This method is the constructor for the object."""
      
      #call the parent constructor
      ScrollableView.__init__( self,
                               **kwds )
      self._player_rows = []
      # The first row of the display will be the column headings for a player
      # TODO: This should probably be done differently
      
      self._label_row = []
      
      #create labels for the header information
      for key in player_keys:
         self._label_row.append( Label( key,
                                        font = Font( style = ["bold"] ) ) )
      #end loop through player keys

      self._player_rows.append( self._label_row )

      #get the list of player names
      player_names = player_list.keys( )

      #put the list in alphabetical order
      player_names.sort( )

      # Iterate through the list of players getting their data
      #for player in player_list.values():
      for name in player_names:
         current_row = [] # Just a list of Labels, not a Row
         
         player = player_list[name]

         current_row = player.Fill_Data( current_row )
         self._player_rows.append( current_row )
      #end for
      
      #The player list will be displayed in tabular format
      self._players_grid = Grid( self._player_rows )
                                     
      # Put the grid into the frame
      self.place( self._players_grid )

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