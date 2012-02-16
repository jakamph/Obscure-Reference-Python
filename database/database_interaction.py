## This is the interaction with the google spreadsheet that will
#  provide interaction with the "database"
#
# Author: Jason Kamphaugh
#
# Date: August 27, 2011
#


import gdata
import gdata.gauth
import atom
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet

_player_table_name = "Players"

class Database_Interaction:

   def __init__( self,
                 username,
                 password,
                 database_name = "Obscure Reference Database" ):
      """This is the initializer of the class that will create the connection
      to the database"""
      
      #get a handle to the spreadsheet client 
      self._client  = gdata.spreadsheet.service.SpreadsheetsService()
      
      #save the user name and password 
      self._client.email = username
      self._client.password = password

      #default the player table
      self._player_table = None
      
      #log in to the system 
      self._client.ProgrammaticLogin()

      #save the name of the database      
      self._database_name = database_name

      self._database_sheet = None

      #get the list of spreadsheets
      self._spreadsheet_list = self._client.GetSpreadsheetsFeed()
      self._key = -1
      
      #make sure we got a list
      if self._spreadsheet_list <> None:
          for sheet in self._spreadsheet_list.entry:
              
              if database_name == sheet.title.text:
                  
                  self._database_sheet = sheet
                  path_parts = sheet.id.text.split( '/' )
                  self._key = path_parts[len(path_parts) - 1]
              #end if database name matches

          #end loop through the database list

      #end if we got a spreadsheet list      

      if self._database_sheet == None:
         print( "Could not find the database." )
      #end if couldn't find the database
      
   #end init

   def Get_Table( self,
                  table_name ):
      """This method will retrieve the table (tab) with the given name"""

      #the variable to return
      worksheet_to_return = None

      #make sure we have a valid table name
      if None <> table_name:

         #retrieve the table from the spreadsheet
         self._worksheet_list = self._client.GetWorksheetsFeed(self._key)
         if self._worksheet_list <> None:
            _wksht_id = ''

            #loop through the possible worksheets
            for worksheet in self._worksheet_list.entry:

                 #if we've found a match for our title
                 if table_name == worksheet.title.text:
                     
                     path_parts = worksheet.id.text.split( '/' )
                     _wksht_id = path_parts[len(path_parts) - 1]

                     #set the variable to return
                     worksheet_to_return = worksheet
                     worksheet_to_return.key = _wksht_id

                  #end if database name matches

            #end loop through the database list
                     
            if _wksht_id == '':
               #print an error
               print( "No table named " + table_name + " found in database." )
            #no table match found

         #end if we got a spreadsheet list      
      
      #end if valid table_name

      return worksheet_to_return

   #end Get_Table

   def Reload_Players( self ):
      """This method will reload the player table"""
      
      #retrieve the player table
      self._player_table = self.Get_Table( _player_table_name )

      #get the feed 
      self._player_feed = \
         self._client.GetListFeed( self._key,
                                   self._player_table.key )
   #end Reload_Players

   def Get_Player_Line( self,
                        player_name ):
      """This method will retrive the specified player."""      

      #default the player line
      player_data = {}

      #make sure that we received a valid player name
      if self._player_table is None:

         self.Reload_Players()

      #end if no player table

      #check to make sure we now have a player table
      if self._player_table <> None:

         #loop through the players, looking for the specified player
         for index, player in enumerate( self._player_feed.entry ):

            #if we've found a match
            if player.title.text.upper() == player_name.upper():

               for key in player.custom:
                  player_data[key] = player.custom[key].text
               #end loop through the keys
               player_data["row_reference"] = player
               player_data["index"] = index
            #end if found a match
         #get the player line
                  

      #end if player table is not none
      else:
         print( "Could not retrieve player table" )
      #end if no player table

      return player_data

   #end Get_Player_Data

   def Get_Team_Table( self,
                       team_name ):
      """This method will retrieve the team of the specified name."""

      #near as I can tell, this is just a pass-through to get the table
      #with the team name.
      #We might want to beef this up so that it will pull all of the pertinent
      #data (players, salary, etc) in to a structure to be read outside of
      #this function.
      return self.Get_Table( team_name )

   #end Get_Team_Table



#end Database_Interaction   
