##
# This is the main file for the Obscure Reference application.
# It is in charge of setting up the environment and launching the main
# window.
#
# Author: Jason Kamphaugh
#
# Date: February 29, 2012
#

import os
import sys

_path_suffixes = [ "/third-party/gdata-2.0.16/src",
                   "/third-party/PyGUI-2.5.3/" ]

#get the current running directory
_base_directory = os.getcwd( )

_resource_directory = _base_directory + "obscure_reference/resources/"

_logo_file = _resource_directory + "obscure_reference_logo.png"

#add the third party directories
for suffix in _path_suffixes:

   sys.path.append( _base_directory + suffix )

#end loop through paths

#now we can import the important files
import obscure_reference.gui.credentials_dialog as credentials_dialog
import obscure_reference.database.database_parser as database_parser
import obscure_reference.common.string_definitions as string_definitions
import obscure_reference.common.number_constants as number_constants
import obscure_reference.reference_objects.player as player
import obscure_reference.reference_objects.manager as manager
import obscure_reference.gui.obscure_main_gui as obscure_main_gui
import obscure_reference.gui.player_frame as player_frame
import obscure_reference.gui.team_frame as team_frame
import obscure_reference.gui.team_dropdown as team_dropdown

#we need access to the BadAuthentication error
import gdata.service

import obscure_reference.application.main_application as main_application

from GUI import Frame
from GUI import ModalDialog
from GUI import Label 
from GUI import Button
from GUI import TextField
from GUI.StdButtons import DefaultButton
from GUI.StdButtons import CancelButton

