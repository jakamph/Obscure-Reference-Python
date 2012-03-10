##
# This file contains the class for displaying the player information to
# the user.
#
# Author: Jason Kamphaugh
#
# Date: March 9, 2012
#


from GUI import Frame

import obscure_reference.reference_objects.player

class Player_Frame( Frame ):
   def __init__( self,
                 player_list ):
      """This method is the constructor for the object."""
      
      #call the parent constructor
      Frame.__init__( self )
   #end __init__

   def _Create_Header_Label( self ):
      """This method will create the header label to be used at the
      top of the display of player information."""

#end class Player_Frame