##
# This file is the common definitions to be used in many files.
#
# Author: Jason Kamphaugh
#
# Date: February 16, 2012
#

#player table definitions
player_table_name = "players"
player_name_field = "name"
player_draft_year = "draftyear"
player_team = "team"
player_manager = "manager"
salary_field_prefix = "salary"

player_row_reference = "row_reference"
player_index = "index"

added_player_data = [player_index, player_row_reference]

#manager table definitions
managers_table_name = "managerlist"
manager_login_name = "manager"
manager_name = "fullname"
team_tab = "tabkey"
full_name = "fullname"
team_name = "teamname"


#session table definitions
session_table_name = "session"
season_year_field = "seasonyear"

default_database_name = "Obscure Reference Database Test"

def Extract_Username( manager_email ):
   """This method will return the username portion of the provided email
   address."""

   username = None
   
   #if we have a valid email string
   if ( (None <> manager_email) and ("" <> manager_email) ):
      
      char_index = manager_email.index("@")

      #pull out the username of the manager
      username = manager_email[0:char_index]

   #end if valid string passed in
   
   return username

#end string_definitions

