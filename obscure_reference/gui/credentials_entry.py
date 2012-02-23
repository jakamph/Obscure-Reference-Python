from GUI import ModalDialog, Label, Button, Task, TextField

class CredentialsDialog(ModalDialog):

    def __init__(self):
        ModalDialog.__init__(self)
        label = Label("Please enter your credentials.")
        self.ok_button = Button("OK", action = "ok", style = "default")
        self.cancel_button = Button("Cancel", style = "cancel", action = "cancel")
        self.user_box = TextField(width = 150)
        self.password_box = TextField(width = 150, password = "True", select_action = "password_click")
        self.place(label, left = 20, top = 20)
        self.place(self.user_box, top = label + 10, right = label.right)
        self.place(self.password_box, top = self.user_box.bottom + 10, right = label.right)
        self.place(self.ok_button, top = self.password_box.bottom + 20, right = label.right)
        self.place(self.cancel_button, top = self.ok_button.top, right = self.ok_button.left - 20)
        self.shrink_wrap(padding = (20, 20))
        self.title = "Google Credentials"
        self.password_box.width = 150
        self.set_text()

    def password_click(self):
        print "password click"

    def ok(self):
        print self.user_box.get_text()
        print self.password_box.get_text()
        self.dismiss(True)

    def cancel(self):
        self.dismiss(True)

    def set_text(self):
        self.user_box.set_text("Username")
        self.password_box.set_text("Password")

dlog = CredentialsDialog()
dlog.present()
