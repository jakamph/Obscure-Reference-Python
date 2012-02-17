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


import string_definitions

class Database_Interaction:

   def __init__( self,
                 username,
                 password,
                 database_name ):
      """This is the initializer of the class that will create the connection
      to the database"""
      
      #get a handle to the spreadsheet client 
      self._client  = gdata.spreadsheet.service.SpreadsheetsService()
      
      #save the user name and password 
      self._client.email = username
      self._client.password = password
      
      #log in to the system 
      self._client.ProgrammaticLogin()

      #save the name of the database      
      self._database_name = database_name

      self._database_sheet = None

      #get the list of spreadsheets
      self._spreadsheet_list = self._client.GetSpreadsheetsFeed()
      self._key = -1

      #create an empty list of the tables.
      self._table_list = {}
      
      #make sure we got a list
      if self._spreadsheet_list <> None:
          for sheet in self._spreadsheet_list.entry:
              
              if database_name == sheet.title.text:
                  
                  self._database_sheet = sheet
                  path_parts = sheet.id.text.split( '/' )
                  self._key = path_parts[len(path_parts) - 1]

                  #we found a match. break out of the loop
                  break
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

                     #save this reference
                     self._table_list[table_name] = worksheet_to_return

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

   def Get_Line( self,
                 worksheet_id,
                 key ):
      """This method will search through the specified worksheet for the 
      specified key."""

      None
   #end Get_Line

   def Set_Line( self,
                 worksheet_feed,
                 index,
                 new_data ):
      """This method is used to update the specified index in the feed
      with the specfied data."""

      successful_set = self._client.UpdateRow( worksheet_feed.entry[index],
                                               new_data )

      if None == successful_set:
         print( "Wasn't able to set the specified data." )
      #end if not a successful set
                 
   # end Set_Line

#end Database_Interaction   
