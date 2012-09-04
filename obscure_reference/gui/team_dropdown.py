##
# This file contains the definition of the drop down for selecting which
# team to be displayed
#
# Author: Jason Kamphaugh
#
# Date April 14, 2012
#

from GUI import ListButton

class Team_Dropdown( ListButton ):
   
   def __init__( self,
                 manager_list,
                 receiver,
                 receiver_function,
                 **kwds ):
      
      #save the manager list
      self._manager_list = manager_list
      
      #get the list of names
      self._key_list = manager_list.keys()
      
      #order the list
      self._key_list.sort( )

      self._dropdown_string_list = []
      
      self._receiver = receiver
      self._receiver_function = receiver_function
      
      index = 0
      
      #loop through the player names
      for manager_name in self._key_list:
         
         current_manager = manager_list[manager_name]
         
         self._dropdown_string_list.append( \
            manager_name + "(" + current_manager.Get_Team_Name( ) + ")" )
   
         #move the index up by 1   
         index += 1
   
      #end loop through the player names
   
      #now that we have everything ready call the parent constructor   
      ListButton.__init__( self, 
                           titles = self._dropdown_string_list,
                           values = range( 0, (len(self._manager_list)) ),
                           action = self.Value_Change,
                           **kwds )

   #end __init__

   def Set_Value( self,
                  value ):
      """This method will change the value of the enumeration to the speicified
      value."""
      
      self.value = value
      
   #end Set_Value

   def Value_Change( self,
                     internal_switch = False ):
      """This method is provided to the parent to be called when there is a 
      change to the list."""

      #get the current value of the button
      value = self.value

      #retrieve the pertinent manager
      manager = self._manager_list[self._key_list[value]]

      #if this wasn't a switch based on a programatic action as opposed
      #to a user action
      if not internal_switch:

         #call the receiver
         exec( "self._receiver." + \
               self._receiver_function + \
               "( manager_name = '" + \
               str( manager.Get_Username( ) ) + \
               "' )" )

      #end if not an internal action

   #end Value_Change
   
#end Team_Dropdown