#create the master class
class Obscure_Reference_Main( main_application.Main_Application ):

   def __init__( self ):

      #call the parent constructor
      main_application.Main_Application.__init__( self )

      self._close = False

      #default our database parser
      self._parser = None

      #default the list of players
      self._player_list = {}

      #default the manager
      self._current_manager = None

      self._manager_list = {}

      self._overall_team_frame = None
      
      self._dropdown_string_table = []

   #end __init__

   def _Determine_Team_Information( self ):
      """This method will retrieve the information from the database that's
      pertinent to the individual team that's running."""
      
      #retrieve the manager table
      self._manager_table = \
         self._parser.Get_Table(string_definitions.managers_table_name)
         
      #retrieve the teams feed
      self._manager_feed = \
         self._parser.Get_Feed(self._manager_table)
         
      #because we could log in with any variation of periods in the 
      #username field, we need to strip them out to make sure we get a 
      #good comparison
      filtered_user_name = self._username.replace( ".", "" )

      #create manager objects based on the information in the table
      for raw_manager in self._manager_feed.entry:
      
         #create the object
         current_manager = manager.Manager( raw_manager )
      
         #save the manager in the manager list based on the username
         self._manager_list[current_manager.Get_Username( )] = current_manager

         current_manager_name = \
            current_manager.Get_Username( ).replace( ".", "" )
         

         #check for a match with the provided username
         if filtered_user_name == current_manager_name:
            self._current_manager = current_manager
         #end if we have a match with the login username
      
      #end loop through manager
      
   #end _Determine_Team_Information

   def _Determine_Session_Information( self ):
      """This method will retrieve the information from the database that's
      pertinent to the session that is currently running."""
      
      #Get the table the contains the information
      self._session_table = \
         self._parser.Get_Table( string_definitions.session_table_name )
      
      #pull out the year field
      self._current_year = \
         self._parser.Get_Current_Year( self._session_table )
      
   #end _Determine_Session_Information

   def Get_Current_Year( self ):
      """This method will return the current season year."""

      return self._current_year

   #end Get_Current_Year

   def Get_Current_Team( self ):
      """This method will retrieve the team associated with the currently-
      logged in manager."""
      
      return self._current_team

   #end Get_Current_Team

   def Get_Current_Manager( self ):
      """This method will retrieve the manager associated with the currently-
      logged-in user."""
      return self._current_manager
   #end Get_Current_Manager

   def _Perform_Login( self ):
      """This method will attempt to log in to Google database."""

      _credentials =  credentials_dialog.Credentials_Dialog( )

      #show the dialog
      _credentials.present( )

      #loop until we get a successful login or the user has canceled
      while self._parser is None and not _credentials.Get_User_Canceled():

         try:
            #try to log in to the parser using the received credentials
            self._parser = database_parser.Database_Parser( \
                              _credentials.Get_User( ),
                              _credentials.Get_Password( ),
                              string_definitions.default_database_name )
         #end try to log in
         except (gdata.service.BadAuthentication, 
                 gdata.service.CaptchaRequired):
            #let the user know that there was a problem
            _credentials.Set_Message( "Login failed. Try again" )
         #end BadAuthentication

      #end loop until successful login/user canceled

      if self._parser <> None:
         #save the username 
         self._username = _credentials.Get_User( )

         if self._username.count("@") > 0:
         
            char_index = self._username.index( "@" ) 
         
            #the user name needs to be everything before the at
            self._username = self._username[0:char_index]
         
         #end if we have the at symbol
      
      #end if valid login

   #end _Perform_Login

   def Load_Player_Data( self ):
      """This method will load the latest player data to be used."""

      #check to make sure that we have a valid parser
      if self._parser <> None:
         #call in to the database to reload the players
         self._parser.Reload_Players( )

         #retrieve the list of players
         raw_player_list = self._parser.Get_Player_List( )

         #if we had a previous list
         if 0 <> len( self._player_list ):

            #delete the previous list
            del( self._player_list )

         #end if we have a previous player list

         self._player_list = {}

         #get the list of keys available for the player table
         self._player_keys = raw_player_list[0].custom.keys()

         #the statically-defined
         self._player_header_keys = ["Action", 
                                     "Name", 
                                     "Manager", 
                                     "Cap Hit" ]

         year_list = []
         
         #loop through the keys looking for salary information
         for key in self._player_keys:
            
            #if we've found a salary
            if key.count( string_definitions.salary_field_prefix ):
   
               #add this year to the year list
               year_list.append( \
                  key.replace( string_definitions.salary_field_prefix, 
                               "" ) )
   
            #end if we've found a salary
   
         #end loop through keys
   
         #put the year list in inverse order
         year_list.sort( reverse=True )
   
         #add the year list to the header keys
         self._player_header_keys += year_list 


         #loop through the player list creating the objects
         for current_player in raw_player_list:
            
            #pull out the player name to make this code not quite as ugly
            player_name = \
               current_player.custom[string_definitions.player_name_field].text

            this_player = \
               player.Player( raw_data = current_player,
                              receiver = self,
                              add_player_function = "Add_Player",
                              drop_player_function = "Drop_Player",
                              trade_player_function = "Trade_Player" )

            #add the new player to our list
            self._player_list[player_name] = this_player

            #retrieve the manager name
            manager_name = this_player.Get_Manager_Name()

            #determine if this player is on a team
            if manager_name <> None and manager_name <> "":

               #get the manager
               current_manager = self._manager_list[manager_name]
   
               #add this player to the manager's team
               current_manager.Add_Player( this_player )
               
            #end if player is on a team
         
         #end loop through players
      #end if valid parser

   #end Load_Player_Data

   #this method doesn't conform to naming standard because it is 
   #automatically called by the GUI framework
   def open_app(self):
      
      #perform the login
      self._Perform_Login( )

      #if we have a successful login, create the main GUI
      if self._parser <> None:

         #determine the team information
         self._Determine_Team_Information( )

         #figure out the important bits about our current session
         self._Determine_Session_Information( )

      #end if valid parser
      else:
         
         #note to self: we're closing
         self._close = True
         
         #exit out of the application
         self.Exit( ) 
      #couldn't log in

      #make sure that we didn't cancel out
      if self._close <> True:

         #create the main GUI
         self._main_gui = \
            obscure_main_gui.Obscure_Main_Gui( controller = self,
                                               logo_file = _logo_file )
         
         #display the main GUI
         self._main_gui.show( )

         #while we're here, let's grab the player data
         self.Load_Player_Data( )

      #end if user didn't cancel out

   #end open_app

   def _Create_Overall_Player_Frame( self ):
      """This method is used to create the overall player frame used when 
      displaying the players."""

      #retrieve the main frame from the GUI
      main_frame = self._main_gui.Get_Main_Frame()

      #create the overall player frame
      self._overall_player_frame = \
         Frame( container = main_frame,
                anchor = "ltrb",
                size = ( main_frame.width,
                         main_frame.height ) )

      #create the search button
      self._player_search_button = Button( "Player Search", 
                                           action = "Player_Search", 
                                           style = "default" )
      
      #put the button in the frame
      self._overall_player_frame.place( self._player_search_button,
                                        left = 0,
                                        top = 0 )
      
      #create the text box
      self._player_search_field = \
         TextField( width = number_constants.text_box_width )
         
      #put the field on the frame
      self._overall_player_frame.place( \
              self._player_search_field,
              left = self._player_search_button.right )

   #end _Create_Overall_Player_Frame

   def Players_Matching_String( self,
                                search_string ):
      """This method will look through the player list for any matching the 
      provided search string."""
      
      #shift the search string to lower case
      search_string = search_string.lower()
      
      player_list = {}
      
      #loop through the player list
      for current_player in self._player_list:
         
         #shift the player name to lower case
         lower_current_player = current_player.lower( )
         
         #if we have a match with the player
         if 0 < lower_current_player.count( search_string ):
            #add this player to the list
            player_list[current_player] = self._player_list[current_player]
         #end if we have a match
      #end loop through player list
      
      return player_list
      
   #end Players_Matching_String

   def Player_Search( self ):
      """This method will be invoked when the user clicks the player search
      button."""

      #retrieve the search string
      search_string = self._player_search_field.get_text( )

      #get the players matching the search string
      player_list = self.Players_Matching_String( search_string )
      
      #clear the existing player frame
      self._overall_player_frame.remove( self._player_frame )

      main_frame = self._main_gui.Get_Main_Frame( )
      
      #create a new player frame with the new list
      self._player_frame = \
         player_frame.Player_Frame( player_list = player_list,
                                    player_keys = self._player_header_keys,
                                    container = self._overall_player_frame,
                                    anchor = "ltrb",
                                    scrolling = "",
                                    size = (main_frame.width - 40, #TODO: Magic numbers need tweaked and defined
                                            (self._overall_player_frame.height - 
                                             self._player_search_button.height -
                                             number_constants.basic_pad - 
                                             number_constants.half_pad)))

      #put the overall player frame on the GUI
      self._overall_player_frame.place( \
              self._player_frame,
              sticky = "nsew", 
              top = (self._player_search_button.bottom + \
                     number_constants.half_pad))

      self._main_gui.Receive_New_Frame(self._overall_player_frame)

   #end Player_Search

   def Show_Players( self ):
      """This method will cause the list of players to be displayed."""


      self._Create_Overall_Player_Frame( )

      #retrieve the main frame from the GUI
      main_frame = self._main_gui.Get_Main_Frame()

      #create the player frame
      self._player_frame = \
         player_frame.Player_Frame( player_list = self._player_list,
                                    player_keys = self._player_header_keys,
                                    container = self._overall_player_frame,
                                    anchor = "ltrb",
                                    scrolling = "",
                                    size = (main_frame.width - 40, #TODO: Magic numbers need tweaked and defined
                                            (self._overall_player_frame.height - 
                                             self._player_search_button.height -
                                             number_constants.basic_pad - 
                                             number_constants.half_pad)))

      #put the overall player frame on the GUI
      self._overall_player_frame.place( \
              self._player_frame,
              sticky = "nsew", 
              top = (self._player_search_button.bottom + \
                     number_constants.half_pad))

      #give the new frame to the main GUI
      self._main_gui.Receive_New_Frame( self._overall_player_frame )

   #end Show_Players

   def Show_Transactions( self ):
      """This method will cause the list of pending transactions to be
      displayed."""
      
      None
      
   #end Show_Transactions

   def _Ask_User( self,
                  question ):
      """This method will ask the user if they're sure that they
      want to do what they've said they do. Basically, we're protecting
      them from themselves."""

      
      #create the confirm dialog
      confirm_dialog = ModalDialog( title = "Please Confirm" )
      
      confirm_dialog.place( Label(text = question ), 
                            left = 20, 
                            top = 20 )

      #create the buttons for OK/Cancel
      confirm_dialog.default_button = DefaultButton()
      confirm_dialog.cancel_button = CancelButton()

      #put the buttons on the GUI
      confirm_dialog.place( confirm_dialog.default_button, 
                            right = -20, 
                            bottom = -20 )
      confirm_dialog.place( confirm_dialog.cancel_button, 
                            left = 20, 
                            bottom = -20 )

      #center the dialog
      confirm_dialog.center( )
      
      #ask for confirmation to make sure that the user really wants to do
      #this
      confirm = confirm_dialog.present( )      
      
      return confirm
      
   #end _Ask_User

   def Add_Player( self,
                   player_to_add ):
      """This function will add the player to the current team."""
      
      if self._current_manager <> None:
         
         if self._Ask_User( "Are you sure that you want to\n add " + \
                            player_to_add.Get_Name( ) + \
                            "?" ):
         
            # Change the local data
            self._current_manager.Add_Player( player_to_add )
         
            #tell the player their new manager
            player_to_add.Set_Manager_Name( \
               self._current_manager.Get_Email( ) )
            try:
               #update the database
               self._parser.Set_Player_Line(player_to_add.Get_Raw_Data())

               #change the player information with the username
               #string instead of the whole email address
               player_to_add.Set_Manager_Name( \
                  string_definitions.Extract_Username( \
                     self._current_manager.Get_Email( ) ) )
            
               #update the GUI
               self.Show_Team( self._current_manager.Get_Username( ) )
            #end try
            except gdata.service.RequestError:
               #create a modal dialog to show
               error_dialog = ModalDialog(title = "Couldn't Add Player", 
                                          size = (400, 70))
               
               #create an information label
               error_dialog.place(Label(text = "Player has already " + \
                                               "been added by someone else"), 
                                  left = 20, 
                                  top = 20)
                                  
               #create the button
               error_dialog.default_button = DefaultButton()
               
               error_dialog.place(error_dialog.default_button, 
                                  right = -20, 
                                  bottom = -20)
   
               #start the reload of the players
               self.Load_Player_Data( )
   
               #show the dialog
               error_dialog.present()
               
               #re-show the player data
               self.Show_Players()
   
            #end except

         #end if user confirmed
            
      #end if
   #end Add_Player

   def Drop_Player( self,
                    player ):
      """This function will add the player to the current team."""

      confirm = self._Ask_User( "Are you sure that you want to \ndrop " + \
                                player.Get_Name( ) + \
                                "?" )
      #if the user was sure
      if confirm:

            
            # Change the local data
            self._current_manager.Drop_Player( player )
         
            #tell the player they no longer have a mananger
            player.Set_Manager_Name( "" )
            try:
               #update the database
               self._parser.Set_Player_Line(player.Get_Raw_Data())

               #update the GUI
               self.Show_Team( self._current_manager.Get_Username( ) )
            #end try
            except gdata.service.RequestError:
               #create a modal dialog to show
               error_dialog = ModalDialog(title = "Couldn't Drop Player", 
                                          size = (400, 70))
               
               #create an information label
               error_dialog.place(Label(text = "Error when trying to drop " + \
                                        "player." ), 
                                  left = 20, 
                                  top = 20)
                                  
               #create the button
               error_dialog.default_button = DefaultButton()
               
               error_dialog.place(error_dialog.default_button, 
                                  right = -20, 
                                  bottom = -20)
   
               #start the reload of the players
               self.Load_Player_Data( )
   
               #show the dialog
               error_dialog.present()
               
               #re-show the player data
               self.Show_Players()
   
            #end except
      
      #end if user wants to continue
         
   #end Drop_Player

   def Trade_Player( self,
                     player ):
      """This function will add the player to the current team."""
      None
   #end Trade_Player

   def Get_Current_Manager_Name( self ):
      """This method will retrieve the name of this instance's manager."""
      
      return self._current_manager.Get_Username( )
   
   #end Get_Current_Manager_Name

   def _Create_Overall_Team_Frame( self ):
      """This method will create the frame that contains the team frame."""
      
      #create the frame 
      self._overall_team_frame = \
         Frame( container = self._main_gui.Get_Main_Frame( ),
                anchor = "ltrb",
                size = ((self._main_gui.Get_Main_Frame_Width() - \
                         number_constants.basic_pad),
                        (self._main_gui.Get_Main_Frame_Height() - \
                         number_constants.basic_pad)))



      #create the drop-down
      self._team_dropdown = \
         team_dropdown.Team_Dropdown( manager_list = self._manager_list,
                                      receiver = self,
                                      receiver_function = "Show_Team",
                                      position = ( 0, 0 ),
                                      width = self._overall_team_frame.width )
      
      #add the drop down to the overall frame
      self._overall_team_frame.add( self._team_dropdown )
      
   #end _Create_Overall_Team_Frame

   def Show_Team( self,
                  manager_name,
                  internal_switch = False ):
      """This method will show the team based on the name of the team's 
      manager."""

      if None == self._overall_team_frame:
         self._Create_Overall_Team_Frame( )
      #end if team frame didn't exist before
      else:
         #remove the existing team frame from the overall team frame
         self._overall_team_frame.remove( self._team_frame )
      #end if the team frame did exist before

      display_manager = self._manager_list[manager_name]

      #if this is a switch triggered by the program
      #if internal_switch:
      #   self._team_dropdown.Set_Value(  )
      #end if internal switch

      #create this team's frame      
      self._team_frame = \
         team_frame.Team_Frame( display_team = display_manager.Get_Team(),
                                player_keys = self._player_header_keys,
                                container = self._overall_team_frame,
                                anchor = "ltrb",
                                size = (self._overall_team_frame.width,
                                        (self._overall_team_frame.height - \
                                         self._team_dropdown.height - \
                                         number_constants.basic_pad) ) ) 

      #add the team frame to the overall team frame
      self._overall_team_frame.place( self._team_frame,
                                      sticky = "nsew", 
                                      left = 0,
                                      top = (self._team_dropdown.height + \
                                             number_constants.basic_pad) )

      #give the new frame to the main GUI
      self._main_gui.Receive_New_Frame(self._overall_team_frame)

   #end Show_Team

#end Obscure_Reference_Main

#create the instance of the class to be run
main_obscure = Obscure_Reference_Main( )

#run the sucker
main_obscure.run( )
