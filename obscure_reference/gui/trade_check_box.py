##
#Created on September 26, 2012
#
#@author: Jason Kamphaugh
#

from GUI import CheckBox

import obscure_reference.reference_objects.player as player

class Trade_Check_Box( CheckBox ):
   """This class is used to be the GUI of a player for a trade."""
   
   def __init__( self,
                 player,
                 callback,
                 **kwds ):
   
      #save the player
      self._player = player
   
      #save the callback
      self._callback = callback
   
      CheckBox.__init__( self,
                         title = self._player.Get_Name( ),
                         action = self._Toggled,
                         kwds )
   
   #end __init__
   
   def Get_Title( self ):
      """This method will return the title that was given to this object at
      initialization."""
      
      return self.title

   #end Get_Title

   def Get_State( self ):
      """This method will return the current state of the check box. True if
      checked. False otherwise."""
   
      return self.value
   
   #end Get_State

   def _Toggled( self ):
      """This method is provided to the parent class to be called when 
      this check box is toggled."""
   
      #invoke the callback
      self._callback( self )
   
   #end _Toggled
#end Trade_Check_Box