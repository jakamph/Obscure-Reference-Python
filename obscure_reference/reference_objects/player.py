##
# This file contains the information for an individual player
#
# Author: Jason Kamphaugh
#
# Date: March 1, 2012
#

import obscure_reference.reference_objects.reference_object as reference_object
import obscure_reference.common.string_definitions as string_definitions

class Player( reference_object.Reference_Object ):

   def __init__( self,
                 raw_data ):
      """This is the constructor for the Player object."""

      #pull the data out and store it locally
      self._raw_data = raw_data
      
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

   #end __init__

   def Get_Raw_Data( self ):
      """This method will retrieve the raw data that was used to
      initialize this player object."""

      return self._raw_data

   #end Get_Raw_Data

   def Fill_Data( self,
                  gui_object ):
      """This method will fill the player data in to the provided GUI object
      to be displayed."""

      #give the row back to the caller
      return gui_object

   #end Fill_Data

#end class Player