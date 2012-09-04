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
from GUI import View
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
      
      #self._win_has_menubar = False
      
      #call the parent constructor
      Window.__init__( self, size = ( 600, 400 ) )

      #set the title
      self.set_title( "Obscure Reference" )

      #center ourselves
      self.center( )

      #save the controller
      self._controller = controller

      #the navigation frame will take up the left quarter of the screen
      self._nav_width = self.width / 4
      
      #the main frame will take up the right remainder of the screen
      self._main_width = self.width - self._nav_width

      #create the bold font
      self._bold_font = Font( style = ["bold"] )

      self._Create_Navigation_Frame( )

      #create the main frame
      self._main_frame = \
         Frame( width = self._main_width,
                height = self.height )#- number_constants.menu_bar_height )
      
      
      #create the initial sub frame
      self._sub_frame = \
         Frame( width = (self._main_width - number_constants.basic_pad),
                height = self.height )

      self._logo_image = Image( logo_file )
      #self._intro_canvas = Canvas( None )
      #self._intro_canvas = View( )
      #self._intro_canvas = Frame( width = 500, height = 300 )

      #put the column on the GUI
      self._sub_frame.place_column( \
         [Label("Welcome to the Obscure Reference League",
                just = "center",
                width = (self._main_width - number_constants.basic_pad),
                font = self._bold_font ),
          #self._intro_canvas],          
          Label( "I would really like an image to be displayed here.")],
         left = 0,
         top = 0)
      self._main_frame.place( self._sub_frame )

      self.place( self._main_frame,
                  left = self._nav_frame.right,
                  top = 20,
                  sticky = "nsew" )

      #draw the image in to the view
      #self._logo_image.draw( \
      #   self._intro_canvas,
      #   self._logo_image.bounds,  
      #   self._logo_image.bounds )


   #end __init

   def _Create_Navigation_Frame( self ):
      """This method will create the navigation frame."""

      self._button_width = self._nav_width - number_constants.basic_pad

      #create the navigation frame
      self._nav_frame = Frame( width = self._nav_width,
                               height = self.height ) 

      #create the label to be at the top of the nav frame
      self._nav_label = Label( "Navigation",
                               just = "center",
                               font = self._bold_font,
                               width = self._button_width )

      self._my_team_button = Button( title = "My Team", 
                                     action = "Go_To_My_Team",
                                     width = self._button_width )

      self._league_button = Button( title = "League",
                                    action = "Go_To_League",
                                     width = self._button_width )

      self._players_button = Button( title = "Players",
                                     action = "Go_To_Players",
                                     width = self._button_width )

      self._transactions_button = Button( title = "My Transactions",
                                          action = "Go_To_Transactions",
                                          width = self._button_width )
      
      self._exit_button = Button( title = "Exit",
                                  action = "Exit_Commanded",
                                  width = self._button_width )

      #add the buttons to the frame
      self._nav_frame.place_column([self._nav_label,
                                    self._my_team_button,
                                    self._league_button,
                                    self._players_button,
                                    self._transactions_button,
                                    self._exit_button],
                                   left = 0, 
                                   top = 0)

      self.place( self._nav_frame, left = 20, top = 20 )

   #end _Create_Navigation_Frame

   def Receive_New_Frame( self,
                          new_frame ):
      """This method is used to receive a new frame to be displayed in the
      main frame area."""
      
      #remove the previous frame
      self._main_frame.remove( self._sub_frame )
            
      #put the new frame in the main frame area
      self._main_frame.place( new_frame,
                              sticky = "nsew", #Stick to all sides of the frame
                              left = 0,
                              top = 0 )
      
      #save the new frame as the current frame
      self._sub_frame = new_frame

      # cause the main frame area to be redrawn.
      self._main_frame.invalidate()

   #end Receive_New_Frame

   def draw( self, canvas, rect ):
      """Cause the frame to re-draw the important area."""
      canvas.erase_rect( rect )
   #end draw

   def Go_To_My_Team( self ):
      """This method will tell the parent that the user wants their team to
      be displayed."""
      
      manager_name = self._controller.Get_Current_Manager_Name( )
      
      #display the team
      self._controller.Show_Team( manager_name = manager_name,
                                  internal_switch = True ) 
      
   #end Go_To_My_Team

   def Go_To_League( self ):
      """This method will tell the controller that the user wants to display
      the league information."""
      
      None
   #end Go_To_League

   def Go_To_Players( self ):
      """This method will tell the controller that the user wants to display
      the list of players."""
      
      #inform the controller that it's supposed to show the players
      self._controller.Show_Players( )

   #end Go_To_Players

   def Go_To_Transactions( self ):
      """This method will tell the controller that the user wants to display
      the currently-pending transactions."""
      
      #inform the controller to show the user's transactions
      self._controller.Show_Transactions( )
      
   #end Go_To_Transactions

   def Exit_Commanded( self ):
      """This method will cause the application to exit."""
      
      #inform the controller that it's time to go away.
      self._controller.Exit( )

   #end Exit_Commanded

   def Get_Width( self ):
      """This method will retrieve the width of this window."""
      return self.width
   #end Get_Width
   
   def Get_Height( self ):
      """This method will retrieve the height of this window."""
      return self.height
   #end Get_Height
   
   def Get_Main_Frame_Width( self ):
      return self._main_frame.width
   #end Get_Main_Frame_Width

   def Get_Main_Frame_Height( self ):
      return self._main_frame.height
   #end Get_Main_Frame_Width
   
   def Get_Main_Frame( self ):
      return self._main_frame
   #end Get_Main_Frame
#end class Obscure_Main_Gui