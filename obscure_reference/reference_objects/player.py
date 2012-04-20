##
# This file contains the information for an individual player
#
# Author: Jason Kamphaugh
#
# Date: March 1, 2012
#

import obscure_reference.reference_objects.reference_object as reference_object
import obscure_reference.common.string_definitions as string_definitions
import obscure_reference.common.number_constants as number_constants

import obscure_reference.gui.player_button as player_button

import obscure_reference.application.main_application as main_application

from GUI import Label

class Player( reference_object.Reference_Object ):

   def __init__( self,
                 raw_data,
                 receiver,
                 add_player_function,
                 drop_player_function,
                 trade_player_function ):
      """This is the constructor for the Player object."""

      #pull the data out and store it locally
      self._raw_data = raw_data
      
      #get the name
      self._name = raw_data.custom[string_definitions.player_name_field].text
      
      #get the manager that is the controller of the team of this player
      self._manager = raw_data.custom[string_definitions.player_manager].text
      
      self._manager_string = self._manager
      
      #if the manager is empty
      if None == self._manager_string:
         self._manager_string = ""
      #end if manager is empty
      else:
         self._manager_string = \
            string_definitions.Extract_Username( self._manager )

      #end if manager string is valid
      
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

            #if it's a zero salary
            if "0" == self._salary_table[new_key]:
               self._salary_table[new_key] = "1"
            #end if it's a zero salary

         #end if we've found a salary

      #end loop through keys

      #save the receiver
      self._receiver = receiver
      
      #use the receiver to pull out the current year
      self._current_year = self._receiver.Get_Current_Year( )

      #use the receiver to pull out the current manager 
      self._current_manager = self._receiver.Get_Current_Manager( )

      self._on_disabled_list = False #TODO add the information to the spreadsheet to determine if this player is on the DL

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

      width = number_constants.action_button_width

      #determine if this player is part of the current user's team
      if self._manager_string == None or self._manager_string == "":
         #this player is not on a team, so provide an add button
         button = \
            player_button.Player_Button( \
               title = "Add Player",
               parent = self._receiver,
               player = self,
               clicked_callback = self._add_player_function,
               width = width )

      #end not on a team
      elif self._manager_string == self._current_manager.Get_Username():
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
      self._button = self._Create_Button()
      
      #add the button to the GUI
      gui_object.append( self._button )
      
      #add my name 
      gui_object.append( Label( self._name ) )

      #add the manager
      gui_object.append( Label( self._manager_string ) )
      
      #fill the current salary
      gui_object.append( Label( str( self.Get_Current_Salary( ) ) ) )

      year_key_list = self._salary_table.keys( )

      #have the salary table be in inverse order (current to past)
      year_key_list.sort( reverse = True )
      
      #loop through the years and add the salary information
      for year in year_key_list:
         gui_object.append( Label( str( self._salary_table[year] ) ) )
      #end loop through the years

      #give the row back to the caller
      return gui_object

   #end Fill_Data

   def Get_Salary( self,
                   year = None ):
      """This method will retrieve the salary of the player based on the
      provided year."""

      # default to an invalid salary
      salary = number_constants.invalid_salary

      internal_year = year
      
      #if we weren't given a year
      if None == internal_year:
         
         #use the current league year
         internal_year = self._current_year
      
      #end if we weren't given a year

      #check if the provided year is part of the list
      if str( internal_year ) in self._salary_table:
         salary = int(self._salary_table[str(internal_year)])
      #end if the key exists in the salary table
   
      return salary

   #end Get_Salary

   def Get_Current_Salary( self ):
      """This method will retrieve the player's salary for the given league
      season."""

      #retrieve the salary for the draft year
      salary = int( self.Get_Salary( self._draft_year ))
      
      #number of years between the draft year and current year
      contract_years = 0
      
      if None <> self._draft_year:
         contract_years = \
            int( self._receiver.Get_Current_Year( ) ) - int( self._draft_year )
      
      #do the math
      salary = salary + (contract_years * number_constants.raise_per_year)

      return salary

   # end Get_Current_Salary

   def Get_Name( self ):
      """This method will retrieve the name of the player."""
      
      return self._name
   
   #end Get_Name

   def On_Disabled_List( self ):
      """This method will retrieve the disabled list state of the palyer."""
      
      return self._on_disabled_list
   
   #end On_Disabled_List

   def Get_Manager_Name( self ):
      """This method will retrieve the name of the team on which this 
      player appears."""
      
      return self._manager_string

   #end Get_Manager_Name

   def Set_Manager_Name( self, manager_name ):
      """This method will change the name of the team on which this player
      appears."""
      
      # Change this locally
      self._manager_string = manager_name
   
      self._raw_data.custom[string_definitions.player_manager].text =\
         manager_name      
   
   #end Set_Manager_Name
#end class Player