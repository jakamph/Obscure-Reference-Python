##
# This file is the main GUI of the system. Through user actions, the 
# main frame will be replaced by new information to be displayed.
#
# Author: Jason Kamphaugh
#
# Date: March 8, 2012
#

from GUI import Window
from GUI import Frame
from GUI import Label
from GUI import Button

import obscure_reference.application.main_application as main_application

class Obscure_Main_Gui( Window ):

   def __init__( self,
                 controller,
                 **kwds ):
      """This method is the constructor for the class."""
      
      #call the parent constructor
      Window.__init__( self, size = ( 600, 400 ) )

      #set the title
      self.set_title( "Obscure Reference" )

      #center ourselves
      self.center( )

      #save the controller
      self._controller = controller

      #the navigation frame will take up the left third of the screen
      nav_width = self.width / 3
      height = self.height
      
      #the main frame will take up the right 2/3's of the screen
      main_width = self.width * 2 / 3

      #create the navigation frame
      self._nav_frame = Frame( width = nav_width,
                               height = height ) 

      self._nav_frame.place_column([Button(title = "My Team", 
                                           action = "Go_To_My_Team"),
                                    Button(title = "Obscure Reference League",
                                           action = "Go_To_League"),
                                    Button(title = "Players",
                                           action = "Go_To_Players")],
                                   left = 0, 
                                   top = 0)

      self.place( self._nav_frame, left = 20, top = 20 )

      #create the main frame
      self._main_frame = Frame( width = main_width,
                                height = height )
      
      self._sub_frame = Frame( )
      self._sub_frame.place_column( [Label("This is"),
                                     Label("the sub"),
                                     Label("frame.")],
                                   left = 0, 
                                   top = 0)
      self._main_frame.place( self._sub_frame )

      self.place( self._main_frame, left = self._nav_frame.right, top = 20 )

   #end __init

   def Receive_New_Frame( self,
                          new_frame ):
      """This method is used to receive a new frame to be displayed in the
      main frame area."""
      
      #put the new frame in the main frame area
      self._main_frame.place( new_frame )
      
   #end Receive_New_Frame

   def resized( self,
                delta ):
      """This method is automatically called when the window is resized."""

      None

      #change the size of the nav frame
      #self._nav_frame.resize
      
      #change the size of the main frame

   #end resized

   def Go_To_My_Team( self ):
      """This method will tell the parent that the user wants their team to
      be displayed."""
      None
   #end Go_To_My_Team

   def Go_To_League( self ):
      """This method will tell the controller that the user wants to display
      the league information."""
      
      None
   #end Go_To_League

   def Go_To_Players( self ):

      """This method will tell the controller that the user wants to display
      the list of players."""
      self._controller.Show_Players( )
   #end Go_To_Players

   def Get_Width( self ):
      """This method will retrieve the width of this window."""
      return self.width
   #end Get_Width
   
   def Get_Height( self ):
      """This method will retrieve the height of this window."""
      return self.height
   #end Get_Height

#end class Obscure_Main_Gui