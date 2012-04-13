'''
Created on Apr 7, 2012

@author: clay
'''
from GUI import ScrollableView
from gui import custom_grid

class Scrolling_Grid_View( ScrollableView ):
   '''
   This class is a scrolling view which contains a Custom_Grid containing the
   contents of the array passed in.
   '''


   def __init__( self, grid_array, **kwds ):
      '''
      Constructor
      '''
      
      #call the parent constructor
      ScrollableView.__init__( self,
                               **kwds )
      
      self._grid = custom_grid.Custom_Grid( grid_array )
      
      self.width = self._grid.width + 20
      
      self.place( self._grid )
      
      self.set_extent( (self._grid.width, self._grid.height) )
      
   # end def __init__
   
   def get_col_width( self, col_num ):
      return self._grid.get_col_width( col_num )
   #end def get_col_width
   
   def set_col_width( self, col_num, width ):
      self._grid.set_col_width( col_num, width )
   #end def set_col_width
    
   def get_row_height( self, row_num ):
      return self._grid.get_row_height( row_num )
   #end def get_row_height
   
   def set_row_height( self, row_num, height ):
      self._grid.set_row_height( row_num, height )
   #end def set_row_height
   
   def get_num_cols( self ):
      return self._grid.get_num_cols()
   #end def get_num_cols
   
   def get_num_rows( self ):
      return self._grid.get_num_rows()
   #end def get_num_rows
   
   #this method doesn't follow the naming standard because it is automatically
   #called by the GUI framework
   def draw( self, canvas, rect ):
      """Cause the frame to re-draw the important area."""
      canvas.erase_rect( rect )

   #end draw
# end class Scrolling_Grid_View