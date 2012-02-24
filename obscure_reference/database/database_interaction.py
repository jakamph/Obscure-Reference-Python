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


import obscure_reference.common.string_definitions as string_definitions

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
                  self._full_key = sheet.id.text

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
                     worksheet_to_return._key = _wksht_id

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
                 feed,
                 key_string,
                 value,
                 start_position = 0,
                 end_position = "end",
                 check_upper = True,
                 check_lower = True ):
      """This method will search through the specified worksheet for the 
      specified key."""

      found_line = None

      new_start = start_position
      new_end   = end_position

      #if we had the default end position
      if end_position is "end":

         end_position = len( feed.entry ) - 1

      #end if default end position

      #if we're supposed to check the upper limit
      if check_upper:
         if value.upper() == feed.entry[start_position].\
                                custom[key_string].text.upper():
            found_line = feed.entry[start_position]
         #end if match of upper
      #end if check upper 

      #if we're supposed to check the upper limit
      if check_lower:
         if value.upper() == feed.entry[end_position].\
                                custom[key_string].text.upper():
            found_line = feed.entry[end_position]
         #end if match of lower
      #end if check lower

      #find the mid-point
      mid_point = int( (start_position + end_position) / 2 )

      current_name = feed.entry[mid_point].\
                             custom[key_string].text.upper()

      #check the mid-point
      if value.upper() == feed.entry[mid_point].\
                              custom[key_string].text.upper():
         found_line = feed.entry[mid_point]
      #end if match of lower

      check_upper = False
      check_lower = False
      current_name = feed.entry[mid_point].\
                             custom[key_string].text.upper()

      #if we still haven't found a match and we have more than 2 things
      if found_line is None and (end_position - start_position > 1):
         if value.upper() < feed.entry[mid_point].\
                             custom[key_string].text.upper():
            #make the mid_point the new end
            new_end = mid_point
         #end if searched for value is less than the current mid_point
         else:

            #make the mid_point the new start
            new_start = mid_point
         #is searched for value is greater than the current mid_point

         #recursion makes me nervous
         found_line = self.Get_Line( feed           = feed,
                                     key_string     = key_string,
                                     value          = value,
                                     start_position = new_start,
                                     end_position   = new_end,
                                     check_upper    = False,
                                     check_lower    = False )

      #end if no match yet

      return found_line

   #end Get_Line

   def Set_Line( self,
                 line_item,
                 new_data ):
      """This method is used to update the specified index in the feed
      with the specfied data."""

      successful_set = self._client.UpdateRow( line_item,
                                               new_data )

      if None == successful_set:
         print( "Wasn't able to set the specified data." )
      #end if not a successful set
                 
   # end Set_Line

   def Insert_Line( self,
                    data,
                    worksheet_key ):
      """This method is used to add a new line to the specified worksheet."""

      #send the row to the spreadsheet
      self._client.InsertRow( data, self._key, worksheet_key )

   #end Insert_Line

   def Delete_Line( self,
                    line_item ):
      """This method will delete the specified line from the worksheed."""

      #send the command to remove the line
      self._client.DeleteRow( line_item )


   #end Delete_Line

   def Get_Feed( self,
                 table ):
      """This method will retrieve the feed of the specified table."""

      return self._client.GetListFeed( self._key,
                                       table._key )

   #end Get_Feed

#end Database_Interaction   
