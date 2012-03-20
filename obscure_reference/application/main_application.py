##
# This file contains the parent class for a main application to be 
# running in the project.
#
# Author: Jason Kamphaugh
#
# Date: February 29, 2012
#

from GUI import Application

class Main_Application( Application ):

   def __init__( self ):
      """This is the constructor for the object."""

      #call the parent constructor
      Application.__init__( self )

   #end __init__

   def open_app( self ):
      #this method intentionally left blank.
      None
   #end open_app

   def Show_Players(self):
      """This method will cause the list of players to be shown. It should
      be overridden by the sub class."""
      None
   #end Show_Players

   def Show_Transactions(self):
      """This method will cause the list of transactions to be shown. It
      should be overridden by the sub class."""
      None
   #end Show_Transactions

   def Get_Current_Year(self):
      """This method will return the current year for any caller. It will
      be overridden by the child class."""
      None
   #end Get_Current_Year
   
   def Get_Current_Team(self):
      """This method will return the current team for any caller. It will
      be overridden by the child class."""
      None

   def Exit( self ):
      """This method will be used when it's time to close the application."""
      #call the parent quit command
      self.quit_cmd()
   #end Exit

#end Main_Application
