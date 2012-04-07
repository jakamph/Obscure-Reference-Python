##
#Created on Apr 6, 2012
#
#@author: Jason Kamphaugh
#

from GUI import Frame

import obscure_reference.reference_objects.team as team
import obscure_reference.gui.player_frame as player_frame

class Team_Frame( Frame ):
   
   def __init__( self,
                 display_team,
                 player_keys,
                 **kwds ):
      """This is the constructor for the team frame."""
      ##
      # @param display_team: The object containing the team to be displayed's
      #                      information.
      #  
      # @param receiver: The object to receive the function calls.
      # 
      # @param function_to_call: The action function to invoke in the 
      #                          receiver when it's time to do something. Since
      #                          this is displaying the contents of a single
      #                          team, the action that needs to be invoked is
      #                          the same for each team.
      # 
      # @param kwds: List of common arguments to pass in to the parent class.
      # 
      
      
      #call the parent init
      Frame.__init__( self, **kwds )
      
      #pull out the list of players
      self._player_list = display_team.Get_Player_List( )

      #create the frame to contain the manager information
      #self._manager_frame = self._Create_Manager_Frame( )

      self._player_frame = player_frame.Player_Frame( self._player_list,
                                                      player_keys,
                                                      container = self,
                                                      anchor = "ltrb",
                                                      scrolling = "hv",
                                                      height = self.height - 50,
                                                      width = self.width,
                                                      extent = (750, 500) ) # TODO programatically determine what the scrolling extent needs to be. 

   #end __init__

   def _Create_Manager_Frame( self ):
      """This method will create the frame to display the manager's info."""

      return None

   #end _Create_Manager_Frame

#end Team_Frame