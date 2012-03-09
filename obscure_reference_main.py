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

#we need access to the BadAuthentication error
import gdata.service

import obscure_reference.application.main_application as main_application

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

   def _Perform_Login( self ):
      """This method will attempt to log in to Google database."""

      _credentials =  credentials_dialog.Credentials_Dialog( )

      #show the dialog
      _credentials.present( )

      if _credentials.Get_User_Canceled():
         print( "User canceled.")
      

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

         #loop through the player list creating the objects
         for current_player in raw_player_list:
            
            #pull out the player name to make this code not quite as ugly
            player_name = \
               current_player.custom[string_definitions.player_name_field].text

            #add the new player to our list
            self._player_list[player_name] = \
               player.Player( current_player )
         #end loop through players
      #end if valid parser

   #end Load_Player_Data

   #this method doesn't conform to naming standard because it is 
   #automatically called by the GUI framework
   def open_app( self ):

      #perform the login
      self._Perform_Login( )

      #if we have a successful login, create the main GUI
      if self._parser <> None:

         #open the Main Window
         None

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
            obscure_main_gui.Obscure_Main_Gui( controller = self )
         
         #display the main GUI
         self._main_gui.show( )

         #while we're here, let's grab the player data
         self.Load_Player_Data( )

      #end if user didn't cancel out

   #end open_app

#end Obscure_Reference_Main

#create the instance of the class to be run
main_obscure = Obscure_Reference_Main( )

#run the sucker
main_obscure.run( )
