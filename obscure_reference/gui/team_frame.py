##
#Created on Apr 6, 2012
#
#@author: Jason Kamphaugh
#

from GUI import Frame
from GUI import Label
from GUI import ListButton

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
      
      self._display_team = display_team
      
      #pull out the list of players
      self._player_list = display_team.Get_Player_List( )

      #create the frame to contain the manager information
      self._manager_frame = self._Create_Manager_Frame( )

      self.place( self._manager_frame )

      #the player frame will be the bottom two thirds of the team frame
      self._player_frame = \
         player_frame.Player_Frame( self._player_list,
                                    player_keys,
                                    container = self,
                                    top = self._manager_frame.height,
                                    anchor = "ltrb",
                                    scrolling = "hv",
                                    height = (self.height * 2 / 3),
                                    width = self.width,
                                    extent = (750, 500) ) # TODO programatically determine what the scrolling extent needs to be. 

   #end __init__

   def _Create_Manager_Frame( self ):
      """This method will create the frame to display the manager's info."""

      #create the containing frame which will be the top third of the 
      #current area
      man_frame = Frame( container = self,
                         top = 0,
                         height = (self.height / 3),
                         width = self.width )
      
      #create a label for the manager name
      self._manager_label = \
         Label( "Manager: " + \
                self._display_team.Get_Manager().Get_Manager_Name() )
         
      self._team_name_label = \
         Label( "Team Name: " + self._display_team.Get_Team_Name( ) )
         
      self._salary_label = \
         Label( "Current Salary: " + `self._display_team.Get_Team_Salary( )` )

      man_frame.place_column( [self._manager_label,
                               self._team_name_label,
                               self._salary_label],
                              left = 0,
                              top = 0 )

      return man_frame

   #end _Create_Manager_Frame


   def draw( self, canvas, rect ):
      """Cause the frame to re-draw the important area."""
      canvas.erase_rect( rect )
   #end draw

#end Team_Frame