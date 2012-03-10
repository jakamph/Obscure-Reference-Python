##
# This file will contain the information for the parent class of reference
# object. It will be used to let the GUI classes import the data without
# having to worry about mutual importation.
#
# Author: Jason Kamphaugh
#
# Date: March 9, 2012
#

class Reference_Object( ):
   
   def __init__( self ):
      
      #We actually do nothing here
      None
   #end __init__
   
   def Fill_Data( self,
                  gui_object ):
      """This method is intended to be overridden by the child class to
      fill its data in to the pertinent fields on a GUI object."""
      
      #This method intentionally left blank
      None

   #end Fill_Data
   
#end Reference_Object