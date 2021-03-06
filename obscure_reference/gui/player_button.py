##
# This file contains the definition of the Player_Button class.
#
# Author: Jason Kamphaugh
#
# Date: March 14, 2012
#

from GUI import Button

class Player_Button( Button ):

   def __init__( self,
                 title,
                 parent,
                 player,
                 clicked_callback,
                 width,
                 **kwds ):
      """This method is the constructor of the class."""

      internal_action = "Player_Button_Clicked"

      #call the parent constructor
      Button.__init__( self,
                       title = title,
                       width = width,
                       action = internal_action,
                       **kwds )

      #save the needed variables
      self._parent = parent
      self._player = player
      self._callback = clicked_callback

   #end init

   def Player_Button_Clicked( self ):
      """This method will capture the event of this button being clicked. It
      will pass that information along to the parent."""

      #pass the information along to the parent
      exec( "self._parent." + self._callback + "( self._player )" ) 

#end class Player_Button