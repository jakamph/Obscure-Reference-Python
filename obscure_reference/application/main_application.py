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

      #call the parent contructor
      Application.__init__( self )

   #end __init__

   def open_app( self ):
      #this method intentionally left blank.
      None
   #end open_app

   def Exit( self ):
      """This method will be used when it's time to close the application."""
      #call the parent quit command
      self.quit_cmd()
   #end Exit

#end Main_Application
