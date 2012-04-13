##
# This file contains the class for displaying the player information to
# the user.
#
# Author: Jason Kamphaugh
#
# Date: March 9, 2012
#


from GUI import ScrollableView
from GUI import Label
from GUI import Font
from GUI import Row

import obscure_reference.gui.custom_grid as custom_grid

import obscure_reference.reference_objects.player
from gui.scrolling_grid_view import Scrolling_Grid_View

class Player_Frame( ScrollableView ):
   def __init__( self,
                 player_list,
                 player_keys,
                 **kwds ):
      """This method is the constructor for the object."""

      #call the parent constructor
      ScrollableView.__init__( self,
                               **kwds )
      
      # Create list of player rows
      player_rows = []

      # get the list of player names
      player_names = player_list.keys( )

      # put the list in alphabetical order
      player_names.sort( )

      # Iterate through the list of players getting their data
      for name in player_names:
         current_row = [] # Just a list of Labels, not a Row
         
         player = player_list[name]

         current_row = player.Fill_Data( current_row )
         player_rows.append( current_row )
      #end for
      
      #The player list will be displayed in tabular format
      self._scrolling_grid_view =\
          Scrolling_Grid_View( grid_array = player_rows,
                               scrolling = "v" )
      
      # Create a list of the labels for headers and line them up with the grid
      label_row = []
      
      #create labels for the header information
      num_cols = min( len(player_keys),
                      self._scrolling_grid_view.get_num_cols() )
      for i in range( 0, num_cols ):
         header_label = Label( player_keys[i],
                               font = Font( style = ["bold"] ) )
         
         # If player grid column is wider than current label
         if self._scrolling_grid_view.get_col_width( i ) > header_label.width:
            # Set column width to match grid
            header_label.width = self._scrolling_grid_view.get_col_width( i )
         else:
            self._scrolling_grid_view.set_col_width( i, header_label.width )
         # end if grid column is wider
                         
         label_row.append( header_label )
      #end loop through player keys

      # Place the column headers in the player frame
      self._header_row = Row( label_row )
      self.place( self._header_row,
                  left = 0,
                  top = 0 )
      
      # Set the height and width of the grid based on the dimensions of the
      # other components
      self._scrolling_grid_view.height = self.height - self._header_row.height
      
      self._scrolling_grid_view.width = max( self._scrolling_grid_view.width,
                                             self.width - 2 )
      
      # Set extent of scrolling to accommodate the entire grid
      self.set_extent( (self._scrolling_grid_view.width, self.height) )
                                     
      # Put the grid into the frame
      self.place( self._scrolling_grid_view,
                  top = self._header_row,
                  sticky = 'nsew' )

   #end __init__
   
   #this method doesn't follow the naming standard because it is automatically
   #called by the GUI framework
   def draw( self, canvas, rect ):
      """Cause the frame to re-draw the important area."""
      canvas.erase_rect( rect )

   #end draw

#end class Player_Frame