#---------------------------------------------------------------------------
#
#   PyGUI - Grid layout component - Generic
#   Clay - modified Grid class from PyGUI since it doesn't provide any way
#   to read info about dimensions, and not able to do it by creating a subclass
#
#---------------------------------------------------------------------------

from GUI import Frame

class Custom_Grid( Frame ):

   def __init__( self, items, row_spacing = 5, column_spacing = 10,
           align = 'l', equalize = '', expand_row = None, expand_column = None,
           padding = ( 0, 0 ), **kwds ):
      Frame.__init__( self )
      self._hpad, self._vpad = padding
      self._num_rows = len( items )
      self._num_cols = max( [len( row ) for row in items] )
      self._col_widths = [0] * self._num_cols
      self._row_heights = [0] * self._num_rows
      
      self._items = items
      self._row_spacing = row_spacing
      self._column_spacing = column_spacing
      self._align = align
      self._equalize = equalize
      self._expand_row = expand_row
      self._expand_column = expand_column
      
      for i, row in enumerate( items ):
         for j, item in enumerate( row ):
            if item:
               self._row_heights[i] = max( self._row_heights[i], item.height )
               self._col_widths[j] = max( self._col_widths[j], item.width )
      self._reset_grid()
      self.set( **kwds )
      
   def _reset_grid( self ):
      tot_width = 0
      row_top = 0
      row_gap = 0
      vanchor = 't'
      for i, row in enumerate( self._items ):
         row_height = self._row_heights[i]
         row_top += row_gap
         col_left = 0
         col_gap = 0
         hanchor = 'l'
         if i == self._expand_row:
            vanchor = 'tb'
         for j, item in enumerate( row ):
            col_width = self._col_widths[j]
            col_left += col_gap
            if item:
               if 'l' in self._align:
                  x = 0
               elif 'r' in self._align:
                  x = col_width - item.width
               else:
                  x = ( col_width - item.width ) // 2
               if 't' in self._align:
                  y = 0
               elif 'b' in self._align:
                  y = row_height - item.height
               else:
                  y = ( row_height - item.height ) // 2
               item.position = ( self._hpad + col_left + x, self._vpad + row_top + y )
               if j == self._expand_column:
                  item.anchor = 'lr' + vanchor
               else:
                  item.anchor = hanchor + vanchor
               self.add( item )
            if j == self._expand_column:
               hanchor = 'r'
            col_left += col_width
            col_gap = self._column_spacing
            tot_width = max( tot_width, col_left )
         if i == self._expand_row:
            vanchor = 'b'
         row_top += row_height
         row_gap = self._row_spacing
      tot_height = row_top
      self.size = ( tot_width + 2 * self._hpad, tot_height + 2 * self._vpad )
      
   
   def get_col_width( self, col_num ):
      return self._col_widths[col_num]
   #end def get_col_width
   
   def set_col_width( self, col_num, width ):
      self._col_widths[col_num] = width
      self._reset_grid()
   #end def set_col_width
   
   def get_row_height( self, row_num ):
      return self._row_heights[row_num]
   #end def get_row_height
   
   def set_row_height( self, row_num, height ):
      self._row_heights[row_num] = height
      self._reset_grid()
   #end def set_row_height
   
   def get_num_cols( self ):
      return self._num_cols
   #end def get_num_cols
   
   def get_num_rows( self ):
      return self._num_rows
   #end def get_num_rows

