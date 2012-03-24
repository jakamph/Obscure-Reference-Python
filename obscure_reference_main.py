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
import obscure_reference.reference_objects.player as player
import obscure_reference.gui.obscure_main_gui as obscure_main_gui
import obscure_reference.gui.player_frame as player_frame

#we need access to the BadAuthentication error
import gdata.service

import obscure_reference.application.main_application as main_application

from GUI import Frame
from GUI import ModalDialog
from GUI import Label 

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

   #end __init__

   def _Determine_Session_Information( self ):
      """This method will retrieve the information from the database that's
      pertinent to the session that is currently running."""
      
      #Get the table the contains the information
      self._session_table = \
         self._parser.Get_Table(string_definitions.session_table_name)
      
      #pull out the year field
      self._current_year = \
         self._parser.Get_Current_Year( self._session_table )


      # TODO: Load the team information and determine what the name of 
      # the team for this player is.
      self._current_team = "myteam"
      
   #end _Determine_Session_Information

   def Get_Current_Year( self ):
      """This method will return the current season year."""

      return self._current_year

   #end Get_Current_Year

   def Get_Current_Team( self ):
      """This method will retrieve the team associated with the currently-
      logged in manager."""
      
      return self._current_team

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

         #loop through the player list creating the objects
         for current_player in raw_player_list:
            
            #pull out the player name to make this code not quite as ugly
            player_name = \
               current_player.custom[string_definitions.player_name_field].text

            #add the new player to our list
            self._player_list[player_name] = \
               player.Player( raw_data = current_player,
                              receiver = self,
                              add_player_function = "Add_Player",
                              drop_player_function = "Drop_Player",
                              trade_player_function = "Trade_Player" )
         #end loop through players
      #end if valid parser

   #end Load_Player_Data

   def Get_Player_Frame( self ):
      """This method will retrieve the player list frame."""
      
      player_frame = Frame( )
      
      return player_frame
   #end Get_Player_Frame

   #this method doesn't conform to naming standard because it is 
   #automatically called by the GUI framework
   def open_app( self ):

      #perform the login
      self._Perform_Login( )

      #if we have a successful login, create the main GUI
      if self._parser <> None:

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

   def Show_Players( self ):
      """This method will cause the list of players to be displayed."""
      
      #get the latest player list
      #self.Load_Player_Data( )
      
      #create the player frame
      self._player_frame = \
         player_frame.Player_Frame( player_list = self._player_list,
                                    player_keys = self._player_keys,
                                    container = self._main_gui._main_frame,
                                    anchor = "ltrb",
                                    scrolling = "hv",
                                    # TODO: Why does setting the size here stop
                                    # this from scrolling?
                                    size = (self._main_gui._main_frame.width - 40, #TODO: Magic numbers need tweaked and defined
                                    self._main_gui._main_frame.height - 40))
      
      #give the new frame to the main GUI
      self._main_gui.Receive_New_Frame( self._player_frame )

   #end Show_Players

   def Show_Transactions( self ):
      """This method will cause the list of pending transactions to be
      displayed."""
      
      None
      
   #end Show_Transactions

   def Add_Player( self,
                   player ):
      """This function will add the player to the current team."""
      None
   #end Add_Player

   def Drop_Player( self,
                    player ):
      """This function will add the player to the current team."""
      
      #create the confirm dialog
      confirm_dialog = ModalDialog( title = "Please Confirm" )
      
      confirm_dialog.place( Label(text = "Do you really want to drop" +\
                                         player.Get_Name( ) + "?" ), 
                            left = 20, top = 20 )

      

      #center the dialog
      confirm_dialog.center( )
      
      #ask for confirmation to make sure that the user really wants to do
      #this
      confirm = confirm_dialog.present( )
      
      if confirm:
         None
      #end if user wants to continue
      else:
         None
      #end if user does not want to continue
         
   #end Drop_Player

   def Trade_Player( self,
                     player ):
      """This function will add the player to the current team."""
      None
   #end Trade_Player

#end Obscure_Reference_Main

#create the instance of the class to be run
main_obscure = Obscure_Reference_Main( )

#run the sucker
main_obscure.run( )
