##
# This file contains the GUI that is used to receive a user's credentials
# and provide them back to the calling code.
#
# Author: Paul Forbes
#
# Date: February 15, 2012
#

from GUI import ModalDialog, Label, Button, TextField

class Credentials_Dialog(ModalDialog):

   def __init__(self):
      """This method is the constructor for a new credentials dialog."""
      ModalDialog.__init__(self)

      #default the credentials information
      self._user = None
      self._password = None

      label = Label("Please enter your credentials.")
      self._ok_button = Button("OK", action = "ok", style = "default")
      self._cancel_button = Button("Cancel", style = "cancel", action = "cancel")
      self._user_box = TextField(width = 150)
      self._password_box = TextField(width = 150,
                                     password = "True",
                                     select_action = "password_click")
      self.place(label, left = 20, top = 20)
      self.place(self._user_box, top = label + 10, right = label.right)
      self.place(self._password_box,
                 top = self._user_box.bottom + 10,
                 right = label.right)
      self.place(self._ok_button,
                 top = self._password_box.bottom + 20,
                 right = label.right)
      self.place(self._cancel_button,
                 top = self._ok_button.top,
                 right = self._ok_button.left - 20)
      self.shrink_wrap(padding = (20, 20))

      self._message_label = None

      #the parent class will use this function to set the title
      self.set_title( "Google Credentials" )
      self._password_box.width = 150
      self._Set_Text()
      self._user_canceled = False
   #end __init__

   def password_click(self):
      print "password click"
   #end password_click

   def ok(self):
      """This method will capture the event of the OK button being clicked."""
      self._user = self._user_box.get_text()
      self._password = self._password_box.get_text()
      self.dismiss(True)
      self.exit_modal_event_loop()

   def cancel(self):
      """This method will capture the event of the Cancel button being
      clicked."""
      self._user_canceled = True
      self.dismiss(True)

   def _Set_Text(self):
      """This method will set the default text in the text boxes."""
      self._user_box.set_text("Username")
      self._password_box.set_text("Password")

   def Get_User( self ):
      """This method will retrieve the user name provided."""
      return self._user
   #end Get_User

   def Get_Password( self ):
      """This method will retrieve the password provided."""
      return self._password
   #end Get_Password

   def Get_User_Canceled( self ):
      """This method will retrieve if the user asked to cancel the
      operation."""
      return self._user_canceled
   #end Get_User_Canceled

   def Set_Message( self, message ):
      """This method will set the message label to be shown to the user."""
      self._message_label.set_text( message )
   #end Set_Message
