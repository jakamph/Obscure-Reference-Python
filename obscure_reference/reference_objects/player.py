##
# This file contains the information for an individual player
#
# Author: Jason Kamphaugh
#
# Date: March 1, 2012
#

import obscure_reference.reference_objects.reference_object as reference_object
import obscure_reference.common.string_definitions as string_definitions

import obscure_reference.gui.player_button as player_button

from GUI import Label

class Player( reference_object.Reference_Object ):

   def __init__( self,
                 raw_data,
                 receiver,
                 add_player_function,
                 drop_player_function,
                 trade_player_function,
                 current_team ):
      """This is the constructor for the Player object."""

      #pull the data out and store it locally
      self._raw_data = raw_data
      
      self._current_team = current_team
      
      #get the name
      self._name = raw_data.custom[string_definitions.player_name_field].text
      
      #get the team
      self._team = raw_data.custom[string_definitions.player_team].text
      
      #get the draft year for this player
      self._draft_year = \
         raw_data.custom[string_definitions.player_draft_year].text

      #get the list of keys
      keys = raw_data.custom.keys( )
      
      #default the list of salary information
      self._salary_table = {}
      
      #loop through the keys looking for salary information
      for key in keys:
         
         #if we've found a salary
         if key.count( string_definitions.salary_field_prefix ):
            
            
            new_key = key.replace( string_definitions.salary_field_prefix, 
                                   "" )
            
            #save the salary information in to the table
            self._salary_table[new_key] = raw_data.custom[key].text

         #end if we've found a salary

      #end loop through keys

      #save the receiver
      self._receiver = receiver

      #save the functions
      self._add_player_function = add_player_function
      self._drop_player_function = drop_player_function
      self._trade_player_function = trade_player_function

   #end __init__

   def Get_Raw_Data( self ):
      """This method will retrieve the raw data that was used to
      initialize this player object."""

      return self._raw_data

   #end Get_Raw_Data

   def _Create_Button( self ):
      """This method will create the button for display on the player list."""

      button = None

      width = 20

      #determine if this player is part of the current user's team
      if self._team == None:
         #this player is not on a team, so provide an add button
         button = \
            player_button.Player_Button( \
               title = "Add Player",
               parent = self._receiver,
               player = self,
               clicked_callback = self._add_player_function,
               width = width )

      #end not on a team
      elif self._team == self._current_team:
         #this player is on the current team, so provide a drop
         button = player_button.Player_Button( \
                     title = "Drop Player",
                     parent = self._receiver,
                     player = self,
                     clicked_callback = self._drop_player_function,
                     width = width )

      #end on the current team
      else:
         #this player is on someone else's team, so provide a trade
         button = player_button.Player_Button( \
                     title = "Trade",
                     parent = self._receiver,
                     player = self,
                     clicked_callback = self._trade_player_function,
                     width = width )

      #end on a different team

      return button

   #end _Create_Button

   def Fill_Data( self,
                  gui_object ):
      """This method will fill the player data in to the provided GUI object
      to be displayed."""

      #Call to create the button
      #self._button = self._Create_Button( gui_object )
      self._button = self._Create_Button()
      gui_object.append( Label( self._name ) )
      
      #loop through the years and add the salary information
      for year in self._salary_table:
         gui_object.append( Label( self._salary_table[year]))
      #end loop through the years

      #give the row back to the caller
      return gui_object

   #end Fill_Data

#end class Player