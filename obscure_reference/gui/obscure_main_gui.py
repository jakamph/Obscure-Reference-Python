##
# This file is the main GUI of the system. Through user actions, the 
# main frame will be replaced by new information to be displayed.
#
# Author: Jason Kamphaugh
#
# Date: March 8, 2012
#

from GUI import Window
from GUI import Frame
from GUI import Label

class Obscure_Main_Gui( Window ):

   def __init__( self,
                 controller,
                 **kwds ):
      """This method is the constructor for the class."""
      
      #call the parent constructor
      Window.__init__( self, size = ( 600, 400 ) )

      #set the title
      self.set_title( "Obscure Reference" )

      #center ourselves
      self.center( )

      #save the controller
      self._controller = controller

      #create the navigation frame
      self._nav_frame = Frame( width = 300 ) 

      self._nav_frame.place_column([Label("This is"),
                                    Label(" the nav "),
                                    Label("frame")],
                                   left = 0, top = 0)

      self._nav_frame.shrink_wrap( padding = (30, 30))


      self.place( self._nav_frame, left = 20, top = 20 )

      #create the main frame
      self._main_frame = Frame( )
      
      self._sub_frame = Frame( )
      self._sub_frame.place_column( [Label("This is"),
                                     Label("the sub"),
                                     Label("frame.")],
                                   left = 0, top = 0)
      self._main_frame.place( self._sub_frame )
      

      self.place( self._main_frame, left = self._nav_frame.right, top = 20 )

      #self.shrink_wrap( padding = (20, 20) )

   #end __init

   def Receive_New_Frame( self,
                          new_frame ):
      """This method is used to receive a new frame to be displayed in the
      main frame area."""
      
      #put the new frame in the main frame area
      self._main_frame.place( new_frame )
      
   #end Receive_New_Frame

#end class Obscure_Main_Gui