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
from GUI import Font
from GUI import Canvas
from GUI import Image
from GUI import Geometry

from GUI.StdFonts import system_font

import obscure_reference.application.main_application as main_application
import obscure_reference.common.number_constants as number_constants

class Obscure_Main_Gui( Window ):

   def __init__( self,
                 controller,
                 logo_file,
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

      button_width = nav_width - number_constants.basic_pad

      #create the bold font
      self._bold_font = Font( style = ["bold"] )

      #create the navigation frame
      self._nav_frame = Frame( width = nav_width,
                               height = height ) 

      #create the label to be at the top of the nav frame
      self._nav_label = Label( "Navigation",
                               just = "center",
                               font = self._bold_font,
                               width = button_width )

      self._my_team_button = Button( title = "My Team", 
                                     action = "Go_To_My_Team",
                                     width = button_width )

      self._league_button = Button( title = "Obscure Reference League",
                                    action = "Go_To_League",
                                     width = button_width )

      self._players_button = Button( title = "Players",
                                     action = "Go_To_Players",
                                     width = button_width )

      self._nav_frame.place_column([self._nav_label,
                                    self._my_team_button,
                                    self._league_button,
                                    self._players_button],
                                   left = 0, 
                                   top = 0)

      self.place( self._nav_frame, left = 20, top = 20 )

      #create the main frame
      self._main_frame = Frame( width = main_width,
                                height = height )
      
      #create the initial sub frame
      self._sub_frame = \
         Frame( width = (main_width - number_constants.basic_pad),
                height = height )

      self._logo_image = Image( logo_file )
      
      #draw the image in to the view
      #self._logo_image.draw( \
      #   self._intro_canvas,
      #   self._logo_image.bounds,  
      #   self._logo_image.bounds )
      
      

      #put the column on the GUI
      self._sub_frame.place_column( \
         [Label("Welcome to the Obscure Reference League",
                just = "center",
                width = (main_width - number_constants.basic_pad),
                font = self._bold_font ),                
          Label( "I would really like an image to be displayed here.")],
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