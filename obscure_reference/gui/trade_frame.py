##
#Created on September 26, 2012
#
#@author: Jason Kamphaugh
#

from GUI import Frame

import obscure_reference.reference_objects.player as player
import obscure_reference.reference_objects.team as team
import obscure_reference.reference_objects.transaction as transaction

class Trade_Frame( Frame ):
   """This class is used to set up a trade between two different teams."""
   
   def __init__( self,
                 offering_team,
                 receiving_team,
                 initial_player = None,
                 **kwds ):
      """This is the constructor for the trade frame."""

      self._offering_team = offering_team
      self._receiving_team = receiving_team
      
      #create defaulted list of players being offered or received
      self._offering_players = {}
      self._receiving_players = {}
      
      #call the parent constructor
      Frame.__init__( self, **kwds )
      
      #if we were given an initial player to be involved in the trade
      if None <> initial_player:
      
         #add this player to the list of receiving players
         self._receiving_players[initial_player.Get_Name( )] = \
            initial_player
      
      #end if we have an initial player
      
      #TODO: Loop throught the players on each team and place them in the
      #sub-frames for the teams.
      
   #end __init__
   
   def draw( self, canvas, rect ):
      """Cause the frame to re-draw the important area."""
      canvas.erase_rect( rect )
   #end draw
